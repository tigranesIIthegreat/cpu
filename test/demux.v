`include "rtl/demux.v"

module mux_tb;
    reg [7:0] data;
    reg select;
    wire [7:0] result0;
    wire [7:0] result1;

    demux DEMUX (
        .data(data),
        .select(select),
        .result0(result0),
        .result1(result1)
    );

    integer log_file;

    initial begin
        log_file = $fopen("log/demux.log", "w");
        $fdisplay(log_file, "data\t\t\tselect\tresult0\t\tresult1\n");

        data = 0;
        
        repeat (2**8) begin
            select = 0;
            #1 $fdisplay(log_file, "%b\t\t%b\t\t%b\t\t%b", data, select, result0, result1);
            select = 1;
            #1 $fdisplay(log_file, "%b\t\t%b\t\t%b\t\t%b", data, select, result0, result1);
            data = data + 1;
        end
        
        $fclose(log_file);
        $finish;
    end

endmodule