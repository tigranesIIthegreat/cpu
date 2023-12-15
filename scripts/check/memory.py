from .verifier import LogFileVerifier, report

class Memory(LogFileVerifier):
    @report
    def verify(self):
        expected_memory = [0, 0, 0, 0]
        actual_memory = [0, 0, 0, 0]
        
        for test_number, test_case in self.test_cases:
            write_address = int(test_case[0], 2)
            write_data = int(test_case[1], 2)
            expected_memory[write_address] = write_data

            actual_memory[0] = int(test_case[2], 2)
            actual_memory[1] = int(test_case[3], 2)
            actual_memory[2] = int(test_case[4], 2)
            actual_memory[3] = int(test_case[5], 2)

            if expected_memory != actual_memory:
                message = f'''
                    Actual and expected memory images are not identical
                    for the test case number {test_number}:
                    expected : {[bin(num) for num in expected_memory]}
                    actual   : {[bin(num) for num in actual_memory]}
                '''
                return False, message
        
        return True, ''
