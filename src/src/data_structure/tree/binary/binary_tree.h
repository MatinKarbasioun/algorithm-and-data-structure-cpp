//
// Created by Matin on 11/30/2024.
//

#include "string"
#include "vector"


#ifndef CPP_BINARY_TREE_H
#define CPP_BINARY_TREE_H

class BinaryTree {
public:
    string key;
    BinaryTree* leftChild;
    BinaryTree* rightChild;
    BinaryTree* parent;
    int height = 0;

    BinaryTree(string key){
        this->key = key;
        height++;
    }

    int size();
    void insert(BinaryTree** node);
    void delete (BinaryTree** node);
    BinaryTree* NearestNeighbors(string key);
    vector<string> RangeSearch(string from, string to);
    vector<string> InOrderTraversal(); //depth-first (DFS)
    vector<string> PreOrderTraversal(); //depth-first (DFS)
    vector<string> PostOrderTraversal(); //depth-first (DFS)
    vector<string> LevelTraversal(); //breadth-first (BFS)
};
#endif //CPP_BINARY_TREE_H
