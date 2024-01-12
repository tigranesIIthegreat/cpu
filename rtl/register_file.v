module register_file (
    input [1:0] read_address_1,
    input [1:0] read_address_2,
    input [1:0] write_address,
    input [7:0] write_data,
    input write_enable,
    input reset,
    output reg [7:0] read_data_1,
    output reg [7:0] read_data_2
    );

    reg [7:0] registers [0:3];

    always @(*) begin
        read_data_1 = registers[read_address_1];
        read_data_2 = registers[read_address_2];
    end

    integer i;
    always @(*) begin
        if (reset) begin
            for (i = 0; i < 4; i = i + 1) begin
                registers[i] <= 8'h00;
            end
        end else begin
            if (write_enable) begin
                registers[write_address] <= write_data;
            end
        end
    end
endmodule