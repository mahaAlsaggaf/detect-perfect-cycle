from unittest import result
from fastapi import APIRouter, Request, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
import json
from typing import List



router = APIRouter()


@router.post("/check", response_model="")
async def check(request: Request):
    lists = await request.json()
    
    # print(lists['list1'])

    for list in lists:
            visitedNodes = []
            
            print("***** New List *****")
            print(lists[list])
            edgeOfTheList = len(lists[list])-1
            lengthOfTheList = len(lists[list])

            print("lengthOfTheList =" , lengthOfTheList)

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
                # print("len of the list is large")
                # print(lengthOfTheList)
                fastPointer = lists[list][1] + 0 
                slowPointer = lists[list][0] + 0

                # positionZero = lists[list][0] + 0 
                # print(positionZero)
                print("fastPointer 1 = " ,fastPointer)
                print("slowPointer 0 = " , slowPointer)

                itration = 0
                while(fastPointer < lengthOfTheList):
                    itration = itration + 1

                    print("##### itration ######")
                    print("value of the slow pointer = " , slowPointer , " = " , lists[list][slowPointer])
                    print("value of the fast pointer = " , fastPointer , " = " , lists[list][fastPointer])


                    if(itration == 20):
                        break
                    pointingNode = slowPointer                 
                    pointedNode = lists[list][slowPointer]
                    #TODO improve this
                    if pointingNode not in visitedNodes:
                        visitedNodes.append(pointingNode) 
                    if pointedNode not in visitedNodes:
                        visitedNodes.append(pointedNode) 

                    if(lists[list][fastPointer] == lists[list][slowPointer]):
                        #track the occurrence of a cycle
                        print("there is a cycle")
                        # lists[list] = True
                        #The last element to be visited takes you back to position zero
                        # print(lists[list][slowPointer])

                        # lastVisitedElement = lists[list][slowPointer]
                        # lastVisitedElement = lists[list][pointerValue]

                        lastVisitedElementPointer = lists[list][slowPointer]
                        lastVisitedElement = lists[list][lastVisitedElementPointer] + 0
                        print("lastVisitedElement = " , lastVisitedElement)
                        # print("lastVisitedElement = " , lastVisitedElement)
                        # print("positionZero = " , positionZero)
                        # if(lastVisitedElement == positionZero):
                        if(lastVisitedElement == 0):
                            print("The last element to be visited takes you back to position zero")
                            lists[list] = True
                        break
                    
                    

                    if(fastPointer < lengthOfTheList-1):
                        # print("value of the fast pointer before the assigment = " , fastPointer)
                        fastPointer = lists[list][lists[list][fastPointer]]
                        # print("After = " , fastPointer)
                    else:
                    #     print("value of the fast pointer before the assigment = " , fastPointer)
                        fastPointer = lists[list][0]
                    #     print("After = " , fastPointer)

                    if(slowPointer < lengthOfTheList):
                        slowPointer = lists[list][slowPointer]
                    else:
                        slowPointer = lists[list][0] 
                

                # print(lists[list])
                if(lists[list] != True):
                    lists[list] = False
                else:
                    # for node in visitedNodes:
                    #     print(node)
                    #All elements of the list must be visited.
                    if( len(visitedNodes) != lengthOfTheList-1):
                        lists[list] = False
                        
                    
                        
                        # if(not node):
                        #     lists[list] = False
                        #     break

                

               

        
                # lists[list] = 0

            # if(1):
            #     lists[list] = True
            # else:
            #     lists[list] = False

   
    return lists
