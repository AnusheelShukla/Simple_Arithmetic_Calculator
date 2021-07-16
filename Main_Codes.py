# Creating a average calculator
DataYouNeed = int(input("Total No. of  = ")) + 1
Number = 0
Sum = 0

for i in range(1, DataYouNeed):
    Number += 1
    EnterTheNumber = int(input("Enter the number " + "#"+str(Number) + ": "))
    Sum += EnterTheNumber
    Average = Sum/DataYouNeed
print("Average: ", Average)
Average = "{:.2f}".format(Average)
print(Average)
