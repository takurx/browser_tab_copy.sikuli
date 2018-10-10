import sys

def close_tab():
    #タブを閉じる
    keyDown(Key.CTRL)
    type("w")
    keyUp(Key.CTRL)

def new_tab():
    #新しいタブ
    keyDown(Key.CTRL)
    type("t")
    keyUp(Key.CTRL)

def copy_link():
    keyDown(Key.CTRL)
    type("l")
    type("c")
    keyUp(Key.CTRL)
 
def paste_link():
    keyDown(Key.CTRL)
    type("v")
    keyUp(Key.CTRL)
    type(Key.ENTER)

def switching_browser():
    keyDown(Key.ALT)
    type(Key.TAB)
    keyUp(Key.ALT)

# click firefox and click chrome
sleep(1)
click("1539146182947.png")
sleep(1)
click("1539146604344.png")
sleep(1)
    
for i in range(0, 2):
    copy_link()
    sleep(1)
    close_tab()
    sleep(2)
    switching_browser()
    sleep(1)
    new_tab()
    sleep(1)
    paste_link()
    sleep(4)
    switching_browser()
    sleep(1)