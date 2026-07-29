import csv

# try:
#     with open('user.csv','w',newline="") as file:
#         writer = csv.writer(file)
#         writer.writerows([['Id','Name','Age'],
#                          ['1',"rakesh",22],
#                          ['2',"sindhu",23]])
# except Exception as e:
#     print("something wrong: {e}")


## reading csv file content

try:
    with open('user.csv','r',newline="") as file:
        reader = csv.reader(file)
        print(reader)
        for row in reader:
            print(row)
except Exception as e:
    print("something wrong: {e}")
