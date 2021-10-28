import time
import os
# path_from = sys.argv[1] - Let us choose that argument in CMD

def readFromFile(*path_to_files):
    if path_to_files is not None:
        for path in path_to_files:
            server_file = open(path, 'r')
            server_configuration = server_file.read()
        print(server_configuration)
        server_file.close()

def writeToFile(*path_to_files):
    if path_to_files is not None:
        for path in path_to_files:
            server_file = open(path, 'w')
            title = "DEVELOPER MODE\n"
            server_file.write(title)
            server_params = ["CPU=20\n", "RAM=30GB\n", "DISKCAPACITY=512GB\n", "\t/dev/fedora34, /dev/\n"]
            server_file.write(''.join(server_params))
        # server_file.close()

readFromFile('server.txt')
writeToFile('server.txt')


start_time = time.localtime()
print("Script start at: {}:{}:{} ".format(start_time.tm_hour, start_time.tm_min, start_time.tm_sec))

stop_time = time.localtime()
print("Script stopped at : {}".format(time.strftime('%X', stop_time)))

difference = time.mktime(stop_time) - time.mktime(start_time)
print("Total time to run the script: {} secounds".format(difference))

stage = os.getenv("STAGE", default='dev').upper()
print(stage)
if stage.startswith("PROD"):
    output = f"SERVER is in {stage} mode"
elif os.path.exists("./server.conf"):
    readFromFile("./server.conf")
else:
    writeToFile("./server.conf")