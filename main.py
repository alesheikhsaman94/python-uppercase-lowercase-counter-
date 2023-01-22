
def myfunc(name):
    counetr_Uppercase = 0
    counetr_Lowercase = 0
    for i in name:
        if i.isupper():
            counetr_Uppercase += 1
        elif i.islower():
            counetr_Lowercase +=1
        else:
            pass
    print(f"upper cases: {counetr_Uppercase}")
    print(f"upper cases: {counetr_Lowercase}")

while True:
    name = input("enter your name: ")
    myfunc(name)