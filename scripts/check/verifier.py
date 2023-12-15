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
        self._path = path

    @property
    def port_valuess(self) -> list[str]:
        with open(self._path, 'r') as file:
            port_names = file.readline()
            test_line = 1
            for line in file.readlines():  # Skip the header lines
                if test_line < 2: continue
                port_values = line.strip().split('\t\t')
                test_line += 1
                yield test_line, dict(zip(port_names, port_values))
    
    def verify(self):
        raise NotImplementedError