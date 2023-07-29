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

    
class ALULogFileVerifier(LogFileVerifier):
    def verify(self):
        for test_case in self._test_cases:
            A = int(test_case[0], 2)  # binary string to integer for A
            B = int(test_case[1], 2)  # binary string to integer for B
            Sel = int(test_case[2], 2)  # binary string to integer for Sel
                # binary string to integer for Out
            Out = int(test_case[3], 2) if not test_case[3].__contains__('x') else 'x'  
            CarryOut = int(test_case[4], 2)  # binary string to integer for CarryOut

            out = (256 + Out if CarryOut else Out) if Out != 'x' else 'x'
            operationString = 'op'
            real = 0
            assertionStatement = True

            if Sel == 0: # addition
                real = A + B
                operationString = f'{A} + {B}'
                assertionStatement = (real - out) % 256 == 0

            elif Sel == 1: # subtraction
                real = A - B
                operationString = f'{A} - {B}'
                assertionStatement = (real - out) % 256 == 0

            elif Sel == 2: # multiplication
                real = A * B
                operationString = f'{A} * {B}'
                assertionStatement = (real - out) % 256 == 0

            elif Sel == 3: # division
                if B == 0:
                    assertionStatement = Out == 'x'
                    assertionMessage = f'{A} / {B} must be \'x\', but Out is {out}'
                else:
                    real = A // B
                    operationString = f'{A} / {B}'
                    assertionStatement = (real - out) % 256 == 0

            elif Sel == 4: # shift left by 1 (A)
                real = A * 2 % 256
                operationString = f'{A} << 1'
                assertionStatement = (real - out) % 256 == 0

            elif Sel == 5: # shift right by 1 (A)
                real = A // 2
                operationString = f'{A} >> 1'
                assertionStatement = (real - out) % 256 == 0

            elif Sel == 6: # rotate left by 1 (A)
                real = A * 2 % 256 + A // 128
                operationString = f'{A} <<< 1'
                assertionStatement = (real - out) % 256 == 0

            elif Sel == 7: # rotate right by 1 (A)
                real = A // 2 + A % 2 * 128
                operationString = f'{A} >>> 1'
                assertionStatement = (real - out) % 256 == 0
            
            elif Sel == 8: # logical and
                real = A & B
                operationString = f'{A} & {B}'
                assertionStatement = (real - out) % 256 == 0

            elif Sel == 9: # logical or
                real = A | B
                operationString = f'{A} | {B}'
                assertionStatement = (real - out) % 256 == 0

            elif Sel == 10: # logical xor
                real = A ^ B
                operationString = f'{A} ^ {B}'
                assertionStatement = (real - out) % 256 == 0

            elif Sel == 11: # logical nand
                real = ~(A | B)
                operationString = f'~({A} | {B})'
                assertionStatement = (real - out) % 256 == 0

            elif Sel == 12: # logical nor
                real = ~(A & B)
                operationString = f'~({A} & {B})'
                assertionStatement = (real - out) % 256 == 0

            elif Sel == 13: # logical xnor
                real = ~(A ^ B)
                operationString = f'~({A} ^ {B})'
                assertionStatement = (real - out) % 256 == 0

            elif Sel == 14: # greater comparision
                real = 1 if A > B else 0
                operationString = f'{A} > {B}'
                assertionStatement = (real - out) % 256 == 0

            elif Sel == 15: # equal comparision
                real = 1 if A == B else 0
                operationString = f'{A} == {B}'
                assertionStatement = (real - out) % 256 == 0

            assertionMessage = f'{operationString} must be {real}, but out is {out}'
            assert assertionStatement, assertionMessage

ALULogFileVerifier('log/core/alu.log').verify()
