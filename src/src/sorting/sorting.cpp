//
// Created by karba on 8/16/2024.
//
#include <vector>
#include <string>
#include <iostream>
#include "sorting/quick_sort.h"


using std::vector;
using std::cout;
using std::cin;
using std::string;

namespace sorting_std{
    vector<int> input(){
        int n;
        cout << "Please specify the number of elements in array:" << "\n";
        cin >> n;
        cout << "Please input elements and divide them with space:" << '\n';
        vector<int> unsorted_array(n);
        for (int & i : unsorted_array) {
            cin >> i;
        }

        return unsorted_array;
    }

    void output(vector<int> & sorted_array){

        cout << "Sorted elements" << '\n';
        for (auto element: sorted_array){
            cout << element << " ";
        }
    }
}

void sorting(){

    auto unsorted_array = sorting_std::input();
    auto sorting_types = vector<string>{"quick", "heap", "bubble", "selection", "merge", "shell", "radix"};
    auto i = 0;
    int choice = 0;
    std::cout << "Please Choose between projects" << std::endl;
    for (const auto& puzzle: sorting_types){
        i++;
        std::cout << i <<"." << puzzle << std::endl;
    }
    std::cin >> choice;

    switch (choice){
        case (1):
            quick_sort(unsorted_array);

        case(2):
            nullptr;

        default:
            quick_sort(unsorted_array);
    }

    sorting_std::output(unsorted_array);
}