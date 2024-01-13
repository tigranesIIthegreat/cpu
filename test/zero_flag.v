`include "rtl/zero_flag.v"

module zero_flag_tb;
    reg value;
    wire result;

    zero_flag FLAG (
        .value(value),
        .result(result)
    );

    reg clock = 0;
    always #5 clock = ~clock;
    reg done = 0;
    integer log_file;
    integer i;

    initial begin
        log_file = $fopen("log/zero_flag.log", "w");
        $fdisplay(log_file, "value\tresult\n");

        @(posedge clock);
        while(!done) @(posedge clock);

        $fclose(log_file);
        $finish;
    end

    initial begin
        i = 0;
        repeat (100) begin
            @(posedge clock);
            value = (3 * i + 1) % 2;
            $fwrite(log_file, "%b\t\t", value);
            #1 $fwrite(log_file, "%b\t\t", result);
            
            $fdisplay(log_file);
            i = i + 1;
        end
        done = 1;
    end
endmodule