def valid_input(input):
    ''' validates all user inputs and returns True/False based on requirements met '''
    if len(input) < 0 and (len(input) < 3 or len(input) > 40):
        return False
    for c in input:
        if c == " ":
            return False
    
    return True

def verify_pass(pass1, pass2):
    ''' matches password with verify password field '''
    if pass2 == pass1:
        return True
    else:
        return False
    