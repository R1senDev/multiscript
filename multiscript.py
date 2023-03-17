import os
import sys
import threading

thrs = []
paths = []

if len(sys.argv) == 1:
    if os.path.isfile('.msclist'):
        with open('.msclist', 'r') as file:
            paths_ = file.read()
            paths = paths_.split('\n')[:-1]
else:
    paths = sys.argv
if not paths:
    raise ValueError('no paths specified')

for i in range(0, len(paths)):
    if paths[i] == __file__.split('/')[-1]: continue
    thrs.append(threading.Thread(target=lambda path: os.system(f'python3 {path}'), args=[paths[i]]))
    thrs[-1].start()
    print(f'- {paths[i]} started')

print()
