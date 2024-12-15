echo "python3 -m Kroow \"\$@\"" > callable.sh
chmod +x callable.sh
CALLABLE_PATH=$(realpath callable.sh)
pip install .
echo "alias kroow='$CALLABLE_PATH'" >> ~/.bashrc
source ~/.bashrc
echo ""
echo "Kroow is Sucessfully Installed......."