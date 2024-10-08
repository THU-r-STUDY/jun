def upHeap(heap, index):
    if index > 1:
        if heap[index] > heap[index//2]:
            tmp = heap[index]
            heap[index] = heap[index//2]
            heap[index//2] = tmp
            upHeap(heap, index//2)

def downHeap(heap, index):
    if index*2 < len(heap):
        child_index = index*2    
        if index*2+1 < len(heap):
            if heap[index*2] < heap[index*2+1]:
                child_index = index*2+1    
        if heap[index] < heap[child_index]:
            tmp = heap[index]
            heap[index] = heap[child_index]
            heap[child_index] = tmp
            downHeap(heap, child_index)

def heapPush(heap, item):
    heap.append(item)
    upHeap(heap, len(heap) - 1)
    print(f"Heap : {heap}\n")
    

def heapPop(heap):
    if len(heap) > 1:
        heap[1] = heap[-1]
        heap.pop()
        downHeap(heap, 1)
        print(f"Heap : {heap}\n")
    else:
        print("\nHeap이 비어있습니다.\n")

heap = [None]

while 1:
    print("*** Heap ***")
    print("HeapPush : 1")
    print("HeapPop : 2")
    print("끝내기 : 3")
    
    print("\n옵션을 입력해주세요 : ", end='')
    try:
        option = int(input())

        if option == 1:
            while 1:
                print("Push 할 값 입력 : ", end = '')
                try:
                    n = int(input())
                    heapPush(heap, n)
                    break
                except ValueError:
                    print("숫자를 입력해주세요!!!")

        elif option == 2:
            heapPop(heap)
        elif option == 3:
            break
        else:
            print("\n1, 2, 3 중에서 입력해 주세요!!!")
    except ValueError:
        print("\n1, 2, 3 중에서 입력해 주세요!!!")