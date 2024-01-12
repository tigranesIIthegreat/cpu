module register_file (
    input [1:0] read_address,
    input [1:0] write_address,
    input [7:0] write_data,
    input write_enable,
    input reset,
    output reg [7:0] read_data
    );

    reg [7:0] registers [0:3];

    always @(*) begin
        read_data = registers[read_address];
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