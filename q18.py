str1=input()

str2=input()

def anagrams(str1, str2):
     

    if(sorted(str1)== sorted(str2)):
        print("The strings are anagrams.") 
    else:
        print("The strings aren't anagrams.") 
