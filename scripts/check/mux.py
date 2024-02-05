from .verifier import LogFileVerifier, report

class Mux(LogFileVerifier):
    @report
    def verify(self):
        for test_number, test_case in self.test_cases:
            data0 = int(test_case[0], 2)
            data1 = int(test_case[1], 2)
            select = int(test_case[2], 2)

            actual_result = int(test_case[3], 2)
            expected_result = data1 if select else data0

            if expected_result != actual_result:
                message = f'''
                    Actual and expected results are not identical
                    for the test case number {test_number}:
                    expected : {expected_result}
                    actual   : {actual_result}
                '''
                return False, message

        return True, ''