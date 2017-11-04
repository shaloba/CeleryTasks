import sys
from tasks import insert_task

tasks_len = int(sys.argv[1::][0])

for i in range(0, tasks_len):
    insert_task.delay(i)    
