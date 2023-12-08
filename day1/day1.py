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
        