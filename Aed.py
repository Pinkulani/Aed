# © 2025 Pinkulani

import subprocess, platform, sys, os

BuildCustom = False

print("Aed © Pinkulani")

def Version():
    print("Aed - Experimental")

def GetConfig() -> str:
    try:
        with open("Config.aed", "r") as File: # Save configuration
            Config = []
            for Line in File:
                Config.append(Line.strip()) # Remove newline character
    except PermissionError:
        print("Insufficient permission.")
        sys.exit(1)
    except FileNotFoundError:
        print("Build file not found.")
        sys.exit(1)
    return Config

def GetFiles(Extension: str) -> str: # Automatic
    Files = [] # Source files
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(Extension):
                Files.append(os.path.join(root, file))
    return Files

def GetFilesCustom() -> str: # From text file
    Files = []
    try:
        with open("Custom.aed", "r") as File:
            for Line in File:
                Files.append(Line.strip())
    except PermissionError:
        print("Insufficient permission.")
        sys.exit(1)
    except FileNotFoundError:
        print("Custom build file not found.")
        sys.exit(1)
    return Files

def Create(): # Creating build folder
    Path = os.getcwd() + "/Build"
    try:
        print("Creating build folder at:", Path)
        os.mkdir(Path)
    except PermissionError:
        print("Insufficient permission.")
        sys.exit(1)
    except FileNotFoundError:
        print("Part of the path doesn't exist.")
        sys.exit(1)

def Build():
    print("Building for platform:", platform.system())
    Config = GetConfig()
    Tool = Config[0]
    Name = Config[1]
    Extension = Config[2]
    Optimization = Config[3]

    Command = Tool + " "
    if (platform.system() == "Windows"):
        Name += ".exe"
    Command += "-o " + Name
    Command += " " + Optimization + " "

    if BuildCustom == True:
        Files = GetFilesCustom()
    else:
        Files = GetFiles(Extension)
    
    for X in range(len(Files)): # Append files
            Command += Files[X] + " "

    try: # Change to build directory, building with absolute paths
        os.chdir(os.getcwd() + "/Build")
    except PermissionError:
        print("Insufficient permission.")
        sys.exit(1)
    except FileNotFoundError:
        print("Build directory doesn't exist.")
        sys.exit(1)

    Result = subprocess.run(Command, shell = True, capture_output = True, text = True)

    print("Command ran:", Command)
    print("Error:", Result.stderr)

def ActivateCustom():
    global BuildCustom
    BuildCustom = True

# argv = ['Aed.py', 'Command']
if len(sys.argv) == 2:
    match sys.argv[1].lower():
        case "build":
            Build()
        case "create":
            Create()
        case "-v":
            Version()
        case "version":
            Version()
elif len(sys.argv) == 3:
    if sys.argv[1].lower() == "build" and sys.argv[2].lower() == "auto":
        Build()
    if sys.argv[1].lower() == "build" and sys.argv[2].lower() == "custom":
        ActivateCustom()
        Build()
else:
    print("No or invalid arguments given.")
