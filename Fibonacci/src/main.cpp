#include "Domain/FibonacciNaive.h"
#include "../Decimal/decimal.h"
#include "../Helper/elapse.h"


int input(){
    int seriesNum;
    std::cout << "Please input your series num:";
    std::cin >> seriesNum;
    return seriesNum;
}

void func(){
    FibonacciNaive<Decimal> fibonacci;
    int seriesNum = input();
    fibonacci.generate(seriesNum);
}

int main(){
    elapse_time(func);
    return 0;
}