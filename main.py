import pywintypes
import win32api
import win32con

devmode = pywintypes.DEVMODEType()
devmode.PelsWidth = 1920
devmode.PelsHeight = 1200

devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

win32api.ChangeDisplaySettings(devmode, 0)
