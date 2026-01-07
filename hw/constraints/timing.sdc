# Clock Constraints
create_clock -name clk -period 10.000 [get_ports {clk}]

# Clock Uncertainty (Jitter + Skew)
# A conservative estimate for Cyclone IV is around 0.2ns
derive_clock_uncertainty

# Automatically constrain PLL and other generated clocks
derive_pll_clocks

# Input/Output Delays
# These constrain the paths from external pins to the first register (Input)
# and from the last register to external pins (Output).
# Assuming a synchronous interface with some external device delay.

# Input Delay: External device sends data 2ns after clock edge
set_input_delay -clock { clk } -max 2.0 [get_ports {pixel_in[*]}]
set_input_delay -clock { clk } -min 0.0 [get_ports {pixel_in[*]}]
set_input_delay -clock { clk } -max 2.0 [get_ports {valid_in}]
set_input_delay -clock { clk } -min 0.0 [get_ports {valid_in}]
set_input_delay -clock { clk } -max 2.0 [get_ports {rst}]
set_input_delay -clock { clk } -min 0.0 [get_ports {rst}]

# Output Delay: External device requires data 2ns before clock edge (Setup time)
set_output_delay -clock { clk } -max 2.0 [get_ports {stream_out[*]}]
set_output_delay -clock { clk } -min 0.0 [get_ports {stream_out[*]}]
set_output_delay -clock { clk } -max 2.0 [get_ports {valid_out}]
set_output_delay -clock { clk } -min 0.0 [get_ports {valid_out}]

# Asynchronous Paths
# Reset is often asynchronous, but if synchronized internally, we might not need this.
# If 'rst' is purely asynchronous reset to FFs:
# set_false_path -from [get_ports {rst}] -to [all_registers]
