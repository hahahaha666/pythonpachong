from queue import  Queue
import  threading
import  time
#
# q=Queue(4)
# q.put(3)
# q.put(2)
# q.put(1)
# q.put(6)
# # 返回队列大小
# print(q.qsize())
# # 判断是否为空
# print(q.empty())
# # 判断队列是否满了
# print(q.full())
#
# print(q.get())
# q.get(block=True)

def one(q):
    index=0
    while True:
        q.put(index)
        index+=1
        time.sleep(1)
def two(q):
    while True:
        print(q.get())
def main():
    q=Queue(4)
    t1=threading.Thread(target=one,args=[q])
    t2=threading.Thread(target=two,args=[q])
    t1.start()
    t2.start()
if __name__ == '__main__':
    main()