import socket #导入socket模板
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建一个socket
s.connect(('www.sina.com.cn',80)) #建立与新浪网站连接

#发送数据请求
s.send(b'GET/HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')
#接收数据
buffer=[]
while True:
    d=s.recv(1024) #每次最多接收服务器端1k字节数据
    if d: #是否为空数据
        buffer.append(d) #字节串增加到列表中
    else:
        break
data=b''.join(buffer)
header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))


#把接收的数据写入文件:
with open('sina.html','wb') as f:
    f.write(html)
                       
          
