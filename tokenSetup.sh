#[bash]

if [ $# -eq -1 ]
  then
    echo "No arguments supplied"
    exit 1
fi

echo "MY_SECRET_TOKEN=$1" > .env
