`timescale 1ns / 1ps

module tb_LWIR_Lossless_Compression;

    // Parameters
    parameter CLK_PERIOD = 10; // 100 MHz

    // Inputs
    reg clk;
    reg rst;
    reg valid_in;
    reg [15:0] pixel_in;

    // Outputs
    wire valid_out;
    wire [31:0] stream_out;

    // File Handles
    integer file_in;
    integer file_out;
    integer scan_status;
    
    // DUT Instance
    LWIR_Lossless_Compression dut (
        .clk(clk),
        .rst(rst),
        .valid_in(valid_in),
        .pixel_in(pixel_in),
        .valid_out(valid_out),
        .stream_out(stream_out)
    );

    // Clock Generation
    initial begin
        clk = 0;
        forever #(CLK_PERIOD/2) clk = ~clk;
    end

    // Test Stimulus
    initial begin
        // Initialize Inputs
        rst = 1;
        valid_in = 0;
        pixel_in = 0;

        // Open Files
        // Note: You need to generate input.hex first!
        file_in = $fopen("input.hex", "r");
        file_out = $fopen("output.hex", "w");

        if (file_in == 0) begin
            $display("Error: Could not open input.hex");
            $finish;
        end

        // Reset Sequence
        #(CLK_PERIOD*2);
        rst = 0;
        #(CLK_PERIOD*2);

        $display("Starting Simulation...");

        // Feed Data
        while (!$feof(file_in)) begin
            @(posedge clk);
            scan_status = $fscanf(file_in, "%h\n", pixel_in);
            if (scan_status == 1) begin
                valid_in = 1;
            end else begin
                valid_in = 0;
            end
        end

        // End of Data
        @(posedge clk);
        valid_in = 0;

        // Wait for pipeline to drain
        #(CLK_PERIOD*20);
        
        $fclose(file_in);
        $fclose(file_out);
        $display("Simulation Finished.");
        $finish;
    end

    // Capture Output
    always @(posedge clk) begin
        if (valid_out) begin
            $fwrite(file_out, "%h\n", stream_out);
        end
    end

endmodule
