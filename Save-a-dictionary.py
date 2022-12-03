# we all know that python dictionaries are very useful for storing and retrieving information but the data is held in memory ,so when we exit the program it disappears.
# In this challenge we will save a python dictionary object to a file.

def save_file(dict,relative_file_path):
    with open(f"./{relative_file_path}","w") as f:
        data=f.write(str(dict))
# for saving the dictionary in the file location

def return_dict(file_path):
    with open(f"./{file_path}","r") as f:
        data=f.read()
    return data
# to return the dictionary when someone inputs the file path

save_file({"a":2,"b":3,"c":4},"file.txt")
print(return_dict("file.txt"))