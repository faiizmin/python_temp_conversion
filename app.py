def convert_cel_to_far(temp_cel):
    # return temperature in Celcius to Fahrenheit
    temp_far = temp_cel * 9/5 + 32
    return temp_far


def convert_far_to_cel(temp_far):
    # return temperature in Fahrenheit to Celcius
    temp_cel = (temp_far-32) * 5/9
    return temp_cel


# prompt the user to input temperatue in Celcius. Use float to convert input (string to number)
temp_cel = float(input("Enter a temperature in degrees: "))

# call the function
temp_far = convert_cel_to_far(temp_cel)

# display the result
print(f"{temp_cel} degrees C = {temp_far} degrees F")

# prompt user to input temperature in Fahrenheit
temp_far = float(input("Enter a temperature in Fahrenheit: "))

# call the function
temp_cel = convert_far_to_cel(temp_far)

# display the result
print(f"{temp_far} degrees Fahrenheit = {round(temp_cel, 2)} degrees Celcius")
