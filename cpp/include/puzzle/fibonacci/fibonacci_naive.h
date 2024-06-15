#ifndef FIBONACCI_H
#define FIBONACCI_H

#include <cstdint>
#include <iostream>
#include <climits>


template <class T> 
class FibonacciNaive
{
    private:
        T* First;
        T* Second;
        T* FirstNewNum;
        T* SecondNewNum;
        int counter;
        T generate();
    
    public:
        FibonacciNaive();
        T generate(int num);
        ~FibonacciNaive();
};

template <class T>
FibonacciNaive<T>::FibonacciNaive(){
    First = new T("0");
    Second = new T("1");
    counter = 0;
}

template<class T>
T FibonacciNaive<T>::generate(int num) {
    FirstNewNum = First;
    SecondNewNum = Second;

    T* fibonacci_num = new T("0");

    if (num == 0){
        fibonacci_num = First;
    }
    else if(num == 1){
        fibonacci_num = Second;
    }
    else{
        int i = 2;
        while (i <= num){
            *fibonacci_num = generate();
            i++;
        }
    }

    return *fibonacci_num;
}

template <class T>  
T FibonacciNaive<T>::generate(){
    counter ++;
    T tempNum = *SecondNewNum;
    *SecondNewNum = *SecondNewNum + *FirstNewNum;
    *FirstNewNum = tempNum;
    std::cout << "New number "<< counter << " is:" << *SecondNewNum << std::endl;
    return *SecondNewNum;
}

template <class T>
FibonacciNaive<T>::~FibonacciNaive(){
    delete First;
    delete Second;
}



#endif // FIBONACCI_H