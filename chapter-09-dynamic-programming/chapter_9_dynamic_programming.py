#9.1. Yes, then MP3 Player + Iphone + guitar would give max value i.e. is 4500

#9.2. Water,Food and Camera are the optimal set of items which you have to take in your campaign trip.
import numpy as np
#Longest common Substring 
str1 = input("Enter a string: ")
lst_str1 = list(str1)
str2 = input("Enter a string: ")
lst_str2 = list(str2)
table = np.zeros((len(str1),len(str2)))

for i in range(len(str1)):
    for j in range(len(str2)):
        if lst_str2[j] == lst_str1[i]:
            table[i][j] = table[i-1][j-1] + 1
        else:
            table[i][j] = 0
print(table)


#Longest Common Subsequence
str1 = input("Enter a string: ")
lst_str1 = list(str1)
str2 = input("Enter a string: ")
lst_str2 = list(str2)
table = np.zeros((len(str1),len(str2)))

for i in range(len(str1)):
    for j in range(len(str2)):
        if lst_str2[j] == lst_str1[i]:
            table[i][j] = table[i-1][j-1] + 1
        else:
            table[i][j] = max(table[i-1][j],table[i][j-1])
print(table)

'''9.3.[[0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 2. 0. 0.]
 [0. 0. 0. 3. 0.]] '''