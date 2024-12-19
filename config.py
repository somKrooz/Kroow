import os
import json
import platform


def CreatePath() -> str:
    if platform.system() == "Windows":
       return "C:/Users/somkr/Downloads/Wallpapers/anime"
    
    elif platform.system() == "Linux":
        return "/home/somkrooz/Downloads/Wallpapers"

default = {
    "dir": CreatePath()
}

def createConfig(path):
    uri = os.path.join(path, "kroow.json")

    with open(uri, "w") as config:
      json.dump(default, config, indent=4)
      print("Generated config file")

# Linux
if platform.system() == "Linux": 
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

#Windows
elif platform.system() == "Windows":
    path = ""
    ispath = False
    home = os.path.expanduser('~')
    for i in os.listdir(home):
        if i.startswith("Krooz"):
            path = os.path.join(home,"Krooz")
            ispath = True

    if ispath == False:
        os.mkdir(os.path.join(home,"Krooz"))
        path = os.path.join(home,"Krooz")
    
    createConfig(path)

else:
    raise NotImplementedError(f"Not Implemented for: {platform.system()}")