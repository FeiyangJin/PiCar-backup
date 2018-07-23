/*
Author: Feiyang Jin
Email: feiyang.jin@wustl.edu
Organization: Washington University in St. Louis
Date: July 2018
*/

#include <unistd.h>		//Needed for I2C port
#include <fcntl.h>		//Needed for I2C port
#include <sys/ioctl.h>		//Needed for I2C port
#include <linux/i2c-dev.h>	//Needed for I2C port
#include <iostream>
#include <stdio.h>
#include <ctime>
#include <chrono>
#include <sys/time.h>

using namespace std;

int main(){

int file_i2c;
int length;
unsigned char buffer[60] = {0};


//----- OPEN THE I2C BUS -----
char *filename = (char*)"/dev/i2c-1";
if ((file_i2c = open(filename, O_RDWR)) < 0)
{
//ERROR HANDLING: you can check errno to see what went wrong
printf("Failed to open the i2c bus");
return -1;
}

int addr = 0x04;          //The I2C address of the slave
if (ioctl(file_i2c, I2C_SLAVE, addr) < 0)
{
	printf("Failed to acquire bus access and/or talk to slave.\n");
	//ERROR HANDLING; you can check errno to see what went wrong
	return -1;
}


//----- READ BYTES -----
length = 1;		//Number of bytes to read
int totalRead = 0;
struct timeval start;
gettimeofday(&start,NULL);

while(totalRead < 10000){
	read(file_i2c,buffer,length);
	totalRead ++;

	/* if (read(file_i2c, buffer, length) != length)
	{
		//ERROR HANDLING: i2c transaction failed
	        //printf("Failed to read from the i2c bus.\n");
	}
	else
	{
		//printf("Data read: %s\n", buffer);
		totalRead ++;
		//cout << "The first element of buffer:" << buffer[0] << endl;
	}*/


}

struct timeval end;
gettimeofday(&end,NULL);
long int startms = start.tv_sec * 1000 + start.tv_usec / 1000;
long int endms = end.tv_sec * 1000 + end.tv_usec / 1000;

cout << "total read time for 10000 bytes in milliseconds is " << (endms - startms) << endl;

//read() returns the number of bytes actually read, if it doesn't match then an error occurred (e.g. no response from the device)
/* if (read(file_i2c, buffer, length) != length)
{
	//ERROR HANDLING: i2c transaction failed
	printf("Failed to read from the i2c bus.\n");
}
else
{
	time_t result = time(NULL);
	cout << asctime(localtime(&result)) << result << " seconds since the Epoch" << endl;
	//printf("Data read: %s\n", buffer);
	cout << "The first element of buffer:" << buffer[0] << endl;
} */

//this is not precise, but what we need is just relative time
/* struct timeval tp;
gettimeofday(&tp,NULL);
long int ms = tp.tv_sec * 1000 + tp.tv_usec / 1000;
cout << "milliseconds since epoch " << ms << endl;
*/

return 0;
}
