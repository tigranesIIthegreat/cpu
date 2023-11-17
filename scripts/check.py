class LogFileVerifier:
    def __init__(self, path: str):
        assert path.endswith('.log'), f'{path} is not a log file'
        test_cases = []
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines[2:]:  # Skip the header lines
                test_case = line.strip().split('\t')
                test_cases.append(test_case)
        self._test_cases = test_cases

    @property
    def test_cases(self) -> list[str]:
        return self._test_cases
    
    def verify(self):
        raise NotImplementedError

    
class operand1LULogFileVerifier(LogFileVerifier):
    def verify(self):
        for test_case in self._test_cases:
            operand1 = int(test_case[0], 2)  # binary string to integer for operand1
            operand2 = int(test_case[1], 2)  # binary string to integer for operand2
            opCode = int(test_case[2], 2)  # binary string to integer for opCode
                # binary string to integer for result
            result = int(test_case[3], 2) if not test_case[3].__contains__('x') else 'x'  
            Carryresult = int(test_case[4], 2)  # binary string to integer for Carryresult

            out = (256 + result if Carryresult else result) if result != 'x' else 'x'
            operationString = 'op'
            real = 0
            assertionStatement = True

            if opCode == 0: # addition
                real = operand1 + operand2
                operationString = f'{operand1} + {operand2}'
                assertionStatement = (real - out) % 256 == 0

            elif opCode == 1: # subtraction
                real = operand1 - operand2
                operationString = f'{operand1} - {operand2}'
                assertionStatement = (real - out) % 256 == 0

            elif opCode == 2: # multiplication
                real = operand1 * operand2
                operationString = f'{operand1} * {operand2}'
                assertionStatement = (real - out) % 256 == 0

            elif opCode == 3: # division
                if operand2 == 0:
                    assertionStatement = result == 'x'
                    assertionMessage = f'{operand1} / {operand2} must be \'x\', but result is {out}'
                else:
                    real = operand1 // operand2
                    operationString = f'{operand1} / {operand2}'
                    assertionStatement = (real - out) % 256 == 0

            elif opCode == 4: # shift left by 1 (operand1)
                real = operand1 * 2 % 256
                operationString = f'{operand1} << 1'
                assertionStatement = (real - out) % 256 == 0

            elif opCode == 5: # shift right by 1 (operand1)
                real = operand1 // 2
                operationString = f'{operand1} >> 1'
                assertionStatement = (real - out) % 256 == 0

            elif opCode == 6: # rotate left by 1 (operand1)
                real = operand1 * 2 % 256 + operand1 // 128
                operationString = f'{operand1} <<< 1'
                assertionStatement = (real - out) % 256 == 0

            elif opCode == 7: # rotate right by 1 (operand1)
                real = operand1 // 2 + operand1 % 2 * 128
                operationString = f'{operand1} >>> 1'
                assertionStatement = (real - out) % 256 == 0
            
            elif opCode == 8: # logical and
                real = operand1 & operand2
                operationString = f'{operand1} & {operand2}'
                assertionStatement = (real - out) % 256 == 0

            elif opCode == 9: # logical or
                real = operand1 | operand2
                operationString = f'{operand1} | {operand2}'
                assertionStatement = (real - out) % 256 == 0

            elif opCode == 10: # logical xor
                real = operand1 ^ operand2
                operationString = f'{operand1} ^ {operand2}'
                assertionStatement = (real - out) % 256 == 0

            elif opCode == 11: # logical nand
                real = ~(operand1 | operand2)
                operationString = f'~({operand1} | {operand2})'
                assertionStatement = (real - out) % 256 == 0

            elif opCode == 12: # logical nor
                real = ~(operand1 & operand2)
                operationString = f'~({operand1} & {operand2})'
                assertionStatement = (real - out) % 256 == 0

            elif opCode == 13: # logical xnor
                real = ~(operand1 ^ operand2)
                operationString = f'~({operand1} ^ {operand2})'
                assertionStatement = (real - out) % 256 == 0

            elif opCode == 14: # greater comparision
                real = 1 if operand1 > operand2 else 0
                operationString = f'{operand1} > {operand2}'
                assertionStatement = (real - out) % 256 == 0

            elif opCode == 15: # equal comparision
                real = 1 if operand1 == operand2 else 0
                operationString = f'{operand1} == {operand2}'
                assertionStatement = (real - out) % 256 == 0

            assertionMessage = f'{operationString} must be {real}, but out is {out}'
            assert assertionStatement, assertionMessage

operand1LULogFileVerifier('log/alu.log').verify()
