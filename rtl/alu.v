module alu(input [7:0] operand1,
           input [7:0] operand2,
           input [3:0] opCode,
           output [7:0] result,
           output carryOut);

    reg [7:0] ALU_Result;
    wire [8:0] tmp;
    assign result = ALU_Result;
    assign tmp = {1'b0,operand1} + {1'b0,operand2};
    assign carryOut = tmp[8];
    always @(*) begin
        case(opCode)
            4'b0000: ALU_Result = operand1 + operand2 ;             // Addition 
            4'b0001: ALU_Result = operand1 - operand2 ;             // Subtraction
            4'b0010: ALU_Result = operand1 * operand2;              // Multiplication
            4'b0011: ALU_Result = operand1/operand2;                // Division
            4'b0100: ALU_Result = operand1<<1;                      // Logical shift left
            4'b0101: ALU_Result = operand1>>1;                      // Logical shift right
            4'b0110: ALU_Result = {operand1[6:0],operand1[7]};      // Rotate left
            4'b0111: ALU_Result = {operand1[0],operand1[7:1]};      // Rotate right
            4'b1000: ALU_Result = operand1 & operand2;              // Logical and 
            4'b1001: ALU_Result = operand1 | operand2;              // Logical or
            4'b1010: ALU_Result = operand1 ^ operand2;              // Logical xor 
            4'b1011: ALU_Result = ~(operand1 | operand2);           // Logical nor
            4'b1100: ALU_Result = ~(operand1 & operand2);           // Logical nand 
            4'b1101: ALU_Result = ~(operand1 ^ operand2);           // Logical xnor
            4'b1110: ALU_Result = (operand1>operand2)?8'd1:8'd0;    // Greater comparison
            4'b1111: ALU_Result = (operand1==operand2)?8'd1:8'd0;   // Equal comparison   
            default: ALU_Result = operand1 + operand2;
        endcase
    end
endmodule