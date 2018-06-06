#!/bin/bash
import os
import time
import subprocess

cmd = "sftp pi@192.168.1.157"

cmd2 = "put /home/pi/Desktop/backup.txt"

cmd3 = "sftp pi@192.168.1.157 <<< $'put /home/pi/Desktop/backup.txt'"

cmd4 = "scp /home/pi/Desktop/backup.txt pi@192.168.1.157:/home/pi"
#os.system(cmd)

#os.system(cmd2)

##subprocess.call(cmd, shell=True)
##time.sleep(5)
##subprocess.call(cmd2,shell=True)

subprocess.call(cmd4,shell=True)
