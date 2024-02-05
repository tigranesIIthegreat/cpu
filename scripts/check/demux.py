from .verifier import LogFileVerifier, report

class Demux(LogFileVerifier):
    @report
    def verify(self):
        for test_number, test_case in self.test_cases:
            data = int(test_case[0], 2)
            select = int(test_case[1], 2)
            actual_result_0 = int(test_case[2], 2)
            actual_result_1 = int(test_case[3], 2)

            expected_result_0 = 0 if select else data
            expected_result_1 = 0 if not select else data

            if expected_result_0 != actual_result_0:
                message = f'''
                    Actual and expected results are not identical
                    for the test case number {test_number}:
                    expected result0 : {expected_result_0}
                    actual result0   : {actual_result_0}
                    {data}, {select}
                '''
                return False, message

            if expected_result_1 != actual_result_1:
                message = f'''
                    Actual and expected results are not identical
                    for the test case number {test_number}:
                    expected result1 : {expected_result_1}
                    actual result1   : {actual_result_1}
                '''
                return False, message

        return True, ''