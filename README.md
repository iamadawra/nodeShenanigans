Node.JS Chat server and Python Cleverbot server
===

Powered with Node.js, Express, Socket.io and Jade.
It use Bootstrap from Twitter and the javascript libraries SlimScroll.
Thanks to Node.js being asynchronous, the chat can handle a lot of simultaneous connections without lag.

The python Chatbot server is a wrapper around the Cleverbot API and communicates with the Node.js server through the ZeroRPC library. The communication is currently dependent on the ZeroMQ library which is deprecated and this aspect of the application needs to updated.

## Install the modules :

	- Go to the chat directory and use this command
	- npm install express@4.12.0
	- npm install socket.io@1.3.4
	- npm install jade@1.9.2
	- npm install zerorpc@0.9.5

## Installation checks:
	- Make sure the Node and Python server are listening on the same port

## How to use :

	- node server.js (On one server)
	- python botspeak.py
	- Go to IP:port from any browser to start chatting !

### Credits

Creator : [Aayush Dawra] (http://github.com/iamadawra)