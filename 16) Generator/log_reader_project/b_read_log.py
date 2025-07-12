import time
def access_logFile(file_path):
    
    with open(file_path, "r") as readFile:
        for line in readFile:
            yield line.strip()

def filter_log(log_read, keyword):
    for line in log_read:
        if keyword in line:
            yield line
        elif keyword == "ALL":
            yield line

def log_read():
    file_path = "16) Generator\\log_reader_project\\log_file.log"
    log_read = access_logFile(file_path)

    option = int(input("Choose an Option (1) Search Log\t(2)Show All LOG): ")) 
    if option == 1:
        keyword = input("Type your Keyword: ").upper()
        filter_logFile = filter_log(log_read, keyword)
        
        print("LOG GENERATING............")
        time.sleep(1)
        count = 0
        for item in filter_logFile:
            print(item)
            count +=1
        print(f"Log Generate Successfully......\nTotal Log Generate: {count}, for Keyword \"{keyword}\"")
    elif option ==2:
        count = 0
        print("LOG GENERATING............")
        time.sleep(1)
        keyword = "ALL"
        filter_logFile = filter_log(log_read, keyword)
        count = 0
        for item in filter_logFile:
            print(item)
            count +=1
        print(f"Log Generate Successfully......\nTotal Log Generate: {count}, for Keyword \"{keyword}\"")
        


