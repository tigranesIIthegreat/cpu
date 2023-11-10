`include "rtl/alu.v"

module alu_tb;
    parameter DATA_WIDTH = 8;
    parameter SEL_WIDTH = 4;

    reg [DATA_WIDTH - 1 : 0] operand1;
    reg [DATA_WIDTH - 1 : 0] operand2;
    reg [SEL_WIDTH - 1 : 0] opCode;

    wire [DATA_WIDTH-1:0] result;
    wire carryOut;

    alu ALU_UUT (
        .operand1(operand1),
        .operand2(operand2),
        .opCode(opCode),
        .result(result),
        .carryOut(carryOut)
    );

    reg clk = 0;
    always #5 clk = ~clk;

    reg reset = 0;
    reg start = 0;
    reg done = 0;

    integer log_file;
    initial begin
        log_file = $fopen("log/core/alu.log", "w");
        $fdisplay(log_file, 
            "operand1\t\t\tB\t\t\tSel\t\tOut\t\t\tCarryOut\n----------------------------------------------------");

        #10 reset = 1;
        #10 reset = 0;
        #10 start = 1;

        @(posedge clk);
        while(!done) @(posedge clk);

        $fclose(log_file);
        $finish;
    end

    initial begin
        operand1 = 0;
        operand2 = 0;
        opCode = 0;

        repeat (2**DATA_WIDTH * 2**DATA_WIDTH * 2**SEL_WIDTH) begin
            @(posedge clk); // Wait for next clock cycle (if using synchronous design)

            // Log the inputs and outputs
            $fdisplay(log_file, "%b\t%b\t%b\t%b\t%b", operand1, operand2, opCode, result, carryOut);

            // Increment inputs for the next test
            if (operand2 == (2**DATA_WIDTH - 1)) begin
                operand2 = 0;
                if (operand1 == (2**DATA_WIDTH - 1)) begin
                    operand1 = 0;
                    if (opCode == (2**SEL_WIDTH - 1)) begin
                        opCode = 0;
                    end
                    else begin
                        opCode = opCode + 1;
                    end
                end
                else begin
                    operand1 = operand1 + 1;
                end
            end
            else begin
                operand2 = operand2 + 1;
            end
        end

        done = 1;
    end
endmodule
