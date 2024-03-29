def intinputrange(prompt, min, max):
    valid_input = False
    valid_number = False
    output = 0
    user_input = input(prompt)
        
    while not valid_input:
        try:
            output = int(user_input)
            if (min <= output) and (output <= max):
                valid_input = True
            else:
                raise ValueError
        except ValueError:
            print("\nPlease enter a number between", min, "and", max)
            user_input = input(prompt)
            valid_input = False    
    return output

def intinputstrmatch(prompt, match1, match2):
    output = ""
    user_input = input(prompt)
    user_input = user_input.lower()
    
    if (user_input == match1) or (user_input == match2):
        output = user_input
        
    return output
    


