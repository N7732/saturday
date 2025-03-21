class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mult(self):
        return self.a * self.b
    def div(self):
        return self.a /self.b
a=int(input("Enter first value: "))
b=int(input("Enter second number: "))
kt=cal(a,b)
choice=1
while choice !=0:
    print(" 0 to exist\n")
    print(" 1 for addition\n")
    print(" 2 for substraction\n")
    print("3 for multiplication\n")
    print("4 for division\n")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("result= ",kt.add())
    elif choice == 2:
        print("result= ",kt.sub())
    elif choice == 3:
        print("result= ",kt.mult())
    elif choice == 4:
        print("result= ",kt.div())
    elif choice == 0:
        print("Existing!")
    else:
        print("Invalid number")
print("thanks")

    
