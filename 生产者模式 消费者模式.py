import  threading
import  random
import  time
gmoney=1000
glock=threading.Lock()
gToaltime=10
gtime=0
class one(threading.Thread):
    def run(self):
        global gmoney
        global gtime
        global gToaltime
        while True:
            money=random.randint(1,1000)
            glock.acquire()
            # print(gtime)
            if gtime>=gToaltime:
                glock.release()
                break
            gmoney+=money
            print("%s生产了%d元钱，剩余%d元钱"%(threading.current_thread(),money,gmoney))
            gtime+=1
            glock.release()
            time.sleep(0.5)


class two(threading.Thread):
    def run(self):
        global gmoney
        global gtime
        global gToaltime
        while True:
            money=random.randint(0,1000)
            glock.acquire()
            if gmoney>=money:
                gmoney-=money
                print("%s消费了%d元钱，剩余%d元钱" % (threading.current_thread(), money, gmoney))
            else:
                if gtime>=gToaltime:
                    glock.release()
                    print("钱不够了")
                    break

            glock.release()
            time.sleep(0.5)

def main():
    x=one()
    x.start()
    t=two()
    t.start()

if __name__ == '__main__':
    main()