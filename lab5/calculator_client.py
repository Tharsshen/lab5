from xmlrpc.client import ServerProxy

proxy = ServerProxy("http://localhost:5050/")

print("Add:", proxy.add(8, 2))
print("Subtract:", proxy.subtract(8, 2))
print("Multiply:", proxy.multiply(8, 2))
print("Divide:", proxy.divide(8, 2))
print("Divide by zero:", proxy.divide(8, 0))
