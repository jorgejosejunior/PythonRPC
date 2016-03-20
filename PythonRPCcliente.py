__author__ = 'Administrador'
import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
multicall = xmlrpclib.MultiCall(proxy)
multicall.adicao(7,3)
multicall.subtracao(7,3)
multicall.multiplicacao(7,3)
multicall.divisao(7,3)
resultado = multicall()
print "7+3=%d, 7-3=%d, 7*3=%d, 7/3=%d"%tuple(resultado)