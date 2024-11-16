#[bash]

python3 -m venv env
if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment."
    exit 1
fi
source env/bin/activate
python3 -m pip install -r requirements.txt
