import pigpio
import time

pi = pigpio.pi()
address = 0x04

SDA = 19
SCL = 13


def communication():
    
    while True:
        connection = pi.bb_i2c_open(SDA,SCL,9600)
        var = int(input("Enter 1  ^ ^  9: "))
        if not var:
            continue
        pi.bb_i2c_zip(SDA,[4,address,0x02,0x07,0x01,var,0x03,0x00])
        print("RPI: Hi Arduino, I sent you ", var)

        time.sleep(1)
        
        number = pi.bb_i2c_zip(SDA,[4,address,0x02,0x06,0x01,0x03,0x00])
        print("Arduino: Hey RPI, I received a digit ", number)
        print()

        pi.bb_i2c_close(SDA)


if __name__ == '__main__':
    try:
        communication()
    except:
        pi.bb_i2c_close(SDA)
