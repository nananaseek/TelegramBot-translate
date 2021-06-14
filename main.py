import subprocess
import threading
import time


startMain = threading.Thread(target=subprocess.call, args=(["python", "Start_main.py"],))
Main = threading.Thread(target=subprocess.call, args=(["python", "main.py"],))

time.sleep(1)

startMain.start()
Main.start()
