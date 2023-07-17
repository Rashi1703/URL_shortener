#import module
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import pyshorteners

def url_short_base():
    Url_short =str(Url.get())
    try:
        type_tiny = pyshorteners.Shortener()
        short_url = type_tiny.tinyurl.short(Url_short)
        Url.delete(0,END)
        Url.insert(0,short_url)
    except:
        messagebox.showinfo('Error',"Enter valid URL")
def url_short():
    global Url,Canvas1,my_wind
    my_wind=Tk()
    my_wind.title("Shorten your URL")
    my_wind.geometry("{0}x{1}+0+0".format(my_wind.winfo_screenwidth(),my_wind.winfo_screenheight()))
    my_wind.overrideredirect(True)
    same=True
    n=1.75
# Adding a background image
    background_image =Image.open("urlbg.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 
    
    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(background_image)
    Canvas1 = Canvas(my_wind)
    Canvas1.create_image(750,340,image = img)      
    Canvas1.config(bg="black",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)  
    headingFrame1 = Frame(my_wind,bg="#005282",bd=10)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Shorten your URL", bg='black', fg='#BCD2E8', font=('Forte',45))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(my_wind,bg='black')
    labelFrame.place(relx=0.18,rely=0.4,relwidth=0.65,relheight=0.25)
        
    #Url
    lb1 = Label(labelFrame,text="URL   :", bg='black', fg='#BCD2E8', font=('Forte',30))
    lb1.place(relx=0.05,rely=0.35, relheight=0.2)
    Url = Entry(labelFrame,font=('Courier New Baltic',18))
    Url.place(relx=0.2,rely=0.35, relwidth=0.7, relheight=0.2)
        
    #Generate Button
    GenerateBtn = Button(my_wind,text="Generate",bg='black', fg='#BCD2E8', font=('Forte',35),command=url_short_base)
    GenerateBtn.place(relx=0.42,rely=0.71, relwidth=0.18,relheight=0.1)

    #Quit Button
    quitBtn = Button(my_wind,text="Quit",bg='black', fg='#BCD2E8', font=('Forte',35),command=my_wind.destroy)
    quitBtn.place(relx=0.42,rely=0.86, relwidth=0.18,relheight=0.1)
    
    my_wind.mainloop()
url_short()

