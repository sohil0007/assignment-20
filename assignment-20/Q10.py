def anagram(s1,s2):

    s1=sorted(s1)
    s2=sorted(s2)
    if s1==s2:
        print("The string are anagrams")
    else:
        print("The string are not anagrams")

s1="python"
s2="thonyp"
anagram(s1,s2)            