import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM0')
pin8 = board.get_pin("d:8:o")
pin9 = board.get_pin("d:9:o")
pin10 = board.get_pin("d:10:o")
pin11 = board.get_pin("d:11:o")

step = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

def move(sec):
	timeNow = int(time.time()) 
	timeEnd = timeNow + sec
	while int(time.time()) <= timeEnd:
		print int(time.time()), "--", timeEnd
		for i in step:
			pin8.write(i[0])
			pin9.write(i[1])
			pin10.write(i[2])
			pin11.write(i[3])
			time.sleep(0.002)
