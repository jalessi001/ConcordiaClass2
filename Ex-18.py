import time

with open("log.txt", 'w') as f:
    f.write("Info-start time" + str(time.asctime(time.localtime((time.time()))) + '\n'))
    time.sleep(2)
    f.write("Warning: " + str(time.asctime(time.localtime(time.time())) + '\n'))
    time.sleep(2)
    f.write("Closing time" + str(time.asctime(time.localtime(time.time())) + '\n'))