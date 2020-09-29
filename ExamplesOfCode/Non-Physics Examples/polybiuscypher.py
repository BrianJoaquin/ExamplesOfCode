# Creating the Polybius Square
L = [['a','b','c','d','e'],
     ['f','g','h','i','j','k'],
     ['l','m','n','o','p'],
     ['q','r','s','t','u'],
     ['v','w','x','y','z']]

def cyph(x):
#   Creating two empty strings, one for encoding the other for decoding
    string = ''
    num = ''
#   Check if numbers or letters were entered, this decides whether we encode or decode with the cypher, if True we encode   
    if x.isalpha() == True:
#       Converting input into lower case to make conversion simpler (no need for another square with capital letters) 
        x = x.lower()
        for i in range(len(L)):
            for n in L[i]:
                for j in x:
                    if n == j:
                        string = string + str(i+1) + str(L[i].index(n)+1)
        return string
#   Decoding time
    else:
#   We need to duplicate spaces because the cypher needs two digits to determine a letter, single spaces will make the string odd and mess up the pairs
        spaces = []
        if ' ' in x:
            x = x.replace(' ', '  ')
#   Looking for and storing location of spaces
        for j in range(len(x)):
            if j % 2 == 0:
                continue
            elif x[j] == ' ':
                spaces.append((j-1)//2)
#   Concatenating the decoded letters
            else:
                num = num + L[(int(x[j-1]) - 1)][(int(x[j]) - 1)]
#   Re-entering the spaces to their original places
        List = [x for x in num]
        for j in spaces:
            List.insert(j, ' ')
        num = ''.join(List)
        return num

print(cyph("543445 14343344 522433 21422415331443 52244423 4311311114"))
print(cyph('hi'))
