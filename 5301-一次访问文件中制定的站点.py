import urllib.request
import chardet

def main():
    i=0

    with open("G:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36-32\\urls.txt")as f: #以只读的方式打开文件
        #读取待访问的网址
        #由于urls.txt每一行一个URL
        #所以按换行符'\n'分割
        urls=f.read().splitlines()

    for each_url in urls:
        response=urllib.request.urlopen(each_url)
        html=response.read()

        #识别网页编码
        encode=chardet.detect(html)['encoding']
        if encode=='GB2312':
            encode='GBK'

        i+=1
        filename="url_%d.txt" % i

        with open(filename,'w',encoding=encode) as each_file:
            each_file.write(html.decode(encode,"ignore"))

if __name__=='__main__':
    main()
        
        
        
