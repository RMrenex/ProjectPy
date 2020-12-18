count = 0;
with open("nameslist.txt", "r") as file:
    for line in file:

        count+=1
print(count)