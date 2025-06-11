# © Pinkulani

import subprocess, platform

print("Building for platform:", platform.system())
if platform.system() == "Windows":
    Tool = "cl "
else:
    Tool = "clang++ " # clang for Unix because of better support for ARM

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

Command = Tool + First + " " # Get compiler command and main file ready
for X in range(len(Files) - 1):
    Command += "Source/" + Files[X + 1] + " " # Add other files and source directory

Command += "-o " + Name # Add name for compilation

if platform.system() == "Windows": # Windows needs .bat for call function which is not supported in PowerShell and globals don't really exist
    Result = subprocess.run(".\Make.bat && "+ Command, shell = True, capture_output = True, text = True)
else:
    Result = subprocess.run(Command, shell = True, capture_output = True, text = True)
    
print("Command ran:", Command)
print("Output: ", Result.stdout)
print("Error: ", Result.stderr)
