import Tkinter
import requests
from PIL import Image,ImageTk

#get image using inspirobot API
def getImgReq():
    link = "http://inspirobot.me/api?generate=true"
    f = requests.get(link)
    imgurl=f.text
    img = Image.open(requests.get(imgurl, stream=True).raw)
    return img
    
def exitTK(event=None):
    root.destroy()

def refreshTK(event=None):
    root.unbind("<Return>")
    refreshButton.configure(state=Tkinter.DISABLED)
    new_img=ImageTk.PhotoImage(getImgReq())
    picture_panel.configure(image=new_img)
    picture_panel.image=new_img
    refreshButton.configure(state=Tkinter.NORMAL)
    root.bind("<Return>",refreshTK)
    
#TKinter window
root = Tkinter.Tk()
root.title("InsBot beta")

#Buttons
exitButton = Tkinter.Button(root, text ="EXIT", bg="red", fg="white", command = exitTK)
refreshButton = Tkinter.Button(root, text ="REFRESH", bg="green", command = refreshTK)

exitButton.pack()
refreshButton.pack()
root.bind("<Return>",refreshTK)
root.bind("<Escape>",exitTK)

#display image
img = ImageTk.PhotoImage(getImgReq())
picture_panel = Tkinter.Label(root, image = img)
picture_panel.pack()

root.mainloop()
