from xmlrpc.server import SimpleXMLRPCServer

server = SimpleXMLRPCServer(("localhost", 9001))
print("Calculator RPC Server running on port 9001...")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")

server.serve_forever()
