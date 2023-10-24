import os


def display_menu():
    print("Menu:")
    print("\033[1;33m1. List files and directories in a directory\033[0m")
    print("\033[1;36m2. Create a directory\033[0m")
    print("\033[1;31m3. Delete a file or directory\033[0m")
    print("\033[1;32m4. Rename a file or directory\033[0m")
    print("\033[1;34m5. Read the contents of a file\033[0m")
    print("\033[1;35m6. Write to a file\033[0m")
    print("\033[1;37m7. Write to a file and append\033[0m")
    print("\033[1;31m8. Clear the prompt or screen\033[0m")
    print("9. Exit")


def list_files_and_directories(directory):
    try:
        items = os.listdir(directory)
        for item in items:
            print("\033[1;34m" + item + "\033[0m")

    except FileNotFoundError:
        print(f"\033[1;31mDirectory '{directory}' not found. \033[0m")
    except PermissionError:
        print(
            f"\033[1;31mPermission denied for directory '{directory}'.\033[0m")


def create_directory(directory):
    try:
        os.mkdir(directory)
        print(
            f"\033[1;32mDirectory '{directory}' created successfully.\033[0m")
    except FileExistsError:
        print(f"\033[1;31mDirectory '{directory}' already exists.\033[0m")
    except PermissionError:
        print(
            f"\033[1;31mPermission denied for creating directory '{directory}'.\033[0m")


def delete_file_or_directory(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"\033[1;31mFile '{path}' deleted successfully.\033[0m")
        elif os.path.isdir(path):
            os.rmdir(path)
            print(f"\033[1;32mDirectory '{path}' deleted successfully.\033[0m")
    except FileNotFoundError:
        print(f"\033[1;31mFile or directory '{path}' not found.\033[0m")
    except PermissionError:
        print(f"\033[1;31mPermission denied for deleting '{path}'.\033[0m")


def rename_file_or_directory(src, dest):
    try:
        os.rename(src, dest)
        print(f"\033[1;32mRenamed '{src}' to '{dest}' successfully.\033[0m")
    except FileNotFoundError:
        print(f"\033[1;31mFile or directory '{src}' not found.\033[0m")
    except PermissionError:
        print(f"\033[1;31mPermission denied for renaming '{src}'.\033[0m")


def read_file_contents(file_path):
    try:
        with open(file_path, "r") as f:
            contents = f.read()
            print(f"Contents of '{file_path}':")
            print(contents)
    except FileNotFoundError:
        print(f"\033[1;31mFile '{file_path}' not found.\033[0m")
    except PermissionError:
        print(f"\033[1;31mPermission denied for reading '{file_path}'.\033[0m")


def write_to_file(file_path, data):
    try:
        with open(file_path, "w") as file:
            file.write(data)
        print(f"\033[1;32mData written to '{file_path}' successfully.\033[0m")
    except PermissionError:
        print(
            f"\033[1;31mPermission denied for writing to '{file_path}'.\033[0m")


# Write a program to write to a file and append text to the file
def write_to_file_and_append(file_path, data):
    try:
        with open(file_path, "a") as file:
            file.write(data)
        print(f"\033[1;32mData appended to '{file_path}' successfully.\033[0m")
    except PermissionError:
        print(
            f"\033[1;31mPermission denied for appending to '{file_path}'.\033[0m")

# Clear Prompt
# Clear the prompt


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    while True:
        try:
            display_menu()
            choice = input("Enter your choice (1-8): ")

            if choice == "1":
                directory = input("Enter directory path: ")
                list_files_and_directories(directory)
            elif choice == "2":
                directory = input("Enter directory name to create: ")
                create_directory(directory)
            elif choice == "3":
                path = input("Enter file or directory path to delete: ")
                delete_file_or_directory(path)
            elif choice == "4":
                src = input("Enter source path: ")
                dest = input("Enter destination path: ")
                rename_file_or_directory(src, dest)
            elif choice == "5":
                file_path = input("Enter file path to read: ")
                read_file_contents(file_path)
            elif choice == "6":
                file_path = input("Enter file path to write to: ")
                data = input("Enter data to write: ")
                write_to_file(file_path, data)
            elif choice == "7":
                file_path = input("Enter file path to write or append to: ")
                data = input("Enter data to write or append: ")
                write_to_file_and_append(file_path, data)
            elif choice == "8":
                clear()
            elif choice == "9":
                break
            else:
                print(
                    "\033[1;31mInvalid choice. Please select a valid option.\033[0m")
        except KeyboardInterrupt:
            print("\033[1;31m\nExiting...\033[0m")
            break
