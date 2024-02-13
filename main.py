import pystray
import pywintypes
import win32api
import win32con
from PIL import Image
from pystray import MenuItem as item

devmode = pywintypes.DEVMODEType()
devmode.PelsWidth = 1920
devmode.PelsHeight = 1200

devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

win32api.ChangeDisplaySettings(devmode, 0)


def on_set_resolution(width: int, height: int):
    devmode = pywintypes.DEVMODEType()
    devmode.PelsWidth = width
    devmode.PelsHeight = height

    devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

    win32api.ChangeDisplaySettings(devmode, 0)

def on_quit():
    icon.visible = False
    icon.stop()

if __name__ == '__main__':
    image = Image.open("resolution.png")
    
    menu=(
        item("16:10", lambda: on_set_resolution(1920, 1200)),
        item("4:3", lambda: on_set_resolution(1600, 1200)),
        item("Quit", on_quit)
        )

    icon = pystray.Icon("Res Switcher", image, "Res Switcher", menu)
    icon.run()
