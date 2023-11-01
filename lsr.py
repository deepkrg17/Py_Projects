import os

END = "\033[00m  "

for (root, dirs, files) in os.walk("."):
    print(root, ":")
    for dirc in dirs:
        print(f"\033[34m{dirc}", end=END)
    for file in files:
        if os.access(root + "/" + file, os.X_OK):
            print(f"\033[32m{file}", end=END)
        else:
            print(file, end=END)
    print("\n")
