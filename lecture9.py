# Необходимо создать два параллельных потока, каждый из которых
# выводил бы на экран числа от 10 до 1 в обратном порядке с
# интервалом в одну секунду.
# В выводе должно быть понятно какая нить выполняется, и когда
# каждая из них начинает и заканчивает своё выполнение.

import threading
import time
import datetime


def countdown_timer(timer_id, interval):
    now_t = datetime.datetime.now()
    clock_t = now_t.strftime("%H:%M:%S")
    print(f"[{clock_t}][Timer {timer_id}]: start")
    for counter in range(10, 0, -1):
        now_t = datetime.datetime.now()
        clock_t = now_t.strftime("%H:%M:%S")
        print(f"[{clock_t}][Timer {timer_id}]: {counter}")
        time.sleep(interval)

    now_t = datetime.datetime.now()
    clock_t = now_t.strftime("%H:%M:%S")
    print(f"[{clock_t}][Timer {timer_id}]: finish")


for i in range(2):
    t = threading.Thread(target=countdown_timer, args=(i, 1,))
    t.daemon = True
    t.start()

time.sleep(12)
