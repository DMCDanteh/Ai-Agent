import os

def get_files_info(working_directory, directory="."):
    try:
        working_directory = os.path.abspath(working_directory)
        file_path = os.path.abspath(os.path.join(working_directory, directory))
        if not file_path.startswith(working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(file_path):
            return f'Error: "{directory}" is not a directory'
        
        contents = os.listdir(file_path)
        lines = []
        for entry in contents:
            entry_path = os.path.join(file_path, entry)
            size = os.path.getsize(entry_path)
            is_dir = os.path.isdir(entry_path)
            line = f"- {entry}: file_size={size} bytes, is_dir={is_dir}"
            lines.append(line)
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"    