import tkinter
import WORK

ventana = tkinter.Tk()
ventana.geometry("250x400")
ventana.title("WORK")

def play():
    WORK.workingLoop = True
    WORK.sleepingTime = int(inputSleepingTime.get())
    WORK.working()

def stop():
    WORK.workingLoop = False

inputSleepingTime = tkinter.Entry(ventana)
inputSleepingTime.pack()
inputSleepingTime.insert(0,str(WORK.sleepingTime))


btnPlay = tkinter.Button(ventana, text="Play" ,padx= 20 , pady=20, command=lambda: play())
btnPlay.pack()

btnStop = tkinter.Button(ventana, text="Stop",padx= 20 , pady=20, command=lambda:stop())
btnStop.pack()



ventana.mainloop()