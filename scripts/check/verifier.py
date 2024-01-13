from colorama import Fore, Style

def report(func):
    def wrapper(*args, **kwargs):
        result, message = func(*args, **kwargs)
        verifier = func.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0]
        check_mark = u'\u2714'
        if result:
            print(f"{Fore.GREEN + Style.BRIGHT}{check_mark}{Style.RESET_ALL}", end='')
        else:
            print(f"{Fore.RED + Style.BRIGHT}{message}{Style.RESET_ALL}", end='')
        print(f" {Fore.YELLOW + Style.BRIGHT}{verifier}")
    return wrapper

class LogFileVerifier:
    def __init__(self, path: str):
        assert path.endswith('.log'), f'{path} is not a log file'
        self._path = path

    @property
    def test_cases(self) -> list[str]:
        with open(self._path, 'r') as file:
            lines = file.readlines()
            test_number = -1
            for line in lines[2:]:  # Skip the header lines
                test_case = line.strip().split('\t\t')
                test_number += 1
                yield test_number, test_case
    
    def verify(self):
        raise NotImplementedError