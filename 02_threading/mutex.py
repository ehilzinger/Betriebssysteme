import threading

# Erzeugung einer Liste als gemeinsam genutzte Ressource
shared_list = []
# Erzeugung eines Mutex
mutex = threading.Lock()

# Funktion zum Hinzufügen von Elementen zur gemeinsam genutzten Liste


def add_to_list(item):
    # Sperren des Mutex, um exklusiven Zugriff sicherzustellen
    mutex.acquire()
    shared_list.append(item)
    print(f"Element {item} wurde zur Liste hinzugefügt.")
    # Freigeben des Mutex nach dem Zugriff
    mutex.release()


# Erzeugung von Threads, die Elemente zur Liste hinzufügen
threads = []
for i in range(5):
    thread = threading.Thread(target=add_to_list, args=(i,))
    threads.append(thread)
    thread.start()

# Auf das Ende aller Threads warten
for thread in threads:
    thread.join()

print("Endgültige Liste:", shared_list)
