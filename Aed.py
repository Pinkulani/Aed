# © Pinkulani

import subprocess, platform

print("Building for platform:", platform.system())

Files = []
with open("Build.aed", "r") as File:
    for Line in File:
        Files.append(Line.strip()) # Removes newline character

First = Files[0] # Save main file
Name = ""
for Character in First: # Get program name
    if Character == ".":
        break
    else:
        Name += Character

Command = "clang++ " + First + " " # Get compiler command and main file ready
for X in range(len(Files) - 1):
    Command += "Source/" + Files[X + 1] + " " # Add other files and source directory

Command += "-o " + Name # Add name for compilation

print("Command ran:", Command)
Result = subprocess.run(Command, shell = True, capture_output = True, text = True)
print("Output: ", Result.stdout)
print("Error: ", Result.stderr)
