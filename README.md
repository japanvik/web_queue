# Web Queue
Web Queue is an extremely simple FIFO Message Queue with a web API written in Python. The message queue is persisted using SQLLite.
You can issue web requests to put and pop arbritary data into the Queue.

It leverages these 2 awesome projects.

- (Persist-Queue)[https://github.com/peter-wangxu/persist-queue/blob/master/persistqueue/exceptions.py]
- (Flask API)[https://www.flaskapi.org]

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

Web Queue is written in Python. The code base was written and tested using Python 3.9.1, buy should be comaptible with any recent versions of Python.

### Installing

Checkout the repostitory and install dependencies

```
$git clone https://github.com/japanvik/web_queue.git
$cd web_queue
$pip install -r requirements.txt
```

### Running the server
Web Queue is a FlaskAPI application, so you can use it to run it in various
ways Flask services can be executed. However, the most simplest way to get
started is to run api.py directly.

```
$python api.py 
```

This should create a local endpoint on port 5002. You can modify the port in
the api.py file to your liking. Also, please be warned that the 'host'
parameter is set to '0.0.0.0' which allows access from other machines on the
network. Please have a look at the Flask documentation for details on how to
configure your application. 


## Usage

### API Endpoints

#### Put a message into the queue
The root ('/') end point accepts a POST with a message parameter which will be
stored in the queue

```
$curl -X POST http://127.0.0.1:5002/ -d message="hello world"
OK 1 in QUEUE
```
Note that the result of the post will return the number of messages in the
queue.

#### Pop a message from the queue
Issuing a GET to the root ('/') endpoint will return a json object with the
below structure.

```
$ curl -X GET http://127.0.0.1:5002/
{"message": "hello world", "created_at": "Mon, 28 Dec 2020 13:11:02 GMT"}
```

#### Retrieving the message count
The /count endpoint will return the number of messages in the queue as an
integer text.

```
$ curl -X GET http://127.0.0.1:5002/count
1
```

