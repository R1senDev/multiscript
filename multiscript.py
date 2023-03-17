import os
import sys
import threading

thrs = []

for i in range(1, len(sys.argv)):
    thrs.append(threading.Thread(target=lambda path: os.system(f'python3 {path}'), args=[sys.argv[i]]))
    thrs[-1].start()
    print(f'- {sys.argv[i]} started')
