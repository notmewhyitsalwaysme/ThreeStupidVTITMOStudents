import time

import task1
import task2
import task3
import task4

def check_1_2_tasks() -> None:
    start_time = time.time()
    for _ in range(100):
        task1.convert("mySchedule.ini", "mySchedule.bin")
        task2.convert("mySchedule.bin", "mySchedule.hcl")
        task4.convert("mySchedule.bin", "mySchedule.xml")
    print(f"Custom converters: {time.time() - start_time}")
    
def check_3_task() -> None:
    start_time = time.time()
    for _ in range(100):
        task3.convert("MySchedule.ini", "MyScheduleWithLibs.bin", "MyScheduleWithLibs.hcl")
    print(f"Lib converter: {time.time() - start_time}")
    
if __name__ == '__main__':
    check_1_2_tasks()
    check_3_task()
        