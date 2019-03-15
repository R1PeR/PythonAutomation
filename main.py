import time, os
import pyautogui
from pywinauto import Application
def click_on_relative(var, relative_pos):
    result = None
    while result is None:
        try:
            result = pyautogui.locateCenterOnScreen(var, region=(relative_pos.left,relative_pos.top,relative_pos.right,relative_pos.bottom))
            pyautogui.click(result);
        except:
            pass
def click_on(var):
    result = None
    while result is None:
        try:
            result = pyautogui.locateCenterOnScreen(var)
            pyautogui.click(result);
        except:
            pass
fileDir = os.path.dirname(os.path.abspath(__file__))
app = Application(backend="uia").start(r"C:\Users\Lenovo\Downloads\BMW 318i stock BY MARK/Pro Tweaker 0.6R.exe")
app['Pro Tweaker 0.6R'].set_focus()
relative_pos = app['Pro Tweaker 0.6R'].rectangle()
pyautogui.moveTo(1,1)
for x in range(1,8):
    dlg = app.top_window()
    relative_pos = app.dlg.rectangle()
    var = ('\\button%s.PNG' % x)
    click_on_relative(fileDir+var, relative_pos)
app = Application(backend="uia").start(r"C:\Users\Lenovo\Downloads\BMW 318i stock BY MARK/DriverPos.exe")
app['DriverPos'].set_focus()
for x in range(8,11):
    var = ('\\button%s.PNG' % x)
    click_on(fileDir+var)
