#Triangle Right Angle Checker!
print('Right Angle Triangle Checker! ')
#Input dimensions of triangle 
hyp = input('Please enter the length of the Hypotenuse. ')
sideA = input('Please enter the length of one of the other sides. ')
sideB = input('Please enter the length of the remaining side. ')
#Validate
if hyp.isdigit() == False:
  hyp = input('The dimensions must be integers! Pleaese enter the length of the Hypotenuse. ')
elif sideA.isdigit() == False:
  sideA = input('The dimensions must be integers! Pleaese enter the length of one of the remaining sides. ')
elif sideB.isdigit() == False:
  sideB = input('The dimensions must be integers! Pleaese enter the length of the remaining side. ')
else:
  print("Critical error. Please restart the program.")
#Check if triangle is right angled 
res = float(sideA)**2 + float(sideB)**2 - float(hyp)**2
if res != 0:
  print('The Triangle is not right angled.')
elif res == 0:
  print('The Triangle is right angled.')
