`include "rtl/program_counter.v"

module program_counter_tb;
    parameter WORD_WIDTH = 8;

    reg enable;
    reg clock;
    reg reset;
    reg jump;
    reg jz;
    reg zero_flag;
    reg [WORD_WIDTH - 1 : 0] jump_address;
    wire [WORD_WIDTH - 1 : 0] result;

    program_counter COUNTER (
        .enable(enable),
        .clock(clock),
        .reset(reset),
        .jump(jump),
        .jz(jz),
        .zero_flag(zero_flag),
        .jump_address(jump_address),
        .result(result)
    );

    reg done = 0;
    integer log_file;
    integer i;

    initial begin
        log_file = $fopen("log/program_counter.log", "w");
        $fdisplay(log_file, "enable\tjump\tjz\t\tzero_f\tjump_address\tresult\n");

        @(posedge clock);
        while(!done) @(posedge clock);

        $fclose(log_file);
        $finish;
    end

    initial begin
        i = 0;
        #5 reset = 1;
        #20 reset = 0;
        enable = 1;
        jump = 0;
        jz = 0;
        zero_flag = 0;
        jump_address = 8'h00;
        
        repeat (1000) begin
            #5 clock = 0;
            enable = (i % 10 == 0) ? 0 : 1;
            jump = (i % 31 == 0) ? 1 : 0;
            jz = (i % 37 == 0) ? 1 : 0;
            zero_flag = (i % 74 == 0) ? 1 : 0;
            jump_address = i % 128;
            #5 clock = 1;

            #5 $fdisplay(log_file, "%b\t\t%b\t\t%b\t\t%b\t\t%b\t\t%b", enable, jump, jz, zero_flag, jump_address, result);
            i = i + 1;
        end
        done = 1;
        $finish;
    end
endmodule