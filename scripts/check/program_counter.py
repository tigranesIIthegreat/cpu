from .verifier import LogFileVerifier, report

class ProgramCounter(LogFileVerifier):
    @report
    def verify(self):
        expected_result = 0

        for test_line, port_values in self.ports:
            enable = int(port_values[0], 2)
            jump = int(port_values[1], 2)
            jz = int(port_values[2], 2)
            zero_flag = int(port_values[3], 2)
            jump_address = int(port_values[4], 2)
            actual_result = int(port_values[5], 2)

            if enable:
                if jump or jz and zero_flag:
                    expected_result = jump_address
                elif expected_result == 126:
                    expected_result = 0
                else:
                    expected_result += 2

            if expected_result != actual_result:
                message = f'''
                    Actual and expected values for program counter are not identical
                    for the test case number {test_line}:
                    expected : {expected_result}
                    actual   : {actual_result}
                '''
                return False, message
        return True, ''