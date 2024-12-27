weight=float(input('Enter Your weight in kg'))
height=float(input('Enter Your weight in mtr'))
bmi=weight/height**2
if bmi<18.5:
    print('you are under weight')
elif bmi<25 :
      print('You are healthy')
elif bmi<30:
      print('You are over weight')
elif bmi<35:
      print('You are severly over weight')
elif bmi<40:
      print('You are Obese')      
else :
      print('You are severly OBESE')