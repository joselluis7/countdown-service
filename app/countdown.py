#-*-coding:utf-8

#The main idea of this simple program is to understand the stdout
#And carriage return functionality, both a old and little used 
#But have specific uses like, as in this case
from datetime import timedelta
from sys import stdout
from time import sleep
 
time = input('Enter the time in this format [hh:mm:ss]: ').split(':')
try:
    hours, minutes,seconds = time
    time = timedelta(hours=int(hours),minutes=int(minutes),seconds=int(seconds))

    while (str(time) != '00:00:00'):
        stdout.write("\r%s "%(str(time).strip('0000')))
        stdout.flush()
        time = time - timedelta(seconds=(1/100))
        sleep(1/100)

except ValueError:
    print('Please insert time only in this format: [hh:mm:ss]')
