class multiFunctions:
    def Subfields():
        items = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub-fields in AI are:")
        for item in items:
            print(item)
    def oddEvenCheck():
        number = int(input("Enter a number:"))
        if number%2 == 0:
            print(str(number) + " is Even Number")
        else:
            print(str(number) + " is Odd Number")
    def Eligible():
        Gender = input("Enter your Gender:")
        Age = int(input("Enter your Age:"))
        if ((Gender == "Male") and (Age < 21) or (Gender == "Female") and (Age < 18)):
            status = "NOT ELIGIBLE"
        else:
            status = "ELIGIBLE"
        print("Your Gender:" + Gender)
        print("Your Age:" + str(Age))
        print(status)
    def percentage():
        num1 = int(input("Enter your subject1 marks"))
        num2 = int(input("Enter your subject2 marks"))
        num3 = int(input("Enter your subject3 marks"))
        num4 = int(input("Enter your subject4 marks"))
        num5 = int(input("Enter your subject5 marks"))
        total = num1 + num2 + num3 + num4 + num5
        percent = (total/500)*100
        print("Subject1=" + str(num1))
        print("Subject2=" + str(num2))
        print("Subject3=" + str(num3))
        print("Subject4=" + str(num4))
        print("Subject5=" + str(num5))
        print("Total :" + str(total))
        print("Percentage: " + str(percent))
    def triangle():
        height = int(input("Enter the height:"))
        breadth = int(input("Enter the breadth:"))
        height1 = int(input("Enter the height1:"))
        height2 = int(input("Enter the height2:"))
        breadth1 = int(input("Enter the breadth1:"))
        area = (height*breadth)/2
        perimeter = height1 + height2 + breadth1
        print("Height : " + str(height))
        print("Breadth : " + str(breadth))
        print("Area of Triangle: " + str(area))
        print("Height1 : " + str(height1))
        print("Height2 : " + str(height2))
        print("Breadth1 : " + str(breadth1))
        print("Perimeter of Triangle: " + str(perimeter))
    def BMI():
        indexNumber = float(input("Enter the BMI Index:"))
        if indexNumber < 18.5:
            print("Underweight")
        elif indexNumber <= 24.9:
            print("Normal range")
        elif indexNumber <= 29.9:
            print("Overweight")
        else:
            print("Obese")