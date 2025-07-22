import os


def write_file(working_directory, file_path, content):
    try:
        working_path = os.path.abspath(working_directory)
        file_path_full = os.path.join(working_path, file_path)
        if not file_path_full.startswith(working_path):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(file_path_full):
            os.makedirs(os.path.dirname(file_path_full), exist_ok=True)   
        with open(file_path_full, "w") as f:
            f.write(content)
        result = f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        return result
    except Exception as e:
        return f"Error: {str(e)}"