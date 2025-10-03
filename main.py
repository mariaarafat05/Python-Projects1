# Python Weight Converter

Weight = float(input('Enter Your Weight : '))
m = input('Kilograms or Pounds? (K or L): ')

if m == 'K' :
    Weight = Weight * 2.205
    m = 'Lbs.'
elif m == 'k' :
    Weight = Weight * 2.205
    m = 'Lbs.'
elif m == 'L' :
    Weight = Weight / 2.205
    m = 'Kgs.'
elif m == 'l' :
    Weight = Weight / 2.205
    m = 'Kgs.'
else :
    print('Eror!')
    
print('Your Weight is ' , (Weight) ,(m))