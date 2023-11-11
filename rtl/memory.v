module memory #(parameter CELL_COUNT = 256)(
  input [7:0] read_address,
  input [7:0] write_address,
  input [7:0] write_data,
  input write_enable,
  input clock,
  input reset,
  output reg [7:0] read_data);

  reg [7:0] registers [0:CELL_COUNT - 1];

  always @(*) begin
    read_data = registers[read_address];
  end

  always @(posedge clock, posedge reset) begin
    if (reset) begin
      for (int i = 0; i < CELL_COUNT; i = i + 1) begin
        registers[i] <= 8'h00;
      end
    end else begin
      if (write_enable) begin
        registers[write_address] <= write_data;
      end
    end
  end
endmodule
