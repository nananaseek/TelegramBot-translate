import subprocess
import threading
import time


startMain = threading.Thread(target=subprocess.call, args=(["python", "start_do_com"],))

time.sleep(1)

startMain.start()
