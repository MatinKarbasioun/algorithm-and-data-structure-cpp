#include "puzzle/puzzle.h"


void puzzleProjects(){
        auto puzzles = std::vector<std::string>{"Fibonacci", "GCC"};
        auto i = 0;
        int choice = 0;
        std::cout << "Please Choose between projects" << std::endl;
        for (auto puzzle: puzzles){
            i++;
            std::cout << i <<"." << puzzle << std::endl;
        }
        std::cin >> choice;

        switch (choice){
            case (1):
                fibonacci_main();
        }
    }


