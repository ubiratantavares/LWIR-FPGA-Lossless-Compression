import numpy as np
from PIL import Image
import os

def generate_test_vectors(image_path, output_hex):
    """
    Reads a TIFF image and converts it to a hex file for Verilog simulation.
    """
    try:
        img = Image.open(image_path)
        data = np.array(img, dtype=np.uint16).flatten()
        
        with open(output_hex, 'w') as f:
            for pixel in data:
                f.write(f"{pixel:04x}\n")
        
        print(f"Generated {output_hex} from {image_path}. Total pixels: {len(data)}")
        return data
    except Exception as e:
        print(f"Error generating test vectors: {e}")
        return None

if __name__ == "__main__":
    # Use the first image from the dataset as a test case
    dataset_dir = "data/flir-lwir-v1"
    files = sorted([f for f in os.listdir(dataset_dir) if f.endswith('.tiff')])
    
    if files:
        first_image = os.path.join(dataset_dir, files[0])
        generate_test_vectors(first_image, "hw/sim/input.hex")
    else:
        print("No TIFF images found in data directory.")
