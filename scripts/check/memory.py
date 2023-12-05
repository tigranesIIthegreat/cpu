from .verifier import LogFileVerifier, report

class Memory(LogFileVerifier):
    @report
    def verify(self):
        expected_memory = [0, 0, 0, 0]
        actual_memory = [0, 0, 0, 0]

        for i in range(0, len(self.test_cases)):
            write_address = int(self.test_cases[i][0], 2)
            write_data = int(self.test_cases[i][1], 2)
            expected_memory[write_address] = write_data

            actual_memory[0] = int(self.test_cases[i][2], 2)
            actual_memory[1] = int(self.test_cases[i][3], 2)
            actual_memory[2] = int(self.test_cases[i][4], 2)
            actual_memory[3] = int(self.test_cases[i][5], 2)

            if expected_memory != actual_memory:
                message = f'''
                    Actual and expected memory images are not identical
                    for the test case number {i}:
                    expected : {[bin(num) for num in expected_memory]}
                    actual   : {[bin(num) for num in actual_memory]}
                '''
                return False, message
        
        return True, ''
