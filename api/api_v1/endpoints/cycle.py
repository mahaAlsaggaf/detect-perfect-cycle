from unittest import result
from fastapi import APIRouter, Request, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
import json
from typing import List


router = APIRouter()


@router.post("/check", response_model="")
async def check(request: Request):
    lists = await request.json()

    for list in lists:
        visitedNodes = []

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
            # print("len of the list is large")
            # print(lengthOfTheList)
            fastPointer = lists[list][1] + 0
            slowPointer = lists[list][0] + 0

          
            print("fastPointer 1 = ", fastPointer)
            print("slowPointer 0 = ", slowPointer)

            itration = 0
            while(fastPointer < lengthOfTheList):
                itration = itration + 1

                print("##### itration ######")
                print("value of the slow pointer = ", slowPointer,
                      " = ", lists[list][slowPointer])
                print("value of the fast pointer = ", fastPointer,
                      " = ", lists[list][fastPointer])

                if(itration == 20):
                    break
                pointingNode = slowPointer
                pointedNode = lists[list][slowPointer]
                # TODO improve this
                if pointingNode not in visitedNodes:
                    visitedNodes.append(pointingNode)
                if pointedNode not in visitedNodes:
                    visitedNodes.append(pointedNode)

                if(lists[list][fastPointer] == lists[list][slowPointer]):
                    print("there is a cycle")

                    lastVisitedElementPointer = lists[list][slowPointer]
                    lastVisitedElement = lists[list][lastVisitedElementPointer] + 0

                    if(lastVisitedElement == 0):
                        print(
                            "The last element to be visited takes you back to position zero")
                        print("back to the beginning of the list")
                        lists[list] = True
                    break

                if(fastPointer < lengthOfTheList-1):
                    fastPointer = lists[list][lists[list][fastPointer]]
                else:
                    fastPointer = lists[list][0]

                if(slowPointer < lengthOfTheList):
                    slowPointer = lists[list][slowPointer]
                else:
                    slowPointer = lists[list][0]

            if(lists[list] != True):
                lists[list] = False
            else:
                # All elements of the list must be visited.
                if(len(visitedNodes) != lengthOfTheList-1):
                    lists[list] = False

    return lists
