from multiprocessing import Process, Pipe

def sender(conn):
    for i in range(5):
        print(f"Sender sending: {i}")
        conn.send(i)
    conn.send(None)  # Sentinel

def receiver(conn):
    while True:
        item = conn.recv()
        if item is None:
            break
        print(f"Receiver got: {item}")

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p1 = Process(target=sender, args=(parent_conn,))
    p2 = Process(target=receiver, args=(child_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
