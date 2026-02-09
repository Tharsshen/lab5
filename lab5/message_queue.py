from multiprocessing import Process, Queue
import time

def producer(name, q):
    for i in range(5):
        msg = f"{name}-{i}"
        print(f"Producer {name} sending: {msg}")
        q.put(msg)
        time.sleep(0.5)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumer received: {item}")

if __name__ == "__main__":
    q = Queue()

    p1 = Process(target=producer, args=("P1", q))
    p2 = Process(target=producer, args=("P2", q))
    c = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()
    c.start()

    p1.join()
    p2.join()

    q.put(None)
    c.join()
