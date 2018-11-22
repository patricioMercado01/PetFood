import sys, Ice
import motorStep
import time

class MotorStep():
	def motorTime(time):
        	motorStep.on(time)
	#def motorTime()
	#	void motorTime(string time);
          #      	void givefood(int weight);
	 #               int getContainerFood();
        #	        int foodEated();
	#               bool eatingNow();

with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("MotorTimeAdapter", "default -h 192.168.43.152 -p 10000")
    object = MotorStep()
    adapter.add(object, communicator.stringToIdentity("MotorTime"))
    adapter.activate()
    communicator.waitForShutdown()
