module LWIR_Lossless_Compression (
    input  wire        clk,
    input  wire        rst,
    input  wire        valid_in,
    input  wire [15:0] pixel_in,
    output wire        valid_out,
    output wire [31:0] stream_out
);

    // Internal Signals
    wire        dpcm_valid;
    wire [16:0] dpcm_residual;

    // Instance: DPCM Predictor
    DPCM_Predictor inst_dpcm (
        .clk       (clk),
        .rst       (rst),
        .valid_in  (valid_in),
        .pixel_in  (pixel_in),
        .valid_out (dpcm_valid),
        .residual  (dpcm_residual)
    );

    // Instance: RLE Encoder
    RLE_Encoder inst_rle (
        .clk       (clk),
        .rst       (rst),
        .valid_in  (dpcm_valid),
        .data_in   (dpcm_residual),
        .valid_out (valid_out),
        .data_out  (stream_out)
    );

endmodule
