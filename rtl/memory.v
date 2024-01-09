module memory #(parameter CELL_COUNT = 256, parameter LINE_WIDTH = 4)(
  input [LINE_WIDTH - 1:0] read_address,
  input [LINE_WIDTH - 1:0] write_address,
  input [LINE_WIDTH - 1:0] write_data,
  input write_enable,
  input reset,
  output reg [LINE_WIDTH - 1:0] read_data);

  reg [LINE_WIDTH - 1:0] registers [0:CELL_COUNT - 1];

  always @(*) begin
    read_data = registers[read_address];
  end

  integer i;
  always @(*) begin
    if (reset) begin
      for (i = 0; i < CELL_COUNT; i = i + 1) begin
        registers[i] <= 8'h00;
      end
    end else begin
      if (write_enable) begin
        registers[write_address] <= write_data;
      end
    end
  end
endmodule
