#[bash]

sudo apt install python3.10-venv
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1
fi

echo "MY_SECRET_TOKEN=$1" > .env
