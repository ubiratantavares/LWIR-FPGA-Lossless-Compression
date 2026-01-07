module DPCM_Predictor (
    input  wire        clk,
    input  wire        rst,
    input  wire        valid_in,
    input  wire [15:0] pixel_in,  // 16-bit Unsigned Input
    output reg         valid_out,
    output reg  [16:0] residual   // 17-bit Signed Output
);

    // Registers
    reg [15:0] prev_pixel;
    
    // Internal signals
    wire signed [16:0] pixel_s;
    wire signed [16:0] prev_pixel_s;
    wire signed [16:0] diff;

    // Sign extension for arithmetic
    assign pixel_s      = {1'b0, pixel_in};
    assign prev_pixel_s = {1'b0, prev_pixel};
    
    // Prediction: Residual = Current - Previous
    assign diff         = pixel_s - prev_pixel_s;

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            prev_pixel <= 16'd0;
            valid_out  <= 1'b0;
            residual   <= 17'sd0;
        end else begin
            valid_out <= valid_in;
            
            if (valid_in) begin
                // Output the residual
                residual <= diff;
                
                // Update Previous Pixel for the NEXT cycle
                prev_pixel <= pixel_in;
            end
        end
    end

endmodule
