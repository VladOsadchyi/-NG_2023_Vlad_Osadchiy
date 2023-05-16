import os
import argparse
def find_files(folder, filename):
    found_files = []
    if not os.path.isdir(folder):
        print("Invalid folder path. Please provide a valid folder path.")
        return found_files
    for file in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, file)) and file == filename:
            found_files.append(os.path.join(folder, file))
    return found_files
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder")
    parser.add_argument("--file")
    args = parser.parse_args()
    folder = args.folder or input("Enter the path to your folder: ")
    filename = args.file or input("Enter the name of your file: ")
    if not folder or not filename:
        print("Please provide the folder and file name.")
        return
    found_files = find_files(folder, filename)
    if found_files:
        print("Found files:")
        for file in found_files:
            print(file)
    else:
        print("No files found")
        return
main()
