import Tkinter 
import tkMessageBox

from alarm.AlarmAction import AlarmAction

top = Tkinter.Tk(className = "Alarm")

def callBack():
    tkMessageBox.showinfo("Alarm", "Alarm Stopped")
    top.quit()


class SoundAlarmAction(AlarmAction):

    def do_action(self):
	B = Tkinter.Button(top, text="Stop Alarm", command = callBack)
	B.pack()
	top.mainloop()

