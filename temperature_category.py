# Student name:Ryan Melendez
# Week:5
# Lab:temp and int
# Date: 9/28

temperature = float(input("enter the temperature in fahrenheit: "))

if temperature < 60:
    category = "cold" 
elif 60 <= temperature <= 80:
    category = "warm"
else:
      category = "hot"

print(f"the temperature is {temperature}°F, which is considered {category}.")
