from celery import Celery
from celery.utils.log import get_task_logger

# Initialize celery
celery = Celery('tasks', backend='redis://' ,broker='amqp://guest:guest@127.0.0.1:5672//')
celery.conf.CELERY_IGNORE_RESULT = False
celery.conf.CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'


@celery.task
def hasPerfectCycles(lists):
    for list in lists:
        hasPerfectCycle = False
        visitedNodes = lists[list][:]
        lengthOfTheList = len(lists[list])

        if(lengthOfTheList == 0):
            lists[list] = False
        elif(lengthOfTheList == 1):
            if(lists[list][0] == 0):
                lists[list] = True
            else:
                lists[list] = False
        else:
            fastPointer = lists[list][1] 
            slowPointer = lists[list][0] 

            beginningOfTheListElement = lists[list][0] 

            while(fastPointer < lengthOfTheList):
                
                if(lists[list][fastPointer] == lists[list][slowPointer]):
                    hasPerfectCycle = True
                    break

                if(fastPointer < lengthOfTheList-1):
                    fastPointer = lists[list][lists[list][fastPointer]]
                else:
                    fastPointer = lists[list][0]

                if(slowPointer < lengthOfTheList):
                    slowPointer = lists[list][slowPointer]
                else:
                    slowPointer = lists[list][0]

            if(hasPerfectCycle != True):
                hasPerfectCycle = False
            else:
                traverse = lists[list][0]
                visitedNodes[0] = True
                for x in range(lengthOfTheList):
                    traverse = lists[list][traverse]
                    visitedNodes[traverse] = True

                #The last element to be visited takes you back to position zero
                if(traverse != beginningOfTheListElement):
                   hasPerfectCycle = False
                
                # All elements of the list must be visited.
                for node in visitedNodes: 
                    if(type(node) != type(True)): 
                        hasPerfectCycle = False
                        break; 

                if(hasPerfectCycle):
                    lists[list] = True
                else:
                    lists[list] = False

    return lists
