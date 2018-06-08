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

int i=0;
int j=0;
while(j < 100000){
j++;
if(wiringPiI2CRead(fd) != -1){
	i++;
	if(i < 500){
		continue;
	}
	else{

		auto now = chrono::high_resolution_clock::now();
		auto duration = chrono::duration_cast<chrono::nanoseconds>(now - last);
		readTimeList.push_front(duration.count());

		last = now;
		i = 0;
	}

	}

}

ofstream myfile;
myfile.open("readTime.csv");
myfile << "hello";
for(auto it=readTimeList.begin(); it!= readTimeList.end(); it++){
	myfile << *it;
	myfile << "\n";

}

return 0;
}
