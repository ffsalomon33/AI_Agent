import os


def get_files_info(working_directory, directory="."):
    try:
        working_path = os.path.abspath(working_directory)
        full_path = os.path.join(working_path, directory)
        directory_path = os.path.abspath(full_path)
        if not directory_path.startswith(working_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(directory_path):
            return f'Error: "{directory}" is not a directory'
        dirs = os.listdir(directory_path)
        result = ""
        for file in dirs:
            file_path = os.path.join(directory_path, file)
            result += f"{file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}\n"
        return result
    except Exception as e:
        return f"Error: {str(e)}"
