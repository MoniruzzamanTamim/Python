# alarm_clock.py

from datetime import datetime, timedelta
import time
import threading


def get_user_alarm():
    """Get alarm name and time from user."""
    print("🔔 Set Your Alarm")

    alarm_name = input("Alarm Name: ")
    alarm_input = input("Enter date & time (YYYY-MM-DD HH:MM:SS): ")

    try:
        alarm_time = datetime.strptime(alarm_input, "%Y-%m-%d %H:%M:%S")
        if alarm_time < datetime.now():
            print("❌ Alarm time must be in the future.")
            return None, None
        return alarm_name, alarm_time
    except ValueError:
        print("❌ Invalid datetime format. Use: YYYY-MM-DD HH:MM:SS")
        return None, None


def wait_for_alarm(alarm_name, alarm_time):
    """Wait until alarm time and then trigger alarm."""
    while datetime.now() < alarm_time:
        time.sleep(1)
    trigger_alarm(alarm_name)


def trigger_alarm(alarm_name):
    """Show alarm message and handle snooze."""
    print(f"\n⏰ '{alarm_name}' is ringing!")
    print("🔕 Press [s] to snooze (5 mins) or any other key to stop.")

    choice = input(">>> ").lower()
    if choice == 's':
        snooze_alarm(alarm_name)
    else:
        print("✅ Alarm stopped.")


def snooze_alarm(alarm_name):
    """Snooze alarm for 5 minutes."""
    snooze_time = datetime.now() + timedelta(minutes=5)
    print(f"😴 Snoozed! Will ring again at {snooze_time.strftime('%I:%M:%S %p')}")

    # Run snoozed alarm in new thread
    threading.Thread(target=wait_for_alarm, args=(alarm_name, snooze_time)).start()


if __name__ == "__main__":
    alarm_name, alarm_time = get_user_alarm()
    if alarm_name and alarm_time:
        print(f"\n✅ Alarm '{alarm_name}' set for {alarm_time.strftime('%Y-%m-%d %I:%M:%S %p')}\n")
        wait_for_alarm(alarm_name, alarm_time)
