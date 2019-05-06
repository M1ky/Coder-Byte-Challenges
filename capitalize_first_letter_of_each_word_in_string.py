def LetterCapitalize(str): 

    lst = [word[0].upper() + word[1:] for word in str.split()]
    s = " ".join(lst)
    return s
 


  