module program_counter (
  input clock,
  input reset,
  input jump,
  input jz,
  input zero_flag,
  input [7:0] jump_address,
  input enable,
  output reg [7:0] current_address
);
  reg [7:0] next_address;
  always @(posedge clock or posedge reset) begin
    if (enable) begin
      if (reset) begin
        current_address <= 8'h00;
      end else begin
        if (jump) begin
          current_address <= jump_address;
        end else if (jz) begin
          if (zero_flag) begin
            current_address <= jump_address;
          end else begin
            next_address <= current_address + 2;
            current_address <= next_address;
          end
          current_address <= jump_address;
        end else begin
          next_address <= current_address + 2;
          current_address <= next_address;
        end
    end
    end
  end
endmodule