# -*- coding: utf-8 -*-
from models import MajorTask
from models import Machine
from models import SubTask
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from settings import DB_URI
from sqlalchemy import or_


engine = create_engine(DB_URI)
Session = sessionmaker(bind=engine)
session = Session()



idle_quality_machines = session.query(Machine).filter(Machine.machine_status==0,Machine.label=='quality').all()

# for q in quality_idle_machines:
#     print q

idle_linux_compile_machines = session.query(Machine).filter(Machine.machine_status==0,Machine.label=='linux_compile').all()

# for l in linux_compile_idle_machines:
#     print l

machine_dict = {'quality':idle_quality_machines, 'linux_compile':idle_linux_compile_machines}



# def pick_subtask():
idle_task_list = session.query(MajorTask).filter(or_(MajorTask.task_status==0,MajorTask.task_status==1)).all()
# for t in idle_task_list:
#     print t


def sub_is_todo(x):
    if x.status == 0:
        return True
    else:
        return False

def find_match(machine_dict):
    for major_task in idle_task_list:
        for subtask in filter(sub_is_todo, major_task.subtasks):
            if len(machine_dict[subtask.label])==0: # this label no machine
                continue
            else:
                target_machine = machine_dict[subtask.label].pop() #get the target machine
                return (target_machine.hostname, subtask.major_task_name, subtask.subtask_type)
    return 0

find_match_result = find_match(machine_dict)
if find_match_result != 0:
    #change the database
    pass

print find_match_result[0]
print find_match_result[1]
print find_match_result[2]