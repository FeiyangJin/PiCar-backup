#include <unistd.h>		//Needed for I2C port
#include <fcntl.h>		//Needed for I2C port
#include <sys/ioctl.h>		//Needed for I2C port
#include <linux/i2c-dev.h>	//Needed for I2C port
#include <iostream>
#include <stdio.h>

using namespace std;

int main(){

int file_i2c;
int length;
int buffer[60] = {0};

	
//----- OPEN THE I2C BUS -----
char *filename = (char*)"/dev/i2c-1";
if ((file_i2c = open(filename, O_RDWR)) < 0)
{
//ERROR HANDLING: you can check errno to see what went wrong
printf("Failed to open the i2c bus");
return -1;
}
	
int addr = 0x04;          //<<<<<The I2C address of the slave
if (ioctl(file_i2c, I2C_SLAVE, addr) < 0)
{
	printf("Failed to acquire bus access and/or talk to slave.\n");
	//ERROR HANDLING; you can check errno to see what went wrong
	return -1;
}

//----- READ BYTES -----
length = 1;			//<<< Number of bytes to read
if (read(file_i2c, buffer, length) != length)
//read() returns the number of bytes actually read, if it doesn't match then an error occurred (e.g. no response from the device)
{
 	//ERROR HANDLING: i2c transaction failed
	printf("Failed to read from the i2c bus.\n");
}
else
{
	//printf("Data read: %s\n", buffer);
	cout << "The first element of buffer:" << buffer[0] << endl;
}

return 0;
}
