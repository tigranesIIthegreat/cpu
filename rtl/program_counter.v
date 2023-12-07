module program_counter (
  input enable,
  input clock,
  input reset,
  input jump,
  input jz,
  input zero_flag,
  input [7:0] jump_address,
  output reg [7:0] result);
  
  reg [7:0] next_address;
  always @(posedge clock or posedge reset) begin
    if (reset) begin
      result <= 8'h00;
    end else begin
      if (enable) begin
        if (jump || (jz && zero_flag)) begin
          result <= jump_address;
        end else begin
          next_address = result == 126 ? 0 : result + 2;
          result <= next_address;
        end
      end
    end
  end
endmodule