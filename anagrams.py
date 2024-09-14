class Anagrams(object):

    #This is initialization of class to receive two words.
    def __init__(self,a,b):
        self.word1 = a
        self.word2 = b
    
    #This fuction make two words which recognize if there are anagrams,then the function will return True or False.
    def match(self):
        if len(self.word1) != len(self.word2):
            return False
        lst1=[0]*26
        lst2=[0]*26
        for i in self.word1:
            lst1[ord('a')-ord(i)] +=1
        for j in self.word2:
            lst2[ord('a')-ord(j)] +=1
        if lst1 != lst2:
            return False
        return True
def anagrams(a,b):
    if len(a) != len(b):
        return False
    lst1=[0]*26
    lst2=[0]*26
    for i in a:
        lst1[ord('a')-ord(i)] +=1
    for j in b:
        lst2[ord('a')-ord(j)] +=1
    if lst1 != lst2:
        return False
    return True


"""word1=input("a:")
word2=input("b")
print(anagrams(word1,word2))"""

test1=Anagrams("bus","gub")
print(test1.match())
