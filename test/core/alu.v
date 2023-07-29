`include "rtl/core/alu.v"

module alu_tb;
    parameter DATA_WIDTH = 8;
    parameter SEL_WIDTH = 4;

    reg [DATA_WIDTH - 1 : 0] A;
    reg [DATA_WIDTH - 1 : 0] B;
    reg [SEL_WIDTH - 1 : 0] Sel;

    wire [DATA_WIDTH-1:0] Out;
    wire CarryOut;

    alu ALU_UUT (
        .A(A),
        .B(B),
        .Sel(Sel),
        .Out(Out),
        .CarryOut(CarryOut)
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
            "A\t\t\tB\t\t\tSel\t\tOut\t\t\tCarryOut\n----------------------------------------------------");

        #10 reset = 1;
        #10 reset = 0;
        #10 start = 1;

        @(posedge clk);
        while(!done) @(posedge clk);

        $fclose(log_file);
        $finish;
    end

    initial begin
        A = 0;
        B = 0;
        Sel = 0;

        repeat (2**DATA_WIDTH * 2**DATA_WIDTH * 2**SEL_WIDTH) begin
            @(posedge clk); // Wait for next clock cycle (if using synchronous design)

            // Log the inputs and outputs
            $fdisplay(log_file, "%b\t%b\t%b\t%b\t%b", A, B, Sel, Out, CarryOut);

            // Increment inputs for the next test
            if (B == (2**DATA_WIDTH - 1)) begin
                B = 0;
                if (A == (2**DATA_WIDTH - 1)) begin
                    A = 0;
                    if (Sel == (2**SEL_WIDTH - 1)) begin
                        Sel = 0;
                    end
                    else begin
                        Sel = Sel + 1;
                    end
                end
                else begin
                    A = A + 1;
                end
            end
            else begin
                B = B + 1;
            end
        end

        done = 1;
    end
endmodule
