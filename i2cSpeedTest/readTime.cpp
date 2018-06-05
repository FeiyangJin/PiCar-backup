#include <iostream>
#include <errno.h>
#include <wiringPiI2C.h>
#include <chrono>
#include <list>
#include <fstream>
#include <wiringPiI2C.h>

using namespace std;

int main(int argc, char* argv[]){
list<int> readTimeList;

int fd = wiringPiI2CSetup(0x6b);
auto start = chrono::high_resolution_clock::now();
auto last = chrono::high_resolution_clock::now();

while(chrono::duration_cast<chrono::seconds>(last - start).count() < 10){
auto beforeIf = chrono::high_resolution_clock::now();
if(wiringPiI2CRead(fd) != -1){
auto afterIf = chrono::high_resolution_clock::now();

auto now = chrono::high_resolution_clock::now();
auto ifTime = chrono::duration_cast<chrono::nanoseconds>(afterIf - beforeIf);
auto duration = chrono::duration_cast<chrono::nanoseconds>(now - last);
auto netTime = chrono::duration_cast<chrono::nanoseconds>(duration - ifTime);
readTimeList.push_front(netTime.count());

last = now;
}

}

ofstream myfile;
myfile.open("readTime.csv");
for(auto it=readTimeList.begin(); it!= readTimeList.end(); it++){
	myfile << *it;
	myfile << "\n";

}

return 0;
}
