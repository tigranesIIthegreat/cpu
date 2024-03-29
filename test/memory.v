`include "rtl/memory.v"

module memory_tb;
    parameter CELL_COUNT = 4;
    parameter LINE_WIDTH = 8;

    reg [LINE_WIDTH - 1:0] read_address;
    reg [LINE_WIDTH - 1:0] write_address; 
    reg [LINE_WIDTH - 1:0] write_data;
    reg write_enable;
    reg reset;
    wire [LINE_WIDTH - 1:0] read_data;

    memory #(CELL_COUNT, LINE_WIDTH) MEMORY (
        .read_address(read_address),
        .write_address(write_address),
        .write_data(write_data),
        .write_enable(write_enable),
        .reset(reset),
        .read_data(read_data)
    );

    reg clock = 0;
    always #5 clock = ~clock;
    reg done = 0;
    integer log_file;
    integer i;
    integer j;

    initial begin
        log_file = $fopen("log/memory.log", "w");
        $fdisplay(log_file, "write_address\twrite_data\t\t00\t\t\t\t01\t\t\t\t02\t\t\t\t03\n");

        @(posedge clock);
        while(!done) @(posedge clock);

        $fclose(log_file);
        $finish;
    end

    initial begin
        i = 0;
        j = 0;
        #1 reset = 0;
        #1 reset = 1;
        #1 reset = 0;
        write_enable = 1;

        repeat (1000) begin
            @(posedge clock);
            write_address = i % CELL_COUNT;
            write_data = i % 256;
            $fwrite(log_file, "%b\t\t", write_address);
            $fwrite(log_file, "%b\t\t", write_data);

            j = 0;
            repeat (CELL_COUNT) begin
                read_address = j;
                #1 $fwrite(log_file, "%b\t\t", read_data);
                j = j + 1;
            end
            
            $fdisplay(log_file);
            i = i + 1;
        end
        done = 1;
    end
endmodule