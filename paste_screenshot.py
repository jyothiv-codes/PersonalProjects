import pyautogui
import time
import os
import tkinter as tk





def paste_screenshot():
    # Captures screenshot, saves it to the specified folder and shows a pop-up message if the screenshot was successful
    message=""
    try:
        screenshot = pyautogui.screenshot()  
        filename = f"Screenshot_{time.strftime('%Y%m%d_%H%M%S')}.png"  # The file is created with the current timestamp
        screenshot.save(os.path.join("/Users/jyothivaidyanathan/projects/PostgreSQL-Practice", filename))  # Save the screenshot
        message = "Success!"
    except:
        message="Failure!"

    # Create the main window of the pop-up
    root = tk.Tk()
    root.title("Screenshot status")
    # Label widget is used to display the image
    label = tk.Label(root, text=message)
    label.pack()

   

    # Set the desired window size
    window_width = 400
    window_height = 200

    # This helps center the message
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    offset_x = (screen_width - window_width) // 2
    offset_y = (screen_height - window_height) // 2

    geometry_string = f"{window_width}x{window_height}+{offset_x}+{offset_y}"

    # Apply the geometry to the root window
    root.geometry(geometry_string)

    # Event loop is started to display the window
    root.mainloop()




while True:
    print("Do you want to click a screenshot now? (y/n)")
    time.sleep(15)
    answer=input()
    if answer=="y":
        print("taking screenshot")
        time.sleep(5)
        paste_screenshot()
    else:
        pass




