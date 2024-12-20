import platform
import os
import ctypes
import subprocess
import json
import random
import click
from abc import ABC, abstractmethod

# PathBuilder
class PathBuilder(ABC):
    @abstractmethod
    def GetConfigPath(self) -> str:
        pass

class WindowsPath(PathBuilder):
    def GetConfigPath(self) -> str:
        return os.path.join(os.path.expanduser("~"), "Krooz", "kroow.json")

class LinuxPath(PathBuilder):
    def GetConfigPath(self):
        return os.path.join(os.path.expanduser("~"), ".config", "Krooz", "kroow.json")

class PathFactory:
    @staticmethod
    def GetPlatform() -> PathBuilder:
        Platform = platform.system()

        if Platform == "Linux":
            return LinuxPath()
        if Platform == "Windows":
            return WindowsPath()
        else:
            raise NotImplementedError(f"We don't support {Platform}.")

# Wallpaper Method
class WallpaperMethod(ABC):
    @abstractmethod
    def Implementation(self, Path: str):
        pass

class WinMethod(WallpaperMethod):
    def Implementation(self, Path: str):
        SPI_SETDESKWALLPAPER = 20  
        SPIF_UPDATEINIFILE = 0x01  
        SPIF_SENDWININICHANGE = 0x02
        try:
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, Path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
            print(f"Wallpaper set to: {Path}")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

class LinMethod(WallpaperMethod):
    def Implementation(self, Path: str):
        try:
            command = f"gsettings set org.gnome.desktop.background picture-uri-dark '{Path}'"
            subprocess.run(command, shell=True, capture_output=True, check=True, text=True)
            print(f"Wallpaper set to: {Path}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            return False

class SettingFactory:
    @staticmethod
    def GetWallpaperMethod() -> WallpaperMethod:

        if platform.system() == "Windows":
            return WinMethod()
        elif platform.system() == "Linux":
            return LinMethod()
        else:
            raise NotImplementedError("Wallpaper setting not supported on this platform.")

class ApplicationSystem(ABC):
    @abstractmethod
    def Behaviour(self, Path: str = None) -> str:
        pass

class RandomWallpaperSystem(ApplicationSystem):
    def Behaviour(self, Path: str = None) -> str:
            path = Path
            try:
                with open(path, "r") as config:
                    try: 
                        path = json.load(config)["dir"]
                    except FileNotFoundError as e:
                        print(f"Invalid Directory: {e}")
            except Exception as e:
                print(f"Error reading configuration: {e}")
                return None

            randomWallpaper = []
            for i in os.listdir(path):
                if not str(i).startswith(".git") and i.endswith(('.png', '.jpeg', '.jpg')):
                    randomWallpaper.append(os.path.join(path, i))

            if randomWallpaper:
                return random.choice(randomWallpaper)
            else:
                print("No valid wallpapers found in the directory.")
                return None

class SimpleWallpaperSystem(ApplicationSystem):
    def __init__(self, wallpaper_path: str):
        self.wallpaper_path = wallpaper_path
    def Behaviour(self, Path: str = None) -> str:
        return self.wallpaper_path


class WallpaperFactory:
    @staticmethod
    def CreateSystem(mode: str, wallpaper_path: str = None) -> ApplicationSystem:
        if mode == "d" and wallpaper_path:
            return SimpleWallpaperSystem(wallpaper_path)
        elif mode == "r" :
            return RandomWallpaperSystem()
        else:
            raise NotImplementedError("This System Not Implemented Yet...")


def ApplyWallpaper(path: str = None , random:bool = False , isconfig:bool = False):
    WallpaperMethod = SettingFactory.GetWallpaperMethod()
    WallpaperSystem = WallpaperFactory()
    ConfigPath = PathFactory().GetPlatform().GetConfigPath()   
    
    if isconfig:
        print(f"Config Path: {ConfigPath}")
        return

    if random:
        Path = WallpaperSystem.CreateSystem(mode="r").Behaviour(ConfigPath)  
    elif not random:
        Path = WallpaperSystem.CreateSystem(mode="d" , wallpaper_path=path).Behaviour() 
    else:
        Path = None

    if Path:
        WallpaperMethod.Implementation(Path)  


@click.command()
@click.option("--d", type=str, help="Set a specific wallpaper by providing the full path")
@click.option("--r", is_flag=True, help="Set a random wallpaper From Config Directory")
@click.option("--config", is_flag=True, help="Get Config File Path")

def setWallpaper(d, r, config):
    if d:
        ApplyWallpaper(path=d)  
    elif r:
        ApplyWallpaper(random=True) 
    elif config:
        ApplyWallpaper(isconfig=True)
    else:
        print("Please provide either a path or use the random flag to set a wallpaper.")

setWallpaper()