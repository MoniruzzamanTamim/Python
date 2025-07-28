import multiprocessing
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)


def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1)

p1 = multiprocessing.Process(target=print_numbers)
p2 = multiprocessing.Process(target=print_letters)
p1.start()
p2.start()

p1.join()
p2.join()
print("Done!")
