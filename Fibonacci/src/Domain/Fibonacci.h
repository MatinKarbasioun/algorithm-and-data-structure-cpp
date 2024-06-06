#ifndef FIBONACCI_H
#define FIBONACCI_H

#include <cstdint>
#include <iostream>
#include <climits>


template <class T> 
class Fibonacci
{
    private:
        T* First;
        T* Second;
        T* FirstNewNum;
        T* SecondNewNum;
        int counter;
    
    public:
        Fibonacci();
        T fibo_num();
        ~Fibonacci();
};

template <class T>  
Fibonacci<T>::Fibonacci(){
    First = new T("0");
    Second = new T("1");
    FirstNewNum = First;
    SecondNewNum = Second;
    counter = 0;
}

template <class T>  
T Fibonacci<T>::fibo_num(){
    counter ++;
    T tempNum = *SecondNewNum;
    *SecondNewNum = *SecondNewNum + *FirstNewNum;
    *FirstNewNum = tempNum;
    std::cout << "New number "<< counter << " is:" << *SecondNewNum << std::endl;
    return *SecondNewNum;
}

template <class T>
Fibonacci<T>::~Fibonacci(){
    delete First;
    delete Second;
}



#endif // FIBONACCI_H