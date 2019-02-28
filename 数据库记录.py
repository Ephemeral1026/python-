import sqlite3
book=[("021",25,"大学计算机"),("022",30,"大学英语"),("023",18,"艺术欣赏"),("024",35,"高级语言程序设计")]
#打开数据库
Con=sqlite3.connect("E:\sales.db")

#创建游标对象
Cur=Con.cursor()
#插入多行数据
Cur.executemany("insert into book(id,price,name) values(?,?,?)",book)
#修改一行数据
Cur.execute("Update book set price=? where name=?",(25,"大学英语"))
#删除一行数据
n=Cur.execute("delete from book where price=?",(25,))
print("删除了",n.rowcount,"行记录")
Con.commit()
Cur.close()
Con.close()
