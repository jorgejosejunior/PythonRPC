__author__ = 'jorge junior'
#exemplo feito para python 2.7
from SimpleXMLRPCServer import SimpleXMLRPCServer

def adicao (x,y):
    return x+y

def subtracao(x,y):
    return x-y

def multiplicacao (x,y):
    return x*y

def divisao (x,y):
    return x/y

server=SimpleXMLRPCServer(("localhost",8000))
print "Ouvindo porta 8000...."
server.register_multicall_functions()
server.register_function(adicao, 'adicao')
server.register_function(subtracao, 'subtracao')
server.register_function(multiplicacao, 'multiplicacao')
server.register_function(divisao, 'divisao')
server.serve_forever()