import os

filepath = input("Enter the Path to the folder:")
try:
    for i in os.listdir(filepath):
        try:
            if not int(i[-5]) % 2 == 0:
                os.remove(filepath + "\\" + str(i))
        except:
            print("Filename did not match expected input: " + str(i))
            break
except:
    print("path does not work")
