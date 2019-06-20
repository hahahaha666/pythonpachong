import  threading
import  time

# 传统方式
# def coding():
#     for x in range(3):
#         print("正在写代码%s"%x)
#         time.sleep(1)
#
# def drawing():
#     for x in range(3):
#         print("正在写画图%s"%x)
#         time.sleep(1)
# def main():
#     coding()
#     drawing()
# if __name__ == '__main__':
#     main()

# 多线程方式
# def coding():
#     for x in range(3):
#         print("正在写代码%s"%x,threading.current_thread())
#         time.sleep(1)
#
# def drawing():
#     for x in range(3):
#         print("正在写画图%s"%x)
#         time.sleep(1)
# # def main():
# #     coding()
# #     drawing()
#
# def thread():
#     t1=threading.Thread(target=coding)
#     t2=threading.Thread(target=drawing)
#     t1.start()
#     t2.start()
#     # 查看总共多少个线程
#     print(threading.enumerate())
# if __name__ == '__main__':
#     thread()

# 继承线程
class  codingT(threading.Thread):
    def run(self):
        for x in range(3):
            print("正在写代码%s" % x, threading.current_thread())
            time.sleep(1)
class drawingT(threading.Thread):
    def run(self):
        for x in range(3):
            print("正在写画图%s" % x)
            time.sleep(1)

def main():
    t1=codingT()
    t2=drawingT()
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()