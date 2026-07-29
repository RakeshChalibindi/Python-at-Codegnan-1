# add 1-n numbers to output.trxt file
try:
    with open("output.txt",'w',newlines="") as file:
        n=int(input())
        for i in range(1,n+1):
            file.write(str(i) + " ")
except Exception as e:
    print(f"Something wrong:{e}")
2