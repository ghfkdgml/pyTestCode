import xmlrpc.client

proxy=xmlrpc.client.ServerProxy("http://localhost:6999/")
num=111
result=proxy.double(num)
print(result)
