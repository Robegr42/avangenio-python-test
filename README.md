# avangenio-python-test
# Client-Server Model

This project shows a client-server connection model, where text strings are generated which are sent to the server to be analyzed and subsequently provide a response to the client.

This solution shows an improvement over a classic model as it supports several clients at the same time.(Multi-Client Model)

## Execution

### Requirements

A computer with python installed, version 3.8 or higher

### Running the server

Open a terminal on the root folder an type

```python
python3 server.py
```
This will start the server where the clients will send messages

### Running the client

Open a terminal on the root folder an type

```
python3 client.py
```
This will start create a cliente instance that will generate a text that will be send to the server to be analyzed. Since this is proposal support multi-client we can create several instances

