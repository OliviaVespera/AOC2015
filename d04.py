from hashlib import md5
import threading
from multiprocessing import Process

stop_threads = False

def calculation(code: str, low, high, size) -> str:
    global stop_threads
    for i in range(low, high+1):
        hash = md5(f"{code}{i}".encode())
        # print(hash.hexdigest(), i, end="\n")
        if hash.hexdigest()[:size] == "0"*size:
            some_rlock = threading.RLock()
            with some_rlock:
                print(f"We found it! {i} ", end="\n")
            stop_threads = True
            return i
        if stop_threads:
            print("we are stopping")
            return -1
    print("not found")


def main() -> None:
    # instruction = read_file("d3_input.txt")
    # results = calculate_answer("ckczppom")
    processes = []
    low = 0
    size = 6
    num_of_processes = 16
    search_range = 250_000
    for i in range(low*num_of_processes, low*num_of_processes+num_of_processes):
        print(i*search_range, (i+1)*search_range-1)
        processes.append(Process(target=calculation, args=("ckczppom" ,i*search_range, (i+1)*search_range-1, size)))

    for i in range(num_of_processes):
        processes[i].start()

if __name__ == "__main__":
    main()
