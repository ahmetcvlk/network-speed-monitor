import psutil
import tkinter as tk

def update_speed():
    net_io = psutil.net_io_counters()
    global last_recv

    download_speed = (net_io.bytes_recv - last_recv) / 1024 /1024  # MB

    last_recv = net_io.bytes_recv
    total = net_io.bytes_recv / 1024 / 1024  # MB

    label.config(text=f"Download: {download_speed:.2f} MB/s\nTotal: {total:.2f} MB")
    root.after(1000, update_speed)




# Başlangıç verileri
last_recv = psutil.net_io_counters().bytes_recv

# Tkinter Penceresi
root = tk.Tk()
root.title("Network")
root.geometry("200x100")
root.attributes("-topmost", True)  # Pencereyi en üstte tut

label = tk.Label(root, text="Bağlantı Hızı Ölçülüyor...", font=("Arial", 10), justify="center")
label.pack(expand=True)

update_speed()
root.mainloop()


# pyinstaller --onefile --windowed app.py

