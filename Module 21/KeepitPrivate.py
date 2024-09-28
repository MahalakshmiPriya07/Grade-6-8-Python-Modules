# Class creation
class myClass:

    # Private variable
    __privateVar = 27

    # Private method
    def __privMeth(self):
        print("I'm inside class myClass")

    # Function to print value of private variable
    def hello(self):
        print("Private Variable value:", myClass.__privateVar)

    # Function to call the private method
    def call_private_method(self):
        self.__privMeth()  # Accessing the private method correctly

# Object creation and method call
foo = myClass()
foo.hello()
foo.call_private_method()  # Calling the method to access the private method
