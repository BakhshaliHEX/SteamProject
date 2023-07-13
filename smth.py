from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk

BG_COLOR = "#171D25"

def activeBtnUnderline(activeBtn: Button, oldBtn: Button):
    activeBtn.config(font=f"{activeBtn['font']} underline", fg="#1A9FFF")
    oldBtn.config(font=f"{activeBtn['font'][:-9]}", fg="#ffffff")


class ScrollableFrame:
    """A scrollable tkinter frame that will fill the whole window"""

    def __init__(self, master, width, height, mousescroll=0):
        self.mousescroll = mousescroll
        self.master = master
        self.height = height
        self.width = width
        self.main_frame = Frame(self.master)
        self.main_frame.pack(fill=BOTH, expand=1)

        self.scrollbar = Scrollbar(self.main_frame, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas = Canvas(self.main_frame, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(expand=True, fill=BOTH)

        self.scrollbar.config(command=self.canvas.yview)

        self.canvas.bind(
            '<Configure>',
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.frame = Frame(self.canvas, width=self.width, height=self.height)
        self.frame.pack(expand=True, fill=BOTH)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.frame.bind("<Enter>", self.entered)
        self.frame.bind("<Leave>", self.left)

    def _on_mouse_wheel(self, event):
        self.canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

    def entered(self, event):
        if self.mousescroll:
            self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)

    def left(self, event):
        if self.mousescroll:
            self.canvas.unbind_all("<MouseWheel>")


class Game:
    def __init__(self, name, price, discount, description, image):
        self.name = name
        self.price = price
        self.discount = discount
        self.description = description
        self.image = image

def getPhotos():
    linksOnPhoto = ["darktide", "division", "ghostrecon", "remnant", "codevein", "arma", "battlefield"]
    photos = []
    for i in range(len(linksOnPhoto)):
        oldImg = Image.open(f"gameImgs/{linksOnPhoto[i]}.png")
        resImg = oldImg.resize((274, 158))
        img = ImageTk.PhotoImage(resImg)
        photos.append(img)
    return photos





class Shop(Frame):
    def __init__(self, master: Tk):
        super().__init__(master)
        self.master = master
        self.master.geometry("1284x798+160+20")
        self.master.resizable(False, False)
        self.master.config(background=BG_COLOR)

        obj = ScrollableFrame(self.master, 1284, 798)
        self.frame = obj.frame

        self.widgets()
        self.setGames()

    def widgets(self):
        self.shopHeaderShopBtn = Button(self.frame, text="МАГАЗИН", background=BG_COLOR, fg="#ffffff", borderwidth=0, font="Arial 16")
        self.shopHeaderLibraryBtn = Button(self.frame, text="БИБЛИОТЕКА", background=BG_COLOR, fg="#ffffff", borderwidth=0, font="Arial 16")
        self.shopHeaderOfficeBtn = Button(self.frame, text="USER", background=BG_COLOR, fg="#ffffff", borderwidth=0, font="Arial 16 underline")

        self.shopHeaderShopBtn.place(relx=0.35, rely=0.03)
        self.shopHeaderLibraryBtn.place(relx=0.45, rely=0.03)
        self.shopHeaderOfficeBtn.place(relx=0.585, rely=0.03)
        for i in range(3): self.frame.columnconfigure(index=i, weight=1)
        activeBtnUnderline(self.shopHeaderShopBtn, self.shopHeaderOfficeBtn)


        smrSaleImg = Image.open("images/summerSale.png")
        resSmrSaleImg = smrSaleImg.resize((1262, 798))
        smrImg = ImageTk.PhotoImage(resSmrSaleImg)
        # Label(self.frame, image=smrImg).place(relx=0, rely=0.1)
        # summerSaleImgLbl.place(relx=0.05, rely=0.1)
        imagesCanvas = Canvas(self.frame, width=1262, height=700, bg="#000000", highlightthickness=0)
        imagesCanvas.place(relx=0.0, rely=0.1)
        imagesCanvas.create_image(0, 0, anchor=NW, image=smrImg)
        imagesCanvas.image = smrImg

    def setGames(self):
        photos = getPhotos()
        darktide = Game(name="Darktide", price=29.99, discount=0, description="smth", image=photos[0])
        division = Game(name="Division", price=16.49, discount=70, description="smth", image=photos[1])
        ghostrecon = Game(name="GhostRecon", price=0, discount=0, description="smth", image=photos[2])
        remnant = Game(name="Remnant", price=18.49, discount=65, description="smth", image=photos[3])
        codevien = Game(name="CodeVien", price=29.99, discount=85, description="smth", image=photos[4])
        arma = Game(name="Arma", price=29.99, discount=75, description="smth", image=photos[5])
        battlefield = Game(name="Battlefield", price=59.99, discount=75, description="smth", image=photos[6])
        classesList = [darktide, division, ghostrecon, remnant, codevien, arma, battlefield]
        canvasList = []
        canvasTextList = []
        posX = 0.035
        for i in range(4):
            curClass = classesList[i]
            canvas = Canvas(self.frame, width=274, height=186, bg=BG_COLOR, highlightthickness=0, cursor="hand2")
            canvas.create_image(0, 79, anchor=W, image=curClass.image)
            canvas.image = curClass.image
            titlePosX = 41
            if len(curClass.name) > 8:
                titlePosX = 54
            textName = canvas.create_text(titlePosX, 171, text=curClass.name, fill="white", font="Arial 11 bold")

            if curClass.price == 0:
                canvas.create_rectangle(160, 157, 274, 186, fill="#A1CD44")
                canvas.create_text(220, 171, text="Бесплатно", font="Arial 12 bold")
            elif curClass.discount == 0:
                canvas.create_rectangle(190, 157, 274, 186, fill="#A1CD44")
                canvas.create_text(232, 171, text=f"${curClass.price}", font="Arial 12 bold")
            else:
                canvas.create_rectangle(213, 157, 274, 186, fill="#A1CD44")
                canvas.create_text(244, 171, text=f"- {curClass.discount}%", font="Arial 12 bold")
                canvas.create_text(185, 171, text=f"${curClass.price}", font="Arial 10 overstrike", fill="#808A8F")
                canvas.create_text(137, 172, text=f"${round(float(curClass.price - (curClass.price * (curClass.discount/100))), 2)}", font="Arial 11 bold", fill="#ffffff")
            canvas.place(relx=posX, rely=0.9)
            canvasList.append(canvas)
            canvasTextList.append(textName)
            posX += 0.239
        print(canvasList)
        print(canvasTextList)
        # for i in range(4):
        #     canvasList[i].bind("<Enter>", lambda event: self.inCanvas(canvas=canvasList[i], text=canvasList[i]))
        #     canvasList[i].bind("<Leave>", lambda event: self.outCanvas(canvas=canvasList[i], text=canvasList[i]))
        canvasList[0].bind("<Enter>", lambda event: self.inCanvas(canvas=canvasList[0], text=canvasList[0]))
        canvasList[0].bind("<Leave>", lambda event: self.outCanvas(canvas=canvasList[0], text=canvasList[0]))
        canvasList[1].bind("<Enter>", lambda event: self.inCanvas(canvas=canvasList[1], text=canvasList[1]))
        canvasList[1].bind("<Leave>", lambda event: self.outCanvas(canvas=canvasList[1], text=canvasList[1]))
        canvasList[2].bind("<Enter>", lambda event: self.inCanvas(canvas=canvasList[2], text=canvasList[2]))
        canvasList[2].bind("<Leave>", lambda event: self.outCanvas(canvas=canvasList[2], text=canvasList[2]))
        canvasList[3].bind("<Enter>", lambda event: self.inCanvas(canvas=canvasList[3], text=canvasList[3]))
        canvasList[3].bind("<Leave>", lambda event: self.outCanvas(canvas=canvasList[3], text=canvasList[3]))



    def inCanvas(self, canvas, text):
        # canvas.itemconfigure(text, font=f"Arial 1")
        canvas.config(background="#ff0000")

    def outCanvas(self, canvas, text):
        # canvas.itemconfigure(text, font="Arial 10 bold")
        canvas.config(background=BG_COLOR)
#
#
#
# shopRoot = Tk()
# shopRoot.geometry("1284x798+160+20")
# shopRoot.config(background=BG_COLOR)
#
# scrollBar = Scrollbar(shopRoot)
# scrollBar.pack(side="right", fill="y")
#
# shopHeaderShopBtn = Button(shopRoot, text="МАГАЗИН", background=BG_COLOR, fg="#ffffff", borderwidth=0, font="Arial 16")
# shopHeaderShopBtn.place(relx=0.37, rely=0.03)
#
# shopHeaderLibraryBtn = Button(shopRoot, text="БИБЛИОТЕКА", background=BG_COLOR, fg="#ffffff", borderwidth=0, font="Arial 16")
# shopHeaderLibraryBtn.place(relx=0.47, rely=0.03)
#
# shopHeaderOfficeBtn = Button(shopRoot, text="USER", background=BG_COLOR, fg="#ffffff", borderwidth=0, font="Arial 16 underline")
# shopHeaderOfficeBtn.place(relx=0.605, rely=0.03)
#
# def activeBtnUnderline(activeBtn, oldBtn):
#     activeBtn.config(font=f"{activeBtn['font']} underline", fg="#1A9FFF")
#     oldBtn.config(font=f"{activeBtn['font'][:-9]}", fg="#ffffff")
# activeBtnUnderline(shopHeaderShopBtn, shopHeaderOfficeBtn)
#
#
# summerSaleImg = Image.open("images/summerSale.png")
# resizedSummerSaleImg = summerSaleImg.resize((1268, 700))
# img = ImageTk.PhotoImage(resizedSummerSaleImg)
# summerSaleImgLbl = Label(shopRoot, image=img)
# summerSaleImgLbl.place(relx=-0.002, rely=0.1)

# shopRoot.mainloop()
if __name__ == '__main__':
    shopRoot = Tk()
    shop = Shop(shopRoot)
    shop.mainloop()

