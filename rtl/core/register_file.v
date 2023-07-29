module register_unit(
  input [7:0] read_address,
  input [7:0] write_address,
  input [7:0] write_data,
  input write_enable,
  input clk,
  input rst,
  output reg [7:0] read_data
);

  // Define the register file as an array of 256 8-bit registers
  reg [7:0] registers [0:255];

  // Output the data from the specified read address
  always @(*) begin
    read_data = registers[read_address];
  end

  // Perform the write operation if write_enable is asserted
  always @(posedge clk, posedge rst) begin
    if (rst) begin
      // Reset all registers to 8'h00 when rst is asserted
      for (int i = 0; i < 256; i = i + 1) begin
        registers[i] <= 8'h00;
      end
    end else begin
      // Write to the specified register if write_enable is high
      if (write_enable) begin
        registers[write_address] <= write_data;
      end
    end
  end

endmodule
