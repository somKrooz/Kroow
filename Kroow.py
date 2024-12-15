import subprocess
import os
import click
import random
import json

def default(d):
    try:
        subprocess.run(f"gsettings set org.gnome.desktop.background picture-uri-dark 'file://{d}'",shell=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print("Error Occured Setting Up The Wallpaper")

def randomWall():
    path = os.path.join(os.path.expanduser("~"),".config","Krooz","kroow.json")
    with open(path,"r") as config: 
        path = json.load(config)["dir"]

    try:
        randomWallpaper = []
        for i in os.listdir(path):
            if str(i).startswith(".git"):
                pass
            randomWallpaper.append(str(os.path.join(path, i)))
        
        subprocess.run(f"gsettings set org.gnome.desktop.background picture-uri-dark 'file://{random.choice(randomWallpaper)}'",shell=True, capture_output=True, check=True,text=True)
    except subprocess.CalledProcessError as e:
        print("Error Occured Setting Up The Wallpaper")

@click.command()
@click.option("--d", type=str, help="Set a specific wallpaper by providing the full path")
@click.option("--r", is_flag=True, help="Set a random wallpaper")
def setWallpaper(d, r):
    if(d):
        default(d)
    elif(r):
        randomWall()
    else:
        print("Please provide flags")

if __name__ == "__main__":
    setWallpaper()