from operator import add

def detect(process, allocation, request, work):
    n=len(process)
    finish=[False]*n
    total_finish = len(finish)
    safe_sequence = []
    not_processed = 0
    while total_finish != len(safe_sequence) and total_finish != not_processed:
        for i in range(n):
            if finish[i]==False and request[i]<=work:
                work=list(map(add, work, allocation[i]))
                finish[i]=True
                safe_sequence.append(process[i])
                not_processed = 0
            else:
                not_processed += 1

    print("Finish:", finish)
    print("Work:", work)
    print("Safe Sequence:")
    print(*safe_sequence, sep = " -> ")
    for i in range(n):
        if finish[i]==False:
            print('Deadlock Occurs For The Process {}'.format(i))
    if finish==[True]*n:
        print('=> No Deadlock!')

if __name__=='__main__':
    process=["P0", "P1", "P2", "P3", "P4"]
    allocation=[[0, 1, 0], [2, 0, 0], [3, 0, 3], [2, 1, 1], [0, 0, 2]]
    request=[[0, 0, 0], [2, 0, 2], [0, 0, 0], [1, 0, 0], [0, 0, 2]]
    available=[0, 0, 0]

    detect(process, allocation, request, available)
