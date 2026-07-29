# file_obj = open("sample.txt",'w')
# string = """Hii Hello
# This is Rakesh
# Today's Topic is fileHandling"""
# file_obj.write(string)
# file_obj.close()


## Opening file in write mode
# file_obj = open("sample.txt",'w')
# string_list = ["Welcome to file handling\n","This is write operation\n"]
# file_obj.writelines(string_list)
# file_obj.close()



## opering file in read mode
# try:
#     file_obj = open("test.txt",'w')
#     data = file_obj.read()
#     print(data)
#     file_obj.close()
# except Exception as e:
#     print(f"Something wrong:{e}")
# finally:
#     file_obj.close() 


## opening file with using "with" keyword
try:
    with open('sample.txt','r') as file_obj:
        data = file_obj.read()
        print(type(data))
        print(data[:10])
        print(data)
except Exception as e:
    print(f"Something wrong: {e}")

