import time
import threading



def timer1(seconds):
    time.sleep(seconds)
    timeout()

def timer2(seconds):
    threading.Timer(seconds, timeout).start()

def timeout():
    print("Таймер остановлен")



for i in range(5):
    print(f'{i}. итерация, таймер запущен')
    timer2(3)
