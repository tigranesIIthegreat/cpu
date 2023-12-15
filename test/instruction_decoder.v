`include "rtl/instruction_decoder.v"

module instruction_decoder_tb;
    parameter INSTRUCTION_LENGTH = 16;
    parameter OP_CODE_LENGTH = 4;
    parameter REG_ADDRESS_WIDTH = 2;
    parameter MEMORY_OR_IMM_LENGTH = 8;

    reg [INSTRUCTION_LENGTH - 1 : 0] instruction;

    wire [OP_CODE_LENGTH - 1 : 0] op_code;
    wire [REG_ADDRESS_WIDTH - 1 : 0] src_reg;
    wire [REG_ADDRESS_WIDTH - 1 : 0] dst_reg;
    wire [MEMORY_OR_IMM_LENGTH - 1 : 0] memory_or_immediate;
    wire is_alu_operation;

    instruction_decoder INSTRUCION_DECODER (
        .instruction(instruction),
        .op_code(op_code),
        .src_reg(src_reg),
        .dst_reg(dst_reg),
        .memory_or_immediate(memory_or_immediate),
        .is_alu_operation(is_alu_operation)
    );

    reg clock = 0;
    reg done = 0;
    integer log_file;
    integer i;

    initial begin
        log_file = $fopen("log/instruction_decoder.log", "w");
        $fdisplay(log_file, "instruction\t\t\t\top_code\t\tsrc_reg\tdst_reg\tmem_or_imm\t\tis_alu_operation\n");

        @(posedge clock);
        while(!done) @(posedge clock);

        $fclose(log_file);
        $finish;
    end

    initial begin
        i = 0;
        instruction = 0;
        repeat (2**INSTRUCTION_LENGTH) begin
            #5 clock = 0;
            instruction = i;
            #5 clock = 1;
            #5 $fdisplay(log_file, "%b\t\t%b\t\t%b\t\t%b\t\t%b\t\t%b", instruction, op_code, src_reg, dst_reg, memory_or_immediate, is_alu_operation);
            i = i + 1;
        end
        done = 1;
    end

endmodule