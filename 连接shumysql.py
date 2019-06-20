import  pymysql
conn=pymysql.connect(host="localhost",user="root",password="123456",database="test",port=3306)

cursor=conn.cursor()
# # cursor.execute("select 1")
# sql="""
# # insert into  jd(name,price,author,pub) values ("3333",'2','33','77')
# insert into  jd(name,price,author,pub) values (null,%s,%s,%s)
# """
#
# one="大家啊空间"
# two="877"
# re="89989"
# cursor.execute(sql,(one,two,re))
# # result=cursor.fetchall()
# conn.commit()
# # print(result)
#
# conn.close()


# 查找数据

sql="""
select  name,price,author, pub from jd  
# select  * from  jd  跟上面同一个意思 *代表所有字段
"""
cursor.execute(sql)
# result=cursor.fetchone()
# result=cursor.fetchall()
# """打印前面两条数据"""
result=cursor.fetchmany(2)
for i in result:
    print(i)
# print(result)


conn.close()