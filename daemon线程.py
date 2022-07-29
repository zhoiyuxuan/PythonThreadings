# from threading import Thread
# from time import sleep
#
# def threadFunc():
#     sleep(2)
#     print('子线程 结束')
#
# thread = Thread(target=threadFunc)
# thread.start()
# print('主线程结束')

'''
主线程结束
子线程 结束
'''

from threading import Thread
from time import sleep

def threadFunc():
    sleep(2)
    print('子线程 结束')

thread = Thread(target=threadFunc,
                daemon=True # 设置新线程为daemon线程
                )
thread.start()
print('主线程结束')