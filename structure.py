import os

def print_directory_structure(path, indentation_level=0):
    for entry in os.scandir(path):
        if entry.is_file():
            print("│" + "   " * indentation_level + "├──", entry.name)
        elif entry.is_dir():
            print("│" + "   " * indentation_level + "├──", entry.name + "/")
            print_directory_structure(entry.path, indentation_level + 1)

if __name__ == "__main__":
    print_directory_structure("src")