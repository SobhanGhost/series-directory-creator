import os


add=input("Enter the directory for the series with no ending back slashes:\n")+"\\"



s="S0"
e="0"

num_season=int(input("Enter the number of seasons:\n"))
num_episode=int(input("Enter the number of each season episode:\n"))

z=input("if folders to be created does not start from 1, enter 0:\n")

tS=1
tE=1
if z=="0":
    tS=int(input("Enter the starting point for folders:\n"))






t = ""

for i in range(num_season):
    if tS > 9:
        s = "S"
    
    t = add + s + str(tS)
    os.mkdir(t)
    os.chdir(t)
    for j in range(num_episode):
        os.mkdir(t + "\\" + e + str(tE))
        if tE > 9:
            e = ""
        tE+=1
    tS+=1
    tE=1
    e="0"
