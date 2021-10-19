class MyClassA:
    
    def __init__(self):
        self.myClassB = MyClassB()
    
    def method1(self):    
        print("Hi")
        n = 0 
        self.myClassB.method2()
        self.myClassB.method1()
        
        print("Possibly this is never going to be executed")
        hola = "Hi"
        print(hola)
            


class MyClassB:

    def method1(self):
        x = 1
        y = x / 0
        z = 99
        
        print("This should not be printed")
        
        raise TypeError

    def method2(self):
        pass

