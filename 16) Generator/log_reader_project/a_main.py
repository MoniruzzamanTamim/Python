from b_read_log import log_read
from generate_log import sentLog
print("MAIN")
def main():
    while True:
        try:
            option = int(input("Choose an Option:\n (1) Show Logs\n (2) Generate Log\n (3) Exit\nYour Choice: "))
        except ValueError:
            print("⚠️ Please enter a valid number (1, 2, or 3).")
            continue

        if option == 1:
            log_read()
        elif option == 2:
            sentLog()
        elif option == 3:
            print("✅ Your task is complete. Exiting...")
            break
        else:
            print("🚫 Invalid option. Please choose 1, 2, or 3.")


main()
