from colorama import Fore, Style

def report(func):
    def wrapper(*args, **kwargs):
        result, message = func(*args, **kwargs)
        verifier = func.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0]
        print(f"{Fore.YELLOW + Style.BRIGHT}{verifier} - ", end='')
        check_mark = u'\u2714'
        if result:
            print(f"{Fore.GREEN + Style.BRIGHT}{check_mark}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED + Style.BRIGHT}{message}{Style.RESET_ALL}")
    return wrapper

class LogFileVerifier:
    def __init__(self, path: str):
        assert path.endswith('.log'), f'{path} is not a log file'
        test_cases = []
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines[2:]:  # Skip the header lines
                test_case = line.strip().split('\t\t')
                test_cases.append(test_case)
        self._test_cases = test_cases

    @property
    def test_cases(self) -> list[str]:
        return self._test_cases
    
    def verify(self):
        raise NotImplementedError