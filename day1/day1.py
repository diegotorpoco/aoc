def calibration_sum(calibration):
    
    digits = [str(value) for value in range(0,10)]
    digits_list = []
    calibration_values = [] 

    wrong_calibration_list = calibration.split("\n")
    
    for wrong_cal in wrong_calibration_list:
        separated_wrong_cal = ','.join(wrong_cal).split(',')
        for letter in separated_wrong_cal:
            if letter in digits:
                digits_list.append(letter)
        if len(digits_list) == 1:
            calibration_values.append(int(digits_list[0]+digits_list[0]))
        if len(digits_list) > 1:
            calibration_values.append(int(digits_list[0]+digits_list[-1]))
        digits_list = []

    sum_calibration_values = sum(calibration_values)       

    return sum_calibration_values     

def calibration_sum_complete(calibration):
    
    digits = [str(value) for value in range(0,10)]
    digits_letter = ["one","two","three","four","five","six","seven","eight","nine"]
    digits_list = []
    calibration_values = [] 

    wrong_calibration_list = calibration.split("\n")
    
    for wrong_cal in wrong_calibration_list:
        for i,letter in enumerate(wrong_cal):
            if letter in digits:
                digits_list.append(letter)
            for index,value in enumerate(digits_letter):
                if wrong_cal[i:].startswith(value):
                    digits_list.append(str(index+1))
        if len(digits_list) == 1:
            calibration_values.append(int(digits_list[0]+digits_list[0]))
        if len(digits_list) > 1:
            calibration_values.append(int(digits_list[0]+digits_list[-1]))
        digits_list = []

    sum_calibration_values = sum(calibration_values)       

    return sum_calibration_values     
        