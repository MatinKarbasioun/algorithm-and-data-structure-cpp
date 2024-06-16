#include <iostream>
#include <chrono>
#include "common/helper/elapse.h"
using namespace alg_time;

void alg_time::elapse_time(void (*func)()){
    auto start = std::chrono::high_resolution_clock::now();
    func();
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << "Elapsed time: " << elapsed.count() << " seconds" << std::endl;    
}

