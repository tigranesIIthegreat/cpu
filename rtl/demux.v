module demux(
    input [7:0] data,
    input select,
    output reg [7:0] result0,
    output reg [7:0] result1);

    always @(select or data) begin
        if (select) begin
            result0 = 0;
            result1 = data;
        end else begin
            result0 = data;
            result1 = 0;
        end
    end
endmodule