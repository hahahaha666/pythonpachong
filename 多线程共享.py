import  threading
value=0
gLock=threading.Lock()
def add_value():
    global value
    # 线程上锁
    gLock.acquire()
    for x in range(10000000):
        value+=1
    # 线程释放
    gLock.release()
    print(value)
def main():
    for x in range(3):
        t=threading.Thread(target=add_value)
        t.start()
if __name__ == '__main__':
    main()