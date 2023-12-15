module instruction_decoder (
    input [15:0] instruction,
    output reg [3:0] op_code,
    output reg [1:0] src_reg,
    output reg [1:0] dst_reg,
    output reg [7:0] memory_or_immediate,
    output reg is_alu_operation
    );

    always @(*) begin
        op_code = instruction[15:12];
        src_reg = instruction[11:10];
        dst_reg = instruction[9:8];
        memory_or_immediate = instruction[7:0];
        is_alu_operation = op_code > 4'b1001 ? 0 : 1;
    end
endmodule