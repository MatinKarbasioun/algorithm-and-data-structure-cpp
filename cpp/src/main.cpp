#include <iostream>
#include <string>
#include "puzzle/puzzle.h"


int main() {
    std::string choice;
    std::cout << "Choose an algorithm to run:" << std::endl;
    std::cout << "1. Puzzle" << std::endl;
    std::cout << "2. Greedy" << std::endl;
    std::cout << "3. Dynamic Programming" << std::endl;
    std::cout << "Enter the name or number: ";
    std::cin >> choice;

    if (choice == "1" || choice == "Puzzle") 
    {
        puzzleProjects();
        return 0;
    } else if (choice == "2" || choice == "Greedy") {
        return 0;
    } else if (choice == "3" || choice == "Dynamic" || choice == "Dynamic Programming") {
        return 0;
    } else {
        std::cout << "Invalid choice." << std::endl;
        return 1;
    }
}
