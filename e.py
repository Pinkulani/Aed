# © Pinkulani

import os, subprocess, platform

for root, dirs, files in os.walk(r"C:\Users\Emilia\Desktop\LemonPy"):
    for file in files:
        if file.endswith(".py"):
            print(os.path.join(root, file))

            print("Building for platform:", platform.system())
if platform.system() == "Windows":
    Tool = "cl "
else:
    Tool = "clang++ " # clang for Unix because of better support for ARM