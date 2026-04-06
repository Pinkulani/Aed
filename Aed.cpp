// © 2026 Pinkulani

#include <iostream>
#include <string>
#include <filesystem>
#include <fstream>

bool Custom = false;

void Create() {
    std::filesystem::path Directory = "Build";
    if (std::filesystem::exists(Directory)) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "Creating a build folder in project..." << std::endl;
    }
}

void Config() {

}

int main() {
    Create();
    std::cout << "Aed" << std::endl;
    return 0;
}
