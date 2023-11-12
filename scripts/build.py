import os
import subprocess

class Path(str):
    TEST = 'test'
    VVP = 'vvp'
    LOG = 'log'

class Extension(str):
    TEST = '.v'
    VVP = '.vvp'
    LOG = '.log'

script_directory = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_directory)

def corresponding_path(path, root):
    path_from_project = os.path.relpath(path, project_root)
    relpath = path_from_project.split('/', 1)[1] if len(path_from_project) == 1 else path_from_project
    return os.path.join(root, relpath)

def change_extension(file_path, new_extension):
    return os.path.splitext(file_path)[0] + new_extension

def generate_log_files():
    test_root = os.path.join(project_root, Path.TEST)
    log_root = os.path.join(project_root, Path.LOG)
    for root, _, files in os.walk(test_root):
        for file in files:
            if not file.endswith(Extension.TEST): 
                continue
            file = os.path.relpath(os.path.join(root, file), test_root)
            log_file = change_extension(corresponding_path(file, log_root), Extension.LOG)
            log_file_dir = os.path.dirname(log_file)
            if not os.path.exists(log_file_dir): 
                os.makedirs(log_file_dir)
            if not os.path.exists(log_file): 
                open(log_file, 'w').close()


def compile():
    test_root = os.path.join(project_root, Path.TEST)
    vvp_root = os.path.join(project_root, Path.VVP)
    for root, _, files in os.walk(test_root):
        for file in files:
            if not file.endswith(Extension.TEST): 
                continue
            file = os.path.relpath(os.path.join(root, file), test_root)
            vvp_file = change_extension(corresponding_path(file, vvp_root), Extension.VVP)
            vvp_file_dir = os.path.dirname(vvp_file)
            if not os.path.exists(vvp_file_dir): 
                os.makedirs(vvp_file_dir)
            if not os.path.exists(vvp_file): 
                open(vvp_file, 'w').close()
            subprocess.run(['iverilog', '-o', vvp_file, os.path.join(test_root, file)])

def run():
    vvp_abs_path = os.path.join(project_root, Path.VVP)
    for root, _, files in os.walk(vvp_abs_path):
        for file in files:
            if not file.endswith('.vvp'):
                continue
            vvp_file_path = os.path.join(root, file)
            command = ['vvp', vvp_file_path]
            subprocess.run(command)
            
generate_log_files()
compile()
run()