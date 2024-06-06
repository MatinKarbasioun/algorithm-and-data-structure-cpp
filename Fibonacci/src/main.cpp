#include "Domain/Fibonacci.h"
#include "Helper/elapse.h"
#include "Decimal/decimal.h"

int input(){
    int seriesNum;
    std::cout << "Please input your series num:";
    std::cin >> seriesNum;
    return seriesNum;
}

void func(){
    Fibonacci<Decimal> fibo;
    int seriesNum = input();
    for (int i = 0; i < seriesNum; ++i) {
        fibo.fibo_num();
    }
}

int main(){
    elapse_time(func);
    return 0;
}