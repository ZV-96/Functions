def check_bmi(bmi):
    if bmi < 18:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# Main Routine
get_bmi = float(input("enter bmi: "))
print(f"With BMI of {get_bmi} your status is {check_bmi(get_bmi)}")


