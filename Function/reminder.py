import dateparser
import datetime
import time
from Function.utils import speak_async

reminders = []


def save_reminder_to_file(task, remind_time):
    with open("reminders.txt", "a") as f:
        f.write(f"{remind_time.strftime('%Y-%m-%d %H:%M')} | {task}\n")


def add_reminder(task, remind_time):
    reminders.append({
        "task": task,
        "time": remind_time,
        "notified": False
    })
    save_reminder_to_file(task, remind_time)


def get_reminder_time(text):
    return dateparser.parse(text)


def check_reminders():
    while True:
        try:
            with open("reminders.txt", "r") as f:
                reminder_lines = f.readlines()

            now_dt = datetime.datetime.now()

            for line in reminder_lines:
                try:
                    reminder_time, message = line.strip().split(" | ")
                    reminder_dt = datetime.datetime.strptime(reminder_time, "%Y-%m-%d %H:%M")

                    if now_dt >= reminder_dt and (now_dt - reminder_dt).total_seconds() < 120:
                        speak_async(f"Reminder: {message}")
                        print(f"Reminder: {message}")
                except ValueError:
                    print(f"Skipping malformed line: {line.strip()}")

            time.sleep(60)
        except Exception as e:
            print("Error checking reminders:", e)
            time.sleep(60)

