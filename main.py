from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk
from pickle import *
import json

BG_COLOR = "#171D25"

def activeBtnUnderline(activeBtn: Button, oldBtn: Button):
    activeBtn.config(font=f"{activeBtn['font']} underline", fg="#1A9FFF")
    oldBtn.config(font=f"{activeBtn['font'][:-9]}", fg="#ffffff")

class Game:
    def __init__(self, name, price, discount, description, image):
        self.name = name
        self.price = price
        self.discount = discount
        self.description = description
        self.image = image

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getDiscount(self):
        return self.discount

    def getDescription(self):
        return self.description

    def getImage(self):
        return self.image


def getPhotos():
    linksOnPhoto = ["darktide", "division", "ghostrecon", "remnant", "codevein", "arma", "battlefield"]
    photos = []
    for i in range(len(linksOnPhoto)):
        oldImg = f"gameImgs/{linksOnPhoto[i]}.png"
        # resImg = oldImg.resize((274, 158))
        # img = ImageTk.PhotoImage(resImg)
        photos.append(oldImg)
    return photos





class Shop(Frame):
    def __init__(self, master: Tk):
        super().__init__(master)
        self.master = master
        self.master.geometry("1284x798+160+20")
        self.master.resizable(False, False)
        self.master.config(background=BG_COLOR)

        self.widgets()
        self.setGames()

    def widgets(self):
        self.shopHeaderShopBtn = Button(self.master, text="МАГАЗИН", background=BG_COLOR, fg="#ffffff", borderwidth=0, font="Arial 16")
        self.shopHeaderLibraryBtn = Button(self.master, text="БИБЛИОТЕКА", background=BG_COLOR, fg="#ffffff", borderwidth=0, font="Arial 16")
        self.shopHeaderOfficeBtn = Button(self.master, text="USER", background=BG_COLOR, fg="#ffffff", borderwidth=0, font="Arial 16 underline")

        self.shopHeaderShopBtn.place(relx=0.35, rely=0.03)
        self.shopHeaderLibraryBtn.place(relx=0.45, rely=0.03)
        self.shopHeaderOfficeBtn.place(relx=0.585, rely=0.03)
        for i in range(3): self.master.columnconfigure(index=i, weight=1)
        activeBtnUnderline(self.shopHeaderShopBtn, self.shopHeaderOfficeBtn)


        # smrSaleImg = Image.open("images/summerSale.png")
        # resSmrSaleImg = smrSaleImg.resize((1262, 798))
        # smrImg = ImageTk.PhotoImage(resSmrSaleImg)
        # # Label(self.master, image=smrImg).place(relx=0, rely=0.1)
        # # summerSaleImgLbl.place(relx=0.05, rely=0.1)
        # imagesCanvas = Canvas(self.master, width=1262, height=700, bg="#000000", highlightthickness=0)
        # imagesCanvas.place(relx=0.0, rely=0.1)
        # imagesCanvas.create_image(0, 0, anchor=NW, image=smrImg)
        # imagesCanvas.image = smrImg

    def setGames(self):
        photos = getPhotos()
        darktide = Game(name="Darktide", price=29.99, discount=0, description="Отбейте город Терциум от полчищ кровожадных врагов в напряженном и брутальном шутере. Warhammer 40,000: Darktide — новая кооперативная игра от удостоенной наград команды создателей серии Vermintide. Терциум падет, отверженные восстанут.", image=photos[0])
        division = Game(name="Division", price=16.49, discount=70, description="ИСТОРИЯ НЕ ЗАБУДЕТ Tom Clancy’s The Division® 2: судьба мира зависит от вас Возглавьте отряд спецагентов и наведите порядок в Вашингтоне, пострадавшем от эпидемии.", image=photos[1])
        ghostrecon = Game(name="GhostRecon", price=0, discount=0, description="Станьте «Призраком» и победите других спецназовцев – «Волков» в обновленной игре серии Tom Clancy's Ghost Recon!", image=photos[2])
        remnant = Game(name="Remnant", price=18.49, discount=65, description="В роли одного из последних представителей человечества, в одиночку или в компании одного-двух товарищей, вам предстоит сразиться с ордами монстров и эпическими боссами, пытаясь закрепиться на чужой земле, отстроиться и вернуть себе утраченное.", image=photos[3])
        codevien = Game(name="CodeVien", price=29.99, discount=85, description="Создайте своего бессмертного, найдите союзников и преодолейте испытания, чтобы вспомнить прошлое и вырваться из ада в игре CODE VEIN.", image=photos[4])
        arma = Game(name="Arma", price=29.99, discount=75, description="Испытайте вкус боевых действий в массовой военной игре. C более чем 20 видами техники и 40 видами оружия, различными режимами игры и безграничными возможностями создания контента, вы получаете наилучший реализм и разнообразие в Arma 3.", image=photos[5])
        battlefield = Game(name="Battlefield", price=59.99, discount=75, description="Вступайте в игровое сообщество Battlefield и откройте для себя зарю мировых войн в командных сетевых боях или в увлекательной одиночной кампании.", image=photos[6])
        with open("Files/gamesData.json", "w") as FileHandler:
            slov = {}
            for i in [darktide, division, ghostrecon, remnant, codevien, arma, battlefield]:
                slov[i.name] = {
                    "name": i.name,
                    "price": i.price,
                    "discount": i.discount,
                    "description": i.description,
                    "image": i.image,
                }
            json.dump(slov, FileHandler)
        with open("Files/gamesData.json", "r") as FileHandler:
            classesDict = json.loads(FileHandler.readline())

        classesList = []
        for key, val in classesDict.items():
            print(f"{key}")
            print(val["image"])
            oldImg = Image.open(val["image"]).resize((274, 158))
            img = ImageTk.PhotoImage(oldImg)
            val["image"] = img

            classesList.append(val)

        # try:
        #     with open("Files/gamesData.json", "wb") as FileHandler:
        #         json.dump({}, FileHandler)
        # except Exception as e:
        #     print("Файл очистился.")
            # obj = {
            #     "name": division.name,
            #     "price": division.price,
            #     "discount": division.discount,
            #     "description": division.description,
            #     "image": str(division.image)
            # }
            # json.dump(obj, FileHandler)

        canvasList = []
        canvasTextList = []
        posX = 0.035
        positionForCanvasInfo = [posX]
        #371x241
        gamesCount = 0
        if len(classesList) <= 4:
            gamesCount = len(classesList)
        elif len(classesList) > 5 and len(classesList) <= 7:
            # print(4)
            ...
        # for gameClass in range(4):
        #     curClass = classesList[i]
        #     canvas = Canvas(self.master, width=274, height=186, bg=BG_COLOR, highlightthickness=0, cursor="hand2")
        #     # canvas.create_image(0, 79, anchor=W, image=curClass.image)
        #     canvas.image = curClass.image
        #     titlePosX = 41
        #     if len(curClass.name) > 8:
        #         titlePosX = 54
        #     textName = canvas.create_text(titlePosX, 171, text=curClass.name, fill="white", font="Arial 11 bold")
        #
        #     if curClass.price == 0:
        #         canvas.create_rectangle(160, 157, 274, 186, fill="#A1CD44")
        #         canvas.create_text(220, 171, text="Бесплатно", font="Arial 12 bold")
        #     elif curClass.discount == 0:
        #         canvas.create_rectangle(190, 157, 274, 186, fill="#A1CD44")
        #         canvas.create_text(232, 171, text=f"${curClass.price}", font="Arial 12 bold")
        #     else:
        #         canvas.create_rectangle(213, 157, 274, 186, fill="#A1CD44")
        #         canvas.create_text(244, 171, text=f"- {curClass.discount}%", font="Arial 12 bold")
        #         canvas.create_text(185, 171, text=f"${curClass.price}", font="Arial 10 overstrike", fill="#808A8F")
        #         canvas.create_text(137, 172, text=f"${round(float(curClass.price - (curClass.price * (curClass.discount/100))), 2)}", font="Arial 11 bold", fill="#ffffff")
        #     canvas.place(relx=posX, rely=0.3)
        #     canvasList.append(canvas)
        #     canvasTextList.append(textName)
        #     posX += 0.239
        #     positionForCanvasInfo.append(posX)
        # print(canvasList)
        # print(canvasTextList)
        # # for i in range(4):
        # #     canvasList[i].bind("<Enter>", lambda event: self.inCanvas(gameClass=classesList[i], pos=positionForCanvasInfo[i]))
        # #     canvasList[i].bind("<Leave>", lambda event: self.outCanvas())
        # canvasList[0].bind("<Enter>", lambda event: self.inCanvas(gameClass=classesList[0], pos=positionForCanvasInfo[0]))
        # canvasList[0].bind("<Leave>", lambda event: self.outCanvas())
        # canvasList[1].bind("<Enter>", lambda event: self.inCanvas(gameClass=classesList[1], pos=positionForCanvasInfo[1]))
        # canvasList[1].bind("<Leave>", lambda event: self.outCanvas())
        # canvasList[2].bind("<Enter>", lambda event: self.inCanvas(gameClass=classesList[2], pos=positionForCanvasInfo[2]))
        # canvasList[2].bind("<Leave>", lambda event: self.outCanvas())
        # canvasList[3].bind("<Enter>", lambda event: self.inCanvas(gameClass=classesList[3], pos=positionForCanvasInfo[3], isLast=True))
        # canvasList[3].bind("<Leave>", lambda event: self.outCanvas())
        # self.infoCanvas = Canvas(self.master, width=305, height=162, highlightthickness=0, background=BG_COLOR)
        # self.intoInfoCanvas = self.infoCanvas.create_rectangle(8, 0, 305, 269, fill="#CEDAE3")
        # self.infoCanvasPolygon = self.infoCanvas.create_polygon(0, 30, 10, 21, 10, 39, fill="#CEDAE3")
        # self.infoCanvasTitle = self.infoCanvas.create_text(22, 10, text="", font="Arial 15", fill="#4B5563", anchor=NW)
        # self.infoCanvasDescription = self.infoCanvas.create_text(23, 40, text="", font="Arial 9", fill="#778696", anchor=NW, width=260)




    def inCanvas(self, gameClass: Game, pos, isLast = False):
        if isLast:
            self.infoCanvas.place(relx=pos-0.245, rely=0.3)
            self.infoCanvas.coords(self.intoInfoCanvas, 0, 0, 297, 269)
            self.infoCanvas.coords(self.infoCanvasPolygon, 296, 39, 296, 21, 306, 30)
            self.infoCanvas.itemconfigure(self.infoCanvasTitle, text=gameClass.name)
            self.infoCanvas.itemconfigure(self.infoCanvasDescription, text=gameClass.description)
        else:
            self.infoCanvas.place(relx=pos+0.215, rely=0.3)
            self.infoCanvas.coords(self.intoInfoCanvas, 8, 0, 305, 269)
            self.infoCanvas.coords(self.infoCanvasPolygon, 0, 30, 10, 21, 10, 39)
            self.infoCanvas.itemconfigure(self.infoCanvasTitle, text=gameClass.name)
            self.infoCanvas.itemconfigure(self.infoCanvasDescription, text=gameClass.description)
    def outCanvas(self):
        self.infoCanvas.place_forget()





if __name__ == '__main__':
    shopRoot = Tk()
    shop = Shop(shopRoot)
    shop.mainloop()
