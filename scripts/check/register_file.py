from .verifier import LogFileVerifier, report

class RegisterFile(LogFileVerifier):
    @report
    def verify(self):
        expected_register_file = [0, 0, 0, 0]
        actual_register_file = [0, 0, 0, 0]

        for test_number, test_case in self.test_cases:
            write_address = int(test_case[0], 2)
            write_data = int(test_case[1], 2)
            expected_register_file[write_address] = write_data

            actual_register_file[0] = int(test_case[2], 2)
            actual_register_file[1] = int(test_case[3], 2)
            actual_register_file[2] = int(test_case[4], 2)
            actual_register_file[3] = int(test_case[5], 2)

            if expected_register_file != actual_register_file:
                message = f'''
                    Actual and expected memory images are not identical
                    for the test case number {test_number}:
                    expected : {[bin(num) for num in expected_register_file]}
                    actual   : {[bin(num) for num in actual_register_file]}
                '''
                return False, message
        
        return True, ''
