import os


def find_files(suffix, path):
    if len(path) == 0:
        print("Please provide a valid path as input.")
        return

    try:
        current_dir_files = os.listdir(path)
    except FileNotFoundError:
        print("No such file or directory. Please input a valid path.")
        return

    list_files = []

    for item in current_dir_files:
        path = os.path.join(path,item)
        if os.path.isdir(path):
            list_files.extend(find_files(suffix,path))
        elif item.endswith(suffix):
            list_files.append(path)

    return list_files


def main():

    ### Test 1 - correctly finds files ending with c
    print(find_files("c", "/Users/jnorman/workspace/udacity/projects/project1"))

    ### Test 2 - Path is empty - should return an error asking for a valid path
    print(find_files("c", ""))

    ### Test 3 - Path is invalid - should return an error asking for valid path
    print(find_files("c", "invalid//directory"))

    return


if __name__ == "__main__":
    main()