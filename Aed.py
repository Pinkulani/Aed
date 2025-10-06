# © 2025 Pinkulani

import subprocess, platform, os

print("Aed © Pinkulani")

try:
    with open("Build.aed", "r") as File: # Save configuration
        Config = []
        for Line in File:
            Config.append(Line.strip()) # Remove newline character
        Tool = Config[0]
        Name = Config[1]
        Extension = Config[2]
except FileNotFoundError:
    print("Build file not found.")

def GetFiles():
    Files = [] # Source files
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(Extension):
                Files.append(os.path.join(root, file))
    return Files

print("Building for platform:", platform.system())
Command = Tool + " "
Files = GetFiles()
for X in range(len(Files)):
    Command += Files[X] + " "
Command += "-o " + Name

Result = subprocess.run(Command, shell = True, capture_output = True, text = True)

print("Command ran:", Command)
print("Error:", Result.stderr)
