from plyer import notification
import time
i = 1
while i <= 5:
    if __name__ == "__main__":
        notification.notify(
            title="Drink Water",
            message="Drinking water keeps you healthy",
            app_icon="Drink_water_remainder\glass.ico.ico",
            timeout=2
        )
        time.sleep(5)
        i = i+1
