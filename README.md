# SimpleFTPSoftware
## Introduction
A small file transmission tool based on C/S architecture, and it can send and receive file based on `socket` module and part of the FTP protocol in Python.
## Function
### Client
1. login via FTP protocol
2. show file list of the server after logged in
3. download file from server
4. upload file to server
### Server
1. authentication and encryption of username and password
2. show users' info and status
3. show file transmission status by asterisk progress bar
## Usage
1. start the FTP server on given IP and port
2. FTP client connect to server
3. client insert Unix-like command to operate on files after logged on, e.g. `rm test.txt` or `get test.jpg`
## Future Improvement
Move the username and encrypted password into real MySQL database instead of storing in `user.ini`
