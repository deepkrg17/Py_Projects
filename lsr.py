import os
for (root, dirs, files) in os.walk("."):
    print(root, ":")
    for dir in dirs:
            print(f"\033[95m{dir}\033[00m", end="  ")
    for file in files:
            if os.access(root + "/" + file, os.X_OK):
                print(f"\033[92m{file}\033[00m", end="  ")
            else:
                print(f"\033[96m{file}\033[00m", end="  ")
    print("\n")
