# Secure-File-Transfer
SecureDrop is a secure file transfer application with user authentication, encryption, and communication via both TCP and UDP protocols. It supports the transfer of files using asymmetric RSA encryption and AES encryption for confidentiality. The application is designed to allow users to securely communicate and send files over an encrypted channel.

Files in the Project:
*Contacts.py: Manages the contacts (email addresses and full names) of users. This file allows users to add new contacts and list existing contacts.
* Encrypt|Decrypt.py: Handles the encryption and decryption of files. Files are encrypted using AES with RSA to secure the symmetric key. The encryption ensures that only authorized users can access the content.
*TCP_Client.py: Implements the TCP client that connects to a server using SSL/TLS. It facilitates secure file transfer over TCP.
* TCP_Server.py: Implements the TCP server that accepts secure connections from clients and handles incoming file transfers.
* Udp_Client.py: Implements the UDP client that sends broadcast messages to a server. Useful for notifying the server of a user's presence.
*Udp_Server.py: Implements the UDP server that listens for broadcast messages and responds to clients.
*User_Login.py: Handles user login by verifying the email and password. The password is securely hashed using bcrypt.
*User_Registration.py: Allows new users to register by providing their full name, email address, and password. The password is securely hashed before saving.
*decrypt_private_key.py: A script to decrypt the user's private RSA key using a passphrase.
* generatekeys.py: Generates a new RSA key pair (private and public keys) and saves them in files. The private key is encrypted with a passphrase for added security.
