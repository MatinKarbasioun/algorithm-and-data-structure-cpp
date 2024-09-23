//
// Created by Matin on 9/11/2024.
//
#include <algorithm>
#include <iostream>
#include <vector>

using std::vector;

int get_majority_element(vector<int> &a, int left, int right) {
    if (left == right) return -1;

    auto candidate = -1;
    auto vote = 0;

    for (auto i = 1; i < a.size(); i++){
        if (vote == 0){
            candidate = a[i];
            vote++;
        }
        else{
            if (a[i] == candidate){
                vote++;
            }
            else{
                vote--;
            }
        }
    }

    auto count = 0;

    for (auto i = 0; i < a.size(); i++){
        if (a[i] == candidate) {
            count++;
        }
    }

    return (count > a.size()/2) ? 1 : -1;
}

int main() {
    int n;
    std::cin >> n;
    vector<int> a(n);
    for (size_t i = 0; i < a.size(); ++i) {
        std::cin >> a[i];
    }
    std::cout << (get_majority_element(a, 0, a.size()) != -1) << '\n';
}
