from .verifier import LogFileVerifier, report

class ALU(LogFileVerifier):
    @report
    def verify(self):
        for test_number, test_case in self.test_cases:
            operand1 = int(test_case[0], 2)  # binary string to integer for operand1
            operand2 = int(test_case[1], 2)  # binary string to integer for operand2
            op_code = int(test_case[2], 2)  # binary string to integer for op_code

            # binary string to integer for result
            result = int(test_case[3], 2) if not test_case[3].__contains__('x') else 'x'

            # binary string to integer for zero_flag
            zero_flag = int(test_case[4], 2) if test_case[4] != 'x' else 'x'

            if op_code == 0: # addition
                real = operand1 + operand2
                operationString = f'add {operand1} {operand2}'
                success = (real - result) % 256 == 0

            elif op_code == 1: # subtraction
                real = operand1 - operand2
                operationString = f'sub {operand1} {operand2}'
                success = (real - result) % 256 == 0

            elif op_code == 2: # incrementation
                real = operand1 + 1
                operationString = f'inc {operand1}'
                success = (real - result) % 256 == 0

            elif op_code == 3: # decrementation
                real = operand1 - 1
                operationString = f'dec {operand1}'
                success = (real - result) % 256 == 0

            elif op_code == 4: # logical and
                real = operand1 & operand2
                operationString = f'and {operand1} {operand2}'
                success = (real - result) % 256 == 0

            elif op_code == 5: # logical or
                real = operand1 | operand2
                operationString = f'or {operand1} {operand2}'
                success = (real - result) % 256 == 0

            elif op_code == 6: # logical xor
                real = operand1 ^ operand2
                operationString = f'xor {operand1} {operand2}'
                success = (real - result) % 256 == 0

            elif op_code == 7: # shift left by 1 (operand1)
                real = operand1 * 2 % 256
                operationString = f'shleft {operand1}'
                success = (real - result) % 256 == 0

            elif op_code == 8: # shift right by 1 (operand1)
                real = operand1 // 2
                operationString = f'shright {operand1}'
                success = (real - result) % 256 == 0

            elif op_code == 9: # equal comparision
                real = 1 if operand1 == operand2 else 0
                operationString = f'cmp {operand1} {operand2}'
                success = real == zero_flag

            errorMessage = f'''
                {operationString} must be {real}, but result is {result}
                in the test case number {test_number}
            '''
            if not success: return False, errorMessage
        return True, ''
