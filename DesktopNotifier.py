from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="***Time To Work***",
            message="Hey!! Hurry up ts time to Code....",
            timeout=5)
        time.sleep(300)
