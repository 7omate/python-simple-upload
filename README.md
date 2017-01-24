# python-simple-upload
SimpleHTTP POST upload script - LAN Transfer files from any device with a web browser

Python script to serve and upload files. I use it to transfer files from my phone to my computer.

Totally unsafe:

- no transport security (TLS, HTTPS)
- no filename sanitization
- no checks of any kind

This is hugly but kind of self contained.

# How to run
Step 1.0:
	git clone https://github.com/7omate/python-simple-upload
	cd python-simple-upload

Step 1 (alt 1):
	wget https://raw.githubusercontent.com/7omate/python-simple-upload/master/pyup.py

Step 1 (alt 2):
	curl -o pyup.py https://raw.githubusercontent.com/7omate/python-simple-upload/master/pyup.py

Step 2 (optional):
	pip install -r requirements.txt

Step 3:
	python pyup.py
