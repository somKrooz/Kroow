import os
import json

default = {
    "dir": "/home/somkrooz/Downloads/Wallpapers"
}

def createConfig(path):
    uri = os.path.join(path, "kroow.json")

    with open(uri, "w") as config:
      json.dump(default, config, indent=4)
      print("Generated config file")

# Look for .config Directory
path = ""
ispath = False
home = os.path.expanduser('~')
for i in os.listdir(home):
    if i.startswith(".config"):
        path = os.path.join(home,".config")
        ispath = True

if ispath == False:
    os.mkdir(os.path.join(home,".config"))
    path = os.path.join(home,".config")

#Look For Krooz File 
if(os.path.isdir(path)):
    if(os.path.isdir(os.path.join(path , "Krooz"))):        
        createConfig(os.path.join(path , "Krooz"))
    else:
        krooz = os.mkdir(os.path.join(path , "Krooz"))
        createConfig(os.path.join(path , "Krooz"))
        print("Created Krooz Directory...")
else:
    for i in range(10):
        print("the .config File doesn't Exist...")