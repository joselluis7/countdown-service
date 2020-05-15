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
        time = time + timedelta(seconds=(1/100))
        sleep(1/100)
except ValueError:
    print('Please insert the time only in this format: [hh:mm:ss]')
