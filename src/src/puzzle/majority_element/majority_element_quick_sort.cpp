#include <algorithm>
#include <iostream>
#include <vector>

using std::vector;


void swap_value(vector<int> &a, int position, int swap_index){
    auto value = a[position];
    a[position] = a[swap_index];
    a[swap_index] = value;
}

int make_partition(vector<int> &a, int left, int right){
    auto value = a[left];
    auto index = left + 1;
    auto swap = false;

    for (auto i = index; i < right; i++){
        if (a[i] <= value){
            if (swap) {
                swap_value(a, index, i);
            }
            index++;
        }
        else{
            swap = true;
        }
    }
    swap_value(a, left, index-1);
    return index-1;
}

void quick_sort(vector<int> &a, int left, int right){
    if (left >= right){
        return;
    }
    auto index = make_partition(a, left, right);
    quick_sort(a, left, index);
    quick_sort(a, index + 1, right);
}

int get_majority_element(vector<int> &a, int left, int right) {
  if (left == right) return -1;
  if (left + 1 == right) return a[left];

  quick_sort(a, left, right);

  auto new_major_count = 1;
  auto previous_element_count = 0;
  auto element = a[0];

  for (auto i = 1; i < a.size(); i++){
      if (a[i] != element and previous_element_count == 0){
          previous_element_count = new_major_count;
          element = a[i];
          new_major_count = 1;
      }
      else if(a[i] != element and previous_element_count > 0){
          (previous_element_count > new_major_count) ? : previous_element_count = new_major_count;
          new_major_count = 1;
          element = a[i];
      }
      else{
          new_major_count ++;
      }
  }

  if (previous_element_count > (a.size()/2) or new_major_count > (a.size()/2)){
      return 1;
  }
  else{
      return -1;
  }
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  std::cout << (get_majority_element(a, 0, a.size()) != -1) << '\n';
}
