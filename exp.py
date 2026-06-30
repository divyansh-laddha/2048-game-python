class Employee:
    lang = "Py"
    salary = 120000

    def getInfo(s):
        print(f"The language is {s.lang}. The salary is {s.salary}")

    def greet(p):
        print("Good morning!")

harry = Employee()

harry.getInfo()
harry.greet()