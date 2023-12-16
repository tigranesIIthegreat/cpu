from .verifier import LogFileVerifier, report

class Memory(LogFileVerifier):
    @report
    def verify(self):
        expected_memory = [0, 0, 0, 0]
        actual_memory = [0, 0, 0, 0]
        
        for test_line, port_values in self.ports:
            write_address = int(port_values[0], 2)
            write_data = int(port_values[1], 2)
            expected_memory[write_address] = write_data

            actual_memory[0] = int(port_values[2], 2)
            actual_memory[1] = int(port_values[3], 2)
            actual_memory[2] = int(port_values[4], 2)
            actual_memory[3] = int(port_values[5], 2)

            if expected_memory != actual_memory:
                message = f'''
                    Actual and expected memory images are not identical
                    for the test case number {test_line}:
                    expected : {[bin(num) for num in expected_memory]}
                    actual   : {[bin(num) for num in actual_memory]}
                '''
                return False, message
        
        return True, ''
