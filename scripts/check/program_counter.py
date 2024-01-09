from .verifier import LogFileVerifier, report

class ProgramCounter(LogFileVerifier):
    @report
    def verify(self):
        expected_result = 0

        for test_number, test_case in self.test_cases:
            enable = int(test_case[0], 2)
            jump = int(test_case[1], 2)
            jz = int(test_case[2], 2)
            zero_flag = int(test_case[3], 2)
            jump_address = int(test_case[4], 2)
            actual_result = int(test_case[5], 2)

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
                    for the test case number {test_number}:
                    expected : {expected_result}
                    actual   : {actual_result}
                '''
                return False, message
        return True, ''