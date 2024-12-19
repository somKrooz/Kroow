#Make it Executable
echo "python3 -m Kroow \"\$@\"" > callable.sh
chmod +x callable.sh

#Create or Overwrite Config File 
python3 ./config.py

#Add To Path
CALLABLE_PATH=$(realpath callable.sh)
pip install .
echo "alias kroow='$CALLABLE_PATH'" >> ~/.bashrc

echo ""
echo "Kroow is Sucessfully Installed......."
source ~/.bashrc
