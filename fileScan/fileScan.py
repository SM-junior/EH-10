import os

def fileScan(path):
    print(f'scanning...{path}')
    result=[]

    for roots, dirs, files in os.walk(path):
        for folder in dirs:
            result.append(folder)
            print(f'folder: {folder}')
        for file in files:
            result.append(file)
            print(f'file: {file}')

        return '\n'.join(result)

scanFolder=input('enter the folder to be scan: ')

if not scanFolder:
    scanFolder='.'

if os.path.exists(scanFolder):
    foundResult=fileScan(scanFolder)
    with open('foundFile.txt', 'w') as file:
        file.write(f'{foundResult}')
        print('all folders and directories are saved.')

else:
    print('Folder does not exists.')


import os

def fileScan(path, extension=None):
    print(f'scanning...{path}\n')

    result = []

    for root, dirs, files in os.walk(path):
        for folder in dirs:
            result.append(f'folder: {os.path.join(root, folder)}')
        for file in files:
            if extension:
                if file.lower().endswith(extension.lower()):
                    result.append(f'file: {os.path.join(root, file)}')
            else:
                result.append(f'file: {os.path.join(root, file)}')

    return result  # Moved outside the loop!

scanFolder = input('Enter the path to scan: ').strip()
extension = input('Enter the extension: (eg: .txt .py etc): ').strip()

if not scanFolder:
    scanFolder = '.'

if os.path.exists(scanFolder):
    final = fileScan(scanFolder, extension)
    for item in final:
        print(item)
    # Optional: save to file
    # with open("scan_result.txt", "w") as f:
    #     for item in final:
    #         f.write(item + "\n")
    # print("\nResults saved to scan_result.txt")
else:
    print('Path does not exist.')




#...................find specific file in a path...................ok
import os

def findFile(path, exact_filename):
    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == exact_filename:
                full_path = os.path.join(root, file)
                result.append(full_path)
    return result

# Input
search_path = input("Enter the folder to search in: ").strip()
filename = input("Enter the exact file name (e.g., test.py): ").strip()

# Default to current folder if nothing provided
if not search_path:
    search_path = '.'

# Check if path exists
if os.path.exists(search_path):
    results = findFile(search_path, filename)
    if results:
        print("File found at:")
        for path in results:
            print(path)
    else:
        print("File not found.")
else:
    print("The path does not exist.")

