#Banker's Algorithm (Using Dictionaries)

#Tạo Dict là Need
def calc_need(allocated,max_):
    need = {}
    for pid in allocated:
        max_list = max_[pid]
        alloc_list = allocated[pid]
        need_values = []
        for i in range(len(max_list)):
            need_values.append(max_list[i] - alloc_list[i])
        need[pid] = need_values
    return need

def bankers(allocated,max,available):
    need = calc_need(allocated,max)
    work = available
    safe_sequence = []
    not_processed = 0
    processes = []
    # Tạo List Các Tiến Trình (Tạm Thời)
    for pid in allocated:
        processes.append(pid)
    total_processes = len(processes)
    finish = {}
    for pid in allocated:
        finish[pid] = False
    # Check Điều Kiện
    while not_processed < total_processes and len(safe_sequence) != total_processes:
        pid = processes.pop(0)
        print("Process:", processes)
        # Lấy Lần Lượt Các Tiến Trình Để Kiểm Tra
        if work >= need[pid] and finish[pid] == False:
            # Thêm Tiến Trình Vào Chuỗi An Toàn
            safe_sequence.append(pid)
            print("Safe Sequence:", safe_sequence)
            # Cho Số Lượng Chuỗi Sai Bằng 0
            not_processed = 0
            finish[pid] = True
            # Cộng Allocated Vào Work
            for i in range(len(work)):
                work[i] += allocated[pid][i]
            print("Work:", work)
        else:
            not_processed += 1
            # Trả Lại Tiến Trình
            processes.append(pid)

    for pid in allocated:
        print("Finish:", finish[pid])
    if len(safe_sequence) != total_processes:
        print("No Safe Sequence Possible !")
    else:
        print("Safe Sequence Possible:")
        print(*safe_sequence, sep = " -> ")
        print("Work:",work)

if __name__ == "__main__":
    available = [3, 3, 2]
    allocated = {"P0":[0,1,0], "P1":[2,0,0], "P2":[3,0,2], "P3":[2,1,1], "P4":[0,0,2]}
    max = {"P0":[7,5,3], "P1":[3,2,2], "P2":[9,0,2], "P3":[2,2,2], "P4":[4,3,3]}
    bankers(allocated,max,available)
