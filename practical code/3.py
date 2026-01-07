# 3. Write a program to count the number of vowels in a given string.
c = 0
str = input("Enter the string: ")
for i in range(len(str)):
    if str[i] == 'a' or str[i]  == 'e' or str[i]  == 'i' or str[i]  == 'o' or str[i]  == 'u' :
        c += 1
print(c) 