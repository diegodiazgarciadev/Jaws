from geopy.geocoders import Nominatim
import re


# We need a function so that we will take only 3 values ( N,Y, Unknown)
# We will use this function to return the correct Character for the Sex.
# If the Character is not F or M we will return "Unknown"
def get_correct_character(x):
    if x == "N" or x == "N " or x == " N ":
        return "N"
    elif x == "Y" or x == "Y " or x == " Y ":
        return "Y"
    else:
        return "Unknown"

# We will use this function to return the correct Character for the Sex.
# If the Character is not F or M we will return "Unknown"
def get_correct_sex(x):
    if x == "M" or x == "M " or x == " M ":
        return "M"
    elif x == "F" or x == "F " or x == " F ":
        return "F"
    else:
        return "Unknown"


# We want to use 5 different kind of sharks (White,Tiger, Lemon, Bull and Reef)
# So we will filter (using these functions an ReGex) the Species columns looking for this 5 species
def kind_of_shark_pattern(shark_str, pattern):
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

