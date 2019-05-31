#include <vector>
#include <algorithm>
#include <iostream>
#include <execution>


int main(){
  //vec1 with 100 elements
  std::vector<int>vec1(100);
  //vec2 with 10 elements
  std::vector<int>vec2(10);
  int counter{1};
  //initiolizing vec1
  std::for_each(vec1.begin(),vec1.end(),[&counter](int& n){n = counter++;});
  // show vec1
  std::cout<<" vec1 : "<<std::endl;
  std::for_each(vec1.begin(),vec1.end() ,[](int n){std::cout<< n <<" "; });
  std::cout<<std::endl;

  //initiolizing vec2
  counter = 1;
  std::for_each(vec2.begin(),vec2.end(),[&counter](int& n){n = counter++;});

  //show vec2
  std::cout<<" vec2 : "<<std::endl;
  std::for_each(vec2.begin(),vec2.end() ,[](int n){std::cout<< n <<" "; });
  std::cout<<std::endl;
  //add vec1 at the end of vec2
  std::copy(vec1.begin(), vec1.end(), back_inserter(vec2));
  //show vec2
  std::cout<<" vec2 : "<<std::endl;
  std::for_each(vec2.begin(),vec2.end() ,[](int n){std::cout<< n <<" "; });
  std::cout<<std::endl;

  std::vector<int>old_vec(50);
  counter = 0;
  //initiolizing old_vec with odd elements of vec1
  std::copy_if (vec1.begin(), vec1.end(),old_vec.begin(), [](int i){return i%2 == 1;} );

  //show old_vec
  std::cout<<" old_vec : "<<std::endl;
  std::for_each(old_vec.begin(),old_vec.end() ,[](int n){std::cout<< n <<" "; });
  std::cout<<std::endl;

  std::vector<int>reverse_vec(100);
  counter = vec1.size() - 1;
  //initiolizing reverse_vec
  std::for_each(reverse_vec.begin(),reverse_vec.end(),[&vec1 ,&counter](int& n){n = vec1[counter--] ;});

  //show reverse_vec
  std::cout<<" reverse_vec : "<<std::endl;
  std::for_each(reverse_vec.begin(),reverse_vec.end() ,[](int n){std::cout<< n <<" "; });
  std::cout<<std::endl;
  //sort vec2
  std::sort(vec2.begin(),vec2.end());

  //show vec2
  std::cout<<" vec2 : "<<std::endl;
  std::for_each(vec2.begin(),vec2.end() ,[](int n){std::cout<< n <<" "; });
  std::cout<<std::endl;

  //sort with execution for vec2
  std::sort(std::execution::par, Vec2.begin(),Vec2.end());
  //show vec2
  std::cout<<" vec2 : "<<std::endl;
  std::for_each(vec2.begin(),vec2.end() ,[](int n){std::cout<< n <<" "; });
  std::cout<<std::endl;

  return 0;
}
