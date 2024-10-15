from Base.Mouth import speak
import psutil
import os
import time
def condition():
    usage = str(psutil.cpu_percent())
    speak(f"CPU is at {usage} percentage")
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"Boss our system have {percentage} percentage battery")

    if percentage>=80:
        speak("we could have enough charging to continue our recording")
    elif percentage>=40 and percentage<=75:
        speak(" we should connect our system to charging point to charge our battery")
    else:
        speak(" we have very low power, please connect to charging otherwise recording should be off...")
def shutdown_system():
    os.system("shutdown /s /t 1")

def restart_system():
    os.system("shutdown /r /t 1")

def shutdown_with_timer(seconds):
    time.sleep(seconds)
    shutdown_system()

def restart_with_timer(seconds):
    time.sleep(seconds)
    restart_system()
def check_ram():
    memory_info = psutil.virtual_memory()
    total_memory = memory_info.total / (1024 ** 3)  # Convert to GB
    available_memory = memory_info.available / (1024 ** 3)
    used_memory = memory_info.used / (1024 ** 3)
    memory_percent = memory_info.percent
    print(f"Total Memory: {total_memory:.2f} GB")
    print(f"Available Memory: {available_memory:.2f} GB")
    print(f"Used Memory: {used_memory:.2f} GB ({memory_percent}%)")
