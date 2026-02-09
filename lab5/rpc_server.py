from xmlrpc.server import SimpleXMLRPCServer

server = SimpleXMLRPCServer(("localhost", 9000))
print("RPC Server running on port 9000...")

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

server.register_function(add, "add")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")

server.serve_forever()
