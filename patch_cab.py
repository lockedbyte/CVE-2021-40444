#!/usr/bin/env python3

# Patch cab file

m_off = 0x2d
f = open('www/out.cab','rb')
cab_data = f.read()
f.close()

out_cab_data = cab_data[:m_off]
out_cab_data += b'\x00\x5c\x41\x00'
out_cab_data += cab_data[m_off+4:]

out_cab_data = out_cab_data.replace(b'..\\championship.inf', b'../championship.inf')

f = open('www/out.cab','wb')
f.write(out_cab_data)
f.close()
