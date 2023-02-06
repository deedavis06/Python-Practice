#Create a while loop that copies the string 'orange' onto a new list and exit the loop if the next value on the list is not 'orange'.
squares= ['orange', 'orange', 'orange', 'purple', 'blue']

#Create new list
new_squares=[]

#start index at 0
i=0
#While the squares list of whatever index number its on is 'orange' AND the index number is less than the length of the squares list... 
while(squares[i]=='orange' and i<len(squares)):
    #add 'orange' to new list
    new_squares.append(squares[i])
    #go onto the next element in the list
    i=i+1
print(new_squares)