# from threading import Thread
#
# def f():
#     while True:
#         b = 53*53
#
# if __name__ == '__main__':
#     plist = []
#     # 启动10个线程
#     for i in range(10):
#         p = Thread(target=f)
#         p.start()
#         plist.append(p)
#
#     for p in plist:
#         p.join()

'''
资源管理器-进程名称PyCharm-%CPU 100%,没有使用其他核心
'''

# from multiprocessing import Process
#
# def f():
#     while True:
#         b = 53*53
#
# if __name__ == '__main__':
#     plist = []
#     for i in range(4):
#         p = Process(target=f)
#         p.start()
#         plist.append(p)
#
#     for p in plist:
#         p.join()

'''
资源管理器-进程名称Python*4-%CPU 100%,没有使用其他核心
'''

from multiprocessing import Process,Manager
from time import sleep

def f(taskno,return_dict):
    sleep(2)
    # 存放计算结果到共享对象中
    return_dict[taskno] = taskno

if __name__ == '__main__':
    manager = Manager()
    # 创建 类似字典的 跨进程 共享对象
    return_dict = manager.dict()
    plist = []
    for i in range(10):
        p = Process(target=f, args=(i,return_dict))
        p.start()
        plist.append(p)

    for p in plist:
        p.join()

    print('get result...')
    # 从共享对象中取出其他进程的计算结果
    for k,v in return_dict.items():
        print (k,v)

