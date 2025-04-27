//
// Created by karba on 8/16/2024.
//
#include <vector>
#include <iostream>
#include "sorting/quick_sort.h"


using std::vector;
using std::cin;
using std::cout;


void swap_value(vector<int> &a, int position, int swap_index){
    auto value = a[position];
    a[position] = a[swap_index];
    a[swap_index] = value;
}

int make_partition(vector<int> &a, int left, int right){
    auto value = a[left];
    auto index = left + 1;
    auto swap = false;

    for (auto i = index; i < right; i++){
        if (a[i] <= value){
            if (swap) {
                swap_value(a, index, i);
            }
            index++;
        }
        else{
            swap = true;
        }
    }
    swap_value(a, left, index-1);
    return index-1;
}

void sort(vector<int> &a, int left, int right){
    if (left >= right){
        return;
    }
    auto index = make_partition(a, left, right);
    sort(a, left, index);
    sort(a, index + 1, right);
}

void quick_sort(vector<int> &a){
    sort(a, 0, a.size());
}


/*
int main() {
    int n;
    cout << "Please specify the number of elements in array:" << "\n";
    cin >> n;
    cout << "Please input elements and divide them with space:" << '\n';
    vector<int> unsorted_array(n);
    for (int & i : unsorted_array) {
        cin >> i;
    }

    cout << '\n';

    quick_sort(unsorted_array, 0, unsorted_array.size());

    cout << "Sorted elements" << '\n';
    for (auto element: unsorted_array){
        cout << element << " ";
    }
}*/
