from .verifier import LogFileVerifier, report

class InstructionDecoder(LogFileVerifier):
    @report
    def verify(self):
        for test_number, test_case in self.test_cases:
            instruction = bin(int(test_case[0], 2))[2:].zfill(16)

            actual_op_code = int(test_case[1], 2)
            actual_src_reg = int(test_case[2], 2)
            actual_dst_reg = int(test_case[3], 2)
            actual_memory_or_immediate = int(test_case[4], 2)
            actual_is_alu_operation = int(test_case[5], 2)

            expected_op_code = int(instruction[:4], 2)
            expected_src_reg = int(instruction[4:6], 2)
            expected_dst_reg = int(instruction[6:8], 2)
            expected_memory_or_immediate = int(instruction[8:], 2)
            expected_is_alu_operation = expected_op_code < 10

            if expected_op_code != actual_op_code:
                message = f'''
                    Actual and expected values for 
                    opcode are not identical
                    for the test case number {test_number}:
                    expected : {expected_op_code}
                    actual   : {actual_op_code}
                '''
                return False, message
            
            if expected_src_reg != actual_src_reg:
                message = f'''
                    Actual and expected values for 
                    source register are not identical
                    for the test case number {test_number}:
                    expected : {expected_src_reg}
                    actual   : {actual_src_reg}
                '''
                return False, message
            
            if expected_dst_reg != actual_dst_reg:
                message = f'''
                    Actual and expected values for 
                    destination register are not identical
                    for the test case number {test_number}:
                    expected : {expected_dst_reg}
                    actual   : {actual_dst_reg}
                '''
                return False, message
            
            if expected_memory_or_immediate != actual_memory_or_immediate:
                message = f'''
                    Actual and expected values for 
                    memory address / imediate value 
                    are not identical
                    for the test case number {test_number}:
                    expected : {expected_memory_or_immediate}
                    actual   : {actual_memory_or_immediate}
                '''
                return False, message
            
            if expected_is_alu_operation != actual_is_alu_operation:
                message = f'''
                    Actual and expected values for 
                    is_alu_operation bit
                    are not identical
                    for the test case number {test_number}:
                    expected : {expected_is_alu_operation}
                    actual   : {actual_is_alu_operation}
                '''
                return False, message
            
        return True, ''
    