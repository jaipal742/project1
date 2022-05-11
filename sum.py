
def getSum(n):  
    sum = 0
    for digit in str(n):   
      sum += int(digit)        
    return sum   
try:
    num = int(input("Enter a number: "))
    if (getSum(num) == 25):
        print("Congratulations, You win free takeaways")
    else:
        print("Better luck next time")
except:
    print("Error: Please enter Unique Id correctly")
finally:
    print("Thankyou for shopping with us,Happy Holidays :)")