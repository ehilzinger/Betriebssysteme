from threading import Semaphore
import threading
import time

# Initialisierung des Semaphors mit einem Zählerwert von 3
semaphore = Semaphore(3)


def access_resource(thread_id):
    print(f"Thread {thread_id} versucht auf die Ressource zuzugreifen.")
    semaphore.acquire()
    print(f"Thread {thread_id} greift auf die Ressource zu.")
    time.sleep(2)  # simuliert den Zugriff auf die Ressource
    semaphore.release()
    print(f"Thread {thread_id} gibt die Ressource frei.")


# Erzeugung von Threads, die auf die Ressource zugreifen
threads = []
for i in range(5):
    thread = threading.Thread(target=access_resource, args=(i,))
    threads.append(thread)
    thread.start()

# Auf das Ende aller Threads warten
for thread in threads:
    thread.join()
