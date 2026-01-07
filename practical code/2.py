# 2. Create a function that converts a list of temperatures from Celsius to Fahrenheit.

lc = [40, 67, 78.5, 87, 110]
def func(): 
    for i in range(len(lc)):
        lc[i] = (lc[i] * 9/5) + 32
    return lc
    
print(func())
