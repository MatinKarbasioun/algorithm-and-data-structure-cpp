//
// Created by karbasioun on 6/7/2024.
//

#ifndef ALGORITHM_FIBONACCIRECURSIVE_H
#define ALGORITHM_FIBONACCIRECURSIVE_H


template <class T> 
class FibonacciRecursive{

    public:
        T generate(int num);
};

#endif //ALGORITHM_FIBONACCIRECURSIVE_H


template<class T>
T FibonacciRecursive<T>::generate(int num) {
    if (num <= 1){
        return n;
    }
    else {
        return generate(num-1) + generate(num-2);
    }
}