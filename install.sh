# Make it Executable
echo "python3 -m Kroow \"\$@\"" > callable.sh
chmod +x callable.sh

# Create or Overwrite Config File 
python3 ./config.py

# Add To Path
CALLABLE_PATH=$(realpath callable.sh)
pip install .

#Add This To Alias
echo "alias kroow='$CALLABLE_PATH'" >> ~/.zshrc


echo ""
echo ""
echo ""
echo "Kroow is Successfully Installed......."
echo "run source ~/.zshrc to reflect the changes"
