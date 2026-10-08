import sys,zlib,struct,json
def encode(data:bytes,out,W=1024):
    data=struct.pack('>I',len(data))+data
    H=(len(data)+W-1)//W; data=data.ljust(W*H,b'\0')
    raw=b''.join(b'\0'+data[i*W:(i+1)*W] for i in range(H))
    def chunk(t,d): return struct.pack('>I',len(d))+t+d+struct.pack('>I',zlib.crc32(t+d)&0xffffffff)
    png=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',W,H,8,0,0,0,0))+chunk(b'IDAT',zlib.compress(raw,0))+chunk(b'IEND',b'')
    open(out,'wb').write(png); return W,H
if __name__=='__main__':
    print(encode(open(sys.argv[1],'rb').read(),sys.argv[2]))
