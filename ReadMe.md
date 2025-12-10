# Aed

Build files automatically by using Aed or adding your files in a list.

- Supports multiple compilers per config file
- Optimization flag
- Automatic building

## Config structure

- The first line should be your build tool, e.g clang++
- The second line is your app name
- The third line is your programming language's extension (used for finding files automatically)
- The fourth line is your optimization flag
- The fifth line is the language implementation

The config file is called Config.aed, an example is given in the repository.

## Custom building structure

Put all your absolute paths to your files into a file named Custom.aed and run the tool for it to automatically build.

An example of Custom.aed is given in the repository.

## Commands

| Command | Function |
| - | - |
| build | Runs building automatically as per config file |
| create | Creates a build folder in the current directory named "Build" |
| version | Shows Aed's version |
| build auto | Builds automatically |
| build custom | Builds files as specified in your Custom.aed |
