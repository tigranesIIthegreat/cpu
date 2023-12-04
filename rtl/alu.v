module alu(input [7:0] operand1,
           input [7:0] operand2,
           input [3:0] opCode,
           output reg [7:0] result,
           output reg zero_flag);

    always @(*) begin
        case(opCode)
            4'b0000: result = operand1 + operand2;                  // Addition 
            4'b0001: result = operand1 - operand2;                  // Subtraction
            4'b0010: result = operand1 + 1;                         // Incrementation
            4'b0011: result = operand1 - 1;                         // Decrementation
            4'b0100: result = operand1 & operand2;                  // Logical and 
            4'b0101: result = operand1 | operand2;                  // Logical or
            4'b0110: result = operand1 ^ operand2;                  // Logical xor 
            4'b0111: result = operand1 << 1;                        // Logical shift left
            4'b1000: result = operand1 >> 1;                        // Logical shift right
            4'b1001: zero_flag = (operand1 == operand2) ? 1 : 0;    // Equal comparison   
            default: result = operand1 + operand2;
        endcase
    end
endmodule