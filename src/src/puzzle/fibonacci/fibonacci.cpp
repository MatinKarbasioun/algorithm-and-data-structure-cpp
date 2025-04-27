#include "puzzle/fibonacci/fibonacci_fast.h"
#include "puzzle/fibonacci/fibonacci.h"
#include "common/decimal/decimal.h"
#include "common/helper/elapse.h"
#include <vector>
#include <string>
using namespace alg_time;


int input(){
    int seriesNum;
    std::cout << "Please input your series num:";
    std::cin >> seriesNum;
    return seriesNum;
}

void fibbo_func(){
    FibonacciFast<Decimal> fibonacci;
    int seriesNum = input();
    fibonacci.generate(seriesNum);
}

void fibonacci_main(){
    auto fibonacci = std::vector<std::string>{"naive", "fast"};
    auto i = 0;
        int choice = 0;
        std::cout << "Please Choose between projects" << std::endl;
    alg_time::elapse_time(fibbo_func);
}

