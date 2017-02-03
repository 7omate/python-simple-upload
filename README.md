# python-simple-upload
SimpleHTTP POST upload script - LAN Transfer files from any device equipped with a web browser.

Python script to serve and upload files. I use it to transfer files from my phone to my computer.

For convenience, a qrcode displays your IP adress, the qcrode is generated using an external service.
This may be sensitive information.

Totally unsafe:

- no transport security (TLS, HTTPS)
- no filename sanitization
- no checks of any kind

Quick and dirty file HTTP Post file upload in Python using Flask.

# How to run
Option 0:

	git clone https://github.com/7omate/python-simple-upload
	cd python-simple-upload
	pip install -r requirements.txt
	python pyup.py

Option 1:

	wget https://raw.githubusercontent.com/7omate/python-simple-upload/master/pyup.py
	python pyup.py

Option 2:

	curl -o pyup.py https://raw.githubusercontent.com/7omate/python-simple-upload/master/pyup.py
	python pyup.py

# Troubleshooting
For options 1 and 2, make sure the required libraries are available to the version of python you're using:

	python -c "import flask"
	pip install flask
