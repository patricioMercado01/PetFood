import sys, Ice
#import motorStep
import time
print "import Time ready"
import WeightSensor
print "import WeightSensor ready"

class SensorControlI(PetFoodSensors.SensorControl):
	def motorTime(time):
		#motorStep.move(time)
		print "motTim"
		
	def givefood(weight):
		#motorStep.foodWeight(weight)
		print "gFood"
		
	def getContainerFood():#podria no necesitarse
		return 1
		
	def getFoodEated():#podria no necesitarse
		return 1
		
	def eatingNow():
		if True and  WeightSensor.variationInWeight():
			return True
		else:
			return False
			
	def getWeight():
		WeightSensor.getWeightNow()

with Ice.initialize(sys.argv) as communicator:
	servant = SensorControl()
	adapter = communicator.createObjectAdapterWithEndpoints("SensorControlAdapter", "default -h 192.168.101.46 -p 10000")
	adapter.add(servant, communicator.stringToIdentity("SensorControl"))
	adapter.activate()
	communicator.waitForShutdown()
