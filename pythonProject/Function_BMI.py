"""BMI = (Weight / Height squared) """


def get_info():
    height0 = float(input("Enter height "))
    weight0 = float(input("Enter weight "))
    system0 = input("Metric or Imperial: ")
    return height0, weight0, system0


def calculate_bmi(weight0, height0, system0='metric'):
    """ Return BMI value for given weight, height and system  """
    if system0 == 'metric':
        bmi0 = (weight0 / (height0 ** 2))
    else:
        bmi0 = (weight0 / (height0 ** 2)) * 703
    return bmi0


while True:
    height, weight, system = get_info()
    if system.startswith("i"):
        bmi = calculate_bmi(weight, height, system0='imperial')
        print(f"Your BMI is  {bmi}")
        break
    elif system.startswith("m"):
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is  {bmi}")
    else:
        print("ERROR: choose i for imperial or m for metric")
