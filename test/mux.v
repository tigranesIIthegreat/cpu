`include "rtl/mux.v"

module mux_tb;
    reg [7:0] data0;
    reg [7:0] data1;
    reg select;
    wire [7:0] result;

    mux MUX (
        .data0(data0),
        .data1(data1),
        .select(select),
        .result(result)
    );

    integer log_file;

    initial begin
        log_file = $fopen("log/mux.log", "w");
        $fdisplay(log_file, "data0\t\t\tdata1\t\t\tselect\tresult\n");

        data0 = 0;
        data1 = 0;
        
        repeat (2**8 * 2**8 * 2) begin
            select = 0;
            #1 $fdisplay(log_file, "%b\t\t%b\t\t%b\t\t%b", data0, data1, select, result);
            select = 1;
            #1 $fdisplay(log_file, "%b\t\t%b\t\t%b\t\t%b", data0, data1, select, result);

            if (data1 == 255) begin
                data1 = 0;
                if (data0 == 255) begin
                    data0 = 0;
                end else data0 = data0 + 1;
            end else data1 = data1 + 1;
        end
        
        $fclose(log_file);
        $finish;
    end

endmodule