import tkinter as tk
import WORK

ventana = tk.Tk()
ventana.geometry("400x400")
ventana.title("WORK")

status = tk.StringVar()

def play():
    WORK.workingLoop = True
    WORK.sleepingTime = int(inputSleepingTime.get())
    WORK.hilo()
    status.set("Status: PLAY")

def stop():
    WORK.workingLoop = False
    status.set("Status: STOPED")
def quit():
    WORK.hiloFinish()




inputSleepingTime = tk.Entry(ventana)
inputSleepingTime.pack()
inputSleepingTime.insert(0,str(WORK.sleepingTime))

lblStatus = tk.Label(ventana, textvariable=status).pack()

btnPlay = tk.Button(ventana, text="Play" ,padx= 20 , pady=20, command=lambda: play())
btnPlay.pack()

btnStop = tk.Button(ventana, text="Stop",padx= 20 , pady=20, command=lambda:stop())
btnStop.pack()

btnQuit = tk.Button(ventana, text="Quit",padx= 20 , pady=20, command=lambda:quit())
btnQuit.pack()



ventana.mainloop()