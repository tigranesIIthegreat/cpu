from check.alu import ALU
from check.demux import Demux
from check.instruction_decoder import InstructionDecoder
from check.instruction_register import InstructionRegister
from check.memory import Memory
from check.mux import Mux
from check.program_counter import ProgramCounter
from check.register_file import RegisterFile
from check.zero_flag import ZeroFlag

import os
import subprocess
from colorama import Fore, Style

class Path(str):
    TEST = 'test'
    VVP = 'vvp'
    LOG = 'log'

class Extension(str):
    TEST = '.v'
    VVP = '.vvp'
    LOG = '.log'

_script_directory = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(_script_directory)

def _corresponding_path(path, root):
    path_from_project = os.path.relpath(path, _project_root)
    relpath = path_from_project.split('/', 1)[1] if len(path_from_project) == 1 else path_from_project
    return os.path.join(root, relpath)

def _change_extension(file_path, new_extension):
    return os.path.splitext(file_path)[0] + new_extension

def _generate_log_files():
    test_root = os.path.join(_project_root, Path.TEST)
    log_root = os.path.join(_project_root, Path.LOG)
    for root, _, files in os.walk(test_root):
        for file in files:
            if not file.endswith(Extension.TEST): 
                continue
            file = os.path.relpath(os.path.join(root, file), test_root)
            log_file = _change_extension(_corresponding_path(file, log_root), Extension.LOG)
            log_file_dir = os.path.dirname(log_file)
            if not os.path.exists(log_file_dir): 
                os.makedirs(log_file_dir)
            if not os.path.exists(log_file): 
                open(log_file, 'w').close()

def _run_command(command: list):
    print(f"{Fore.YELLOW + Style.BRIGHT}COMMAND |{Style.RESET_ALL}", ' '.join(command))
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.stdout:
        print(f"{Fore.YELLOW + Style.BRIGHT} STDOUT |{Style.RESET_ALL}", result.stdout, end='')
    if result.stderr:
        print(f"{Fore.YELLOW + Style.BRIGHT} STDERR |{Style.RESET_ALL}", result.stderr, end='')

    print(f"{Fore.YELLOW + Style.BRIGHT} STATUS |", end='')
    print(f"{Fore.RED} FAIL" if result.returncode else f"{Fore.GREEN} SUCCESS")
    console_width = os.get_terminal_size().columns
    print(f"{Fore.YELLOW + Style.NORMAL}{'-' * 8}{Style.BRIGHT}|{Style.NORMAL}{'-' * (console_width - 9)}{Style.RESET_ALL}")


def compile():
    _generate_log_files()
    test_root = os.path.join(_project_root, Path.TEST)
    vvp_root = os.path.join(_project_root, Path.VVP)
    for root, _, files in os.walk(test_root):
        for file in files:
            if not file.endswith(Extension.TEST): 
                continue
            file = os.path.relpath(os.path.join(root, file), test_root)
            vvp_file = _change_extension(_corresponding_path(file, vvp_root), Extension.VVP)
            vvp_file_dir = os.path.dirname(vvp_file)
            if not os.path.exists(vvp_file_dir): 
                os.makedirs(vvp_file_dir)
            if not os.path.exists(vvp_file): 
                open(vvp_file, 'w').close()
            _run_command(['iverilog', '-o', vvp_file, os.path.join(test_root, file)])

def run():
    vvp_abs_path = os.path.join(_project_root, Path.VVP)
    for root, _, files in os.walk(vvp_abs_path):
        for file in files:
            if not file.endswith('.vvp'):
                continue
            vvp_file_path = os.path.join(root, file)
            _run_command(['vvp', vvp_file_path])

def check():
    ALU('log/alu.log').verify()
    Demux('log/demux.log').verify()
    InstructionDecoder('log/instruction_decoder.log').verify()
    InstructionRegister('log/instruction_register.log').verify()
    Memory('log/memory.log').verify()
    Mux('log/mux.log').verify()
    ProgramCounter('log/program_counter.log').verify()
    RegisterFile('log/register_file.log').verify()
    ZeroFlag('log/zero_flag.log').verify()

if __name__ == '__main__':     
    compile()
    run()
    check()