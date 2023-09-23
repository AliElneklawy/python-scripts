import os
import ctypes

def hide_files_by_extension(folder_path, extension):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)

                ctypes.windll.kernel32.SetFileAttributesW(file_path, 2)  # 2 corresponds to hidden

                print(f"Hid {file}")

if __name__ == "__main__":
    folder_path = input('Path to the directory: ')
    extension = input('Extension: ')
    
    hide_files_by_extension(folder_path, extension)
