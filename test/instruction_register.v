`include "rtl/instruction_register.v"
`include "rtl/memory.v"

module instruction_register_tb;
    parameter MEMORY_CELL_COUNT = 256;
    parameter MEMORY_LINE_WIDTH = 16;
    parameter MEMORY_ADDRESS_WIDTH = 8;

    reg [MEMORY_ADDRESS_WIDTH - 1:0] program_counter;
    reg [MEMORY_ADDRESS_WIDTH - 1:0] write_address;
    reg [MEMORY_LINE_WIDTH - 1:0] write_data;
    reg write_enable;
    reg reset;

    wire [MEMORY_ADDRESS_WIDTH - 1:0] read_address;
    wire [MEMORY_LINE_WIDTH - 1:0] read_data;

    wire [MEMORY_LINE_WIDTH - 1:0] instruction;

    memory #(MEMORY_CELL_COUNT, MEMORY_LINE_WIDTH) MEMORY (
        .read_address(read_address),
        .write_address(write_address),
        .write_data(write_data),
        .write_enable(write_enable),
        .reset(reset),
        .read_data(read_data)
    );

    instruction_register INSTRUCTION_REGISTER (
        .program_counter(program_counter),
        .memory_read_data(read_data),
        .memory_read_address(read_address),
        .instruction(instruction)
    );

    reg clock;
    reg done = 0;
    integer log_file;
    integer i;

    initial begin
        log_file = $fopen("log/instruction_register.log", "w");
        $fdisplay(log_file, "program_counter\tinstruction\n");

        @(posedge clock);
        while(!done) @(posedge clock);

        $fclose(log_file);
        $finish;
    end

    initial begin
        i = 0;
        #1 reset = 0;
        #1 reset = 1;
        #1 reset = 0;
        write_enable = 1;

        repeat (MEMORY_CELL_COUNT) begin
            #5 clock = 0;
            write_address = i;
            write_data = 3 * i + 1;
            i = i + 1;
            #5 clock = 1;
        end

        write_enable = 0;
        write_address = 8'b0;
        write_data = 8'b0;

        program_counter = 0;

        repeat (MEMORY_CELL_COUNT) begin
            #5 clock = 0;
            #5 clock = 1;
            $fdisplay(log_file, "%b\t\t%b", program_counter, instruction);
            program_counter = program_counter + 1;
        end

        done = 1;
        $finish;
    end
endmodule
