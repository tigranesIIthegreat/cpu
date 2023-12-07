from .verifier import LogFileVerifier, report

class ProgramCounter(LogFileVerifier):
    @report
    def verify(self):
        expected_result = 0

        for i in range(0, len(self.test_cases)):
            enable = int(self.test_cases[i][0], 2)
            jump = int(self.test_cases[i][1], 2)
            jz = int(self.test_cases[i][2], 2)
            zero_flag = int(self.test_cases[i][3], 2)
            jump_address = int(self.test_cases[i][4], 2)
            actual_result = int(self.test_cases[i][5], 2)

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
                    for the test case number {i}:
                    expected : {expected_result}
                    actual   : {actual_result}
                '''
                return False, message
        return True, ''