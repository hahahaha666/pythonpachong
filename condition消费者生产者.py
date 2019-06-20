import  threading
import  random,time
gmoney=1000
Condition=threading.Condition()
gToaltime=10
gtime=0
class one(threading.Thread):
    def run(self):
        global gmoney
        global gtime
        global gToaltime
        while True:
            money=random.randint(1,1000)
            Condition.acquire()
            # print(gtime)
            if gtime>=gToaltime:
                Condition.release()
                break
            gmoney+=money
            print("%s生产了%d元钱，剩余%d元钱"%(threading.current_thread(),money,gmoney))
            gtime += 1
            Condition.notify_all()
            Condition.release()
            time.sleep(0.5)


class two(threading.Thread):
    def run(self):
        global gmoney
        global gtime
        global gToaltime
        while True:
            money=random.randint(0,10000)
            Condition.acquire()
            while gmoney<money:
                if gtime>=gToaltime:
                    return
                print("%s准备消费%d元钱，剩余%d元钱"%(threading.current_thread(),money,gmoney))
                Condition.wait()
            gmoney-=money
            print("%s消费了%d元钱，剩余%d元钱" %(threading.current_thread(),money,gmoney))
            Condition.release()
            time.sleep(0.5)

def main():
    x=one()
    x.start()
    t=two()
    t.start()

if __name__ == '__main__':
    main()