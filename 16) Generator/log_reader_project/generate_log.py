import random

def lofinfo(logName, logMessages):
    """Generate a single log entry with a random message."""
    return f"[{logName}] {random.choice(logMessages)}\n"  # Added newline for file formatting

def gen_log(file_path, log_entry):
    """Append the generated log entry to the file."""
    with open(file_path, "a") as file:
        file.write(log_entry)

def sentLog():
    file_path = "16) Generator\\log_reader_project\\log_file.log"
    option = int(input("log Type 1) INFO 2)ERROR 3) WARNING : "))
    if option==1:
        logName = "INFO"
        randomLogs = ["Server started at 08:00", "User logged in", "Backup completed"]
        log_entry = lofinfo(logName, randomLogs)
        gen_log(file_path, log_entry)
        print(f"Log entry written: {log_entry.strip()}")
    elif option==2:
        logName = "ERROR"
        randomLogs = ["Failed to connect to database"]
        log_entry = lofinfo(logName, randomLogs)
        gen_log(file_path, log_entry)
        print(f"Log entry written: {log_entry.strip()}")
    elif option==3:
        logName = "WARNING"
        randomLogs = ["Disk space low"]
        log_entry = lofinfo(logName, randomLogs)
        gen_log(file_path, log_entry)
        print(f"Log entry written: {log_entry.strip()}")
    else:
        print("Please Choose Option 1-3")


