`include "rtl/register_file.v"

module register_file_tb;
    reg [1:0] read_address_1;
    reg [1:0] read_address_2;
    reg [1:0] write_address;
    reg [7:0] write_data;
    reg write_enable;
    reg reset;
    wire [7:0] read_data_1;
    wire [7:0] read_data_2;

    register_file GPR (
        .read_address_1(read_address_1),
        .read_address_2(read_address_2),
        .write_address(write_address),
        .write_data(write_data),
        .write_enable(write_enable),
        .reset(reset),
        .read_data_1(read_data_1),
        .read_data_2(read_data_2)
    );

    reg clock = 0;
    always #5 clock = ~clock;
    reg done = 0;
    integer log_file;
    integer i;
    integer j;

    initial begin
        log_file = $fopen("log/register_file.log", "w");
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
            write_address = i % 4;
            write_data = i % 256;
            $fwrite(log_file, "%b\t\t", write_address);
            $fwrite(log_file, "%b\t\t", write_data);

            j = 0;
            repeat (2) begin
                read_address_1 = j;
                read_address_2 = j + 1;
                #1 $fwrite(log_file, "%b\t\t%b\t\t", read_data_1, read_data_2);
                j = j + 2;
            end

            $fdisplay(log_file);
            i = i + 1;
        end
        done = 1;
    end
endmodule