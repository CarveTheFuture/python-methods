class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
def Subtract (a, b): 
    return (a-b) 
  
print( Subtract(10, 12) ) # prints -2 
  
print( Subtract(15, 6) ) # prints 9 
