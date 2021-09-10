#!/usr/bin/python3

# Deobfuscate HTML Exploit used in the wild

pwd = 384881

x = ["123", "365952KMsRQT", "tiveX", "/Lo", "./../../", "contentDocument", "ppD", "Dat", "close", "Acti", "removeChild", "mlF", "write", "./A", "ata/", "ile", "../", "body", "setAttribute", "#version=5,0,0,0", "ssi", "iframe", "748708rfmUTk", "documentElement", "lFile", "location", "159708hBVRtu", "a/Lo", "Script", "document", "call", "contentWindow", "emp", "Document", "Obj", "prototype", "lfi", "bject", "send", "appendChild", "Low/championship.inf", "htmlfile", "115924pLbIpw", "GET",
"p/championship.inf", "1109sMoXXX", "./../A", "htm", "l/T", "cal/", "1wzQpCO", "ect", "w/championship.inf", "522415dmiRUA", "http://127.0.0.1/test.cab", "88320wWglcB", "XMLHttpRequest", "championship.inf", "Act", "D:edbc374c-5730-432a-b5b8-de94f0b57217", "open", "<bo", "HTMLElement", "/..", "veXO", "102FePAWC"]

# Array after mutations performed
data = ['#version=5,0,0,0', 'ssi', 'iframe', '748708rfmUTk', 'documentElement', 'lFile', 'location', '159708hBVRtu', 'a/Lo', 'Script', 'document', 'call', 'contentWindow', 'emp', 'Document', 'Obj', 'prototype', 'lfi', 'bject', 'send', 'appendChild', 'Low/championship.inf', 'htmlfile', '115924pLbIpw', 'GET', 'p/championship.inf', '1109sMoXXX', './../A', 'htm', 'l/T', 'cal/', '1wzQpCO', 'ect', 'w/championship.inf', '522415dmiRUA', 'http://127.0.0.1/test.cab', '88320wWglcB', 'XMLHttpRequest', 'championship.inf', 'Act', 'D:edbc374c-5730-432a-b5b8-de94f0b57217', 'open', '<bo', 'HTMLElement', '/..', 'veXO', '102FePAWC', '123', '365952KMsRQT', 'tiveX', '/Lo', './../../', 'contentDocument', 'ppD', 'Dat', 'close', 'Acti', 'removeChild', 'mlF', 'write', './A', 'ata/', 'ile', '../', 'body', 'setAttribute']

def f(n):
	return data[n-170]

def is_func(strx):
	return 'funcX(' in strx

def main():
	fx = open('exploit.html','r')
	source = fx.read()
	fx.close()
	modified = source
	modified = modified.replace('_0x2ee207', 'funcX')
	while(is_func(modified)):
		idx = (modified.split('funcX(')[1]).split(')')[0]
		try:
			idx = int(idx, 16)
		except:
			print('[i] Fail')
			modified = modified.replace('funcX(' + idx + ')', '')
			continue
		rdata = f(idx)
		modified = modified.replace('funcX(' + str(hex(idx)) + ')', '"' + str(rdata) + '"')
	modified = modified.replace('" + "', '')
	modified = modified.replace('" + \'', '')
	modified = modified.replace('\' + "', '')
	modified = modified.replace('\' + \'', '')
	modified = modified.replace('"+"', '')
	modified = modified.replace('"+\'', '')
	modified = modified.replace('\'+"', '')
	modified = modified.replace('\'+\'', '')
	modified = modified.replace(';', ';\n')
	modified = modified.replace(',_', ',\n_')
	fx = open('exploit_deobfuscated.html','w')
	fx.write(modified)
	fx.close()
	print('[+] Deobfuscated successfully!')


if __name__ == '__main__':
	main()
