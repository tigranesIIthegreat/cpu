`include "rtl/alu.v"

module alu_tb;
    parameter WORD_WIDTH = 8;
    parameter OPCODE_WIDTH = 4;

    reg [WORD_WIDTH - 1 : 0] operand1;
    reg [WORD_WIDTH - 1 : 0] operand2;
    reg [OPCODE_WIDTH - 1 : 0] opCode;

    wire [WORD_WIDTH-1:0] result;
    wire zero_flag;

    alu ALU (
        .operand1(operand1),
        .operand2(operand2),
        .opCode(opCode),
        .result(result),
        .zero_flag(zero_flag)
    );

    reg clk = 0;
    always #5 clk = ~clk;
    reg done = 0;
    integer log_file;

    initial begin
        log_file = $fopen("log/alu.log", "w");
        $fdisplay(log_file, "operand1\t\toperand2\t\topCode\t\tresult\t\t\tzero_flag\n");

        @(posedge clk);
        while(!done) @(posedge clk);

        $fclose(log_file);
        $finish;
    end

    initial begin
        operand1 = 0;
        operand2 = 0;
        opCode = 0;

        repeat (2**WORD_WIDTH * 2**WORD_WIDTH * 2**OPCODE_WIDTH) begin
            @(posedge clk); // Wait for next clock cycle
            $fdisplay(log_file, "%b\t\t%b\t\t%b\t\t%b\t\t%b", operand1, operand2, opCode, result, zero_flag);

            // Increment inputs for the next test
            if (operand2 == (2**WORD_WIDTH - 1)) begin
                operand2 = 0;
                if (operand1 == (2**WORD_WIDTH - 1)) begin
                    operand1 = 0;
                    if (opCode == (2**OPCODE_WIDTH - 1)) opCode = 0;
                    else opCode = opCode + 1;
                end
                else operand1 = operand1 + 1;
            end
            else operand2 = operand2 + 1;
        end
        done = 1;
    end
endmodule
