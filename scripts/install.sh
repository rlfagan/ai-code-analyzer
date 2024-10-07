#!/bin/bash
# Install required system packages
sudo apt-get update
sudo apt-get install -y python3 python3-venv python3-pip git

# Set up virtual environment and install dependencies
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start the backend server
echo "Starting backend server..."
python3 app.py &

