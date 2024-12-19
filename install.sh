#Make it Executable
echo "python3 -m Kroow \"\$@\"" > callable.sh
chmod +x callable.sh

#Create or Overwrite Config File 
python3 ./config.py

#Add To Path
CALLABLE_PATH=$(realpath callable.sh)
pip install .

if [[ "$SHELL" == *"bash"* ]]; then
    echo "alias kroow='$CALLABLE_PATH'" >> ~/.bashrc
    source ~/.bashrc

elif [[ "$SHELL" == *"zsh"* ]]; then
    echo "alias kroow='$CALLABLE_PATH'" >> ~/.zshrc
    source ~/.zshrc
else
    echo "Unknown shell"
fi


echo ""
echo ""
echo "Kroow is Sucessfully Installed......."
