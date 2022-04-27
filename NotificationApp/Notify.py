from email import message
from socket import timeout
import time 
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title="** Now it's Coding Time..!!",
        message = "You're the Computer Engineer You must do coding Everyday it improves your skills..",
        app_icon = "E:\Shivam 27.01.21 Backup\D Backup\Desktop\My_App\Alarm_Clock\code.ico",
        timeout=10
    )