#Input dimensions of triangle 
hyp = float(input('Please enter the length of the Hypotenuse. '))
sideA = float(input('Please enter the length of one of the other sides. '))
sideB = float(input('Please enter the length of the remaining side. '))
#Check if triangle is right angled 
res = sideA**2 + sideB**2 - hyp**2
if res == 0:
  print('The Triangle is right angled.')

