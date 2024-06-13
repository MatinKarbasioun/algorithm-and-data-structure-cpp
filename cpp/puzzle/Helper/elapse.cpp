#include <iostream>
#include <chrono>
#include "elapse.h"
using namespace std;


void elapse_time(void (*func)()){
    auto start = chrono::high_resolution_clock::now();
    func();
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = end - start;
    cout << "Elapsed time: " << elapsed.count() << " seconds" << std::endl;    
}