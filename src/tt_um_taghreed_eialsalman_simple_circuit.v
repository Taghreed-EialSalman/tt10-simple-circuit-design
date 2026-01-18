`default_nettype none
module tt_um_taghreed_eialsalman_simple_circuit (
    input  wire [7:0] ui_in,     // Dedicated inputs
    output wire [7:0] uo_out,    // Dedicated outputs
    input  wire [7:0] uio_in,    // IOs: Input path
    output wire [7:0] uio_out,   // IOs: Output path
    output wire [7:0] uio_oe,    // IOs: Enable path (0=input, 1=output)
    input  wire       ena,       // Always 1 when design is powered
    input  wire       clk,       // Clock input
    input  wire       rst_n      // Active-low reset
);

  // Map input wires for clarity
  wire A = ui_in[0];
  wire B = ui_in[1];
  wire C = ui_in[2];

  // Internal wire
  wire e;
  wire x;
  wire y;

  // Logic implementation
  and g1(e, A, B);
  not g2(y, C);
  or  g3(x, e, y);

  // Assign outputs
  assign uo_out[0] = x;
  assign uo_out[1] = y;
  assign uo_out[2] = 1'b0;
  assign uo_out[3] = 1'b0;
  assign uo_out[4] = 1'b0;
  assign uo_out[5] = 1'b0;
  assign uo_out[6] = 1'b0;
  assign uo_out[7] = 1'b0;

  assign uio_out = 8'b00000000;
  assign uio_oe  = 8'b00000000;

  // Prevent unused input warnings
  wire _unused = &{ena, clk, rst_n, ui_in[7:3], uio_in};

endmodule
