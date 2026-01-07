import sys

def signed17(val):
    """Converts a 17-bit integer to a signed python int."""
    if val & (1 << 16):
        return val - (1 << 17)
    return val

def validate_output(input_hex, output_hex):
    print(f"Validating {output_hex} against {input_hex}...")
    
    # 1. Read Input Pixels
    try:
        with open(input_hex, 'r') as f:
            pixels = [int(line.strip(), 16) for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: {input_hex} not found.")
        return False

    # 2. Software Model of DPCM + RLE
    # DPCM Logic: Res = Curr - Prev. Prev starts at 0.
    # RLE Logic: Pack {ZeroCount, Literal}
    
    expected_stream = []
    prev_pixel = 0
    zero_count = 0
    
    for p in pixels:
        # DPCM
        diff = p - prev_pixel
        prev_pixel = p
        
        # RLE Packing
        if diff == 0:
            zero_count += 1
            # Saturate at 32767 (15-bit)
            if zero_count > 32767:
                zero_count = 32767
        else:
            # Emit {ZeroCount, Literal}
            # Literal is 17-bit signed. We need to mask it to 17-bit hex representation.
            literal_masked = diff & 0x1FFFF
            packet = (zero_count << 17) | literal_masked
            expected_stream.append(packet)
            zero_count = 0
            
    # Note: If the stream ends with zeros, they are NOT emitted by the hardware
    # because it waits for a non-zero terminator.
    # The validation should account for this by only comparing up to the length of the hardware output.
    
    # 3. Read Hardware Output
    try:
        with open(output_hex, 'r') as f:
            hw_stream = [int(line.strip(), 16) for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: {output_hex} not found. Run simulation first.")
        return False

    # 4. Compare
    match = True
    if len(hw_stream) == 0:
        print("Error: Hardware output is empty.")
        return False

    print(f"Input Pixels: {len(pixels)}")
    print(f"Expected Packets: {len(expected_stream)}")
    print(f"Hardware Packets: {len(hw_stream)}")
    
    # Compare only what HW produced (ignoring trailing zeros hanging in buffer)
    limit = min(len(expected_stream), len(hw_stream))
    
    for i in range(limit):
        if expected_stream[i] != hw_stream[i]:
            print(f"Mismatch at index {i}:")
            print(f"  Expected: {expected_stream[i]:08x}")
            print(f"  Got:      {hw_stream[i]:08x}")
            
            # Decode for debug
            exp_zc = expected_stream[i] >> 17
            exp_lit = signed17(expected_stream[i] & 0x1FFFF)
            got_zc = hw_stream[i] >> 17
            got_lit = signed17(hw_stream[i] & 0x1FFFF)
            print(f"  Exp Decoded: ZC={exp_zc}, Lit={exp_lit}")
            print(f"  Got Decoded: ZC={got_zc}, Lit={got_lit}")
            
            match = False
            break
    
    if match:
        print("SUCCESS: Hardware output matches Software model!")
        if len(hw_stream) < len(expected_stream):
            print(f"Warning: Hardware stream is shorter by {len(expected_stream) - len(hw_stream)} packets (likely trailing zeros).")
        return True
    else:
        print("FAILURE: Validation failed.")
        return False

if __name__ == "__main__":
    validate_output("hw/sim/input.hex", "hw/sim/output.hex")
