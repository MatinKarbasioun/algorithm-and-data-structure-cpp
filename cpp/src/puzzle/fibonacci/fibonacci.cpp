#include "puzzle/fibonacci/fibonacci_naive.h"
#include "puzzle/fibonacci/fibonacci.h"
#include "common/decimal/decimal.h"
#include "common/helper/elapse.h"
using namespace alg_time;


int input(){
    int seriesNum;
    std::cout << "Please input your series num:";
    std::cin >> seriesNum;
    return seriesNum;
}

void fibbo_func(){
    FibonacciNaive<Decimal> fibonacci;
    int seriesNum = input();
    fibonacci.generate(seriesNum);
}

int fibonacci_main(){
    alg_time::elapse_time(fibbo_func);
    return 0;
}