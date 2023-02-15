# program to illustrate protected access modifier in a class
 
# super class
'''
class Student:
    
     # protected data members
     _name = None
     _roll = None
     _branch = None
    
     # constructor
     def __init__(self, name, roll, branch): 
          self._name = name
          self._roll = roll
          self._branch = branch
    
     # protected member function  
     def _displayRollAndBranch(self):
 
          # accessing protected data members
          print("Roll: ", self._roll)
          print("Branch: ", self._branch)
 
 
# derived class
class Geek(Student):
 
       # constructor
       def __init__(self, name, roll, branch):
                Student.__init__(self, name, roll, branch)
         
       # public member function
       def displayDetails(self):
                   
                 # accessing protected data members of super class
                print("Name: ", self._name)
                   
                 # accessing protected member functions of super class
                self._displayRollAndBranch()
 
# creating objects of the derived class       
obj = Geek("R2J", 1706256, "Information Technology")
 
# calling public member functions of the class
obj.displayDetails()
'''
class Geek:
    # private data members
    __name = None
    __roll = None
    __branch = None

    # constructor(__init__ initializise the class attributes)
    def __init__(self, name, roll, branch):
        # assigning private data members to arguments received
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    # private function member
    def __displayDetails(self):
        # accessing private data members
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)

    # public member function 'inside' class
    def accessPrivateFunction(self):
        # accessing private function member
        self.__displayDetails()

# creating object
obj = Geek("R2J", 1706256, "Information Technology")

# calling public funciton member of the class
obj.accessPrivateFunction()
