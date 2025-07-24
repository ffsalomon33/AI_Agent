import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    try:
        working_path = os.path.abspath(working_directory)
        file_path_full = os.path.abspath(os.path.join(working_path, file_path))
        if not file_path_full.startswith(working_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(file_path_full):
            return f'Error: File "{file_path}" not found.'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        try:
            python_args = ["python", file_path_full]
            if args:
                python_args.extend(args)
            complete_process = subprocess.run(python_args, timeout=30, capture_output=True)
        except Exception as e:
            return f"Error: executing Python file: {e}"
        result = ""
        if complete_process.stdout:
            result += f"STDOUT: {complete_process.stdout}\n"
        if complete_process.stderr:
            result += f"STDERR: {complete_process.stderr}\n"
        if complete_process.returncode != 0:
            result += f"Process exited with code {complete_process.returncode}"
        if result == "":
            return "No output produced"
        else:
            return result
    except Exception as e:
        return f"Error: {str(e)}"