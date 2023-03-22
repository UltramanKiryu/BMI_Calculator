def bmi_gauge(BMI, weight, height):
    if BMI < 18.5:
        return "The BMI for a person who is "+str(height)+" inches with a weight of "+str(weight)+" lbs is "+str(BMI)+" which is underweight"
    elif BMI >= 18.5 and BMI <= 24.9:
         return "The BMI for a person who is "+str(height)+" inches with a weight of "+str(weight)+" lbs is "+str(BMI)+" which is normal"
    elif BMI >= 25 and BMI <= 29.9:
         return "The BMI for a person who is "+str(height)+" inches with a weight of "+str(weight)+" lbs is "+str(BMI)+" which is overweight"
    elif BMI >= 30:
         return "The BMI for a person who is "+str(height)+" inches with a weight of "+str(weight)+" lbs is "+str(BMI)+" which is obese"

sweight = float(input("Enter in a weight:"))
weight = sweight*0.45
sheight = float(input("Enter in a height:"))
height = sheight*0.025
mheight = float(pow(height, 2))
BMI = weight/mheight
BMI = round(BMI, 1)
strs = bmi_gauge(BMI, sweight, sheight)
print(strs)
