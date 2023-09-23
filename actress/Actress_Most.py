

# Python program to read
# json file
 
 
import json
import os
 

#
# Codes for reading the data file "actress.json"
# You do not need to change this part
basedir = '.'
file = os.path.join(basedir, "actress.json")

f = open(file,)

data = json.load(f)

#Load the data into a dictionary
nominated = dict()


for i in data['best_actress']:    
    y = i['year']
    n= i['nominated']
    nominated[y]=n
    print(nominated)
    
# The dict should now looks something like: 
#
#nominated = {
#   2013: ["Name1", "Name2", "Name3", "Name4", "Name5"], 
#   2014: ["Name1", "Name2", "Name3", "Name4", "Name5"], 
#   2015: ["Name1", "Name2", "Name3", "Name4", "Name5"],
#   ETC
#}
 
#######################################
#Add your code here for Ex 8.5
name_counts = dict()
for year, names in nominated.items():
    for name in names:
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1


for name, count in name_counts.items():
    print(f"{name}: {count}")

 
########################################
#Add your code here for the bonus part (optional)
#remember to copy and rename your bonus part program as actress_most.py

most_nom_actor = max(name_counts.values())
actresses = [name for name, count in name_counts.items() if count == most_nom_actor]

print("most_nom_actor=")
for actress in actresses:
    print(actress)
#
# Closing file
f.close()
input()    