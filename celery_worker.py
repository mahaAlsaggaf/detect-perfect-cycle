from celery import Celery
from celery.utils.log import get_task_logger

# Initialize celery
celery = Celery('tasks', backend='redis://' ,broker='amqp://guest:guest@127.0.0.1:5672//')
celery.conf.CELERY_IGNORE_RESULT = False
celery.conf.CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'


@celery.task
def detectPerfectCycles(lists):
    for list in lists:
        visitedNodes = lists[list][:]
        print("***** New List *****")
        print(lists[list])
        lengthOfTheList = len(lists[list])

        print("lengthOfTheList =", lengthOfTheList)

        if(lengthOfTheList == 0):
            lists[list] = False
            print("len of the list = 0")
        elif(lengthOfTheList == 1):
            if(lists[list][0] == 0):
                lists[list] = True
                print("len of the list = 1")
            else:
                lists[list] = False
        else:
            fastPointer = lists[list][1] 
            slowPointer = lists[list][0] 

            beginningOfTheListElement = lists[list][slowPointer] 

            print("beginningOfTheListElement = " , beginningOfTheListElement)

            print("fastPointer 1 = ", fastPointer)
            print("slowPointer 0 = ", slowPointer)

            while(fastPointer < lengthOfTheList):

                print("##### itration ######")
                print("value of the slow pointer = ", slowPointer,
                      " = ", lists[list][slowPointer])
                print("value of the fast pointer = ", fastPointer,
                      " = ", lists[list][fastPointer])
                
                if(lists[list][fastPointer] == lists[list][slowPointer]):
                    print("there is a cycle")

                    visitedNodes[slowPointer] = True
                    visitedNodes[fastPointer] = True

                    lastVisitedElementPointer = lists[list][slowPointer]
                    print("lastVisitedElementPointer = ", lastVisitedElementPointer)
                    lastVisitedElement = lists[list][lastVisitedElementPointer] 
                    print("lastVisitedElement = ", lastVisitedElement)

                    visitedNodes[lastVisitedElementPointer] = True

                    if(lastVisitedElement == 0 or lastVisitedElement == beginningOfTheListElement):
                        print("The last element to be visited takes you back to position zero")
                        print("back to the beginning of the list")
                        lists[list] = True
                    break

                if(fastPointer < lengthOfTheList-1):
                    visitedNodes[fastPointer] = True
                    fastPointer = lists[list][lists[list][fastPointer]]
                else:
                    fastPointer = lists[list][0]

                if(slowPointer < lengthOfTheList):
                    visitedNodes[slowPointer] = True
                    slowPointer = lists[list][slowPointer]
                else:
                    slowPointer = lists[list][0]

            if(lists[list] != True):
                lists[list] = False
            else:
                # All elements of the list must be visited.
                for node in visitedNodes: 
                    print("The node is = " , node)
                    if(type(node) != type(True)): 
                        lists[list] = False

    return lists
