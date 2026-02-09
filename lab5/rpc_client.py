from xmlrpc.client import ServerProxy

proxy = ServerProxy("http://localhost:9000/")

a = 10
b = 5
c = 0

print(f"{a} / {b} = {proxy.divide(a, b)}")
print(f"{a} / {c} = {proxy.divide(a, c)}")
