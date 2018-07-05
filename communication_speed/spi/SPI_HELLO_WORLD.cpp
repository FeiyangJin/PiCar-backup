/**********************************************************
 SPI_Hello_Arduino
   Configures an Raspberry Pi as an SPI master and  
   demonstrates bidirectional communication with an 
   Arduino Slave
   
Compile String:
g++ -o SPI_Hello_Arduino SPI_Hello_Arduino.cpp
***********************************************************/

#include <unistd.h>
#include <sys/ioctl.h>
#include <linux/spi/spidev.h>
#include <fcntl.h>
#include <cstring>
#include <iostream>
#include <ctime>
#include <sys/time.h>
#include <cstdlib>

using namespace std;


/**********************************************************
Declare Global Variables
***********************************************************/

int fd;
unsigned char result;

/**********************************************************
Declare Functions
***********************************************************/

int spiTxRx(unsigned char txDat);


/**********************************************************
Main
  Setup SPI
    Open file spidev0.0 (chip enable 0) for read/write 
      access with the file descriptor "fd"
    Configure transfer speed (1MkHz)
***********************************************************/


int main (int argc, char *argv[])
{
	int loopNumber = 10;
	int loopByte = 1000000;
	unsigned int speed = 2000000;
	int count = 0;

	if(argc > 1){
		speed = atoi(argv[1]);
	}

	cout << "Enter the SPI speed you want: " << endl;
	cin >> speed;

	fd = open("/dev/spidev0.0", O_RDWR);

	ioctl (fd, SPI_IOC_WR_MAX_SPEED_HZ, &speed);
	
	struct timeval start;
	gettimeofday(&start,NULL);

		
	for (int i = 0; i < loopByte; i++)
	{
	 result = spiTxRx('J');
	}

	struct timeval end;
	gettimeofday(&end,NULL);
	long int startms = start.tv_sec * 1000 + start.tv_usec / 1000;
	long int endms = end.tv_sec * 1000 + end.tv_usec / 1000; 
	cout << "total read time for " << (loopByte) << " bytes in milliseconds is " << (endms - startms) << endl;
	cout << "The speed we set is " << speed << endl;

	return 0;

}

/**********************************************************
spiTxRx
 Transmits one byte via the SPI device, and returns one byte
 as the result.

 Establishes a data structure, spi_ioc_transfer as defined
 by spidev.h and loads the various members to pass the data
 and configuration parameters to the SPI device via IOCTL

 Local variables txDat and rxDat are defined and passed by
 reference.  
***********************************************************/

int spiTxRx(unsigned char txDat)
{
 
  unsigned char rxDat;

  struct spi_ioc_transfer spi;

  memset (&spi, 0, sizeof (spi));

  spi.tx_buf        = (unsigned long)&txDat;
  spi.rx_buf        = (unsigned long)&rxDat;
  spi.len           = 1;

  ioctl (fd, SPI_IOC_MESSAGE(1), &spi);

  return rxDat;
}
