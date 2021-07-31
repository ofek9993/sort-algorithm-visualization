# in the algorithms directory i created each algorithm which then get imported in the main directory
import time

# Importing colors from colors.py
from colors import *
#merge algo func which merge each list to a sorted list after each stack call of the merg sort funcition
def merge_to_sorted_list(data, start, mid, end, drawData, timeTick):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end + 1):
        #when we done compare each value untill we reached the mid of the list then the other half of the list is already sorted and we just append it
        if p > mid:
            tempArray.append(data[q])
            q += 1
         #same logic in here
        elif q > end:
            tempArray.append(data[p])
            p += 1
        #compare each value in data list form start to mid to each value in data list form mid to last
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p += 1
        else:
            tempArray.append(data[q])
            q += 1

    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start += 1
def merge_sort(data, start, end, drawData, timeTick):
    if start < end:
        mid = int((start + end) / 2)
        #recursive call that break down our list
        merge_sort(data, start, mid, drawData, timeTick)
        merge_sort(data, mid+1, end, drawData, timeTick)
        #recursive call that merg the broke down lists into a sorted one
        merge_to_sorted_list(data, start, mid, end, drawData, timeTick)
        # the line that prints the data into the ui screen
        drawData(data, [PURPLE if x >= start and x < mid else YELLOW if x == mid
                        else DARK_BLUE if x > mid and x <=end else BLUE for x in range(len(data))])
        #the speed in which the sorted algorithm runs
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])

#this sort algo is really straightforward
def insertion_sort(data, drawData, timeTick):
    for i in range(len(data)):
        temp = data[i]
        k = i
        while k > 0 and temp < data[k - 1]:
            data[k] = data[k - 1]
            k -= 1
        data[k] = temp
        drawData(data, [YELLOW if x == k or x == i else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])

#this function iterate our sub data list that are geiven by our quick sort func below and retun our new pivot posotion in the list
def partition(data, start, end, drawData, timeTick):
    #index to the first item on the list
    i = start
    j=end-1
    #our pivot is the last item of our list
    pivot=data[end]
    while i<j:
        while i<end and data[i]<pivot:
            i+=1
        while j>start and data[j]>=pivot:
            j-=1
        #the two while loops moving i forward and j backwards correspondingly and if the statment in the if line is ture we initiate a swap
        if i<j:
            data[i],data[j]=data[j],data[i]
    # at the end if the line in the if statment is ture then data[i] is our new pivot and we return his index
    if data[i]>pivot:
        data[i],data[end]=data[end],data[i]
    return i


def quick_sort(data, start, end, drawData, timeTick):
    if start < end:
        pivot_position = partition(data, start, end, drawData, timeTick)
        quick_sort(data, start, pivot_position - 1, drawData, timeTick)
        quick_sort(data, pivot_position + 1, end, drawData, timeTick)

        drawData(data, [PURPLE if x >= start and x < pivot_position else YELLOW if x == pivot_position
        else DARK_BLUE if x > pivot_position and x <= end else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])