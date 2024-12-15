from setuptools import setup

setup(
    name="Kroow",  
    version="0.1",        
    py_modules=["Kroow"], 
    install_requires=[    
        "click==8.*",
    ],
    entry_points={       
        "console_scripts": [
            "Kroow = Kroow:setWallpaper",  
        ],
    }, 
    author="SomKrooz",
    description="A CLI tool to set wallpapers on Gnome",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",  
        "Operating System :: Linux(Gnome)",
    ],
)
