import re

def get_calibration(filepath):
    with open(filepath) as f:
        lines = f.readlines()
    
    calibration = 0
    digit_map = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    # this regex pattern finds overlapping matches of spelled out digits and any digits
    pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'

    for line in lines:
        line = line.rstrip()
        first_digit, last_digit = None, None
       
        # first search the string to identify digits and
        # words that could be digits, such as seven 
        # 
        # example:  zcsvvlslqvfive11chhzmdjdgz8vbgldl
        # replaced: zcsvvlslqv511chhzmdjdgz8vbgldl

        matches = re.findall(pattern, line)

        if not matches[0].isdigit(): # the first match was a digit spelled out
            first_digit = digit_map[matches[0]]
        else:
            first_digit = matches[0]
        
        if not matches[-1].isdigit(): # the last digit was spelled out
            last_digit = digit_map[matches[-1]]
        else:
            last_digit = matches[-1]
        
        # Concatenate the digits into a two-digit number
        if last_digit is None:
            last_digit = first_digit
        found_digit = first_digit + last_digit
        calibration += int(found_digit)
    
    return calibration

result = get_calibration('input.txt')
print(f'The sum of all digit numbers in the file is {result}')

