import re


#We need a function so that we will return 3 values ( N,Y, Unknown)
def get_correct_character(x):
    """ We need a function so that we will take only 3 values ( N,Y, Unknown)
            We will use this function to return the correct Character for the Sex.
            If the Character is not F or M we will return "Unknown" 

    parameters : str (Character that determine if there is or not a deadly attack (y/N)) 

    
    returns : str (Return only Values N, Y, or Unknown depending on the input string)
    """
    if x == "N" or x == "N " or x == " N ":
        return "N"
    elif x == "Y" or x == "Y " or x == " Y ":
        return "Y"
    else:
        return "Unknown"

# We will use this function to return the correct Character for the Sex.
# If the Character is not F or M we will return "Unknown"
def get_correct_sex(x):
    """ We will use this function to return the correct Character for the Sex. 

    parameters : str (Character that determine the sex( M/F)) 

    
    returns : str (Return only Values M, F, or Unknown depending on the input string)
    """
    if x == "M" or x == "M " or x == " M ":
        return "M"
    elif x == "F" or x == "F " or x == " F ":
        return "F"
    else:
        return "Unknown"


# We want to use 5 different kind of sharks (White,Tiger, Lemon, Bull and Reef)
# So we will filter (using these functions an ReGex) the Species columns looking for this 5 species
def kind_of_shark_pattern(shark_str, pattern):
    """ We will use this function to return a string of the pattern we are sending on the string we are sending. 

    parameters : str, str (string where we want to find our patter, the patter) 

    
    returns : str (Return the string with the pattern if it finds it and an empty string if not)
    """
    kind_of_shark = re.findall(pattern, shark_str)
    if kind_of_shark:
        return kind_of_shark
    else:
        return ""

def kind_of_shark(shark_string):
    pattern1 = "w?W?hite shark"
    pattern2 = "t?T?iger shark" 
    pattern3 = "l?L?emon shark" 
    pattern4 = "b?B?ull shark" 
    pattern5 = "r?R?eef shark"
    
    match_pattern_1 = kind_of_shark_pattern(shark_string, pattern1)
    match_pattern_2 = kind_of_shark_pattern(shark_string, pattern2)
    match_pattern_3 = kind_of_shark_pattern(shark_string, pattern3)
    match_pattern_4 = kind_of_shark_pattern(shark_string, pattern4)
    match_pattern_5 = kind_of_shark_pattern(shark_string, pattern5)
    if match_pattern_1:
        return match_pattern_1[0].lower()
    elif match_pattern_2:
        return match_pattern_2[0].lower()
    elif match_pattern_3:
        return match_pattern_3[0].lower()
    elif match_pattern_4:
        return match_pattern_4[0].lower()
    elif match_pattern_5:
        return match_pattern_5[0].lower()
    else:
        return "Other"

