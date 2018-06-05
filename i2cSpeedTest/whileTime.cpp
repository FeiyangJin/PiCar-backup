#include <iostream>
#include <errno.h>
#include <wiringPiI2C.h>
#include <chrono>
#include <list>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]){
//address for IMU
list<int> time;

int fd = wiringPiI2CSetup(0x6b);

auto start = chrono::high_resolution_clock::now();
auto last = chrono::high_resolution_clock::now();
while(chrono::duration_cast<chrono::seconds>(last - start).count() < 10){
auto now = chrono::high_resolution_clock::now();
auto duration = chrono::duration_cast<chrono::nanoseconds>(now - last);
//cout << duration.count() << "ns" << endl;
//add to list
time.push_front(duration.count());
last = now;

}

ofstream myfile;
myfile.open("whileTime.csv");
//myfile << "hello\n";
for(auto it=time.begin(); it!=time.end(); it++){
	myfile << *it;
	myfile << "\n";
}
myfile.close();

return 0;
}
