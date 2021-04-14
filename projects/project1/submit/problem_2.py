import os


def find_files(suffix, path):
    list_files = []
    current_dir_files = os.listdir(path)

    for item in current_dir_files:
        path = os.path.join(path,item)
        if os.path.isdir(path):
            list_files.extend(find_files(suffix,path))
        elif item.endswith(suffix):
            list_files.append(path)

    return list_files


def main():
    print(find_files("c", "/testdir"))
    return


if __name__ == "__main__":
    main()