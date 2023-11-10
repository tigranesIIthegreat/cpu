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

project_abs_path = os.path.dirname(os.path.abspath(__file__))

def corresponding_path(path, root):
    path_from_project = os.path.relpath(path, project_abs_path)
    relpath = path_from_project.split('/', 1)[1] if len(path_from_project) == 1 else path_from_project
    return os.path.join(root, relpath)

def change_extension(file_path, new_extension):
    return os.path.splitext(file_path)[0] + new_extension

def generate_log_filesystem():
    log_root_path = os.path.join(project_abs_path, Path.LOG)
    if not os.path.exists(log_root_path):
        os.makedirs(log_root_path)
    test_abs_path = os.path.join(project_abs_path, Path.TEST)
    for root, _, files in os.walk(test_abs_path):
        for file in files:
            if not file.endswith(Extension.TEST):
                continue
            log_root = corresponding_path(root, log_root_path)
            if not os.path.exists(log_root):
                os.makedirs(log_root)


def generate_vvp_files():
    test_abs_path = os.path.join(project_abs_path, Path.TEST)
    for root, _, files in os.walk(test_abs_path):
        for file in files:
            if not file.endswith(Extension.TEST):
                continue
            test_file_path = os.path.join(root, file)
            vvp_abs_path = os.path.join(project_abs_path, Path.VVP)
            vvp_file_path = change_extension(corresponding_path(test_file_path, vvp_abs_path), Extension.VVP)
            vvp_root = corresponding_path(root, vvp_abs_path)
            if not os.path.exists(vvp_root):
                os.makedirs(vvp_root)
            compile_command = ['iverilog', '-o', vvp_file_path, test_file_path]
            subprocess.run(compile_command)

def run_vvp_files():
    vvp_abs_path = os.path.join(project_abs_path, Path.VVP)
    for root, _, files in os.walk(vvp_abs_path):
        for file in files:
            if not file.endswith('.vvp'):
                continue
            vvp_file_path = os.path.join(root, file)
            command = ['vvp', vvp_file_path]
            subprocess.run(command)
            
generate_log_filesystem()
generate_vvp_files()
run_vvp_files()
