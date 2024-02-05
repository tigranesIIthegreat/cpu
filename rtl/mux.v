module mux (
  input [7:0] data0,
  input [7:0] data1,
  input select,
  output reg [7:0] result);

  always @(select or data0 or data1) begin
    result = select ? data1 : data0;
  end
endmodule