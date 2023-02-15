class Robot:
    # represents a robot with a name

    # a class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        # initializes the data
        self.nam = name
        print("inititalizing {}".format(self.nam))

        # when this person is created, the robot adds to the populatn
        Robot.population += 1

    def die(self):
        # i am dying
        print("{} is being destroyed".format(self.nam))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.nam))

        else:
            print("there are still {:d} robots".format(Robot.population))
            
    def say_hi(self):
        # robot greeting

        print("Greetings, I am Rob {}".format(self.nam))

    @classmethod
    def how_many(cls):
        # prints current population
        print("we have {:d} robots".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()                                                                             
Robot.how_many() 

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work.\n")
print("Robots are done, destroy them")
droid1.die()
droid2.die()

Robot.how_many()
