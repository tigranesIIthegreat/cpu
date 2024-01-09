module instruction_register (
    input wire [7:0] program_counter,
    input wire [15:0] memory_read_data,
    output reg [7:0] memory_read_address,
    output reg [15:0] instruction);

    always @(*) begin
        memory_read_address = program_counter;
        instruction = memory_read_data;
    end
endmodule
