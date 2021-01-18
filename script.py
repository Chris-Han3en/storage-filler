import os, sys

def application():
    x = 0
    with open("name.txt", "w") as file: #change the file name
        file.write(
            "write here" #write a first line for the first line
        )
        while 100 > x:
            file.write("example") #write what you want spammed here, the larger the better
            x += x

application()
