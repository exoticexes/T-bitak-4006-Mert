import serial
import pyautogui
import time

# Arduino bağlantı noktası (Windows'ta genelde COM3, COM4 olur)
# Deneme yanılmayla bulabilirsin: Arduino IDE'deki 'Araçlar > Port' kısmında yazar
arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # Bağlantı otursun

print("Subway Surfers Kontrol Sistemi Başlatıldı!")

while True:
    if arduino.in_waiting > 0:
        data = arduino.readline().decode().strip()
        print("Gelen veri:", data)

        if data == "RIGHT":
            pyautogui.press('right')
        elif data == "LEFT":
            pyautogui.press('left')
        elif data == "UP":
            pyautogui.press('up')
        elif data == "DOWN":
            pyautogui.press('down')