module zero_flag(input wire value, output reg result);
    always @(*) begin
        result = value;
    end
endmodule