from .verifier import LogFileVerifier, report

class InstructionRegister(LogFileVerifier):
    @report
    def verify(self):
        for test_number, test_case in self.test_cases:
            program_counter = int(test_case[0], 2)
            actual_instruction = int(test_case[1], 2)
            expected_instruction = 3 * program_counter + 1

            if actual_instruction != expected_instruction:
                message = f'''
                    Actual and expected values for
                    instruction are not identical
                    for the test case number {test_number}:
                    expected : {expected_instruction}
                    actual   : {actual_instruction}
                '''
                return False, message
        return True, ''
