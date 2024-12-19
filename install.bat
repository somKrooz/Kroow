:: Step 1: Create a Batch File (equivalent to callable.sh)
echo @echo off > callable.bat
echo python3 -m Kroow %* >> callable.bat

:: Step 2: Make the batch file executable (no chmod in Windows, just creation is enough)

:: Step 3: Create or overwrite the config file by running the Python script
python3 config.py

:: Step 4: Add `callable.bat` path to environment variable (PATH)
set CALLABLE_PATH=%CD%\callable.bat

:: Step 5: Install the Python package
pip install .

:: Step 6: Add a new system command (a simple batch file as an alias)
:: On Windows, we create a batch file to execute the kroow command
echo @echo off > kroow.bat
echo call "%CALLABLE_PATH%" %* >> kroow.bat

:: Step 7: Add the path to `kroow.bat` to the environment variable (PATH)
set KROOW_PATH=%CD%\kroow.bat
setx PATH "%PATH%;%KROOW_PATH%"

:: Step 8: Inform the user that the installation was successful
echo ""
echo Kroow is Successfully Installed.......

:: Step 9: Instructions to refresh environment variables
echo Please restart your Command Prompt or open a new one for the changes to take effect.

