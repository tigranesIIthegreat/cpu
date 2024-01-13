from .verifier import LogFileVerifier, report

class ZeroFlag(LogFileVerifier):
    @report
    def verify(self):
        for test_number, test_case in self.test_cases:
            value = int(test_case[0], 2)
            result = int(test_case[1], 2)
            if value != result:
                message = f'''
                    Actual and expected values for zero_flag are not identical
                    for the test case number {test_number}:
                    expected : {[bin(value)]}
                    actual   : {[bin(result)]}
                '''
                return False, message
        return True, ''