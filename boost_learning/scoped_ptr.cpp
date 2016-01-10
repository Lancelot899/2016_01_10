#include <boost/smart_ptr.hpp>
#include <string>
#include <iostream>

using namespace boost;

struct posix_file{
    posix_file(const char* file_name){
        std::cout << "open file:"<< file_name <<std::endl;
    }
    ~posix_file(){
        std::cout << "close file" << std::endl;
    }
};


int main(){
    scoped_ptr<std::string> pStr(new std::string("hello scoped_ptr"));
    std::cout << *pStr << std::endl;
    std::cout << pStr->size() << std::endl;

    std::cout << "*****************************************************************" << std::endl;
    scoped_ptr<posix_file> pf(new posix_file("./a.txt"));

    scoped_ptr<int> p(new int);

    if(p){
        *p = 100;
        std::cout << *p << std::endl;
    }

    p.reset();
    if(p)
        std::cout<< "this pointer is free" << std::endl;

    return 0;
}
