# from threading import Thread
# from time import sleep
#
# bank = {
#     'byhy' : 0
# }
#
# # 定义一个函数，作为新线程执行的入口函数
# def deposit(theadidx,amount):
#     balance =  bank['byhy']
#     # 执行一些任务，耗费了0.1秒
#     sleep(0.1)
#     bank['byhy']  = balance + amount
#     print(f'子线程 {theadidx} 结束')
#
# theadlist = []
# for idx in range(10):
#     thread = Thread(target = deposit,
#                     args = (idx,1)
#                     )
#     thread.start()
#     # 把线程对象都存储到 threadlist中
#     theadlist.append(thread)
#
# for thread in theadlist:
#     thread.join()
#
# print('主线程结束')
# print(f'最后我们的账号余额为 {bank["byhy"]}')

'''
子线程 1 结束
子线程 7 结束
子线程 0 结束子线程 6 结束
子线程 2 结束
子线程 8 结束

子线程 9 结束
子线程 5 结束
子线程 3 结束
子线程 4 结束
主线程结束
最后我们的账号余额为 1
'''

from threading import Thread, Lock
from time import sleep

print('主线程开始')

bank = {
    'byhy': 0
}

bankLock = Lock()


# 定义一个函数，作为新线程执行的入口函数
def deposit(theadidx, amount):
    # 操作共享数据前，申请获取锁
    bankLock.acquire()

    balance = bank['byhy']
    # 执行一些任务，耗费了0.1秒
    sleep(0.1)
    bank['byhy'] = balance + amount
    print(f'子线程 {theadidx} 结束')

    # 操作完共享数据后，申请释放锁
    bankLock.release()


theadlist = []
for idx in range(10):
    thread = Thread(target=deposit,
                    args=(idx, 1)
                    )
    thread.start()
    # 把线程对象都存储到 threadlist中
    theadlist.append(thread)

for thread in theadlist:
    thread.join()

print('主线程结束')
print(f'最后我们的账号余额为 {bank["byhy"]}')