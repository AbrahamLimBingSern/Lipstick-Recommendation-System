from tkinter import *
from tkinter import filedialog,messagebox
from tkinter import Frame
import cv2
import dlib
import numpy as np
import tkinter as tk
from PIL import ImageTk, Image, ImageGrab
import time
from numpy import *

def information_user():

    if firstname.get() == '' or lastname.get() == '' or pnumber.get() == '':
        messagebox.showerror('Error', 'Please Enter Your Information!')
    else:
        messagebox.showinfo('Success','Your information has been stored.')
        window.destroy()

        window1 = tk.Tk()
        window1.title("Makeup Application")
        window1.geometry('950x785+0+0')

        canvas = tk.Canvas(window1)
        canvas.pack(fill=tk.BOTH, expand=True)

        def apply_makeup():
            cap = cv2.VideoCapture(0)
            detector = dlib.get_frontal_face_detector()
            predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
            landmarkspoints = []


            def empty(a):
                pass

            window2 = tk.Tk()
            window2.title("Choose Your Lipstick Colour")
            window2.geometry('575x785+950+0')

            page1 = tk.Frame(window2, height=785, width=575, bg='#FFEC8B', bd=10, relief=RIDGE)
            page1.pack(ipadx=20, ipady=20)

            page2 = tk.Frame(window2, height=785, width=575, bg='#FFEC8B', bd=10, relief=RIDGE) #Red
            page3 = tk.Frame(window2, height=785, width=575, bg='#FFEC8B', bd=10, relief=RIDGE) #Pink
            page4 = tk.Frame(window2, height=785, width=575, bg='#FFEC8B', bd=10, relief=RIDGE) #Green
            page5 = tk.Frame(window2, height=785, width=575, bg='#FFEC8B', bd=10, relief=RIDGE) #Blue
            page6 = tk.Frame(window2, height=785, width=575, bg='#FFEC8B', bd=10, relief=RIDGE) #Purple
            page7 = tk.Frame(window2, height=785, width=575, bg='#FFEC8B', bd=10, relief=RIDGE) #Black
            page8 = tk.Frame(window2, height=785, width=575, bg='#FFEC8B', bd=10, relief=RIDGE) #Result



            for frame in (page1, page2, page3, page4, page5, page6, page7, page8):
                frame.grid(row=0, column=0, sticky='nsew')

            def show_page(frame):
                frame.tkraise()  # tkraise() method is used to stack the new frame on top of previous frame



            show_page(page1)

            red = Button(page1, text='Red', bg="red", fg="white", width=30, height=12, command=lambda: show_page(page2))
            red.place(x=50, y=50)

            pink = Button(page1, text='Pink', bg="pink", fg="white", width=30, height=12, command=lambda: show_page(page3))
            pink.place(x=300 ,y=50)

            green = Button(page1, text='Green', bg="green", fg="white", width=30, height=12, command=lambda: show_page(page4))
            green.place(x=50 ,y=300)

            blue = Button(page1, text='Blue', bg="blue", fg="white", width=30, height=12, command=lambda: show_page(page5))
            blue.place(x=300 ,y=300)

            purple = Button(page1, text='Purple', bg="purple", fg="white", width=30, height=12, command=lambda: show_page(page6))
            purple.place(x=50 ,y=550)

            black = Button(page1, text='Black', bg="black", fg="white", width=30, height=12, command=lambda: show_page(page7))
            black.place(x=300 ,y=550)

            backred = tk.Button(page2, text='Back', bg="cyan", width=30, height=5,command=lambda: show_page(page1)) #Back Button at red series
            backred.place(x=185, y=670)

            backpink = tk.Button(page3, text='Back', bg="cyan", width=30, height=5,command=lambda: show_page(page1)) #Back Button at pink series
            backpink.place(x=185, y=670)

            backgreen = tk.Button(page4, text='Back', bg="cyan", width=30, height=5,command=lambda: show_page(page1)) #Back Button at green series
            backgreen.place(x=185, y=670)

            backblue = tk.Button(page5, text='Back', bg="cyan", width=30, height=5,command=lambda: show_page(page1)) #Back Button at blue series
            backblue.place(x=185, y=670)

            backpurple = tk.Button(page6, text='Back', bg="cyan", width=30, height=5,command=lambda: show_page(page1)) #Back Button at purple series
            backpurple.place(x=185, y=670)

            backblack = tk.Button(page7, text='Back', bg="cyan", width=30, height=5,command=lambda: show_page(page1)) #Back Button at black series
            backblack.place(x=185, y=670)

            result_button = tk.Button(window1frame, text="Show The Result", command=lambda: show_page(page8))
            result_button.grid(row=0, column=3, padx=20, pady=20)

            backresult = tk.Button(page8, text='Back', bg="cyan", width=30, height=5,command=lambda: show_page(page1)) #Back Button at show result
            backresult.place(x=185, y=670)

            def receipt(button_text, location_text):

                textReceipt.delete(1.0, END)
                x = random.randint(100, 1000)

                billnumber = 'NO BILL : 00' + str(x)
                date = time.strftime('%d.%m.%Y')
                textReceipt.insert(END, '*******************************************************************')
                textReceipt.insert(END, f'\t\t ~Thank You For Using Our System~ \n')
                textReceipt.insert(END, '*******************************************************************\n\n')
                textReceipt.insert(END, billnumber + '\t\t\t            DATE : ' + date)
                textReceipt.insert(END, f'\nName : {str(firstname.get())} {str(lastname.get())}\n')
                textReceipt.insert(END, f'Phone Number : {str(pnumber.get())}\n\n')
                textReceipt.insert(END, '*******************************************************************\n\n\n\n\n\n\n')
                textReceipt.insert(tk.END, f'\t       Color Lipstick that Selected: \n\t\t    {button_text}\n\n\n\n\n')
                textReceipt.insert(tk.END, f'\t\tLocation: \t{location_text}\n\n\n\n\n\n')
                textReceipt.insert(END, '*******************************************************************')
                textReceipt.insert(END, f'\t\t ~Thank You For Using Our System~ \n')
                textReceipt.insert(END, '*******************************************************************')



            textReceipt = tk.Text(page8, font=('arial', 12, 'bold'), bd=3, width=45, height=30)
            textReceipt.pack()
            textReceipt.place(x=70, y=50)

            # Red Series
            imperialred_button = tk.Button(page2, bg="#ED2939", width=4, height=3, command=lambda: [set_color(237, 41, 57), receipt("Imperialred", "RD001")])
            imperialred_button.grid(row=0, column=0, padx=1, pady=2)

            scarlet_button = tk.Button(page2, bg="#FF2400", width=4, height=3, command=lambda: [set_color(255, 36, 0), receipt("Scarlet", "RD002")])
            scarlet_button.grid(row=0, column=1, padx=1, pady=2)

            indianred_button = tk.Button(page2, bg="#CD5C5C", width=4, height=3, command=lambda: [set_color(205, 92, 92), receipt("Indianred", "RD003")])
            indianred_button.grid(row=0, column=2, padx=1, pady=2)

            barnred_button = tk.Button(page2, bg="#7C0A02", width=4, height=3, command=lambda: [set_color(124, 10, 2), receipt("Barnred", "RD004")])
            barnred_button.grid(row=0, column=3, padx=1, pady=2)

            ChiliRed_button = tk.Button(page2, bg="#C21807", width=4, height=3, command=lambda: [set_color(194, 24, 7), receipt("ChiliRed", "RD005")])
            ChiliRed_button.grid(row=0, column=4, padx=1, pady=2)

            ruby_button = tk.Button(page2, bg="#E0115F", width=4, height=3, command=lambda: [set_color(224, 17, 95), receipt("Ruby", "RD006")])
            ruby_button.grid(row=0, column=5, padx=1, pady=2)

            maroon_button = tk.Button(page2, bg="#800000", width=4, height=3, command=lambda: [set_color(128, 0, 0), receipt("Maroon", "RD007")])
            maroon_button.grid(row=0, column=6, padx=1, pady=2)

            firebrick_button = tk.Button(page2, bg="#B22222", width=4, height=3, command=lambda: [set_color(178, 34, 34), receipt("Firebrick", "RD008")])
            firebrick_button.grid(row=0, column=7, padx=1, pady=2)

            redwood_button = tk.Button(page2, bg="#A45A52", width=4, height=3, command=lambda: [set_color(164, 90, 82), receipt("Redwood", "RD009")])
            redwood_button.grid(row=0, column=8, padx=1, pady=2)

            carmine_button = tk.Button(page2, bg="#960018", width=4, height=3, command=lambda: [set_color(150, 0, 24), receipt("Carmine", "RD010")])
            carmine_button.grid(row=0, column=9, padx=1, pady=2)

            desire_button = tk.Button(page2, bg="#EA3C53", width=4, height=3, command=lambda: [set_color(234, 60, 83), receipt("Desire", "RD011")])
            desire_button.grid(row=0, column=10, padx=1, pady=2)

            vermilion_button = tk.Button(page2, bg="#7E191B", width=4, height=3, command=lambda: [set_color(126, 25, 27), receipt("Vermilion", "RD012")])
            vermilion_button.grid(row=0, column=11, padx=1, pady=2)

            Raspberry_button = tk.Button(page2, bg="#D21F3C", width=4, height=3, command=lambda: [set_color(210, 31, 60), receipt("Raspberry", "RD013")])
            Raspberry_button.grid(row=0, column=12, padx=1, pady=2)

            candyapple_button = tk.Button(page2, bg="#FF0800", width=4, height=3, command=lambda: [set_color(255, 8, 0), receipt("Candyapple", "RD014")])
            candyapple_button.grid(row=0, column=13, padx=1, pady=2)

            persian_button = tk.Button(page2, bg="#CA3433", width=4, height=3, command=lambda: [set_color(202, 52, 51), receipt("Persian", "RD015")])
            persian_button.grid(row=1, column=0, padx=1, pady=2)

            Hibiscus_button = tk.Button(page2, bg="#B43757", width=4, height=3, command=lambda: [set_color(180, 55, 87), receipt("Hibiscus", "RD016")])
            Hibiscus_button.grid(row=1, column=1, padx=1, pady=2)

            usflag_button = tk.Button(page2, bg="#BF0A30", width=4, height=3, command=lambda: [set_color(191, 10, 48), receipt("USFlag", "RD017")])
            usflag_button.grid(row=1, column=2, padx=1, pady=2)

            ferrari_button = tk.Button(page2, bg="#CA3433", width=4, height=3, command=lambda: [set_color(202, 52, 51), receipt("Ferrari", "RD018")])
            ferrari_button.grid(row=1, column=3, padx=1, pady=2)

            sangria_button = tk.Button(page2, bg="#5E1914", width=4, height=3, command=lambda: [set_color(94, 25, 20), receipt("Sangria", "RD019")])
            sangria_button.grid(row=1, column=4, padx=1, pady=2)

            Mahogany_button = tk.Button(page2, bg="#420D09", width=4, height=3, command=lambda: [set_color(66, 13, 9), receipt("Mahogany", "RD020")])
            Mahogany_button.grid(row=1, column=5, padx=1, pady=2)

            Burgundy_button = tk.Button(page2, bg="#8D021F", width=4, height=3, command=lambda: [set_color(141, 2, 31), receipt("Burgundy", "RD021")])
            Burgundy_button.grid(row=1, column=6, padx=1, pady=2)

            Crimson_button = tk.Button(page2, bg="#B80F0A", width=4, height=3, command=lambda: [set_color(184, 15, 10), receipt("Crimson", "RD022")])
            Crimson_button.grid(row=1, column=7, padx=1, pady=2)

            Rust_button = tk.Button(page2, bg="#933A16", width=4, height=3, command=lambda: [set_color(147, 58, 22), receipt("Rust", "RD023")])
            Rust_button.grid(row=1, column=8, padx=1, pady=2)

            LightSalmon_button = tk.Button(page2, bg="#FFA07A", width=4, height=3, command=lambda: [set_color(255, 160, 122), receipt("LightSalmon", "RD024")])
            LightSalmon_button.grid(row=1, column=9, padx=1, pady=2)

            Salmon_button = tk.Button(page2, bg="#FA8072", width=4, height=3, command=lambda: [set_color(250, 128, 114), receipt("Salmon", "RD025")])
            Salmon_button.grid(row=1, column=10, padx=1, pady=2)

            DarkSalmon_button = tk.Button(page2, bg="#E9967A", width=4, height=3, command=lambda: [set_color(233, 150, 122), receipt("DarkSalmon", "RD026")])
            DarkSalmon_button.grid(row=1, column=11, padx=1, pady=2)

            LightCoral_button = tk.Button(page2, bg="#F08080", width=4, height=3, command=lambda: [set_color(240, 128, 128), receipt("LightCoral", "RD027")])
            LightCoral_button.grid(row=1, column=12, padx=1, pady=2)

            Red_button = tk.Button(page2, bg="#FF0000", width=4, height=3, command=lambda: [set_color(255, 0, 0), receipt("Red", "RD028")])
            Red_button.grid(row=1, column=13, padx=1, pady=2)

            Darkred_button = tk.Button(page2, bg="#8B0000", width=4, height=3, command=lambda: [set_color(139, 0, 0), receipt("Darkred", "RD029")])
            Darkred_button.grid(row=2, column=0, padx=1, pady=2)

            Tomato_button = tk.Button(page2, bg="#FF6347", width=4, height=3, command=lambda: [set_color(255, 99, 71), receipt("Tomato", "RD030")])
            Tomato_button.grid(row=2, column=1, padx=1, pady=2)

            OrangeRed_button = tk.Button(page2, bg="#FF4500", width=4, height=3, command=lambda: [set_color(255, 69, 0), receipt("OrangeRed", "RD031")])
            OrangeRed_button.grid(row=2, column=2, padx=1, pady=2)

            PaleVioletRed_button = tk.Button(page2, bg="#DB7093", width=4, height=3, command=lambda: [set_color(219, 112, 147), receipt("PaleVioletRed", "RD032")])
            PaleVioletRed_button.grid(row=2, column=3, padx=1, pady=2)

            LightBrick_button = tk.Button(page2, bg="#FB607F", width=4, height=3, command=lambda: [set_color(251, 96, 127), receipt("LightBrick", "RD033")])
            LightBrick_button.grid(row=2, column=4, padx=1, pady=2)

            Brick_button = tk.Button(page2, bg="#7E2811", width=4, height=3, command=lambda: [set_color(126, 40, 17), receipt("Brick", "RD034")])
            Brick_button.grid(row=2, column=5, padx=1, pady=2)

            PrismaticRed_button = tk.Button(page2, bg="#D03D33", width=4, height=3, command=lambda: [set_color(208, 61, 51), receipt("PrismaticRed", "RD035")])
            PrismaticRed_button.grid(row=2, column=6, padx=1, pady=2)

            PrismaticLegacy_button = tk.Button(page2, bg="#BA1607", width=4, height=3, command=lambda: [set_color(186, 22, 7), receipt("PrismaticLegacy", "RD036")])
            PrismaticLegacy_button.grid(row=2, column=7, padx=1, pady=2)

            PrismaticVermilionRenewal_button = tk.Button(page2, bg="#CA0123", width=4, height=3, command=lambda: [set_color(202, 1, 35), receipt("PrismaticVermilionRenewal", "RD037")])
            PrismaticVermilionRenewal_button.grid(row=2, column=8, padx=1, pady=2)

            PrismaticReflectionShade_button = tk.Button(page2, bg="#FF3C28", width=4, height=3, command=lambda: [set_color(255, 60, 40), receipt("PrismaticReflectionShade", "RD038")])
            PrismaticReflectionShade_button.grid(row=2, column=9, padx=1, pady=2)

            ErsRed_button = tk.Button(page2, bg="#AA0000", width=4, height=3, command=lambda: [set_color(170, 0, 0), receipt("ErsRed", "RD039")])
            ErsRed_button.grid(row=2, column=10, padx=1, pady=2)

            AZCardinalsRed_button = tk.Button(page2, bg="#BD2031", width=4, height=3, command=lambda: [set_color(189, 32, 49), receipt("AZCardinalsRed", "RD040")])
            AZCardinalsRed_button.grid(row=2, column=11, padx=1, pady=2)

            AirbnbRed_button = tk.Button(page2, bg="#FF5A5F", width=4, height=3, command=lambda: [set_color(255, 90, 95), receipt("AirbnbRed", "RD041")])
            AirbnbRed_button.grid(row=2, column=12, padx=1, pady=2)

            AjaxRed_button = tk.Button(page2, bg="#D2122E", width=4, height=3, command=lambda: [set_color(210, 18, 46), receipt("AjaxRed", "RD042")])
            AjaxRed_button.grid(row=2, column=13, padx=1, pady=2)

            AlabamaCrimson_button = tk.Button(page2, bg="#9E1B32", width=4, height=3, command=lambda: [set_color(158, 27, 50), receipt("AlabamaCrimson", "RD043")])
            AlabamaCrimson_button.grid(row=3, column=0, padx=1, pady=2)

            AlizarinCrimson_button = tk.Button(page2, bg="#E32636", width=4, height=3, command=lambda: [set_color(227, 38, 54), receipt("AlizarinCrimson", "RD044")])
            AlizarinCrimson_button.grid(row=3, column=1, padx=1, pady=2)

            AmaranthRed_button = tk.Button(page2, bg="#F4364C", width=4, height=3, command=lambda: [set_color(244, 54, 76), receipt("AmaranthRed", "RD045")])
            AmaranthRed_button.grid(row=3, column=2, padx=1, pady=2)

            AmericanRose_button = tk.Button(page2, bg="#FF033E", width=4, height=3, command=lambda: [set_color(255, 3, 62), receipt("AmericanRose", "RD046")])
            AmericanRose_button.grid(row=3, column=3, padx=1, pady=2)

            AngelsRed_button = tk.Button(page2, bg="#BA0021", width=4, height=3, command=lambda: [set_color(186, 0, 33), receipt("AngelsRed", "RD047")])
            AngelsRed_button.grid(row=3, column=4, padx=1, pady=2)

            AlmostApricotRed_button = tk.Button(page2, bg="#E5B39B", width=4, height=3, command=lambda: [set_color(229, 179, 155), receipt("AlmostApricotRed", "RD048")])
            AlmostApricotRed_button.grid(row=3, column=5, padx=1, pady=2)

            ArsenalRed_button = tk.Button(page2, bg="#DB0007", width=4, height=3, command=lambda: [set_color(219, 0, 7), receipt("ArsenalRed", "RD049")])
            ArsenalRed_button.grid(row=3, column=6, padx=1, pady=2)

            AuburnRed_button = tk.Button(page2, bg="#A52A2A", width=4, height=3, command=lambda: [set_color(165, 42, 42), receipt("AuburnRed", "RD050")])
            AuburnRed_button.grid(row=3, column=7, padx=1, pady=2)

            BUScarlet_button = tk.Button(page2, bg="#CC0000", width=4, height=3, command=lambda: [set_color(204, 0, 0), receipt("BUScarlet", "RD051")])
            BUScarlet_button.grid(row=3, column=8, padx=1, pady=2)

            BillsRed_button = tk.Button(page2, bg="#C60C30", width=4, height=3, command=lambda: [set_color(198, 12, 48), receipt("BillsRed", "RD052")])
            BillsRed_button.grid(row=3, column=9, padx=1, pady=2)

            BittersweetShimmerRed_button = tk.Button(page2, bg="#BF4F51", width=4, height=3, command=lambda: [set_color(191, 79, 81), receipt("BittersweetShimmerRed", "RD053")])
            BittersweetShimmerRed_button.grid(row=3, column=10, padx=1, pady=2)

            BloodRed_button = tk.Button(page2, bg="#660000", width=4, height=3, command=lambda: [set_color(102, 0, 0), receipt("BloodRed", "RD054")])
            BloodRed_button.grid(row=3, column=11, padx=1, pady=2)

            CGRed_button = tk.Button(page2, bg="#E03C31", width=4, height=3, command=lambda: [set_color(224, 60, 49), receipt("CGRed", "RD055")])
            CGRed_button.grid(row=3, column=12, padx=1, pady=2)

            CadmiumRed_button = tk.Button(page2, bg="#E30022", width=4, height=3, command=lambda: [set_color(227, 0, 34), receipt("CadmiumRed", "RD056")])
            CadmiumRed_button.grid(row=3, column=13, padx=1, pady=2)

            CardinalRed_button = tk.Button(page2, bg="#C41E3A", width=4, height=3, command=lambda: [set_color(196, 30, 58), receipt("CardinalRed", "RD057")])
            CardinalRed_button.grid(row=4, column=0, padx=1, pady=2)

            CarnelianRed_button = tk.Button(page2, bg="#B31B1B", width=4, height=3, command=lambda: [set_color(179, 27, 27), receipt("CarnelianRed", "RD058")])
            CarnelianRed_button.grid(row=4, column=1, padx=1, pady=2)

            CeriseRed_button = tk.Button(page2, bg="#DE3163", width=4, height=3, command=lambda: [set_color(222, 49, 99), receipt("CeriseRed", "RD059")])
            CeriseRed_button.grid(row=4, column=2, padx=1, pady=2)

            ChiefsRed_button = tk.Button(page2, bg="#E31837", width=4, height=3, command=lambda: [set_color(227, 24, 55), receipt("ChiefsRed", "RD060")])
            ChiefsRed_button.grid(row=4, column=3, padx=1, pady=2)

            ChocolateCosmosRed_button = tk.Button(page2, bg="#58111A", width=4, height=3, command=lambda: [set_color(88, 17, 26), receipt("ChocolateCosmosRed", "RD061")])
            ChocolateCosmosRed_button.grid(row=4, column=4, padx=1, pady=2)

            CincinnatiRed_button = tk.Button(page2, bg="#C6011F", width=4, height=3, command=lambda: [set_color(198, 1, 31), receipt("CincinnatiRed", "RD062")])
            CincinnatiRed_button.grid(row=4, column=5, padx=1, pady=2)

            CinnabarRed_button = tk.Button(page2, bg="#E44D2E", width=4, height=3, command=lambda: [set_color(228, 77, 46), receipt("CinnabarRed", "RD063")])
            CinnabarRed_button.grid(row=4, column=6, padx=1, pady=2)

            CokeRed_button = tk.Button(page2, bg="#F40009", width=4, height=3, command=lambda: [set_color(244, 0, 9), receipt("CokeRed", "RD064")])
            CokeRed_button.grid(row=4, column=7, padx=1, pady=2)

            CoquelicotRed_button = tk.Button(page2, bg="#FF3800", width=4, height=3, command=lambda: [set_color(255, 56, 0), receipt("CoquelicotRed", "RD065")])
            CoquelicotRed_button.grid(row=4, column=8, padx=1, pady=2)

            CoralRed_button = tk.Button(page2, bg="#FF7F50", width=4, height=3, command=lambda: [set_color(255, 127, 80), receipt("CoralRed", "RD066")])
            CoralRed_button.grid(row=4, column=9, padx=1, pady=2)

            CordovanRed_button = tk.Button(page2, bg="#893F45", width=4, height=3, command=lambda: [set_color(137, 63, 69), receipt("CordovanRed", "RD067")])
            CordovanRed_button.grid(row=4, column=10, padx=1, pady=2)

            CrayolaRed_button = tk.Button(page2, bg="#EE204D", width=4, height=3, command=lambda: [set_color(238, 32, 77), receipt("CrayolaRed", "RD068")])
            CrayolaRed_button.grid(row=4, column=11, padx=1, pady=2)

            ElectricCrimson_button = tk.Button(page2, bg="#FF003F", width=4, height=3, command=lambda: [set_color(255, 0, 63), receipt("ElectricCrimson", "RD069")])
            ElectricCrimson_button.grid(row=4, column=12, padx=1, pady=2)

            EnglishRed_button = tk.Button(page2, bg="#AB4B52", width=4, height=3, command=lambda: [set_color(171, 75, 82), receipt("EnglishRed", "RD070")])
            EnglishRed_button.grid(row=4, column=13, padx=1, pady=2)

            FalconsRed_button = tk.Button(page2, bg="#A71930", width=4, height=3, command=lambda: [set_color(167, 25, 48), receipt("FalconsRed", "RD071")])
            FalconsRed_button.grid(row=5, column=0, padx=1, pady=2)

            FaluRed_button = tk.Button(page2, bg="#801818", width=4, height=3, command=lambda: [set_color(128, 24, 24), receipt("FaluRed", "RD072")])
            FaluRed_button.grid(row=5, column=1, padx=1, pady=2)

            FireEngineRed_button = tk.Button(page2, bg="#CE2029", width=4, height=3, command=lambda: [set_color(206, 32, 41), receipt("FireEngineRed", "RD073")])
            FireEngineRed_button.grid(row=5, column=2, padx=1, pady=2)

            FlameRed_button = tk.Button(page2, bg="#E25822", width=4, height=3, command=lambda: [set_color(226, 88, 34), receipt("FlameRed", "RD074")])
            FlameRed_button.grid(row=5, column=3, padx=1, pady=2)

            FollyRed_button = tk.Button(page2, bg="#FF004F", width=4, height=3, command=lambda: [set_color(255, 0, 79), receipt("FollyRed", "RD075")])
            FollyRed_button.grid(row=5, column=4, padx=1, pady=2)

            FrenchPuceRed_button = tk.Button(page2, bg="#4E1609", width=4, height=3, command=lambda: [set_color(78, 22, 9), receipt("FrenchPuceRed", "RD076")])
            FrenchPuceRed_button.grid(row=5, column=5, padx=1, pady=2)

            Fuchsia_button = tk.Button(page2, bg="#FF00FF", width=4, height=3, command=lambda: [set_color(255, 0, 255), receipt("Fuchsia", "RD077")])
            Fuchsia_button.grid(row=5, column=6, padx=1, pady=2)

            FuzzyWuzzyRed_button = tk.Button(page2, bg="#CC6666", width=4, height=3, command=lambda: [set_color(204, 102, 102), receipt("FuzzyWuzzyRed", "RD078")])
            FuzzyWuzzyRed_button.grid(row=5, column=7, padx=1, pady=2)

            GarnetRed_button = tk.Button(page2, bg="#733635", width=4, height=3, command=lambda: [set_color(115, 54, 53), receipt("GarnetRed", "RD079")])
            GarnetRed_button.grid(row=5, column=8, padx=1, pady=2)

            HarvardCrimson_button = tk.Button(page2, bg="#A51C30", width=4, height=3, command=lambda: [set_color(165, 28, 48), receipt("HarvardCrimson", "RD080")])
            HarvardCrimson_button.grid(row=5, column=9, padx=1, pady=2)

            HollywoodCeriseRed_button = tk.Button(page2, bg="#F400A1", width=4, height=3, command=lambda: [set_color(244, 0, 161), receipt("HollywoodCeriseRed", "RD081")])
            HollywoodCeriseRed_button.grid(row=5, column=10, padx=1, pady=2)

            HuskerRed_button = tk.Button(page2, bg="#E41C38", width=4, height=3, command=lambda: [set_color(228, 28, 56), receipt("HuskerRed", "RD082")])
            HuskerRed_button.grid(row=5, column=11, padx=1, pady=2)

            JapaneseCarmine_button = tk.Button(page2, bg="#9D2933", width=4, height=3, command=lambda: [set_color(157, 41, 51), receipt("JapaneseCarmine", "RD083")])
            JapaneseCarmine_button.grid(row=5, column=12, padx=1, pady=2)

            JasperRed_button = tk.Button(page2, bg="#D73B3E", width=4, height=3, command=lambda: [set_color(215, 59, 62), receipt("JasperRed", "RD084")])
            JasperRed_button.grid(row=5, column=13, padx=1, pady=2)

            JellyBeanRed_button = tk.Button(page2, bg="#DA614E", width=4, height=3, command=lambda: [set_color(218, 97, 78), receipt("JellyBeanRed", "RD085")])
            JellyBeanRed_button.grid(row=6, column=0, padx=1, pady=2)

            KenyanCopperRed_button = tk.Button(page2, bg="#7C1C05", width=4, height=3, command=lambda: [set_color(124, 28, 5), receipt("KenyanCopperRed", "RD086")])
            KenyanCopperRed_button.grid(row=6, column=1, padx=1, pady=2)

            LavaRed_button = tk.Button(page2, bg="#CF1020", width=4, height=3, command=lambda: [set_color(207, 16, 32), receipt("LavaRed", "RD087")])
            LavaRed_button.grid(row=6, column=2, padx=1, pady=2)

            LiverpoolRed_button = tk.Button(page2, bg="#C8102E", width=4, height=3, command=lambda: [set_color(200, 16, 46), receipt("LiverpoolRed", "RD088")])
            LiverpoolRed_button.grid(row=6, column=3, padx=1, pady=2)

            LustRed_button = tk.Button(page2, bg="#E62020", width=4, height=3, command=lambda: [set_color(230, 32, 32), receipt("LustRed", "RD089")])
            LustRed_button.grid(row=6, column=4, padx=1, pady=2)

            MITRed_button = tk.Button(page2, bg="#A31F34", width=4, height=3, command=lambda: [set_color(163, 31, 52), receipt("MITRed", "RD090")])
            MITRed_button.grid(row=6, column=5, padx=1, pady=2)

            MadderRed_button = tk.Button(page2, bg="#A50021", width=4, height=3, command=lambda: [set_color(165, 0, 33), receipt("MadderRed", "RD091")])
            MadderRed_button.grid(row=6, column=6, padx=1, pady=2)

            PigmentMagenta_button = tk.Button(page2, bg="#FF0090", width=4, height=3, command=lambda: [set_color(255, 0, 144), receipt("PigmentMagenta", "RD092")])
            PigmentMagenta_button.grid(row=6, column=7, padx=1, pady=2)

            ManchesterUnitedRed_button = tk.Button(page2, bg="#DA291C", width=4, height=3, command=lambda: [set_color(218, 41, 28), receipt("ManchesterUnitedRed", "RD093")])
            ManchesterUnitedRed_button.grid(row=6, column=8, padx=1, pady=2)

            MediumVioletRed_button = tk.Button(page2, bg="#C71585", width=4, height=3, command=lambda: [set_color(199, 21, 133), receipt("MediumVioletRed", "RD094")])
            MediumVioletRed_button.grid(row=6, column=9, padx=1, pady=2)

            MunsellRed_button = tk.Button(page2, bg="#F2003C", width=4, height=3, command=lambda: [set_color(242, 0, 60), receipt("MunsellRed", "RD095")])
            MunsellRed_button.grid(row=6, column=10, padx=1, pady=2)

            NCSRed_button = tk.Button(page2, bg="#C40233", width=4, height=3, command=lambda: [set_color(196, 2, 51), receipt("NCSRed", "RD096")])
            NCSRed_button.grid(row=6, column=11, padx=1, pady=2)

            NationalsRed_button = tk.Button(page2, bg="#AB0003", width=4, height=3, command=lambda: [set_color(171, 0, 3), receipt("NationalsRed", "RD097")])
            NationalsRed_button.grid(row=6, column=12, padx=1, pady=2)

            OklahomaCrimson_button = tk.Button(page2, bg="#841617", width=4, height=3, command=lambda: [set_color(132, 22, 23), receipt("OklahomaCrimson", "RD098")])
            OklahomaCrimson_button.grid(row=6, column=13, padx=1, pady=2)

            OxbloodRed_button = tk.Button(page2, bg="#800020", width=4, height=3, command=lambda: [set_color(128, 0, 32), receipt("OxbloodRed", "RD099")])
            OxbloodRed_button.grid(row=7, column=0, padx=1, pady=2)

            PastelRed_button = tk.Button(page2, bg="#FF6961", width=4, height=3, command=lambda: [set_color(255, 105, 97), receipt("PastelRed", "RD100")])
            PastelRed_button.grid(row=7, column=1, padx=1, pady=2)

            PennRed_button = tk.Button(page2, bg="#990000", width=4, height=3, command=lambda: [set_color(153, 0, 0), receipt("PennRed", "RD101")])
            PennRed_button.grid(row=7, column=2, padx=1, pady=2)

            PersianRoseRed_button = tk.Button(page2, bg="#FE28A2", width=4, height=3, command=lambda: [set_color(254, 40, 162), receipt("PersianRoseRed", "RD102")])
            PersianRoseRed_button.grid(row=7, column=3, padx=1, pady=2)

            PhilliesRed_button = tk.Button(page2, bg="#E81828", width=4, height=3, command=lambda: [set_color(232, 24, 40), receipt("PhilliesRed", "RD103")])
            PhilliesRed_button.grid(row=7, column=4, padx=1, pady=2)

            PigmentRed_button = tk.Button(page2, bg="#ED1C24", width=4, height=3, command=lambda: [set_color(237, 28, 36), receipt("PigmentRed", "RD104")])
            PigmentRed_button.grid(row=7, column=5, padx=1, pady=2)

            PinterestRed_button = tk.Button(page2, bg="#E60023", width=4, height=3, command=lambda: [set_color(230, 0, 35), receipt("PinterestRed", "RD105")])
            PinterestRed_button.grid(row=7, column=6, padx=1, pady=2)

            PopstarRed_button = tk.Button(page2, bg="#BE4F62", width=4, height=3, command=lambda: [set_color(190, 79, 98), receipt("PopstarRed", "RD106")])
            PopstarRed_button.grid(row=7, column=7, padx=1, pady=2)

            PortlandOrangeRed_button = tk.Button(page2, bg="#FF5A36", width=4, height=3, command=lambda: [set_color(255, 90, 54), receipt("PortlandOrangeRed", "RD107")])
            PortlandOrangeRed_button.grid(row=7, column=8, padx=1, pady=2)

            PruneRed_button = tk.Button(page2, bg="#701C1C", width=4, height=3, command=lambda: [set_color(112, 28, 28), receipt("PruneRed", "RD108")])
            PruneRed_button.grid(row=7, column=9, padx=1, pady=2)

            RadicalRed_button = tk.Button(page2, bg="#FF355E", width=4, height=3, command=lambda: [set_color(255, 53, 94), receipt("RadicalRed", "RD109")])
            RadicalRed_button.grid(row=7, column=10, padx=1, pady=2)

            RedDevil_button = tk.Button(page2, bg="#860111", width=4, height=3, command=lambda: [set_color(134, 1, 17), receipt("RedDevil", "RD110")])
            RedDevil_button.grid(row=7, column=11, padx=1, pady=2)

            RedSox_button = tk.Button(page2, bg="#BD3039", width=4, height=3, command=lambda: [set_color(189, 48, 57), receipt("RedSox", "RD111")])
            RedSox_button.grid(row=7, column=12, padx=1, pady=2)

            RoseRed_button = tk.Button(page2, bg="#C21E56", width=4, height=3, command=lambda: [set_color(194, 30, 86), receipt("RoseRed", "RD112")])
            RoseRed_button.grid(row=7, column=13, padx=1, pady=2)

            RosewoodRed_button = tk.Button(page2, bg="#65000B", width=4, height=3, command=lambda: [set_color(101, 0, 11), receipt("RosewoodRed", "RD113")])
            RosewoodRed_button.grid(row=8, column=0, padx=1, pady=2)

            RufousRed_button = tk.Button(page2, bg="#A81C07", width=4, height=3, command=lambda: [set_color(168, 28, 7), receipt("RufousRed", "RD114")])
            RufousRed_button.grid(row=8, column=1, padx=1, pady=2)

            RussetRed_button = tk.Button(page2, bg="#80461B", width=4, height=3, command=lambda: [set_color(128, 70, 27), receipt("RussetRed", "RD115")])
            RussetRed_button.grid(row=8, column=2, padx=1, pady=2)

            RustyRed_button = tk.Button(page2, bg="#DA2C43", width=4, height=3, command=lambda: [set_color(218, 44, 67), receipt("RustyRed", "RD116")])
            RustyRed_button.grid(row=8, column=3, padx=1, pady=2)

            SanguineRed_button = tk.Button(page2, bg="#BC3F4A", width=4, height=3, command=lambda: [set_color(188, 63, 74), receipt("SanguineRed", "RD117")])
            SanguineRed_button.grid(row=8, column=4, padx=1, pady=2)

            SpanishRed_button = tk.Button(page2, bg="#E60026", width=4, height=3, command=lambda: [set_color(230, 0, 38), receipt("SpanishRed", "RD118")])
            SpanishRed_button.grid(row=8, column=5, padx=1, pady=2)

            TangoRed_button = tk.Button(page2, bg="#E4717A", width=4, height=3, command=lambda: [set_color(228, 113, 122), receipt("TangoRed", "RD119")])
            TangoRed_button.grid(row=8, column=6, padx=1, pady=2)

            TawnyRed_button = tk.Button(page2, bg="#CD5700", width=4, height=3, command=lambda: [set_color(205, 87, 0), receipt("TawnyRed", "RD120")])
            TawnyRed_button.grid(row=8, column=7, padx=1, pady=2)

            TeaRoseRed_button = tk.Button(page2, bg="#F88379", width=4, height=3, command=lambda: [set_color(248, 131, 121), receipt("TeaRoseRed", "RD121")])
            TeaRoseRed_button.grid(row=8, column=8, padx=1, pady=2)

            TerracottaRed_button = tk.Button(page2, bg="#E2725B", width=4, height=3, command=lambda: [set_color(226, 114, 91), receipt("TerracottaRed", "RD122")])
            TerracottaRed_button.grid(row=8, column=9, padx=1, pady=2)

            TractorRed_button = tk.Button(page2, bg="#FD0E35", width=4, height=3, command=lambda: [set_color(253, 14, 53), receipt("TractorRed", "RD123")])
            TractorRed_button.grid(row=8, column=10, padx=1, pady=2)

            TurkeyRed_button = tk.Button(page2, bg="#A91101", width=4, height=3, command=lambda: [set_color(169, 17, 1), receipt("TurkeyRed", "RD124")])
            TurkeyRed_button.grid(row=8, column=11, padx=1, pady=2)

            TuscanRed_button = tk.Button(page2, bg="#7C3030", width=4, height=3, command=lambda: [set_color(124, 48, 48), receipt("TuscanRed", "RD125")])
            TuscanRed_button.grid(row=8, column=12, padx=1, pady=2)

            UpsdellRed_button = tk.Button(page2, bg="#AE2029", width=4, height=3, command=lambda: [set_color(174, 32, 41), receipt("UpsdellRed", "RD126")])
            UpsdellRed_button.grid(row=8, column=13, padx=1, pady=2)

            VenetianRed_button = tk.Button(page2, bg="#C80815", width=4, height=3, command=lambda: [set_color(200, 8, 21), receipt("VenetianRed", "RD127")])
            VenetianRed_button.grid(row=9, column=0, padx=1, pady=2)

            VirginLustRed_button = tk.Button(page2, bg="#E4181E", width=4, height=3, command=lambda: [set_color(228, 24, 30), receipt("VirginLustRed", "RD128")])
            VirginLustRed_button.grid(row=9, column=1, padx=1, pady=2)

            WineRed_button = tk.Button(page2, bg="#722F37", width=4, height=3, command=lambda: [set_color(114, 47, 55), receipt("WineRed", "RD129")])
            WineRed_button.grid(row=9, column=2, padx=1, pady=2)

            LightRedOchre_button = tk.Button(page2, bg="#E97451", width=4, height=3, command=lambda: [set_color(233, 116, 81), receipt("LightRedOchre", "RD130")])
            LightRedOchre_button.grid(row=9, column=3, padx=1, pady=2)

            MediumVermillion_button = tk.Button(page2, bg="#D9603B", width=4, height=3, command=lambda: [set_color(217, 96, 59), receipt("MediumVermillion", "RD131")])
            MediumVermillion_button.grid(row=9, column=4, padx=1, pady=2)

            UPMaroon_button = tk.Button(page2, bg="#7B1113", width=4, height=3, command=lambda: [set_color(123, 17, 19), receipt("UPMaroon", "RD132")])
            UPMaroon_button.grid(row=9, column=5, padx=1, pady=2)

            OutrageousOrangeRed_button = tk.Button(page2, bg="#FF6E4A", width=4, height=3, command=lambda: [set_color(255, 110, 74), receipt("OutrageousOrangeRed", "RD133")])
            OutrageousOrangeRed_button.grid(row=9, column=6, padx=1, pady=2)

            UtahCrimson_button = tk.Button(page2, bg="#D3003F", width=4, height=3, command=lambda: [set_color(211, 0, 63), receipt("UtahCrimson", "RD134")])
            UtahCrimson_button.grid(row=9, column=7, padx=1, pady=2)

            # Pink Series
            Watermelon_button = tk.Button(page3, bg="#FC6C85", width=4, height=3, command=lambda: [set_color(252, 108, 133), receipt("Watermelon", "PK001")])
            Watermelon_button.grid(row=0, column=0, padx=1, pady=2)

            Flamingo_button = tk.Button(page3, bg="#FC8EAC", width=4, height=3, command=lambda: [set_color(252, 142, 172), receipt("Flamingo", "PK002")])
            Flamingo_button.grid(row=0, column=1, padx=1, pady=2)

            Coral_button = tk.Button(page3, bg="#F88379", width=4, height=3, command=lambda: [set_color(248, 131, 121), receipt("Coral", "PK003")])
            Coral_button.grid(row=0, column=2, padx=1, pady=2)

            Salmon_button = tk.Button(page3, bg="#FF9999", width=4, height=3, command=lambda: [set_color(255, 153, 153), receipt("Salmon", "PK004")])
            Salmon_button.grid(row=0, column=3, padx=1, pady=2)

            PastelPink_button = tk.Button(page3, bg="#FFD1DC", width=4, height=3, command=lambda: [set_color(255, 209, 220), receipt("PastelPink", "PK005")])
            PastelPink_button.grid(row=0, column=4, padx=1, pady=2)

            LightPink_button = tk.Button(page3, bg="#FFB6C1", width=4, height=3, command=lambda: [set_color(255, 182, 193), receipt("LightPink", "PK006")])
            LightPink_button.grid(row=0, column=5, padx=1, pady=2)

            CherryBlossom_button = tk.Button(page3, bg="#FFB7C5", width=4, height=3, command=lambda: [set_color(255, 183, 197), receipt("CherryBlossom", "PK007")])
            CherryBlossom_button.grid(row=0, column=6, padx=1, pady=2)

            Bubblegum_button = tk.Button(page3, bg="#FFC1CC", width=4, height=3, command=lambda: [set_color(255, 193, 204), receipt("Bubblegum", "PK008")])
            Bubblegum_button.grid(row=0, column=7, padx=1, pady=2)

            BabyPink_button = tk.Button(page3, bg="#F4C2C2", width=4, height=3, command=lambda: [set_color(244, 194, 194), receipt("BabyPink", "PK009")])
            BabyPink_button.grid(row=0, column=8, padx=1, pady=2)

            DarkPink_button = tk.Button(page3, bg="#E75480", width=4, height=3, command=lambda: [set_color(231, 84, 128), receipt("DarkPink", "PK010")])
            DarkPink_button.grid(row=0, column=9, padx=1, pady=2)

            BrightPink_button = tk.Button(page3, bg="#FF007F", width=4, height=3, command=lambda: [set_color(255, 0, 127), receipt("BrightPink", "PK011")])
            BrightPink_button.grid(row=0, column=10, padx=1, pady=2)

            Rouge_button = tk.Button(page3, bg="#A94064", width=4, height=3, command=lambda: [set_color(169, 64, 100), receipt("Rouge", "PK012")])
            Rouge_button.grid(row=0, column=11, padx=1, pady=2)

            NeonPink_button = tk.Button(page3, bg="#FF6EC7", width=4, height=3, command=lambda: [set_color(255, 110, 199), receipt("NeonPink", "PK013")])
            NeonPink_button.grid(row=0, column=12, padx=1, pady=2)

            Blush_button = tk.Button(page3, bg="#DE5D83", width=4, height=3, command=lambda: [set_color(222, 93, 131), receipt("Blush", "PK014")])
            Blush_button.grid(row=0, column=13, padx=1, pady=2)

            Fuchsia_button = tk.Button(page3, bg="#C154C1", width=4, height=3, command=lambda: [set_color(193, 84, 193), receipt("Fuchsia", "PK015")])
            Fuchsia_button.grid(row=1, column=0, padx=1, pady=2)

            Mauve_button = tk.Button(page3, bg="#E0B0FF", width=4, height=3, command=lambda: [set_color(224, 176, 255), receipt("Mauve", "PK016")])
            Mauve_button.grid(row=1, column=1, padx=1, pady=2)

            Orchid_button = tk.Button(page3, bg="#DA70D6", width=4, height=3, command=lambda: [set_color(218, 112, 214), receipt("Orchid", "PK017")])
            Orchid_button.grid(row=1, column=2, padx=1, pady=2)

            Magenta_button = tk.Button(page3, bg="#FF00FF", width=4, height=3, command=lambda: [set_color(255, 0, 255), receipt("Magenta", "PK018")])
            Magenta_button.grid(row=1, column=3, padx=1, pady=2)

            HotPink_button = tk.Button(page3, bg="#FF69B4", width=4, height=3, command=lambda: [set_color(255, 105, 180), receipt("HotPink", "PK019")])
            HotPink_button.grid(row=1, column=4, padx=1, pady=2)

            Carnation_button = tk.Button(page3, bg="#FFA6C9", width=4, height=3, command=lambda: [set_color(255, 166, 201), receipt("Carnation", "PK020")])
            Carnation_button.grid(row=1, column=5, padx=1, pady=2)

            TulipPink_button = tk.Button(page3, bg="#FF8E8E", width=4, height=3, command=lambda: [set_color(255, 142, 142), receipt("TulipPink", "PK021")])
            TulipPink_button.grid(row=1, column=6, padx=1, pady=2)

            TeaRose_button = tk.Button(page3, bg="#F4C2C2", width=4, height=3, command=lambda: [set_color(244, 194, 194), receipt("TeaRose", "PK022")])
            TeaRose_button.grid(row=1, column=7, padx=1, pady=2)

            CottonCandy_button = tk.Button(page3, bg="#FFBCD9", width=4, height=3, command=lambda: [set_color(255, 188, 217), receipt("CottonCandy", "PK023")])
            CottonCandy_button.grid(row=1, column=8, padx=1, pady=2)

            CameoPink_button = tk.Button(page3, bg="#EFBBCC", width=4, height=3, command=lambda: [set_color(239, 187, 204), receipt("CameoPink", "PK024")])
            CameoPink_button.grid(row=1, column=9, padx=1, pady=2)

            FrenchPink_button = tk.Button(page3, bg="#F64A8A", width=4, height=3, command=lambda: [set_color(246, 74, 138), receipt("FrenchPink", "PK025")])
            FrenchPink_button.grid(row=1, column=10, padx=1, pady=2)

            Strawberry_button = tk.Button(page3, bg="#E8888A", width=4, height=3, command=lambda: [set_color(232, 136, 138), receipt("Strawberry", "PK026")])
            Strawberry_button.grid(row=1, column=11, padx=1, pady=2)

            PersianPink_button = tk.Button(page3, bg="#F77FBE", width=4, height=3, command=lambda: [set_color(247, 127, 190), receipt("PersianPink", "PK027")])
            PersianPink_button.grid(row=1, column=12, padx=1, pady=2)

            NewYorkPink_button = tk.Button(page3, bg="#DD8374", width=4, height=3, command=lambda: [set_color(221, 131, 116), receipt("NewYorkPink", "PK028")])
            NewYorkPink_button.grid(row=1, column=13, padx=1, pady=2)

            IndianRed_button = tk.Button(page3, bg="#CD5C5C", width=4, height=3, command=lambda: [set_color(205, 92, 92), receipt("IndianRed", "PK029")])
            IndianRed_button.grid(row=2, column=0, padx=1, pady=2)

            MunsellRed_button = tk.Button(page3, bg="#F2003C", width=4, height=3, command=lambda: [set_color(242, 0, 60), receipt("MunsellRed", "PK030")])
            MunsellRed_button.grid(row=2, column=1, padx=1, pady=2)

            Cardinal_button = tk.Button(page3, bg="#C41E3A", width=4, height=3, command=lambda: [set_color(196, 30, 58), receipt("Cardinal", "PK031")])
            Cardinal_button.grid(row=2, column=2, padx=1, pady=2)

            CrayolaRed_button = tk.Button(page3, bg="#EE204D", width=4, height=3, command=lambda: [set_color(238, 32, 77), receipt("CrayolaRed", "PK032")])
            CrayolaRed_button.grid(row=2, column=3, padx=1, pady=2)

            Crimson_button = tk.Button(page3, bg="#DC143C", width=4, height=3, command=lambda: [set_color(220, 20, 60), receipt("Crimson", "PK033")])
            Crimson_button.grid(row=2, column=4, padx=1, pady=2)

            Ruby_button = tk.Button(page3, bg="#E0115F", width=4, height=3, command=lambda: [set_color(224, 17, 95), receipt("Ruby", "PK034")])
            Ruby_button.grid(row=2, column=5, padx=1, pady=2)

            Redwood_button = tk.Button(page3, bg="#A45A52", width=4, height=3, command=lambda: [set_color(164, 90, 82), receipt("Redwood", "PK035")])
            Redwood_button.grid(row=2, column=6, padx=1, pady=2)

            RustyRed_button = tk.Button(page3, bg="#DA2C43", width=4, height=3, command=lambda: [set_color(218, 44, 67), receipt("RustyRed", "PK036")])
            RustyRed_button.grid(row=2, column=7, padx=1, pady=2)

            Amaranth_button = tk.Button(page3, bg="#E52B50", width=4, height=3, command=lambda: [set_color(229, 43, 80), receipt("Amaranth", "PK037")])
            Amaranth_button.grid(row=2, column=8, padx=1, pady=2)

            BrightMaroon_button = tk.Button(page3, bg="#C32148", width=4, height=3, command=lambda: [set_color(195, 33, 72), receipt("BrightMaroon", "PK038")])
            BrightMaroon_button.grid(row=2, column=9, padx=1, pady=2)

            BurntSienna_button = tk.Button(page3, bg="#E97451", width=4, height=3, command=lambda: [set_color(233, 116, 81), receipt("BurntSienna", "PK039")])
            BurntSienna_button.grid(row=2, column=10, padx=1, pady=2)

            CandyPink_button = tk.Button(page3, bg="#E4717A", width=4, height=3, command=lambda: [set_color(228, 113, 122), receipt("CandyPink", "PK040")])
            CandyPink_button.grid(row=2, column=11, padx=1, pady=2)

            CherryPink_button = tk.Button(page3, bg="#DE3163", width=4, height=3, command=lambda: [set_color(222, 49, 99), receipt("CherryPink", "PK041")])
            CherryPink_button.grid(row=2, column=12, padx=1, pady=2)

            Chestnut_button = tk.Button(page3, bg="#CD5C5C", width=4, height=3, command=lambda: [set_color(205, 92, 92), receipt("Chestnut", "PK042")])
            Chestnut_button.grid(row=2, column=13, padx=1, pady=2)

            DarkCoral_button = tk.Button(page3, bg="#CD5B45", width=4, height=3, command=lambda: [set_color(205, 91, 69), receipt("DarkCoral", "PK043")])
            DarkCoral_button.grid(row=3, column=0, padx=1, pady=2)

            DarkPastelRed_button = tk.Button(page3, bg="#C23B22", width=4, height=3, command=lambda: [set_color(194, 59, 34), receipt("DarkPastelRed", "PK044")])
            DarkPastelRed_button.grid(row=3, column=1, padx=1, pady=2)

            DarkTerraCotta_button = tk.Button(page3, bg="#CC4E5C", width=4, height=3, command=lambda: [set_color(204, 78, 92), receipt("DarkTerraCotta", "PK045")])
            DarkTerraCotta_button.grid(row=3, column=2, padx=1, pady=2)

            DarkSalmon_button = tk.Button(page3, bg="#E9967A", width=4, height=3, command=lambda: [set_color(233, 150, 122), receipt("DarkSalmon", "PK046")])
            DarkSalmon_button.grid(row=3, column=3, padx=1, pady=2)

            Lemonade_button = tk.Button(page3, bg="#F2DBE7", width=4, height=3, command=lambda: [set_color(242, 219, 231), receipt("Lemonade", "PK047")])
            Lemonade_button.grid(row=3, column=4, padx=1, pady=2)

            Peach_button = tk.Button(page3, bg="#FAD1AF", width=4, height=3, command=lambda: [set_color(250, 209, 175), receipt("Peach", "PK048")])
            Peach_button.grid(row=3, column=5, padx=1, pady=2)

            Crepe_button = tk.Button(page3, bg="#F89883", width=4, height=3, command=lambda: [set_color(248, 152, 131), receipt("Crepe", "PK049")])
            Crepe_button.grid(row=3, column=6, padx=1, pady=2)

            PiggyPink_button = tk.Button(page3, bg="#FDDDE6", width=4, height=3, command=lambda: [set_color(253, 221, 230), receipt("PiggyPink", "PK050")])
            PiggyPink_button.grid(row=3, column=7, padx=1, pady=2)

            DeepPink_button = tk.Button(page3, bg="#FF1493", width=4, height=3, command=lambda: [set_color(255, 20, 147), receipt("DeepPink", "PK051")])
            DeepPink_button.grid(row=3, column=8, padx=1, pady=2)

            DustStorm_button = tk.Button(page3, bg="#E5CCC9", width=4, height=3, command=lambda: [set_color(229, 204, 201), receipt("DustStorm", "PK052")])
            DustStorm_button.grid(row=3, column=9, padx=1, pady=2)

            NadeshikoPink_button = tk.Button(page3, bg="#F6ADC6", width=4, height=3, command=lambda: [set_color(246, 173, 198), receipt("NadeshikoPink", "PK053")])
            NadeshikoPink_button.grid(row=3, column=10, padx=1, pady=2)

            RoseQuartz_button = tk.Button(page3, bg="#AA98A9", width=4, height=3, command=lambda: [set_color(170, 152, 169), receipt("RoseQuartz", "PK054")])
            RoseQuartz_button.grid(row=3, column=11, padx=1, pady=2)

            WildStrawberry_button = tk.Button(page3, bg="#FF43A4", width=4, height=3, command=lambda: [set_color(255, 67, 164), receipt("WildStrawberry", "PK055")])
            WildStrawberry_button.grid(row=3, column=12, padx=1, pady=2)

            Razzmatazz_button = tk.Button(page3, bg="#E3256B", width=4, height=3, command=lambda: [set_color(227, 37, 107), receipt("Razzmatazz", "PK056")])
            Razzmatazz_button.grid(row=3, column=13, padx=1, pady=2)

            RoseTaupe_button = tk.Button(page3, bg="#905D5D", width=4, height=3, command=lambda: [set_color(144, 93, 93), receipt("RoseTaupe", "PK057")])
            RoseTaupe_button.grid(row=4, column=0, padx=1, pady=2)

            RubineRed_button = tk.Button(page3, bg="#D10056", width=4, height=3, command=lambda: [set_color(209, 0, 86), receipt("RubineRed", "PK058")])
            RubineRed_button.grid(row=4, column=1, padx=1, pady=2)

            HollywoodCerise_button = tk.Button(page3, bg="#F400A1", width=4, height=3, command=lambda: [set_color(244, 0, 161), receipt("HollywoodCerise", "PK059")])
            HollywoodCerise_button.grid(row=4, column=2, padx=1, pady=2)

            MexicanPink_button = tk.Button(page3, bg="#E4007C", width=4, height=3, command=lambda: [set_color(228, 0, 124), receipt("MexicanPink", "PK060")])
            MexicanPink_button.grid(row=4, column=3, padx=1, pady=2)

            SteelPink_button = tk.Button(page3, bg="#CC3366", width=4, height=3, command=lambda: [set_color(204, 51, 102), receipt("SteelPink", "PK061")])
            SteelPink_button.grid(row=4, column=4, padx=1, pady=2)

            RoseGold_button = tk.Button(page3, bg="#B76E79", width=4, height=3, command=lambda: [set_color(183, 110, 121), receipt("RoseGold", "PK062")])
            RoseGold_button.grid(row=4, column=5, padx=1, pady=2)

            RoseBonbon_button = tk.Button(page3, bg="#F9429E", width=4, height=3, command=lambda: [set_color(249, 66, 158), receipt("RoseBonbon", "PK063")])
            RoseBonbon_button.grid(row=4, column=6, padx=1, pady=2)

            BarbiePink_button = tk.Button(page3, bg="#E0218A", width=4, height=3, command=lambda: [set_color(224, 33, 138), receipt("BarbiePink", "PK064")])
            BarbiePink_button.grid(row=4, column=7, padx=1, pady=2)

            Mulberry_button = tk.Button(page3, bg="#C54B8C", width=4, height=3, command=lambda: [set_color(197, 75, 140), receipt("Mulberry", "PK065")])
            Mulberry_button.grid(row=4, column=8, padx=1, pady=2)

            RazzleDazzleRose_button = tk.Button(page3, bg="#FF33CC", width=4, height=3, command=lambda: [set_color(255, 51, 204), receipt("RazzleDazzleRose", "PK066")])
            RazzleDazzleRose_button.grid(row=4, column=9, padx=1, pady=2)

            Fandango_button = tk.Button(page3, bg="#B53389", width=4, height=3, command=lambda: [set_color(181, 51, 137), receipt("Fandango", "PK067")])
            Fandango_button.grid(row=4, column=10, padx=1, pady=2)

            Puce_button = tk.Button(page3, bg="#CC8899", width=4, height=3, command=lambda: [set_color(204, 136, 153), receipt("Puce", "PK068")])
            Puce_button.grid(row=4, column=11, padx=1, pady=2)

            OldRose_button = tk.Button(page3, bg="#C08081", width=4, height=3, command=lambda: [set_color(192, 128, 129), receipt("OldRose", "PK069")])
            OldRose_button.grid(row=4, column=12, padx=1, pady=2)

            Rosewood_button = tk.Button(page3, bg="#9E4244", width=4, height=3, command=lambda: [set_color(158, 66, 68), receipt("Rosewood", "PK070")])
            Rosewood_button.grid(row=4, column=13, padx=1, pady=2)

            Taffy_button = tk.Button(page3, bg="#FA86C4", width=4, height=3, command=lambda: [set_color(250, 134, 196), receipt("Taffy", "PK071")])
            Taffy_button.grid(row=5, column=0, padx=1, pady=2)

            TurkishRose_button = tk.Button(page3, bg="#B57281", width=4, height=3, command=lambda: [set_color(181, 114, 129), receipt("TurkishRose", "PK072")])
            TurkishRose_button.grid(row=5, column=1, padx=1, pady=2)

            Punch_button = tk.Button(page3, bg="#F25278", width=4, height=3, command=lambda: [set_color(242, 82, 120), receipt("Punch", "PK073")])
            Punch_button.grid(row=5, column=2, padx=1, pady=2)

            ParadisePink_button = tk.Button(page3, bg="#E63E62", width=4, height=3, command=lambda: [set_color(230, 62, 98), receipt("ParadisePink", "PK074")])
            ParadisePink_button.grid(row=5, column=3, padx=1, pady=2)

            RaspberryRose_button = tk.Button(page3, bg="#B3446C", width=4, height=3, command=lambda: [set_color(179, 68, 108), receipt("RaspberryRose", "PK075")])
            RaspberryRose_button.grid(row=5, column=4, padx=1, pady=2)

            LightCrimson_button = tk.Button(page3, bg="#F56991", width=4, height=3, command=lambda: [set_color(245, 105, 145), receipt("LightCrimson", "PK076")])
            LightCrimson_button.grid(row=5, column=5, padx=1, pady=2)

            PinkSherbet_button = tk.Button(page3, bg="#F78FA7", width=4, height=3, command=lambda: [set_color(247, 143, 167), receipt("PinkSherbet", "PK077")])
            PinkSherbet_button.grid(row=5, column=6, padx=1, pady=2)

            TickleMePink_button = tk.Button(page3, bg="#FC89AC", width=4, height=3, command=lambda: [set_color(252, 137, 172), receipt("TickleMePink", "PK078")])
            TickleMePink_button.grid(row=5, column=7, padx=1, pady=2)

            ThulianPink_button = tk.Button(page3, bg="#DE6FA1", width=4, height=3, command=lambda: [set_color(222, 111, 161), receipt("ThulianPink", "PK079")])
            ThulianPink_button.grid(row=5, column=8, padx=1, pady=2)

            BrilliantRose_button = tk.Button(page3, bg="#FF55A3", width=4, height=3, command=lambda: [set_color(255, 85, 163), receipt("BrilliantRose", "PK080")])
            BrilliantRose_button.grid(row=5, column=9, padx=1, pady=2)

            Lace_button = tk.Button(page3, bg="#FFD8F0", width=4, height=3, command=lambda: [set_color(255, 216, 240), receipt("Lace", "PK081")])
            Lace_button.grid(row=5, column=10, padx=1, pady=2)

            Smitten_button = tk.Button(page3, bg="#C84186", width=4, height=3, command=lambda: [set_color(200, 65, 134), receipt("Smitten", "PK082")])
            Smitten_button.grid(row=5, column=11, padx=1, pady=2)

            Your_button = tk.Button(page3, bg="#FFC0C0", width=4, height=3, command=lambda: [set_color(255, 192, 192), receipt("Your", "PK083")])
            Your_button.grid(row=5, column=12, padx=1, pady=2)

            Careys_button = tk.Button(page3, bg="#D8A8A8", width=4, height=3, command=lambda: [set_color(216, 168, 168), receipt("Careys", "PK084")])
            Careys_button.grid(row=5, column=13, padx=1, pady=2)

            Oyster_button = tk.Button(page3, bg="#F0D8D8", width=4, height=3, command=lambda: [set_color(240, 216, 216), receipt("Oyster", "PK085")])
            Oyster_button.grid(row=6, column=0, padx=1, pady=2)

            ShimmeringBlush_button = tk.Button(page3, bg="#D98695", width=4, height=3, command=lambda: [set_color(217, 134, 149), receipt("ShimmeringBlush", "PK086")])
            ShimmeringBlush_button.grid(row=6, column=1, padx=1, pady=2)

            Sea_button = tk.Button(page3, bg="#F09090", width=4, height=3, command=lambda: [set_color(240, 144, 144), receipt("Sea", "PK087")])
            Sea_button.grid(row=6, column=2, padx=1, pady=2)

            Brink_button = tk.Button(page3, bg="#FF6090", width=4, height=3, command=lambda: [set_color(255, 96, 144), receipt("Brink", "PK088")])
            Brink_button.grid(row=6, column=3, padx=1, pady=2)

            Hippie_button = tk.Button(page3, bg="#A84860", width=4, height=3, command=lambda: [set_color(168, 72, 96), receipt("Hippie", "PK089")])
            Hippie_button.grid(row=6, column=4, padx=1, pady=2)

            LightDeepPink_button = tk.Button(page3, bg="#FF5CCD", width=4, height=3, command=lambda: [set_color(255, 92, 205), receipt("LightDeepPink", "PK090")])
            LightDeepPink_button.grid(row=6, column=5, padx=1, pady=2)

            WildOrchid_button = tk.Button(page3, bg="#D470A2", width=4, height=3, command=lambda: [set_color(212, 112, 162), receipt("WildOrchid", "PK091")])
            WildOrchid_button.grid(row=6, column=6, padx=1, pady=2)

            CerisePink_button = tk.Button(page3, bg="#EC3B83", width=4, height=3, command=lambda: [set_color(236, 59, 131), receipt("CerisePink", "PK092")])
            CerisePink_button.grid(row=6, column=7, padx=1, pady=2)

            ShockingPink_button = tk.Button(page3, bg="#FC0FC0", width=4, height=3, command=lambda: [set_color(252, 15, 192), receipt("ShockingPink", "PK093")])
            ShockingPink_button.grid(row=6, column=8, padx=1, pady=2)

            Hit_button = tk.Button(page3, bg="#FFA878", width=4, height=3, command=lambda: [set_color(255, 168, 120), receipt("Hit", "PK094")])
            Hit_button.grid(row=6, column=9, padx=1, pady=2)

            Lady_button = tk.Button(page3, bg="#F0C0A8", width=4, height=3, command=lambda: [set_color(240, 192, 168), receipt("Lady", "PK095")])
            Lady_button.grid(row=6, column=10, padx=1, pady=2)

            NeonFuchsia_button = tk.Button(page3, bg="#FE4164", width=4, height=3, command=lambda: [set_color(254, 65, 100), receipt("NeonFuchsia", "PK096")])
            NeonFuchsia_button.grid(row=6, column=11, padx=1, pady=2)

            UltraPink_button = tk.Button(page3, bg="#FF6FFF", width=4, height=3, command=lambda: [set_color(255, 111, 255), receipt("UltraPink", "PK097")])
            UltraPink_button.grid(row=6, column=12, padx=1, pady=2)

            SchaussPink_button = tk.Button(page3, bg="#FF91AF", width=4, height=3, command=lambda: [set_color(255, 145, 175), receipt("SchaussPink", "PK098")])
            SchaussPink_button.grid(row=6, column=13, padx=1, pady=2)

            RuddyPink_button = tk.Button(page3, bg="#E18E96", width=4, height=3, command=lambda: [set_color(225, 142, 150), receipt("RuddyPink", "PK099")])
            RuddyPink_button.grid(row=7, column=0, padx=1, pady=2)

            PinkPearl_button = tk.Button(page3, bg="#E7ACCF", width=4, height=3, command=lambda: [set_color(231, 172, 207), receipt("PinkPearl", "PK100")])
            PinkPearl_button.grid(row=7, column=1, padx=1, pady=2)

            LavenderRose_button = tk.Button(page3, bg="#FBA0E3", width=4, height=3, command=lambda: [set_color(251, 160, 227), receipt("LavenderRose", "PK101")])
            LavenderRose_button.grid(row=7, column=2, padx=1, pady=2)

            Shampoo_button = tk.Button(page3, bg="#FFCFF1", width=4, height=3, command=lambda: [set_color(255, 207, 241), receipt("Shampoo", "PK102")])
            Shampoo_button.grid(row=7, column=3, padx=1, pady=2)

            SpanishPink_button = tk.Button(page3, bg="#F7BFBE", width=4, height=3, command=lambda: [set_color(247, 191, 190), receipt("SpanishPink", "PK103")])
            SpanishPink_button.grid(row=7, column=4, padx=1, pady=2)

            ValentinePink_button = tk.Button(page3, bg="#E6A6BE", width=4, height=3, command=lambda: [set_color(230, 166, 190), receipt("ValentinePink", "PK104")])
            ValentinePink_button.grid(row=7, column=5, padx=1, pady=2)

            SilveryPink_button = tk.Button(page3, bg="#DCB5B4", width=4, height=3, command=lambda: [set_color(220, 181, 180), receipt("SilveryPink", "PK105")])
            SilveryPink_button.grid(row=7, column=6, padx=1, pady=2)

            Melon_button = tk.Button(page3, bg="#F7BCAC", width=4, height=3, command=lambda: [set_color(247, 188, 172), receipt("Melon", "PK106")])
            Melon_button.grid(row=7, column=7, padx=1, pady=2)

            Milano_button = tk.Button(page3, bg="#D95D67", width=4, height=3, command=lambda: [set_color(217, 93, 103), receipt("Milano", "PK107")])
            Milano_button.grid(row=7, column=8, padx=1, pady=2)

            SweetPink_button = tk.Button(page3, bg="#EE918D", width=4, height=3, command=lambda: [set_color(238, 145, 141), receipt("SweetPink", "PK108")])
            SweetPink_button.grid(row=7, column=9, padx=1, pady=2)

            KnockoutPink_button = tk.Button(page3, bg="#FF3EA5", width=4, height=3, command=lambda: [set_color(255, 62, 165), receipt("KnockoutPink", "PK109")])
            KnockoutPink_button.grid(row=7, column=10, padx=1, pady=2)

            GrapefruitPink_button = tk.Button(page3, bg="#E0707C", width=4, height=3, command=lambda: [set_color(224, 112, 124), receipt("GrapefruitPink", "PK110")])
            GrapefruitPink_button.grid(row=7, column=11, padx=1, pady=2)

            ChampagnePink_button = tk.Button(page3, bg="#F6E1D3", width=4, height=3, command=lambda: [set_color(246, 225, 211), receipt("ChampagnePink", "PK111")])
            ChampagnePink_button.grid(row=7, column=12, padx=1, pady=2)

            LipPink_button = tk.Button(page3, bg="#DBAC98", width=4, height=3, command=lambda: [set_color(219, 172, 152), receipt("LipPink", "PK112")])
            LipPink_button.grid(row=7, column=13, padx=1, pady=2)

            PassionPink_button = tk.Button(page3, bg="#CE74A7", width=4, height=3, command=lambda: [set_color(206, 116, 167), receipt("PassionPink", "PK113")])
            PassionPink_button.grid(row=8, column=0, padx=1, pady=2)

            NudePink_button = tk.Button(page3, bg="#DDC0B4", width=4, height=3, command=lambda: [set_color(221, 192, 180), receipt("NudePink", "PK114")])
            NudePink_button.grid(row=8, column=1, padx=1, pady=2)

            RosyPink_button = tk.Button(page3, bg="#FF66CC", width=4, height=3, command=lambda: [set_color(255, 102, 204), receipt("RosyPink", "PK115")])
            RosyPink_button.grid(row=8, column=2, padx=1, pady=2)

            GoldPink_button = tk.Button(page3, bg="#E6C7C2", width=4, height=3, command=lambda: [set_color(230, 199, 194), receipt("GoldPink", "PK116")])
            GoldPink_button.grid(row=8, column=3, padx=1, pady=2)

            MistyRose_button = tk.Button(page3, bg="#FFE4E1", width=4, height=3, command=lambda: [set_color(255, 228, 225), receipt("MistyRose", "PK117")])
            MistyRose_button.grid(row=8, column=4, padx=1, pady=2)

            Mauvelous_button = tk.Button(page3, bg="#EF98AA", width=4, height=3, command=lambda: [set_color(239, 152, 170), receipt("Mauvelous", "PK118")])
            Mauvelous_button.grid(row=8, column=5, padx=1, pady=2)

            LightBlush_button = tk.Button(page3, bg="#F1ABB9", width=4, height=3, command=lambda: [set_color(241, 171, 185), receipt("LightBlush", "PK119")])
            LightBlush_button.grid(row=8, column=6, padx=1, pady=2)

            CopperRose_button = tk.Button(page3, bg="#996666", width=4, height=3, command=lambda: [set_color(153, 102, 102), receipt("CopperRose", "PK120")])
            CopperRose_button.grid(row=8, column=7, padx=1, pady=2)

            RaspberryGlace_button = tk.Button(page3, bg="#915F6D", width=4, height=3, command=lambda: [set_color(145, 95, 109), receipt("RaspberryGlace", "PK121")])
            RaspberryGlace_button.grid(row=8, column=8, padx=1, pady=2)

            DebianRed_button = tk.Button(page3, bg="#D70A53", width=4, height=3, command=lambda: [set_color(215, 10, 83), receipt("DebianRed", "PK122")])
            DebianRed_button.grid(row=8, column=9, padx=1, pady=2)

            Ruber_button = tk.Button(page3, bg="#CE4676", width=4, height=3, command=lambda: [set_color(206, 70, 118), receipt("Ruber", "PK123")])
            Ruber_button.grid(row=8, column=10, padx=1, pady=2)

            VanillaIce_button = tk.Button(page3, bg="#F38FA9", width=4, height=3, command=lambda: [set_color(243, 143, 169), receipt("VanillaIce", "PK124")])
            VanillaIce_button.grid(row=8, column=11, padx=1, pady=2)

            LightHotPink_button = tk.Button(page3, bg="#FFB3DE", width=4, height=3, command=lambda: [set_color(255, 179, 222), receipt("LightHotPink", "PK125")])
            LightHotPink_button.grid(row=8, column=12, padx=1, pady=2)

            SuperPink_button = tk.Button(page3, bg="#CF6BA9", width=4, height=3, command=lambda: [set_color(207, 107, 169), receipt("SuperPink", "PK126")])
            SuperPink_button.grid(row=8, column=13, padx=1, pady=2)

            ChinaRose_button = tk.Button(page3, bg="#A8516E", width=4, height=3, command=lambda: [set_color(168, 81, 110), receipt("ChinaRose", "PK127")])
            ChinaRose_button.grid(row=9, column=0, padx=1, pady=2)

            DeepPruce_button = tk.Button(page3, bg="#A95C68", width=4, height=3, command=lambda: [set_color(169, 92, 104), receipt("DeepPruce", "PK128")])
            DeepPruce_button.grid(row=9, column=1, padx=1, pady=2)

            FrenchFuchsia_button = tk.Button(page3, bg="#FD3F92", width=4, height=3, command=lambda: [set_color(253, 63, 146), receipt("FrenchFuchsia", "PK129")])
            FrenchFuchsia_button.grid(row=9, column=2, padx=1, pady=2)

            # Purple Series
            TruePurple_button = tk.Button(page6, bg="#6A0DAD", width=4, height=3,command=lambda: [set_color(106, 13, 173), receipt("TruePurple", "RD001")])
            TruePurple_button.grid(row=0, column=0, padx=1, pady=2)

            Thistle_button = tk.Button(page6, bg="#D8BFD8", width=4, height=3,command=lambda: [set_color(216, 191, 216), receipt("Thistle", "RD002")])
            Thistle_button.grid(row=0, column=1, padx=1, pady=2)

            Plum_button = tk.Button(page6, bg="#DDA0DD", width=4, height=3,command=lambda: [set_color(221, 160, 221), receipt("Plum", "RD003")])
            Plum_button.grid(row=0, column=2, padx=1, pady=2)

            Violet_button = tk.Button(page6, bg="#8F00FF", width=4, height=3,command=lambda: [set_color(143, 0, 255), receipt("Violet", "RD004")])
            Violet_button.grid(row=0, column=3, padx=1, pady=2)

            Orchid_button = tk.Button(page6, bg="#DA70D6", width=4, height=3,command=lambda: [set_color(218, 112, 214), receipt("Orchid", "RD005")])
            Orchid_button.grid(row=0, column=4, padx=1, pady=2)

            Fuchsia_button = tk.Button(page6, bg="#FF00FF", width=4, height=3,command=lambda: [set_color(255, 0, 255), receipt("Fuchsia", "RD006")])
            Fuchsia_button.grid(row=0, column=5, padx=1, pady=2)

            MediumOrchid_button = tk.Button(page6, bg="#BA55D3", width=4, height=3,command=lambda: [set_color(186, 85, 211), receipt("MediumOrchid", "RD007")])
            MediumOrchid_button.grid(row=0, column=6, padx=1, pady=2)

            MediumPurple_button = tk.Button(page6, bg="#9370DB", width=4, height=3,command=lambda: [set_color(147, 112, 219),receipt("MediumPurple", "RD008")])
            MediumPurple_button.grid(row=0, column=7, padx=1, pady=2)

            BlueViolet_button = tk.Button(page6, bg="#8A2BE2", width=4, height=3,command=lambda: [set_color(138, 43, 226), receipt("BlueViolet", "RD009")])
            BlueViolet_button.grid(row=0, column=8, padx=1, pady=2)

            DarkViolet_button = tk.Button(page6, bg="#9400D3", width=4, height=3,command=lambda: [set_color(148, 0, 211), receipt("DarkViolet", "RD010")])
            DarkViolet_button.grid(row=0, column=9, padx=1, pady=2)

            DarkOrchid_button = tk.Button(page6, bg="#9932CC", width=4, height=3,command=lambda: [set_color(153, 50, 204), receipt("DarkOrchid", "RD011")])
            DarkOrchid_button.grid(row=0, column=10, padx=1, pady=2)

            DarkMagenta_button = tk.Button(page6, bg="#8B008B", width=4, height=3,command=lambda: [set_color(139, 0, 139), receipt("DarkMagenta", "RD012")])
            DarkMagenta_button.grid(row=0, column=11, padx=1, pady=2)

            Indigo_button = tk.Button(page6, bg="#4B0082", width=4, height=3,command=lambda: [set_color(75, 0, 130), receipt("Indigo", "RD013")])
            Indigo_button.grid(row=0, column=12, padx=1, pady=2)

            Veronica_button = tk.Button(page6, bg="#A020F0", width=4, height=3,command=lambda: [set_color(160, 32, 240), receipt("Veronica", "RD014")])
            Veronica_button.grid(row=0, column=13, padx=1, pady=2)

            PalePurple_button = tk.Button(page6, bg="#FAE6FA", width=4, height=3,command=lambda: [set_color(250, 230, 250), receipt("PalePurple", "RD015")])
            PalePurple_button.grid(row=1, column=0, padx=1, pady=2)

            Mauve_button = tk.Button(page6, bg="#E0B0FF", width=4, height=3,command=lambda: [set_color(224, 176, 255), receipt("Mauve", "RD016")])
            Mauve_button.grid(row=1, column=1, padx=1, pady=2)

            Heliotrope_button = tk.Button(page6, bg="#DF73FF", width=4, height=3,command=lambda: [set_color(223, 115, 255), receipt("Heliotrope", "RD017")])
            Heliotrope_button.grid(row=1, column=2, padx=1, pady=2)

            Phlox_button = tk.Button(page6, bg="#DF00FF", width=4, height=3,command=lambda: [set_color(223, 0, 255), receipt("Phlox", "RD018")])
            Phlox_button.grid(row=1, column=3, padx=1, pady=2)

            PurplePizzazz_button = tk.Button(page6, bg="#FE4EDA", width=4, height=3,command=lambda: [set_color(254, 78, 218),receipt("PurplePizzazz", "RD019")])
            PurplePizzazz_button.grid(row=1, column=4, padx=1, pady=2)

            LiserianPurple_button = tk.Button(page6, bg="#DE6FA1", width=4, height=3,command=lambda: [set_color(222, 111, 161),receipt("LiserianPurple", "RD020")])
            LiserianPurple_button.grid(row=1, column=5, padx=1, pady=2)

            Mulberry_button = tk.Button(page6, bg="#C54B8C", width=4, height=3,command=lambda: [set_color(197, 75, 140), receipt("Mulberry", "RD021")])
            Mulberry_button.grid(row=1, column=6, padx=1, pady=2)

            PearlyPurple_button = tk.Button(page6, bg="#B768A2", width=4, height=3,command=lambda: [set_color(183, 104, 162),receipt("PearlyPurple", "RD022")])
            PearlyPurple_button.grid(row=1, column=7, padx=1, pady=2)

            Purpureus_button = tk.Button(page6, bg="#9A4EAE", width=4, height=3,command=lambda: [set_color(154, 78, 174), receipt("Purpureus", "RD023")])
            Purpureus_button.grid(row=1, column=8, padx=1, pady=2)

            NorthwesternPurple_button = tk.Button(page6, bg="#4E2A84", width=4, height=3,command=lambda: [set_color(78, 42, 132),receipt("NorthwesternPurple", "RD024")])
            NorthwesternPurple_button.grid(row=1, column=9, padx=1, pady=2)

            KSUPurple_button = tk.Button(page6, bg="#512888", width=4, height=3,command=lambda: [set_color(81, 40, 136), receipt("KSUPurple", "RD025")])
            KSUPurple_button.grid(row=1, column=10, padx=1, pady=2)

            PompandPower_button = tk.Button(page6, bg="#86608E", width=4, height=3,command=lambda: [set_color(134, 96, 142), receipt("PompandPower", "RD026")])
            PompandPower_button.grid(row=1, column=11, padx=1, pady=2)

            MardiGras_button = tk.Button(page6, bg="#880085", width=4, height=3,command=lambda: [set_color(136, 0, 133), receipt("MardiGras", "RD027")])
            MardiGras_button.grid(row=1, column=12, padx=1, pady=2)

            Eminence_button = tk.Button(page6, bg="#6C3082", width=4, height=3,command=lambda: [set_color(108, 48, 130), receipt("Eminence", "RD028")])
            Eminence_button.grid(row=1, column=13, padx=1, pady=2)

            PansyPurple_button = tk.Button(page6, bg="#78184A", width=4, height=3,command=lambda: [set_color(120, 24, 74), receipt("PansyPurple", "RD029")])
            PansyPurple_button.grid(row=2, column=0, padx=1, pady=2)

            Palatinate_button = tk.Button(page6, bg="#72246C", width=4, height=3,command=lambda: [set_color(114, 36, 108), receipt("Palatinate", "RD030")])
            Palatinate_button.grid(row=2, column=1, padx=1, pady=2)

            DarkPurple_button = tk.Button(page6, bg="#301934", width=4, height=3,command=lambda: [set_color(48, 25, 52), receipt("DarkPurple", "RD031")])
            DarkPurple_button.grid(row=2, column=2, padx=1, pady=2)

            Byzantium_button = tk.Button(page6, bg="#702963", width=4, height=3,command=lambda: [set_color(112, 41, 99), receipt("Byzantium", "RD032")])
            Byzantium_button.grid(row=2, column=3, padx=1, pady=2)

            AfricanViolet_button = tk.Button(page6, bg="#B284BE", width=4, height=3,command=lambda: [set_color(178, 132, 190),receipt("AfricanViolet", "RD033")])
            AfricanViolet_button.grid(row=2, column=4, padx=1, pady=2)

            Amethyst_button = tk.Button(page6, bg="#9966CC", width=4, height=3,command=lambda: [set_color(153, 102, 204), receipt("Amethyst", "RD034")])
            Amethyst_button.grid(row=2, column=5, padx=1, pady=2)

            ChineseViolet_button = tk.Button(page6, bg="#856088", width=4, height=3,command=lambda: [set_color(133, 96, 136),receipt("ChineseViolet", "RD035")])
            ChineseViolet_button.grid(row=2, column=6, padx=1, pady=2)

            EnglishViolet_button = tk.Button(page6, bg="#563C5C", width=4, height=3,command=lambda: [set_color(86, 60, 92), receipt("EnglishViolet", "RD036")])
            EnglishViolet_button.grid(row=2, column=7, padx=1, pady=2)

            RussianViolet_button = tk.Button(page6, bg="#32174D", width=4, height=3,command=lambda: [set_color(50, 23, 77), receipt("RussianViolet", "RD037")])
            RussianViolet_button.grid(row=2, column=8, padx=1, pady=2)

            FairyTale_button = tk.Button(page6, bg="#F2C1D1", width=4, height=3,command=lambda: [set_color(242, 193, 209), receipt("FairyTale", "RD038")])
            FairyTale_button.grid(row=2, column=9, padx=1, pady=2)

            Fandango_button = tk.Button(page6, bg="#B53389", width=4, height=3,command=lambda: [set_color(181, 51, 137), receipt("Fandango", "RD039")])
            Fandango_button.grid(row=2, column=10, padx=1, pady=2)

            FrenchMauve_button = tk.Button(page6, bg="#D473D4", width=4, height=3,command=lambda: [set_color(212, 115, 212), receipt("FrenchMauve", "RD040")])
            FrenchMauve_button.grid(row=2, column=11, padx=1, pady=2)

            Affair_button = tk.Button(page6, bg="#6F4685", width=4, height=3,command=lambda: [set_color(111, 70, 133), receipt("Affair", "RD041")])
            Affair_button.grid(row=2, column=12, padx=1, pady=2)

            BossJokes_button = tk.Button(page6, bg="#B0306A", width=4, height=3,command=lambda: [set_color(176, 48, 106), receipt("BossJokes", "RD042")])
            BossJokes_button.grid(row=2, column=13, padx=1, pady=2)

            Iris_button = tk.Button(page6, bg="#9867C5", width=4, height=3,command=lambda: [set_color(152, 103, 197), receipt("Iris", "RD043")])
            Iris_button.grid(row=3, column=0, padx=1, pady=2)

            LongDistance_button = tk.Button(page6, bg="#6F456E", width=4, height=3,command=lambda: [set_color(111, 69, 110), receipt("LongDistance", "RD044")])
            LongDistance_button.grid(row=3, column=1, padx=1, pady=2)

            PrinceCharming_button = tk.Button(page6, bg="#493F5E", width=4, height=3,command=lambda: [set_color(73, 63, 94),receipt("PrinceCharming", "RD045")])
            PrinceCharming_button.grid(row=3, column=2, padx=1, pady=2)

            LipstickStain_button = tk.Button(page6, bg="#8E4785", width=4, height=3,command=lambda: [set_color(142, 71, 133),receipt("LipstickStain", "RD046")])
            LipstickStain_button.grid(row=3, column=3, padx=1, pady=2)

            Pompadour_button = tk.Button(page6, bg="#720058", width=4, height=3,command=lambda: [set_color(114, 0, 88), receipt("Pompadour", "RD047")])
            Pompadour_button.grid(row=3, column=4, padx=1, pady=2)

            GrapeColor_button = tk.Button(page6, bg="#6F2DA8", width=4, height=3,command=lambda: [set_color(111, 45, 168), receipt("GrapeColor", "RD048")])
            GrapeColor_button.grid(row=3, column=5, padx=1, pady=2)

            Wine_button = tk.Button(page6, bg="#2C041C", width=4, height=3,command=lambda: [set_color(44, 4, 28), receipt("Wine", "RD049")])
            Wine_button.grid(row=3, column=6, padx=1, pady=2)

            PizzaEdge_button = tk.Button(page6, bg="#9A2CA0", width=4, height=3,command=lambda: [set_color(154, 44, 160), receipt("PizzaEdge", "RD050")])
            PizzaEdge_button.grid(row=3, column=7, padx=1, pady=2)

            TyrianPurple_button = tk.Button(page6, bg="#66023C", width=4, height=3,command=lambda: [set_color(102, 2, 60), receipt("TyrianPurple", "RD051")])
            TyrianPurple_button.grid(row=3, column=8, padx=1, pady=2)

            UltraViolet_button = tk.Button(page6, bg="#645394", width=4, height=3,command=lambda: [set_color(100, 83, 148), receipt("UltraViolet", "RD052")])
            UltraViolet_button.grid(row=3, column=9, padx=1, pady=2)

            Studio_button = tk.Button(page6, bg="#7851A9", width=4, height=3,command=lambda: [set_color(120, 81, 169), receipt("Studio", "RD053")])
            Studio_button.grid(row=3, column=10, padx=1, pady=2)

            ElectricPurple_button = tk.Button(page6, bg="#BF00FF", width=4, height=3,command=lambda: [set_color(191, 0, 255),receipt("ElectricPurple", "RD054")])
            ElectricPurple_button.grid(row=3, column=11, padx=1, pady=2)

            Eggplant_button = tk.Button(page6, bg="#311432", width=4, height=3,command=lambda: [set_color(49, 20, 50), receipt("Eggplant", "RD055")])
            Eggplant_button.grid(row=3, column=12, padx=1, pady=2)

            PeriwinklePurple_button = tk.Button(page6, bg="#BE93E4", width=4, height=3,command=lambda: [set_color(190, 147, 228),receipt("PeriwinklePurple", "RD056")])
            PeriwinklePurple_button.grid(row=3, column=13, padx=1, pady=2)

            Sangria_button = tk.Button(page6, bg="#4D0F28", width=4, height=3,command=lambda: [set_color(77, 15, 40), receipt("Sangria", "RD057")])
            Sangria_button.grid(row=4, column=0, padx=1, pady=2)

            Raisin_button = tk.Button(page6, bg="#290916", width=4, height=3,command=lambda: [set_color(41, 9, 22), receipt("Raisin", "RD058")])
            Raisin_button.grid(row=4, column=1, padx=1, pady=2)

            MountbattenPink_button = tk.Button(page6, bg="#997A8D", width=4, height=3,command=lambda: [set_color(153, 122, 141),receipt("MountbattenPink", "RD059")])
            MountbattenPink_button.grid(row=4, column=2, padx=1, pady=2)

            FuchsiaBlue_button = tk.Button(page6, bg="#9C51B6", width=4, height=3,command=lambda: [set_color(156, 81, 182), receipt("FuchsiaBlue", "RD060")])
            FuchsiaBlue_button.grid(row=4, column=3, padx=1, pady=2)

            GoodTax_button = tk.Button(page6, bg="#C9A0FF", width=4, height=3,command=lambda: [set_color(201, 160, 255), receipt("GoodTax", "RD061")])
            GoodTax_button.grid(row=4, column=4, padx=1, pady=2)

            Jam_button = tk.Button(page6, bg="#67032F", width=4, height=3,command=lambda: [set_color(103, 3, 47), receipt("Jam", "RD062")])
            Jam_button.grid(row=4, column=5, padx=1, pady=2)

            RipePlum_button = tk.Button(page6, bg="#410056", width=4, height=3,command=lambda: [set_color(65, 0, 86), receipt("RipePlum", "RD063")])
            RipePlum_button.grid(row=4, column=6, padx=1, pady=2)

            Heather_button = tk.Button(page6, bg="#9E7BB5", width=4, height=3,command=lambda: [set_color(158, 123, 181), receipt("Heather", "RD064")])
            Heather_button.grid(row=4, column=7, padx=1, pady=2)

            MagentaPurple_button = tk.Button(page6, bg="#A32CC4", width=4, height=3,command=lambda: [set_color(163, 44, 196),receipt("MagentaPurple", "RD065")])
            MagentaPurple_button.grid(row=4, column=8, padx=1, pady=2)

            MountainsMajesty_button = tk.Button(page6, bg="#9078C0", width=4, height=3,command=lambda: [set_color(144, 120, 192),receipt("MountainsMajesty", "RD066")])
            MountainsMajesty_button.grid(row=4, column=9, padx=1, pady=2)

            OldLavender_button = tk.Button(page6, bg="#796878", width=4, height=3,command=lambda: [set_color(121, 104, 120), receipt("OldLavender", "RD067")])
            OldLavender_button.grid(row=4, column=10, padx=1, pady=2)

            RebeccaPurple_button = tk.Button(page6, bg="#663399", width=4, height=3,command=lambda: [set_color(102, 51, 153),receipt("RebeccaPurple", "RD068")])
            RebeccaPurple_button.grid(row=4, column=11, padx=1, pady=2)

            RazzmicBerryPurple_button = tk.Button(page6, bg="#8D4E85", width=4, height=3,command=lambda: [set_color(141, 78, 133),receipt("RazzmicBerryPurple", "RD069")])
            RazzmicBerryPurple_button.grid(row=4, column=12, padx=1, pady=2)

            WineDregsPurple_button = tk.Button(page6, bg="#673147", width=4, height=3,command=lambda: [set_color(103, 49, 71),receipt("WineDregsPurple", "RD070")])
            WineDregsPurple_button.grid(row=4, column=13, padx=1, pady=2)

            RegaliaPurple_button = tk.Button(page6, bg="#522D80", width=4, height=3,command=lambda: [set_color(82, 45, 128),receipt("RegaliaPurple", "RD071")])
            RegaliaPurple_button.grid(row=5, column=0, padx=1, pady=2)

            TwilightLavenderPurple_button = tk.Button(page6, bg="#8A496B", width=4, height=3,command=lambda: [set_color(138, 73, 107),receipt("TwilightLavenderPurple", "RD072")])
            TwilightLavenderPurple_button.grid(row=5, column=1, padx=1, pady=2)

            TraditionalPurple_button = tk.Button(page6, bg="#8E4585", width=4, height=3,command=lambda: [set_color(142, 69, 133),receipt("TraditionalPurple", "RD073")])
            TraditionalPurple_button.grid(row=5, column=2, padx=1, pady=2)

            SpanishVioletPurple_button = tk.Button(page6, bg="#4C2882", width=4, height=3,command=lambda: [set_color(76, 40, 130),receipt("SpanishVioletPurple", "RD074")])
            SpanishVioletPurple_button.grid(row=5, column=3, padx=1, pady=2)

            ImperialPurple_button = tk.Button(page6, bg="#602F6B", width=4, height=3,command=lambda: [set_color(96, 47, 107),receipt("ImperialPurple", "RD075")])
            ImperialPurple_button.grid(row=5, column=4, padx=1, pady=2)

            JapaneseVioletPurple_button = tk.Button(page6, bg="#5B3256", width=4, height=3,command=lambda: [set_color(91, 50, 86),receipt("JapaneseVioletPurple", "RD076")])
            JapaneseVioletPurple_button.grid(row=5, column=5, padx=1, pady=2)

            MunsellPurple_button = tk.Button(page6, bg="#9F00C5", width=4, height=3,command=lambda: [set_color(159, 0, 197),receipt("MunsellPurple", "RD077")])
            MunsellPurple_button.grid(row=5, column=6, padx=1, pady=2)

            DeepRubyPurple_button = tk.Button(page6, bg="#843F5B", width=4, height=3,command=lambda: [set_color(132, 63, 91),receipt("DeepRubyPurple", "RD078")])
            DeepRubyPurple_button.grid(row=5, column=7, padx=1, pady=2)

            PurpleHeart_button = tk.Button(page6, bg="#7442C8", width=4, height=3,command=lambda: [set_color(116, 66, 200), receipt("PurpleHeart", "RD079")])
            PurpleHeart_button.grid(row=5, column=8, padx=1, pady=2)

            LavenderBlush_button = tk.Button(page6, bg="#FFF0F5", width=4, height=3,command=lambda: [set_color(255, 240, 245),receipt("LavenderBlush", "RD080")])
            LavenderBlush_button.grid(row=5, column=9, padx=1, pady=2)

            EarlyBird_button = tk.Button(page6, bg="#CEA2FD", width=4, height=3,command=lambda: [set_color(206, 162, 253), receipt("EarlyBird", "RD081")])
            EarlyBird_button.grid(row=5, column=10, padx=1, pady=2)

            Lilac_button = tk.Button(page6, bg="#B65FCF", width=4, height=3,command=lambda: [set_color(182, 95, 207), receipt("Lilac", "RD082")])
            Lilac_button.grid(row=5, column=11, padx=1, pady=2)

            PurpleTaupe_button = tk.Button(page6, bg="#50404D", width=4, height=3,command=lambda: [set_color(80, 64, 77), receipt("PurpleTaupe", "RD083")])
            PurpleTaupe_button.grid(row=5, column=12, padx=1, pady=2)

            CyberGrapePurple_button = tk.Button(page6, bg="#58427C", width=4, height=3,command=lambda: [set_color(88, 66, 124),receipt("CyberGrapePurple", "RD084")])
            CyberGrapePurple_button.grid(row=5, column=13, padx=1, pady=2)

            KingfisherDaisy_button = tk.Button(page6, bg="#653780", width=4, height=3,command=lambda: [set_color(101, 55, 128),receipt("KingfisherDaisy", "RD085")])
            KingfisherDaisy_button.grid(row=6, column=0, padx=1, pady=2)

            Seance_button = tk.Button(page6, bg="#61346B", width=4, height=3,command=lambda: [set_color(97, 52, 107), receipt("Seance", "RD086")])
            Seance_button.grid(row=6, column=1, padx=1, pady=2)

            LavenderGray_button = tk.Button(page6, bg="#B6B5D8", width=4, height=3,command=lambda: [set_color(182, 181, 216),receipt("LavenderGray", "RD087")])
            LavenderGray_button.grid(row=6, column=2, padx=1, pady=2)

            Hopbush_button = tk.Button(page6, bg="#D05FAD", width=4, height=3,command=lambda: [set_color(208, 95, 173), receipt("Hopbush", "RD088")])
            Hopbush_button.grid(row=6, column=3, padx=1, pady=2)

            Tacao_button = tk.Button(page6, bg="#6F3096", width=4, height=3,command=lambda: [set_color(111, 48, 150), receipt("Tacao", "RD089")])
            Tacao_button.grid(row=6, column=4, padx=1, pady=2)

            BrilliantPurple_button = tk.Button(page6, bg="#D399E6", width=4, height=3,command=lambda: [set_color(211, 153, 230),receipt("BrilliantPurple", "RD090")])
            BrilliantPurple_button.grid(row=6, column=5, padx=1, pady=2)

            MurasakiPurple_button = tk.Button(page6, bg="#4F284B", width=4, height=3,command=lambda: [set_color(79, 40, 75),receipt("MurasakiPurple", "RD091")])
            MurasakiPurple_button.grid(row=6, column=6, padx=1, pady=2)

            BlackishPurple_button = tk.Button(page6, bg="#291E29", width=4, height=3,command=lambda: [set_color(41, 30, 41),receipt("BlackishPurple", "RD092")])
            BlackishPurple_button.grid(row=6, column=7, padx=1, pady=2)

            LovelyPurple_button = tk.Button(page6, bg="#7F38EC", width=4, height=3,command=lambda: [set_color(127, 56, 236), receipt("LovelyPurple", "RD093")])
            LovelyPurple_button.grid(row=6, column=8, padx=1, pady=2)

            VulgarPurpleGrapeJelly_button = tk.Button(page6, bg="#3E2F84", width=4, height=3,command=lambda: [set_color(62, 47, 132),receipt("VulgarPurpleGrapeJelly", "RD094")])
            VulgarPurpleGrapeJelly_button.grid(row=6, column=9, padx=1, pady=2)

            UniversityofCentralArkansasPurple_button = tk.Button(page6, bg="#4F2D7F", width=4, height=3,command=lambda: [set_color(79, 45, 127), receipt("UniversityofCentralArkansasPurple", "RD095")])
            UniversityofCentralArkansasPurple_button.grid(row=6, column=10, padx=1, pady=2)

            FedExPurple_button = tk.Button(page6, bg="#660099", width=4, height=3, command=lambda: [set_color(102, 0, 153), receipt("FedExPurple", "RD096")])
            FedExPurple_button.grid(row=6, column=11, padx=1, pady=2)

            CarolinaPlum_button = tk.Button(page6, bg="#9B84A1", width=4, height=3,command=lambda: [set_color(155, 132, 161),receipt("CarolinaPlum", "RD097")])
            CarolinaPlum_button.grid(row=6, column=12, padx=1, pady=2)

            Kalamata_button = tk.Button(page6, bg="#705160", width=4, height=3,command=lambda: [set_color(112, 81, 96), receipt("Kalamata", "RD098")])
            Kalamata_button.grid(row=6, column=13, padx=1, pady=2)

            BlackCurrant_button = tk.Button(page6, bg="#540E32", width=4, height=3,command=lambda: [set_color(84, 14, 50), receipt("BlackCurrant", "RD099")])
            BlackCurrant_button.grid(row=7, column=0, padx=1, pady=2)

            Purple4_button = tk.Button(page6, bg="#551A8B", width=4, height=3,command=lambda: [set_color(85, 26, 139), receipt("Purple4", "RD100")])
            Purple4_button.grid(row=7, column=1, padx=1, pady=2)

            StrongPurple_button = tk.Button(page6, bg="#875692", width=4, height=3,command=lambda: [set_color(135, 86, 146), receipt("StrongPurple", "RD101")])
            StrongPurple_button.grid(row=7, column=2, padx=1, pady=2)

            PalePurple_button = tk.Button(page6, bg="#AA98A9", width=4, height=3,command=lambda: [set_color(170, 152, 169), receipt("PalePurple", "RD102")])
            PalePurple_button.grid(row=7, column=3, padx=1, pady=2)

            VividReddishPurple_button = tk.Button(page6, bg="#870074", width=4, height=3,command=lambda: [set_color(135, 0, 116),receipt("VividReddishPurple", "RD103")])
            VividReddishPurple_button.grid(row=7, column=4, padx=1, pady=2)

            MediumPurple3_button = tk.Button(page6, bg="#8968CD", width=4, height=3,command=lambda: [set_color(137, 104, 205),receipt("MediumPurple3", "RD104")])
            MediumPurple3_button.grid(row=7, column=5, padx=1, pady=2)

            MiddlePurple_button = tk.Button(page6, bg="#D982B5", width=4, height=3,command=lambda: [set_color(217, 130, 181),receipt("MiddlePurple", "RD105")])
            MiddlePurple_button.grid(row=7, column=6, padx=1, pady=2)

            Cardinal_button = tk.Button(page6, bg="#8A244E", width=4, height=3,command=lambda: [set_color(138, 36, 78), receipt("Cardinal", "RD106")])
            Cardinal_button.grid(row=7, column=7, padx=1, pady=2)

            EmbassyPurple_button = tk.Button(page6, bg="#3B343C", width=4, height=3,command=lambda: [set_color(59, 52, 60), receipt("EmbassyPurple", "RD107")])
            EmbassyPurple_button.grid(row=7, column=8, padx=1, pady=2)

            LakersPurple_button = tk.Button(page6, bg="#552582", width=4, height=3,command=lambda: [set_color(85, 37, 130), receipt("LakersPurple", "RD108")])
            LakersPurple_button.grid(row=7, column=9, padx=1, pady=2)

            AmaranthPurple_button = tk.Button(page6, bg="#AB274F", width=4, height=3,command=lambda: [set_color(171, 39, 79),receipt("AmaranthPurple", "RD109")])
            AmaranthPurple_button.grid(row=7, column=10, padx=1, pady=2)

            PurpleNavy_button = tk.Button(page6, bg="#4E5180", width=4, height=3,command=lambda: [set_color(78, 81, 128), receipt("PurpleNavy", "RD110")])
            PurpleNavy_button.grid(row=7, column=11, padx=1, pady=2)

            InsolentPurple_button = tk.Button(page6, bg="#682E3C", width=4, height=3,command=lambda: [set_color(104, 46, 60),receipt("InsolentPurple", "RD111")])
            InsolentPurple_button.grid(row=7, column=12, padx=1, pady=2)

            SmyrnaPurple_button = tk.Button(page6, bg="#A2627A", width=4, height=3,command=lambda: [set_color(162, 98, 122), receipt("SmyrnaPurple", "RD112")])
            SmyrnaPurple_button.grid(row=7, column=13, padx=1, pady=2)

            EastCarolinaUniversityPurple_button = tk.Button(page6, bg="#592A8A", width=4, height=3,command=lambda: [set_color(89, 42, 138),receipt("EastCarolinaUniversityPurple", "RD113")])
            EastCarolinaUniversityPurple_button.grid(row=8, column=0, padx=1, pady=2)

            LittlePrincess_button = tk.Button(page6, bg="#E9DCE5", width=4, height=3,command=lambda: [set_color(233, 220, 229),receipt("LittlePrincess", "RD114")])
            LittlePrincess_button.grid(row=8, column=1, padx=1, pady=2)

            AestheticPurple_button = tk.Button(page6, bg="#502380", width=4, height=3,command=lambda: [set_color(80, 35, 128),receipt("AestheticPurple", "RD115")])
            AestheticPurple_button.grid(row=8, column=2, padx=1, pady=2)

            KikyoIru_button = tk.Button(page6, bg="#5D3F6A", width=4, height=3,command=lambda: [set_color(93, 63, 106), receipt("KikyoIru", "RD116")])
            KikyoIru_button.grid(row=8, column=3, padx=1, pady=2)

            MetallicPurple_button = tk.Button(page6, bg="#520E7D", width=4, height=3,command=lambda: [set_color(82, 14, 125),receipt("MetallicPurple", "RD117")])
            MetallicPurple_button.grid(row=8, column=4, padx=1, pady=2)

            HotPurple_button = tk.Button(page6, bg="#A420D0", width=4, height=3,command=lambda: [set_color(164, 32, 208), receipt("HotPurple", "RD118")])
            HotPurple_button.grid(row=8, column=5, padx=1, pady=2)

            FadedPurple_button = tk.Button(page6, bg="#795F80", width=4, height=3,command=lambda: [set_color(121, 95, 128), receipt("FadedPurple", "RD119")])
            FadedPurple_button.grid(row=8, column=6, padx=1, pady=2)

            MythicalPurple_button = tk.Button(page6, bg="#53277E", width=4, height=3,command=lambda: [set_color(83, 39, 126),receipt("MythicalPurple", "RD120")])
            MythicalPurple_button.grid(row=8, column=7, padx=1, pady=2)

            LanguidLavender_button = tk.Button(page6, bg="#D6CADD", width=4, height=3,command=lambda: [set_color(214, 202, 221),receipt("LanguidLavender", "RD121")])
            LanguidLavender_button.grid(row=8, column=8, padx=1, pady=2)

            Mauveine_button = tk.Button(page6, bg="#8D029B", width=4, height=3,command=lambda: [set_color(141, 2, 155), receipt("Mauveine", "RD122")])
            Mauveine_button.grid(row=8, column=9, padx=1, pady=2)

            BlueLilac_button = tk.Button(page6, bg="#7B679A", width=4, height=3,command=lambda: [set_color(123, 103, 154), receipt("BlueLilac", "RD123")])
            BlueLilac_button.grid(row=8, column=10, padx=1, pady=2)

            DarkByzantium_button = tk.Button(page6, bg="#5D3954", width=4, height=3,command=lambda: [set_color(93, 57, 84), receipt("DarkByzantium", "RD124")])
            DarkByzantium_button.grid(row=8, column=11, padx=1, pady=2)

            LuxuryPurple_button = tk.Button(page6, bg="#743089", width=4, height=3,command=lambda: [set_color(116, 48, 137), receipt("LuxuryPurple", "RD125")])
            LuxuryPurple_button.grid(row=8, column=12, padx=1, pady=2)

            AztechPurple_button = tk.Button(page6, bg="#893BFF", width=4, height=3,command=lambda: [set_color(137, 59, 255), receipt("AztechPurple", "RD126")])
            AztechPurple_button.grid(row=8, column=13, padx=1, pady=2)

            BaltimoreRavensPurple_button = tk.Button(page6, bg="#280353", width=4, height=3,command=lambda: [set_color(40, 3, 83),receipt("BaltimoreRavensPurple", "RD127")])
            BaltimoreRavensPurple_button.grid(row=9, column=0, padx=1, pady=2)

            DeepMagenta_button = tk.Button(page6, bg="#CC00CC", width=4, height=3,command=lambda: [set_color(204, 0, 204), receipt("DeepMagenta", "RD128")])
            DeepMagenta_button.grid(row=9, column=1, padx=1, pady=2)

            DeepPurple_button = tk.Button(page6, bg="#524F81", width=4, height=3,command=lambda: [set_color(82, 79, 129), receipt("DeepPurple", "RD129")])
            DeepPurple_button.grid(row=9, column=2, padx=1, pady=2)

            RusticPurple_button = tk.Button(page6, bg="#593163", width=4, height=3,command=lambda: [set_color(89, 49, 99), receipt("RusticPurple", "RD130")])
            RusticPurple_button.grid(row=9, column=3, padx=1, pady=2)

            SunsetPurple_button = tk.Button(page6, bg="#A865B5", width=4, height=3,command=lambda: [set_color(168, 101, 181),receipt("SunsetPurple", "RD131")])
            SunsetPurple_button.grid(row=9, column=4, padx=1, pady=2)

            ArtistsPurple_button = tk.Button(page6, bg="#C71585", width=4, height=3,command=lambda: [set_color(199, 21, 133),receipt("ArtistsPurple", "RD132")])
            ArtistsPurple_button.grid(row=9, column=5, padx=1, pady=2)

            DullPurple_button = tk.Button(page6, bg="#9861A5", width=4, height=3,command=lambda: [set_color(152, 97, 165), receipt("DullPurple", "RD133")])
            DullPurple_button.grid(row=9, column=6, padx=1, pady=2)

            TrafficPurple_button = tk.Button(page6, bg="#913073", width=4, height=3,command=lambda: [set_color(145, 48, 115),receipt("TrafficPurple", "RD134")])
            TrafficPurple_button.grid(row=9, column=7, padx=1, pady=2)

            MattePurple_button = tk.Button(page6, bg="#392A48", width=4, height=3,command=lambda: [set_color(57, 42, 72), receipt("MattePurple", "RD135")])
            MattePurple_button.grid(row=9, column=8, padx=1, pady=2)

            PurpleViolet_button = tk.Button(page6, bg="#47243C", width=4, height=3,command=lambda: [set_color(71, 36, 60), receipt("PurpleViolet", "RD136")])
            PurpleViolet_button.grid(row=9, column=9, padx=1, pady=2)

            PurpleCMYK_button = tk.Button(page6, bg="#6A317F", width=4, height=3,command=lambda: [set_color(106, 49, 127), receipt("PurpleCMYK", "RD137")])
            PurpleCMYK_button.grid(row=9, column=10, padx=1, pady=2)

            OceanPurple_button = tk.Button(page6, bg="#6E2D91", width=4, height=3,command=lambda: [set_color(110, 45, 145), receipt("OceanPurple", "RD138")])
            OceanPurple_button.grid(row=9, column=11, padx=1, pady=2)

            ShinyPurple_button = tk.Button(page6, bg="#B941FF", width=4, height=3,command=lambda: [set_color(185, 65, 255), receipt("ShinyPurple", "RD139")])
            ShinyPurple_button.grid(row=9, column=12, padx=1, pady=2)

            AutumnPurple_button = tk.Button(page6, bg="#834468", width=4, height=3,command=lambda: [set_color(131, 68, 104), receipt("AutumnPurple", "RD140")])
            AutumnPurple_button.grid(row=9, column=13, padx=1, pady=2)

            # BlueSeries
            turquoise_button = tk.Button(page5, bg="#40E0D0", width=4, height=3, command=lambda: [set_color(64, 224, 208),receipt("turqoise","BL001")])
            turquoise_button.grid(row=0, column=0, padx=1, pady=2)
            celeste_button = tk.Button(page5, bg="#B2FFFF", width=4, height=3, command=lambda: [set_color(178, 255, 255),receipt("celeste","BL002")])
            celeste_button.grid(row=0, column=1, padx=1, pady=2)
            lightTurquoise_button = tk.Button(page5, bg="#AFEEEE", width=4, height=3, command=lambda: [set_color(175, 238, 238),receipt("lightTurquoise","BL003")])
            lightTurquoise_button.grid(row=0, column=2, padx=1, pady=2)
            turquoiseBlue_button = tk.Button(page5, bg="#00FFEF", width=4, height=3, command=lambda: [set_color( 0, 255, 239),receipt("turquoiseBlue","BL004")])
            turquoiseBlue_button.grid(row=0, column=3, padx=1, pady=2)
            MediumTurquoise_button = tk.Button(page5, bg="#48D1CC", width=4, height=3, command=lambda: [set_color(72, 209, 204),receipt("MediumTurquoise","BL005")])
            MediumTurquoise_button.grid(row=0, column=4, padx=1, pady=2)
            DarkTurquoise_button = tk.Button(page5, bg="#00CED1", width=4, height=3, command=lambda: [set_color(0, 206, 209),receipt("DarkTurquoise","BL006")])
            DarkTurquoise_button.grid(row=0, column=5, padx=1, pady=2)
            BrightTurquoise_button = tk.Button(page5, bg="#08E8DE", width=4, height=3, command=lambda: [set_color(8, 232, 222),receipt("BrightTurquoise","BL007")])
            BrightTurquoise_button.grid(row=0, column=6, padx=1, pady=2)
            powderBlue_button = tk.Button(page5, bg="#B0E0E6", width=4, height=3, command=lambda: [set_color(176, 224, 230),receipt("powderBlue","BL008")])
            powderBlue_button.grid(row=0, column=7, padx=1, pady=2)
            SkyBlue_button = tk.Button(page5, bg="#ADD8E6", width=4, height=3, command=lambda: [set_color(173, 216, 230),receipt("SkyBlue","BL009")])
            SkyBlue_button.grid(row=0, column=8, padx=1, pady=2)
            ElectricBlue_button = tk.Button(page5, bg="#7DF9FF", width=4, height=3, command=lambda: [set_color(125, 249, 255),receipt("ElectricBlue","BL010")])
            ElectricBlue_button.grid(row=0, column=9, padx=1, pady=2)
            AirForceBlueRAF_button = tk.Button(page5, bg="#5D8AA8", width=4, height=3, command=lambda: [set_color(93, 138, 168),receipt("AirForceBlueRAF","BL011")])
            AirForceBlueRAF_button.grid(row=0, column=10, padx=1, pady=2)
            AirForceBlueUSAF_button = tk.Button(page5, bg="#00308F", width=4, height=3, command=lambda: [set_color(0, 48, 143),receipt("AirForceBlueUSAF","BL012")])
            AirForceBlueUSAF_button.grid(row=0, column=11, padx=1, pady=2)
            USAirForceAcademyBlue_button = tk.Button(page5, bg="#004F98", width=4, height=3, command=lambda: [set_color(0, 79, 152),receipt("USAirForceAcademyBlue","BL013")])
            USAirForceAcademyBlue_button.grid(row=0, column=12, padx=1, pady=2)
            BeauBlue_button = tk.Button(page5, bg="#BCD4E6", width=4, height=3, command=lambda: [set_color(188, 212, 230),receipt("BeauBlue","BL014")])
            BeauBlue_button.grid(row=0, column=13, padx=1, pady=2)
            BabyBlue_button = tk.Button(page5, bg="#89CFF0", width=4, height=3, command=lambda: [set_color(137, 207, 240),receipt("BabyBlue","BL015")])
            BabyBlue_button.grid(row=1, column=0, padx=1, pady=2)
            BabyBlueEyes_button = tk.Button(page5, bg="#A1CAF1", width=4, height=3, command=lambda: [set_color(161, 202, 241),receipt("BabyBlueEyes","BL016")])
            BabyBlueEyes_button.grid(row=1, column=1, padx=1, pady=2)
            LittleBoyBlue_button = tk.Button(page5, bg="#6CA0DC", width=4, height=3, command=lambda: [set_color(108, 160, 220),receipt("LittleBoyBlue","BL017")])
            LittleBoyBlue_button.grid(row=1, column=2, padx=1, pady=2)
            TiffanyBlue_button = tk.Button(page5, bg="#81D8D0", width=4, height=3, command=lambda: [set_color(129, 216, 208),receipt("TiffanyBlue","BL018")])
            TiffanyBlue_button.grid(row=1, column=3, padx=1, pady=2)
            SteelBlue_button = tk.Button(page5, bg="#4682B4", width=4, height=3, command=lambda: [set_color(70, 130, 180),receipt("SteelBlue","BL019")])
            SteelBlue_button.grid(row=1, column=4, padx=1, pady=2)
            CarolinaBlue_button = tk.Button(page5, bg="#4B9CD3", width=4, height=3, command=lambda: [set_color(75, 156, 211),receipt("CarolinaBlue","BL020")])
            CarolinaBlue_button.grid(row=1, column=5, padx=1, pady=2)
            TurkishBlue_button = tk.Button(page5, bg="#4F97A3", width=4, height=3, command=lambda: [set_color(79, 151, 163),receipt("TurkishBlue","BL021")])
            TurkishBlue_button.grid(row=1, column=6, padx=1, pady=2)
            MayaBlue_button = tk.Button(page5, bg="#73C2FB", width=4, height=3, command=lambda: [set_color(115, 194, 251),receipt("MayaBlue","BL022")])
            MayaBlue_button.grid(row=1, column=7, padx=1, pady=2)
            Teal_button = tk.Button(page5, bg="#008080", width=4, height=3, command=lambda: [set_color(0, 128, 128),receipt("Teal","BL023")])
            Teal_button.grid(row=1, column=8, padx=1, pady=2)
            IndependenceBlue_button = tk.Button(page5, bg="#4C516D", width=4, height=3, command=lambda: [set_color(76, 81, 109),receipt("IndependenceBlue","BL024")])
            IndependenceBlue_button.grid(row=1, column=9, padx=1, pady=2)
            CornflowerBlue_button = tk.Button(page5, bg="#6495ED", width=4, height=3, command=lambda: [set_color(100, 149, 237),receipt("CornflowerBlue","BL025")])
            CornflowerBlue_button.grid(row=1, column=10, padx=1, pady=2)
            SapphireBlue_button = tk.Button(page5, bg="#0F52BA", width=4, height=3, command=lambda: [set_color(15, 82, 186),receipt("SapphireBlue","BL026")])
            SapphireBlue_button.grid(row=1, column=11, padx=1, pady=2)
            MediumSapphire_button = tk.Button(page5, bg="#2D5DA1", width=4, height=3, command=lambda: [set_color(45, 93, 161),receipt("MediumSapphire","BL027")])
            MediumSapphire_button.grid(row=1, column=12, padx=1, pady=2)
            BdazzledBlue_button = tk.Button(page5, bg="#2E5894", width=4, height=3, command=lambda: [set_color(46, 88, 148),receipt("BdazzledBlue","BL028")])
            BdazzledBlue_button.grid(row=1, column=13, padx=1, pady=2)
            BlueSapphire_button = tk.Button(page5, bg="#126180", width=4, height=3, command=lambda: [set_color(18, 97, 128),receipt("BlueSapphire","BL029")])
            BlueSapphire_button.grid(row=2, column=0, padx=1, pady=2)
            DarkSapphire_button = tk.Button(page5, bg="#082567", width=4, height=3, command=lambda: [set_color(8, 37, 103),receipt("DarkSapphire","BL030")])
            DarkSapphire_button.grid(row=2, column=1, padx=1, pady=2)
            Azure_button = tk.Button(page5, bg="#007FFF", width=4, height=3, command=lambda: [set_color(0, 127, 255),receipt("Azure","BL031")])
            Azure_button.grid(row=2, column=2, padx=1, pady=2)
            EgyptianBlue_button = tk.Button(page5, bg="#1034A6", width=4, height=3, command=lambda: [set_color(16, 52, 166),receipt("EgyptianBlue","BL032")])
            EgyptianBlue_button.grid(row=2, column=3, padx=1, pady=2)
            YaleBlue_button = tk.Button(page5, bg="#00356B", width=4, height=3, command=lambda: [set_color(0, 53, 107),receipt("YaleBlue","BL033")])
            YaleBlue_button.grid(row=2, column=4, padx=1, pady=2)
            NavyBlue_button = tk.Button(page5, bg="#000080", width=4, height=3, command=lambda: [set_color(0, 0, 128),receipt("NavyBlue","BL034")])
            NavyBlue_button.grid(row=2, column=5, padx=1, pady=2)
            PrussianBlue_button = tk.Button(page5, bg="#003153", width=4, height=3, command=lambda: [set_color(0, 49, 83),receipt("PrussianBlue","BL035")])
            PrussianBlue_button.grid(row=2, column=6, padx=1, pady=2)
            SpaceCadet_button = tk.Button(page5, bg="#1D2951", width=4, height=3, command=lambda: [set_color(29, 41, 81),receipt("SpaceCadet","BL036")])
            SpaceCadet_button.grid(row=2, column=7, padx=1, pady=2)
            TraditionalRoyalBlue_button = tk.Button(page5, bg="#002366", width=4, height=3, command=lambda: [set_color(0, 35, 102),receipt("TraditionalRoyalBlue","BL037")])
            TraditionalRoyalBlue_button.grid(row=2, column=8, padx=1, pady=2)
            QueenBlue_button = tk.Button(page5, bg="#436B95", width=4, height=3, command=lambda: [set_color(67, 107, 149),receipt("QueenBlue","BL038")])
            QueenBlue_button.grid(row=2, column=9, padx=1, pady=2)
            ImperialBlue_button = tk.Button(page5, bg="#005A92", width=4, height=3, command=lambda: [set_color(0, 90, 146),receipt("ImperialBlue","BL039")])
            ImperialBlue_button.grid(row=2, column=10, padx=1, pady=2)
            Periwinkle_button = tk.Button(page5, bg="#CCCCFF", width=4, height=3, command=lambda: [set_color(204, 204, 255),receipt("Periwinkle","BL040")])
            Periwinkle_button.grid(row=2, column=11, padx=1, pady=2)
            MorningBlue_button = tk.Button(page5, bg="#8DA399", width=4, height=3, command=lambda: [set_color(141, 163, 153),receipt("MorningBlue","BL041")])
            MorningBlue_button.grid(row=2, column=12, padx=1, pady=2)
            UranianBlue_button = tk.Button(page5, bg="#AFDBF5", width=4, height=3, command=lambda: [set_color(175,219, 245),receipt("UranianBlue","BL042")])
            UranianBlue_button.grid(row=2, column=13, padx=1, pady=2)
            FluorescentBlue_button = tk.Button(page5, bg="#15F4EE", width=4, height=3, command=lambda: [set_color(21, 244, 238),receipt("FluorescentBlue","BL043")])
            FluorescentBlue_button.grid(row=3, column=0, padx=1, pady=2)
            RuddyBlue_button = tk.Button(page5, bg="#76ABDF", width=4, height=3, command=lambda: [set_color(118, 171, 223),receipt("RuddyBlue","BL044")])
            RuddyBlue_button.grid(row=3, column=1, padx=1, pady=2)
            AdmiralBlue_button = tk.Button(page5, bg="#2C3863", width=4, height=3, command=lambda: [set_color(44, 56, 99),receipt("AdmiralBlue","BL045")])
            AdmiralBlue_button.grid(row=3, column=2, padx=1, pady=2)
            AegeanBlue_button = tk.Button(page5, bg="#4E6E81", width=4, height=3, command=lambda: [set_color(78, 110, 129),receipt("AegeanBlue","BL046")])
            AegeanBlue_button.grid(row=3, column=3, padx=1, pady=2)
            AeroBlue_button = tk.Button(page5, bg="#C9FFE5", width=4, height=3, command=lambda: [set_color(201, 255, 229),receipt("AeroBlue","BL047")])
            AeroBlue_button.grid(row=3, column=4, padx=1, pady=2)
            AirSuperiorityBlue_button = tk.Button(page5, bg="#72A0C1", width=4, height=3, command=lambda: [set_color(114, 160, 193),receipt("AirSuperiorityBlue","BL048")])
            AirSuperiorityBlue_button.grid(row=3, column=5, padx=1, pady=2)
            AliceBlue_button = tk.Button(page5, bg="#F0F8FF", width=4, height=3, command=lambda: [set_color(240, 248, 255),receipt("AliceBlue","BL049")])
            AliceBlue_button.grid(row=3, column=6, padx=1, pady=2)
            AquaBlue_button = tk.Button(page5, bg="#0AFFFF", width=4, height=3, command=lambda: [set_color(10, 255, 255),receipt("AquaBlue","BL050")])
            AquaBlue_button.grid(row=3, column=7, padx=1, pady=2)
            AquamarineBlue_button = tk.Button(page5, bg="#6BCAE2", width=4, height=3, command=lambda: [set_color(107, 202, 226),receipt("AquamarineBlue","BL051")])
            AquamarineBlue_button.grid(row=3, column=8, padx=1, pady=2)
            ArcticBlue_button = tk.Button(page5, bg="#C6E6FB", width=4, height=3, command=lambda: [set_color(198, 230, 251),receipt("ArcticBlue","BL052")])
            ArcticBlue_button.grid(row=3, column=9, padx=1, pady=2)
            ArgentinaBlue_button = tk.Button(page5, bg="#6CB4EE", width=4, height=3, command=lambda: [set_color(108, 180, 238),receipt("ArgentinaBlue","BL052")])
            ArgentinaBlue_button.grid(row=3, column=10, padx=1, pady=2)
            AstroNavy_button = tk.Button(page5, bg="#002D62", width=4, height=3, command=lambda: [set_color(0, 45, 98),receipt("AstroNavy","BL054")])
            AstroNavy_button.grid(row=3, column=11, padx=1, pady=2)
            BayernBlue_button = tk.Button(page5, bg="#0066B2", width=4, height=3, command=lambda: [set_color(0, 102, 178),receipt("BayernBlue","BL0255")])
            BayernBlue_button.grid(row=3, column=12, padx=1, pady=2)
            BerryBlue_button = tk.Button(page5, bg="#4F86F7", width=4, height=3, command=lambda: [set_color(79, 134, 247),receipt("BerryBlue","BL056")])
            BerryBlue_button.grid(row=3, column=13, padx=1, pady=2)
            Blue_button = tk.Button(page5, bg="#0000FF", width=4, height=3, command=lambda: [set_color(0, 0, 255),receipt("Blue","BL057")])
            Blue_button.grid(row=4, column=0, padx=1, pady=2)
            BlueYonder_button = tk.Button(page5, bg="#5072A7", width=4, height=3, command=lambda: [set_color(80, 114, 167),receipt("BlueYonder","BL058")])
            BlueYonder_button.grid(row=4, column=1, padx=1, pady=2)
            BleudeFranceBlue_button = tk.Button(page5, bg="#318CE7", width=4, height=3, command=lambda: [set_color(49, 140, 231),receipt("BleudeFranceBlue","BL059")])
            BleudeFranceBlue_button.grid(row=4, column=2, padx=1, pady=2)
            BlueGray_button = tk.Button(page5, bg="#6699CC", width=4, height=3, command=lambda: [set_color(102, 153, 204),receipt("BlueGray","BL060")])
            BlueGray_button.grid(row=4, column=3, padx=1, pady=2)
            BoeingBlue_button = tk.Button(page5, bg="#0039A6", width=4, height=3, command=lambda: [set_color(0, 57, 166),receipt("BoeingBlue","BL061")])
            BoeingBlue_button.grid(row=4, column=4, padx=1, pady=2)
            BravesNavy_button = tk.Button(page5, bg="#13274F", width=4, height=3, command=lambda: [set_color(19, 39, 79),receipt("BravesNavy","BL062")])
            BravesNavy_button.grid(row=4, column=5, padx=1, pady=2)
            BrewersBlue_button = tk.Button(page5, bg="#0A2351", width=4, height=3, command=lambda: [set_color(10, 35, 81),receipt("BrewersBlue","BL063")])
            BrewersBlue_button.grid(row=4, column=6, padx=1, pady=2)
            BroncosBlue_button = tk.Button(page5, bg="#002244", width=4, height=3, command=lambda: [set_color(0, 34, 68),receipt("BroncosBlue","BL064")])
            BroncosBlue_button.grid(row=4, column=7, padx=1, pady=2)
            ByzantineBlue_button = tk.Button(page5, bg="#3457D5", width=4, height=3, command=lambda: [set_color(52, 87, 213),receipt("ByzantineBlue","BL065")])
            ByzantineBlue_button.grid(row=4, column=8, padx=1, pady=2)
            CambridgeBlue_button = tk.Button(page5, bg="#A3C1AD", width=4, height=3, command=lambda: [set_color(163, 193, 173),receipt("CambridgeBlue","BL066")])
            CambridgeBlue_button.grid(row=4, column=9, padx=1, pady=2)
            CapriBlue_button = tk.Button(page5, bg="#00BFFF", width=4, height=3, command=lambda: [set_color(0, 191, 255),receipt("CapriBlue","BL067")])
            CapriBlue_button.grid(row=4, column=10, padx=1, pady=2)
            CeruleanBlue_button = tk.Button(page5, bg="#2A52BE", width=4, height=3, command=lambda: [set_color(42, 82, 190),receipt("CeruleanBlue","BL068")])
            CeruleanBlue_button.grid(row=4, column=11, padx=1, pady=2)
            ChelseaBlue_button = tk.Button(page5, bg="#034694", width=4, height=3, command=lambda: [set_color(3, 70, 148 ),receipt("ChelseaBlue","BL069")])
            ChelseaBlue_button.grid(row=4, column=12, padx=1, pady=2)
            ChlorineBlue_button = tk.Button(page5, bg="#0CAFFF", width=4, height=3, command=lambda: [set_color( 12, 175, 255),receipt("ChlorineBlue","BL070")])
            ChlorineBlue_button.grid(row=4, column=13, padx=1, pady=2)
            CobaltBlue_button = tk.Button(page5, bg="#0047AB", width=4, height=3, command=lambda: [set_color(0, 71, 171),receipt("CobaltBlue","BL071")])
            CobaltBlue_button.grid(row=5, column=0, padx=1, pady=2)
            CollegeNavy_button = tk.Button(page5, bg="#002244", width=4, height=3, command=lambda: [set_color(0, 34, 68),receipt("CollegeNavy","BL072")])
            CollegeNavy_button.grid(row=5, column=1, padx=1, pady=2)
            ColumbiaBlue_button = tk.Button(page5, bg="#B9D9EB", width=4, height=3, command=lambda: [set_color(185, 217, 235),receipt("ColumbiaBlue","BL073")])
            ColumbiaBlue_button.grid(row=5, column=2, padx=1, pady=2)
            CrayolaBlue_button = tk.Button(page5, bg="#1F75FE", width=4, height=3, command=lambda: [set_color(31, 117, 254),receipt("CrayolaBlue","BL074")])
            CrayolaBlue_button.grid(row=5, column=3, padx=1, pady=2)
            CyanBlue_button = tk.Button(page5, bg="#00FFFF", width=4, height=3, command=lambda: [set_color(0, 255, 255),receipt("CyanBlue","BL075")])
            CyanBlue_button.grid(row=5, column=4, padx=1, pady=2)
            DallasCowboysBlue_button = tk.Button(page5, bg="#041E42", width=4, height=3, command=lambda: [set_color(4, 30, 66),receipt("DallasCowboysBlue","BL076")])
            DallasCowboysBlue_button.grid(row=5, column=5, padx=1, pady=2)
            DarkBlue_button = tk.Button(page5, bg="#00008B", width=4, height=3, command=lambda: [set_color(0, 0, 139),receipt("DarkBlue","BL077")])
            DarkBlue_button.grid(row=5, column=6, padx=1, pady=2)
            DelftBlue_button = tk.Button(page5, bg="#1F305E", width=4, height=3, command=lambda: [set_color(31, 48, 94),receipt("DelftBlue","BL078")])
            DelftBlue_button.grid(row=5, column=7, padx=1, pady=2)
            DellBlue_button = tk.Button(page5, bg="#0076CE", width=4, height=3, command=lambda: [set_color(0, 118, 206),receipt("DellBlue","BL079")])
            DellBlue_button.grid(row=5, column=8, padx=1, pady=2)
            DenimBlue_button = tk.Button(page5, bg="#1560BD", width=4, height=3, command=lambda: [set_color(21, 96, 189),receipt("DenimBlue","BL080")])
            DenimBlue_button.grid(row=5, column=9, padx=1, pady=2)
            DodgersBlue_button = tk.Button(page5, bg="#005A9C", width=4, height=3, command=lambda: [set_color(0, 90, 156),receipt("DodgersBlue","BL081")])
            DodgersBlue_button.grid(row=5, column=10, padx=1, pady=2)
            DolphinsAqua_button = tk.Button(page5, bg="#008E97", width=4, height=3, command=lambda: [set_color(0, 142, 151),receipt("DolphinsAqua","BL082")])
            DolphinsAqua_button.grid(row=5, column=11, padx=1, pady=2)
            DuckBlue_button = tk.Button(page5, bg="#007791", width=4, height=3, command=lambda: [set_color(0, 119, 145),receipt("DuckBlue","BL083")])
            DuckBlue_button.grid(row=5, column=12, padx=1, pady=2)
            DukeBlue_button = tk.Button(page5, bg="#012169", width=4, height=3, command=lambda: [set_color(1, 33, 105),receipt("DukeBlue","BL084")])
            DukeBlue_button.grid(row=5, column=13, padx=1, pady=2)
            ElectricIndigo_button = tk.Button(page5, bg="#6F00FF", width=4, height=3, command=lambda:[set_color(111, 0, 255),receipt("ElectricIndigo","BL085")])
            ElectricIndigo_button.grid(row=6, column=0, padx=1, pady=2)
            EvertonBlue_button = tk.Button(page5, bg="#003399", width=4, height=3, command=lambda: [set_color(0, 51, 153),receipt("EvertonBlue","BL086")])
            EvertonBlue_button.grid(row=6, column=1, padx=1, pady=2)
            FacebookBlue_button = tk.Button(page5, bg="#1877F2", width=4, height=3, command=lambda: [set_color(24, 119, 242),receipt("FacebookBlue","BL087")])
            FacebookBlue_button.grid(row=6, column=2, padx=1, pady=2)
            FordBlue_button = tk.Button(page5, bg="#2C3968", width=4, height=3, command=lambda: [set_color(44, 57, 104),receipt("FordBlue","BL088")])
            FordBlue_button.grid(row=6, column=3, padx=1, pady=2)
            GeneralMotorsBlue_button = tk.Button(page5, bg="#073980", width=4, height=3, command=lambda: [set_color(7, 57, 128),receipt("GeneralMotorsBlue","BL089")])
            GeneralMotorsBlue_button.grid(row=6, column=4, padx=1, pady=2)
            GlaucousBlue_button = tk.Button(page5, bg="#6082B6", width=4, height=3, command=lambda: [set_color(96, 130, 182),receipt("GlaucousBlue","BL090")])
            GlaucousBlue_button.grid(row=6, column=5, padx=1, pady=2)
            IBMBlue_button = tk.Button(page5, bg="#0530AD", width=4, height=3, command=lambda: [set_color( 5, 48, 173),receipt("IBMBlue","BL091")])
            IBMBlue_button.grid(row=6, column=6, padx=1, pady=2)
            IceBlue_button = tk.Button(page5, bg="#99FFFF", width=4, height=3, command=lambda: [set_color(153, 255, 255),receipt("IceBlue","BL092")])
            IceBlue_button.grid(row=6, column=7, padx=1, pady=2)
            IndigoBlue_button = tk.Button(page5, bg="#3F00FF", width=4, height=3, command=lambda: [set_color(63, 0, 255),receipt("IndigoBlue","BL093")])
            IndigoBlue_button.grid(row=6, column=8, padx=1, pady=2)
            IndigoDyeBlue_button = tk.Button(page5, bg="#00416A", width=4, height=3, command=lambda: [set_color(0, 65, 106),receipt("IndigoDyeBlue","BL094")])
            IndigoDyeBlue_button.grid(row=6, column=9, padx=1, pady=2)
            IntelBlue_button = tk.Button(page5, bg="#0071C5", width=4, height=3, command=lambda: [set_color(0, 113, 197),receipt("IntelBlue","BL095")])
            IntelBlue_button.grid(row=6, column=10, padx=1, pady=2)
            InternationalKleinBlue_button = tk.Button(page5, bg="#002FA7", width=4, height=3, command=lambda: [set_color(0, 47, 167),receipt("InternationalKleinBlue","BL096")])
            InternationalKleinBlue_button.grid(row=6, column=11, padx=1, pady=2)
            IrisBlue_button = tk.Button(page5, bg="#5A4FCF", width=4, height=3, command=lambda: [set_color(90, 79, 207),receipt("IrisBlue","BL097")])
            IrisBlue_button.grid(row=6, column=12, padx=1, pady=2)
            KCRoyalsBlue_button = tk.Button(page5, bg="#004687", width=4, height=3, command=lambda: [set_color(0, 70, 135),receipt("KCRoyalsBlue","BL098")])
            KCRoyalsBlue_button.grid(row=6, column=13, padx=1, pady=2)
            LapisBlue_button = tk.Button(page5, bg="#26619C", width=4, height=3, command=lambda: [set_color(38, 97, 156),receipt("LapisBlue","BL099")])
            LapisBlue_button.grid(row=7, column=0, padx=1, pady=2)
            LibertyBlue_button = tk.Button(page5, bg="#545AA7", width=4, height=3, command=lambda: [set_color(84, 90, 167),receipt("LibertyBlue","BL100")])
            LibertyBlue_button.grid(row=7, column=1, padx=1, pady=2)
            LowesBlue_button = tk.Button(page5, bg="#004792", width=4, height=3, command=lambda: [set_color(0, 71, 146),receipt("LowesBlue","BL101")])
            LowesBlue_button.grid(row=7, column=2, padx=1, pady=2)
            MagicBlue_button = tk.Button(page5, bg="#0077C0", width=4, height=3, command=lambda: [set_color( 0, 119, 192),receipt("MagicBlue","BL102")])
            MagicBlue_button.grid(row=7, column=3, padx=1, pady=2)
            MajorelleBlue_button = tk.Button(page5, bg="#6050DC", width=4, height=3, command=lambda: [set_color(96, 80, 220),receipt("MajorelleBlue","BL103")])
            MajorelleBlue_button.grid(row=7, column=4, padx=1, pady=2)
            MarianBlue_button = tk.Button(page5, bg="#E1EBEE", width=4, height=3, command=lambda: [set_color(225, 235, 238),receipt("MarianBlue","BL104")])
            MarianBlue_button.grid(row=7, column=5, padx=1, pady=2)
            MavericksBlue_button = tk.Button(page5, bg="#00538C", width=4, height=3, command=lambda: [set_color(0, 83, 140),receipt("MavericksBlue","BL105")])
            MavericksBlue_button.grid(row=7, column=6, padx=1, pady=2)
            MediumBlue_button = tk.Button(page5, bg="#0000CD", width=4, height=3, command=lambda: [set_color(0, 0, 205),receipt("MediumBlue","BL106")])
            MediumBlue_button.grid(row=7, column=7, padx=1, pady=2)
            MediumSlateBlue_button = tk.Button(page5, bg="#7B68EE", width=4, height=3, command=lambda: [set_color(123, 104, 238),receipt("MediumSlateBlue","BL107")])
            MediumSlateBlue_button.grid(row=7, column=8, padx=1, pady=2)
            MillenniumBlue_button = tk.Button(page5, bg="#002244", width=4, height=3, command=lambda: [set_color(0, 34, 68),receipt("MillenniumBlue","BL108")])
            MillenniumBlue_button.grid(row=7, column=9, padx=1, pady=2)
            MunsellBlue_button = tk.Button(page5, bg="#0093AF", width=4, height=3, command=lambda: [set_color(0, 147, 175),receipt("MunsellBlue","BL109")])
            MunsellBlue_button.grid(row=7, column=10, padx=1, pady=2)
            NeonBlue_button = tk.Button(page5, bg="#4D4DFF", width=4, height=3, command=lambda: [set_color(77, 77, 255),receipt("NeonBlue","BL110")])
            NeonBlue_button.grid(row=7, column=11, padx=1, pady=2)
            NonPhotoBlue_button = tk.Button(page5, bg="#A4DDED", width=4, height=3, command=lambda: [set_color(164, 221, 237),receipt("NonPhotoBlue","BL111")])
            NonPhotoBlue_button.grid(row=7, column=12, padx=1, pady=2)
            OceanBlue_button = tk.Button(page5, bg="#009DC4", width=4, height=3, command=lambda: [set_color(0, 157, 196),receipt("OceanBlue","BL112")])
            OceanBlue_button.grid(row=7, column=13, padx=1, pady=2)
            OxfordBlue_button = tk.Button(page5, bg="#002147", width=4, height=3, command=lambda: [set_color(0, 33, 71),receipt("OxfordBlue","BL113")])
            OxfordBlue_button.grid(row=8, column=0, padx=1, pady=2)
            PSGBlue_button = tk.Button(page5, bg="#004170", width=4, height=3, command=lambda: [set_color(0, 65, 112),receipt("PSGBlue","BL114")])
            PSGBlue_button.grid(row=8, column=1, padx=1, pady=2)
            PacificBlue_button = tk.Button(page5, bg="#1CA9C9", width=4, height=3, command=lambda: [set_color(28, 169, 201),receipt("PacificBlue","BL115")])
            PacificBlue_button.grid(row=8, column=2, padx=1, pady=2)
            PantoneBlue_button = tk.Button(page5, bg="#0018A8", width=4, height=3, command=lambda: [set_color(0, 24, 168),receipt("PantoneBlue","BL116")])
            PantoneBlue_button.grid(row=8, column=3, padx=1, pady=2)
            PeacockBlue_button = tk.Button(page5, bg="#005F69", width=4, height=3, command=lambda: [set_color(0, 95, 105),receipt("PeacockBlue","BL117")])
            PeacockBlue_button.grid(row=8, column=4, padx=1, pady=2)
            PennBlue_button = tk.Button(page5, bg="#011F5B", width=4, height=3, command=lambda: [set_color(1, 31, 91),receipt("PennBlue","BL118")])
            PennBlue_button.grid(row=8, column=5, padx=1, pady=2)
            PersianBlue_button = tk.Button(page5, bg="#1C39BB", width=4, height=3, command=lambda: [set_color(28, 57, 187),receipt("PersianBlue","BL119")])
            PersianBlue_button.grid(row=8, column=6, padx=1, pady=2)
            PhthaloBlue_button = tk.Button(page5, bg="#000F89", width=4, height=3, command=lambda: [set_color(0, 15, 137),receipt("PhthaloBlue","BL120")])
            PhthaloBlue_button.grid(row=8, column=7, padx=1, pady=2)
            PicoteeBlue_button = tk.Button(page5, bg="#2E2787", width=4, height=3, command=lambda: [set_color(46, 39, 135),receipt("PicoteeBlue","BL121")])
            PicoteeBlue_button.grid(row=8, column=8, padx=1, pady=2)
            PolynesianBlue_button = tk.Button(page5, bg="#224C98", width=4, height=3, command=lambda: [set_color(34, 76, 152),receipt("PolynesianBlue","BL122")])
            PolynesianBlue_button.grid(row=8, column=9, padx=1, pady=2)
            ResolutionBlue_button = tk.Button(page5, bg="#002387", width=4, height=3, command=lambda: [set_color(0, 35, 135),receipt("ResolutionBlue","BL123")])
            ResolutionBlue_button.grid(row=8, column=10, padx=1, pady=2)
            RobinEggBlue_button = tk.Button(page5, bg="#00CCCC", width=4, height=3, command=lambda: [set_color(0, 204, 204),receipt("RobinEggBlue","BL124")])
            RobinEggBlue_button.grid(row=8, column=11, padx=1, pady=2)
            SavoyBlue_button = tk.Button(page5, bg="#4B61D1", width=4, height=3, command=lambda: [set_color(75, 97, 209),receipt("SavoyBlue","BL125")])
            SavoyBlue_button.grid(row=8, column=12, padx=1, pady=2)
            SlateBlue_button = tk.Button(page5, bg="#6A5ACD", width=4, height=3, command=lambda: [set_color(106, 90, 205),receipt("SlateBlue","BL126")])
            SlateBlue_button.grid(row=8, column=13, padx=1, pady=2)
            SpanishBlue_button = tk.Button(page5, bg="#0070BB", width=4, height=3, command=lambda: [set_color(0, 112, 187),receipt("SpanishBlue","BL127")])
            SpanishBlue_button.grid(row=9, column=0, padx=1, pady=2)
            SpruceBlue_button = tk.Button(page5, bg="#617178", width=4, height=3, command=lambda: [set_color(97, 113, 120),receipt("SpruceBlue","BL128")])
            SpruceBlue_button.grid(row=9, column=1, padx=1, pady=2)
            StoneBlue_button = tk.Button(page5, bg="#819EA8", width=4, height=3, command=lambda: [set_color(129, 158, 168),receipt("StoneBlue","BL129")])
            StoneBlue_button.grid(row=9, column=2, padx=1, pady=2)
            TottenhamNavy_button = tk.Button(page5, bg="#132257", width=4, height=3, command=lambda: [set_color(19, 34, 87),receipt("TottenhamNavy","BL130")])
            TottenhamNavy_button.grid(row=9, column=3, padx=1, pady=2)
            TrueBlue_button = tk.Button(page5, bg="#2D68C4", width=4, height=3, command=lambda: [set_color(45, 104, 196),receipt("TrueBlue","BL131")])
            TrueBlue_button.grid(row=9, column=4, padx=1, pady=2)
            TuftsBlue_button = tk.Button(page5, bg="#3E8EDE", width=4, height=3, command=lambda: [set_color( 62, 142, 222),receipt("TuftsBlue","BL132")])
            TuftsBlue_button.grid(row=9, column=5, padx=1, pady=2)
            TwitterBlue_button = tk.Button(page5, bg="#1DA1F2", width=4, height=3, command=lambda: [set_color(29, 161, 242),receipt("TwitterBlue","BL133")])
            TwitterBlue_button.grid(row=9, column=6, padx=1, pady=2)
            UCLABlue_button = tk.Button(page5, bg="#2774AE", width=4, height=3, command=lambda: [set_color( 39, 116, 174),receipt("UCLABlue","BL134")])
            UCLABlue_button.grid(row=9, column=7, padx=1, pady=2)
            UltramarineBlue_button = tk.Button(page5, bg="#120A8F", width=4, height=3, command=lambda: [set_color(18, 10, 143),receipt("UltramarineBlue","BL135")])
            UltramarineBlue_button.grid(row=9, column=8, padx=1, pady=2)
            VioletBlue_button = tk.Button(page5, bg="#324AB2", width=4, height=3, command=lambda: [set_color(50, 74, 178),receipt("VioletBlue","BL136")])
            VioletBlue_button.grid(row=9, column=9, padx=1, pady=2)
            VisaBlue_button = tk.Button(page5, bg="#1A1F71", width=4, height=3, command=lambda: [set_color(26, 31, 113),receipt("VisaBlue","BL137")])
            VisaBlue_button.grid(row=9, column=10, padx=1, pady=2)
            VividSkyBlue_button = tk.Button(page5, bg="#00CCFF", width=4, height=3, command=lambda: [set_color(0, 204, 255),receipt("VividSkyBlue","BL138")])
            VividSkyBlue_button.grid(row=9, column=11, padx=1, pady=2)
            WarriorsBlue_button = tk.Button(page5, bg="#1D428A", width=4, height=3, command=lambda: [set_color(29, 66, 138),receipt("WarriorsBlue","BL139")])
            WarriorsBlue_button.grid(row=9, column=12, padx=1, pady=2)
            YankeesBlue_button = tk.Button(page5, bg="#0C2340", width=4, height=3, command=lambda: [set_color(12, 35, 64),receipt("YankeesBlue","BL140")])
            YankeesBlue_button.grid(row=9, column=13, padx=1, pady=2)
            YInMnBlue_button = tk.Button(page5, bg="#2E5090", width=4, height=3, command=lambda: [set_color(46, 80, 144),receipt("YInMnBlue","BL141")])
            YInMnBlue_button.grid(row=10, column=0, padx=1, pady=2)
            SteelBlue_button = tk.Button(page5, bg="#4682B4", width=4, height=3, command=lambda: [set_color(70, 130, 180),receipt("SteelBlue","BL142")])
            SteelBlue_button.grid(row=10, column=1, padx=1, pady=2)
            AlaskanBlue_button = tk.Button(page5, bg="#6DA9D2", width=4, height=3, command=lambda: [set_color(109, 169, 210),receipt("AlaskanBlue","BL143")])
            AlaskanBlue_button.grid(row=10, column=2, padx=1, pady=2)
            TallShipsBlue_button = tk.Button(page5, bg="#0E81B9", width=4, height=3, command=lambda: [set_color(14, 129, 185),receipt("TallShipsBlue","BL0144")])
            TallShipsBlue_button.grid(row=10, column=3, padx=1, pady=2)

            # Black Series
            Abbey_button = tk.Button(page7, bg="#494F55", width=4, height=3, command=lambda: [set_color(73, 79, 85), receipt("Abbey", "BK001")])
            Abbey_button.grid(row=0, column=0, padx=1, pady=2)
            AshGray_button = tk.Button(page7, bg="#666362", width=4, height=3, command=lambda: [set_color(102, 99, 98), receipt("Ash Gray", "BK002")])
            AshGray_button.grid(row=0, column=1, padx=1, pady=2)
            Asphalt_button = tk.Button(page7, bg="#0C0404", width=4, height=3, command=lambda: [set_color(12, 4, 4), receipt("Asphalt", "BK003")])
            Asphalt_button.grid(row=0, column=2, padx=1, pady=2)
            Black_button = tk.Button(page7, bg="#000000", width=4, height=3, command=lambda: [set_color(0, 0, 0), receipt("Black", "BK004")])
            Black_button.grid(row=0, column=3, padx=1, pady=2)
            BlackBean_button = tk.Button(page7, bg="#3D0C02", width=4, height=3, command=lambda: [set_color(61, 12, 2), receipt("Black Bean", "BK005")])
            BlackBean_button.grid(row=0, column=4, padx=1, pady=2)
            BlackCat_button = tk.Button(page7, bg="#413839", width=4, height=3, command=lambda: [set_color(65, 56, 57), receipt("Black Cat", "BK006")])
            BlackCat_button.grid(row=0, column=5, padx=1, pady=2)
            BlackCow_button = tk.Button(page7, bg="#4C4646", width=4, height=3, command=lambda: [set_color(76, 70, 70), receipt("Black Cow", "BK007")])
            BlackCow_button.grid(row=0, column=6, padx=1, pady=2)
            BlackEel_button = tk.Button(page7, bg="#463E3F", width=4, height=3, command=lambda: [set_color(70, 62, 63), receipt("Black Eel", "BK008")])
            BlackEel_button.grid(row=0, column=7, padx=1, pady=2)
            BlackOlive_button = tk.Button(page7, bg="#3B3C36", width=4, height=3, command=lambda: [set_color(59, 60, 54), receipt("Black Olive", "BK009")])
            BlackOlive_button.grid(row=0, column=8, padx=1, pady=2)
            Charcoal_button = tk.Button(page7, bg="#36454F", width=4, height=3, command=lambda: [set_color(54, 69, 79), receipt("Charcoal", "BK010")])
            Charcoal_button.grid(row=0, column=9, padx=1, pady=2)
            CharlestonGreen_button = tk.Button(page7, bg="#232B2B", width=4, height=3, command=lambda: [set_color(35, 43, 43), receipt("Charleston Green", "BK011")])
            CharlestonGreen_button.grid(row=0, column=10, padx=1, pady=2)
            DarkJungleGreen_button = tk.Button(page7, bg="#1A2421", width=4, height=3, command=lambda: [set_color(26, 36, 33), receipt("Dark Jungle Green", "BK012")])
            DarkJungleGreen_button.grid(row=0, column=11, padx=1, pady=2)
            DavysGray_button = tk.Button(page7, bg="#555555", width=4, height=3, command=lambda: [set_color(85, 85, 85), receipt("DavysGray", "BK013")])
            DavysGray_button.grid(row=0, column=12, padx=1, pady=2)
            DimGray_button = tk.Button(page7, bg="#696969", width=4, height=3, command=lambda: [set_color(105, 105, 105), receipt("DimGray", "BK014")])
            DimGray_button.grid(row=0, column=13, padx=1, pady=2)
            Ebony_button = tk.Button(page7, bg="#555D50", width=4, height=3, command=lambda: [set_color(85, 93, 80), receipt("Ebony", "BK015")])
            Ebony_button.grid(row=1, column=0, padx=1, pady=2)
            EerieBlack_button = tk.Button(page7, bg="#1B1B1B", width=4, height=3, command=lambda: [set_color(27, 27, 27), receipt("Eerie Black", "BK016")])
            EerieBlack_button.grid(row=1, column=1, padx=1, pady=2)
            Granite_button = tk.Button(page7, bg="#676767", width=4, height=3, command=lambda: [set_color(103, 103, 103), receipt("Granite", "BK017")])
            Granite_button.grid(row=1, column=2, padx=1, pady=2)
            Gray_button = tk.Button(page7, bg="#808080", width=4, height=3, command=lambda: [set_color(128, 128, 128), receipt("Gray", "BK018")])
            Gray_button.grid(row=1, column=3, padx=1, pady=2)
            GrayCloud_button = tk.Button(page7, bg="#B6B6B4", width=4, height=3, command=lambda: [set_color(182, 182, 180), receipt("Gray Cloud", "BK019")])
            GrayCloud_button.grid(row=1, column=4, padx=1, pady=2)
            GrayWolf_button = tk.Button(page7, bg="#504A4B", width=4, height=3, command=lambda: [set_color(80, 74, 75), receipt("Gray Wolf", "BK020")])
            GrayWolf_button.grid(row=1, column=5, padx=1, pady=2)
            Gunmetal_button = tk.Button(page7, bg="#2C3539", width=4, height=3, command=lambda: [set_color(44, 53, 57), receipt("Gunmetal", "BK021")])
            Gunmetal_button.grid(row=1, column=6, padx=1, pady=2)
            Iridium_button = tk.Button(page7, bg="#3D3C3A", width=4, height=3, command=lambda: [set_color(61, 60, 58), receipt("Iridium", "BK022")])
            Iridium_button.grid(row=1, column=7, padx=1, pady=2)
            Jet_button = tk.Button(page7, bg="#343434", width=4, height=3, command=lambda: [set_color(52, 52, 52), receipt("Jet", "BK023")])
            Jet_button.grid(row=1, column=8, padx=1, pady=2)
            Licorice_button = tk.Button(page7, bg="#1A1110", width=4, height=3, command=lambda: [set_color(26, 17, 16), receipt("Licorice", "BK024")])
            Licorice_button.grid(row=1, column=9, padx=1, pady=2)
            Midnight_button = tk.Button(page7, bg="#2B1B17", width=4, height=3, command=lambda: [set_color(43, 27, 23), receipt("Midnight", "BK025")])
            Midnight_button.grid(row=1, column=10, padx=1, pady=2)
            Night_button = tk.Button(page7, bg="#0C090A", width=4, height=3, command=lambda: [set_color(12, 9, 10), receipt("Night", "BK026")])
            Night_button.grid(row=1, column=11, padx=1, pady=2)
            Oil_button = tk.Button(page7, bg="#3B3131", width=4, height=3, command=lambda: [set_color(59, 49, 49), receipt("Oil", "BK027")])
            Oil_button.grid(row=1, column=12, padx=1, pady=2)
            OldBurgundy_button = tk.Button(page7, bg="#43302E", width=4, height=3, command=lambda: [set_color(67, 48, 46), receipt("Old Burgundy", "BK028")])
            OldBurgundy_button.grid(row=1, column=13, padx=1, pady=2)
            Onyx_button = tk.Button(page7, bg="#353839", width=4, height=3, command=lambda: [set_color(53, 56, 57), receipt("Onyx", "BK029")])
            Onyx_button.grid(row=2, column=0, padx=1, pady=2)
            OuterSpace_button = tk.Button(page7, bg="#414A4C", width=4, height=3, command=lambda: [set_color(65, 74, 76), receipt("Outer Space", "BK030")])
            OuterSpace_button.grid(row=2, column=1, padx=1, pady=2)
            RaisinBlack_button = tk.Button(page7, bg="#242124", width=4, height=3, command=lambda: [set_color(36, 33, 36), receipt("Raisin Black", "BK031")])
            RaisinBlack_button.grid(row=2, column=2, padx=1, pady=2)
            SmokyBlack_button = tk.Button(page7, bg="#100C08", width=4, height=3, command=lambda: [set_color(16, 12, 8), receipt("Smoky Black", "BK032")])
            SmokyBlack_button.grid(row=2, column=3, padx=1, pady=2)
            Taupe_button = tk.Button(page7, bg="#483C32", width=4, height=3, command=lambda: [set_color(72, 60, 50), receipt("Taupe", "BK033")])
            Taupe_button.grid(row=2, column=4, padx=1, pady=2)
            VampireGray_button = tk.Button(page7, bg="#565051", width=4, height=3, command=lambda: [set_color(86, 80, 81), receipt("Vampire Gray", "BK034")])
            VampireGray_button.grid(row=2, column=5, padx=1, pady=2)
            BlackLeatherJacket_button = tk.Button(page7, bg="#253529", width=4, height=3, command=lambda: [set_color(37, 53, 41), receipt("Black Leather Jacket", "BK035")])
            BlackLeatherJacket_button.grid(row=2, column=6, padx=1, pady=2)
            CafeAmericano_button = tk.Button(page7, bg="#362819", width=4, height=3, command=lambda: [set_color(54, 40, 25), receipt("Cafe Americano", "BK036")])
            CafeAmericano_button.grid(row=2, column=7, padx=1, pady=2)
            Blackberry_button = tk.Button(page7, bg="#3A3A38", width=4, height=3, command=lambda: [set_color(58, 58, 56), receipt("Blackberry", "BK037")])
            Blackberry_button.grid(row=2, column=8, padx=1, pady=2)
            LampBlack_button = tk.Button(page7, bg="#2E473B", width=4, height=3, command=lambda: [set_color(46, 71, 59), receipt("Lamp Black", "BK038")])
            LampBlack_button.grid(row=2, column=9, padx=1, pady=2)
            ArmyUniform_button = tk.Button(page7, bg="#353F3E", width=4, height=3, command=lambda: [set_color(53, 63, 62), receipt("Army Uniform", "BK039")])
            ArmyUniform_button.grid(row=2, column=10, padx=1, pady=2)
            Slate_button = tk.Button(page7, bg="#26282A", width=4, height=3, command=lambda: [set_color(38, 40, 42), receipt("Slate", "BK040")])
            Slate_button.grid(row=2, column=11, padx=1, pady=2)
            PitchBlack_button = tk.Button(page7, bg="#27251F", width=4, height=3, command=lambda: [set_color(39, 37, 31), receipt("Pitch Black", "BK041")])
            PitchBlack_button.grid(row=2, column=12, padx=1, pady=2)
            Spider_button = tk.Button(page7, bg="#040200", width=4, height=3, command=lambda: [set_color(4, 2, 0), receipt("Spider", "BK042")])
            Spider_button.grid(row=2, column=13, padx=1, pady=2)
            Metal_button = tk.Button(page7, bg="#0E0C0A", width=4, height=3, command=lambda: [set_color(14, 12, 10), receipt("Metal", "BK043")])
            Metal_button.grid(row=3, column=0, padx=1, pady=2)
            Grease_button = tk.Button(page7, bg="#080806", width=4, height=3, command=lambda: [set_color(8, 8, 6), receipt("Grease", "BK044")])
            Grease_button.grid(row=3, column=1, padx=1, pady=2)
            Crow_button = tk.Button(page7, bg="#0D0907", width=4, height=3, command=lambda: [set_color(13, 9, 7), receipt("Crow", "BK045")])
            Crow_button.grid(row=3, column=2, padx=1, pady=2)
            BlackRock_button = tk.Button(page7, bg="#010127", width=4, height=3, command=lambda: [set_color(1, 1, 39), receipt("Black Rock", "BK046")])
            BlackRock_button.grid(row=3, column=3, padx=1, pady=2)
            BasaltBlack_button = tk.Button(page7, bg="#4D423E", width=4, height=3, command=lambda: [set_color(77, 66, 62), receipt("Basalt Black", "BK047")])
            BasaltBlack_button.grid(row=3, column=4, padx=1, pady=2)
            NeutralBlack_button = tk.Button(page7, bg="#0B0B0B", width=4, height=3, command=lambda: [set_color(11, 11, 11), receipt("Neutral Black", "BK048")])
            NeutralBlack_button.grid(row=3, column=5, padx=1, pady=2)
            BlackDenim_button = tk.Button(page7, bg="#191C27", width=4, height=3, command=lambda: [set_color(25, 28, 39), receipt("Black Denim", "BK049")])
            BlackDenim_button.grid(row=3, column=6, padx=1, pady=2)
            VampireBlack_button = tk.Button(page7, bg="#0F0404", width=4, height=3, command=lambda: [set_color(15, 4, 4), receipt("Vampire Black", "BK050")])
            VampireBlack_button.grid(row=3, column=7, padx=1, pady=2)
            CoolBlack_button = tk.Button(page7, bg="#151922", width=4, height=3, command=lambda: [set_color(21, 25, 34), receipt("Cool Black", "BK051")])
            CoolBlack_button.grid(row=3, column=8, padx=1, pady=2)
            PandaBlack_button = tk.Button(page7, bg="#3C4748", width=4, height=3, command=lambda: [set_color(60, 71, 72), receipt("Panda Black", "BK052")])
            PandaBlack_button.grid(row=3, column=9, padx=1, pady=2)
            FrostBlack_button = tk.Button(page7, bg="#191C20", width=4, height=3, command=lambda: [set_color(25, 28, 32), receipt("Frost Black", "BK053")])
            FrostBlack_button.grid(row=3, column=10, padx=1, pady=2)
            InkBlackRAL_button = tk.Button(page7, bg="#212122", width=4, height=3, command=lambda: [set_color(33, 33, 34), receipt("Ink Black RAL", "BK054")])
            InkBlackRAL_button.grid(row=3, column=11, padx=1, pady=2)
            Raven_button = tk.Button(page7, bg="#050301", width=4, height=3, command=lambda: [set_color(5, 3, 1), receipt("Raven", "BK055")])
            Raven_button.grid(row=3, column=12, padx=1, pady=2)
            Leather_button = tk.Button(page7, bg="#0B0705", width=4, height=3, command=lambda: [set_color(11, 7, 5), receipt("Leather", "BK056")])
            Leather_button.grid(row=3, column=13, padx=1, pady=2)
            Sable_button = tk.Button(page7, bg="#060606", width=4, height=3, command=lambda: [set_color(6, 6, 6), receipt("Sable", "BK057")])
            Sable_button.grid(row=4, column=0, padx=1, pady=2)
            PowerBlack_button = tk.Button(page7, bg="#0E0C01", width=4, height=3, command=lambda: [set_color(14, 12, 1), receipt("Power Black", "BK058")])
            PowerBlack_button.grid(row=4, column=1, padx=1, pady=2)
            Soot_button = tk.Button(page7, bg="#160D08", width=4, height=3, command=lambda: [set_color(22, 13, 8), receipt("Soot", "BK059")])
            Soot_button.grid(row=4, column=2, padx=1, pady=2)
            Jade_button = tk.Button(page7, bg="#000302", width=4, height=3, command=lambda: [set_color(0, 3, 2), receipt("Jade", "BK060")])
            Jade_button.grid(row=4, column=3, padx=1, pady=2)
            TrueBlack_button = tk.Button(page7, bg="#0A0B0B", width=4, height=3, command=lambda: [set_color(10, 11, 11), receipt("True Black", "BK061")])
            TrueBlack_button.grid(row=4, column=4, padx=1, pady=2)
            PremiumBlack_button = tk.Button(page7, bg="#100E09", width=4, height=3, command=lambda: [set_color(16, 14, 9), receipt("Premium Black", "BK062")])
            PremiumBlack_button.grid(row=4, column=5, padx=1, pady=2)
            Obsidian_button = tk.Button(page7, bg="#020403", width=4, height=3, command=lambda: [set_color(2, 4, 3), receipt("Obsidian", "BK063")])
            Obsidian_button.grid(row=4, column=6, padx=1, pady=2)
            BlackGrain_button = tk.Button(page7, bg="#2C2C2A", width=4, height=3, command=lambda: [set_color(44, 44, 42), receipt("Black Grain", "BK064")])
            BlackGrain_button.grid(row=4, column=7, padx=1, pady=2)
            BlackMagic_button = tk.Button(page7, bg="#0B0510", width=4, height=3, command=lambda: [set_color(11, 5, 16), receipt("Black Magic", "BK065")])
            BlackMagic_button.grid(row=4, column=8, padx=1, pady=2)
            IronBlack_button = tk.Button(page7, bg="#343432", width=4, height=3, command=lambda: [set_color(52, 52, 50), receipt("Iron Black", "BK066")])
            IronBlack_button.grid(row=4, column=9, padx=1, pady=2)
            RichBlackFOGRA29_button = tk.Button(page7, bg="#010B13", width=4, height=3, command=lambda: [set_color(1, 11, 19), receipt("Rich Black FOGRA29", "BK067")])
            RichBlackFOGRA29_button.grid(row=4, column=10, padx=1, pady=2)
            WarmBlack_button = tk.Button(page7, bg="#004242", width=4, height=3, command=lambda: [set_color(0, 66, 66), receipt("Warm Black", "BK068")])
            WarmBlack_button.grid(row=4, column=11, padx=1, pady=2)
            BlackCoral_button = tk.Button(page7, bg="#54626F", width=4, height=3, command=lambda: [set_color(84, 98, 111), receipt("BlackCoral", "BK069")])
            BlackCoral_button.grid(row=4, column=12, padx=1, pady=2)
            BlackShadows_button = tk.Button(page7, bg="#BFAFB2", width=4, height=3, command=lambda: [set_color(191, 175, 178), receipt("Black Shadows", "BK070")])
            BlackShadows_button.grid(row=4, column=13, padx=1, pady=2)
            BlackRaspberry_button = tk.Button(page7, bg="#451425", width=4, height=3, command=lambda: [set_color(69, 20, 37), receipt("Black Raspberry", "BK071")])
            BlackRaspberry_button.grid(row=5, column=0, padx=1, pady=2)
            KombuGreen_button = tk.Button(page7, bg="#354230", width=4, height=3, command=lambda: [set_color(53, 66, 48), receipt("Kombu Green", "BK072")])
            KombuGreen_button.grid(row=5, column=1, padx=1, pady=2)
            ZinnwalditeBrown_button = tk.Button(page7, bg="#2C1608", width=4, height=3, command=lambda: [set_color(44, 22, 8), receipt("Zinnwaldite Brown", "BK073")])
            ZinnwalditeBrown_button.grid(row=5, column=2, padx=1, pady=2)
            DarkSlateGray_button = tk.Button(page7, bg="#2F4F4F", width=4, height=3, command=lambda: [set_color(47, 79, 79), receipt("Dark Slate Gray", "BK074")])
            DarkSlateGray_button.grid(row=5, column=3, padx=1, pady=2)
            DarkCharcoal_button = tk.Button(page7, bg="#333333", width=4, height=3, command=lambda: [set_color(51, 51, 51), receipt("Dark Charcoal", "BK075")])
            DarkCharcoal_button.grid(row=5, column=4, padx=1, pady=2)
            RussianViolet_button = tk.Button(page7, bg="#32174D", width=4, height=3, command=lambda: [set_color(50, 23, 77), receipt("Russian Violet", "BK076")])
            RussianViolet_button.grid(row=5, column=5, padx=1, pady=2)
            OliveDrab7_button = tk.Button(page7, bg="#3C341F", width=4, height=3, command=lambda: [set_color(60, 52, 31), receipt("Olive Drab 7", "BK0077")])
            OliveDrab7_button.grid(row=5, column=6, padx=1, pady=2)
            DarkSienna_button = tk.Button(page7, bg="#3C1414", width=4, height=3, command=lambda: [set_color(60, 20, 20), receipt("Dark Sienna", "BK078")])
            DarkSienna_button.grid(row=5, column=7, padx=1, pady=2)
            AlienBlack_button = tk.Button(page7, bg="#1A2228", width=4, height=3, command=lambda: [set_color(26, 34, 40), receipt("Alien Black", "BK079")])
            AlienBlack_button.grid(row=5, column=8, padx=1, pady=2)
            BlackChocolate_button = tk.Button(page7, bg="#1B1811", width=4, height=3, command=lambda: [set_color(27, 24, 17), receipt("Black Chocolate", "BK080")])
            BlackChocolate_button.grid(row=5, column=9, padx=1, pady=2)
            BlueCharcoal_button = tk.Button(page7, bg="#262B2F", width=4, height=3, command=lambda: [set_color(38, 43, 47), receipt("Blue Chorcoal", "BK081")])
            BlueCharcoal_button.grid(row=5, column=10, padx=1, pady=2)
            GothicGrape_button = tk.Button(page7, bg="#120321", width=4, height=3, command=lambda: [set_color(18, 3, 33), receipt("Gothic Grape", "BK082")])
            GothicGrape_button.grid(row=5, column=11, padx=1, pady=2)
            Metropolis_button = tk.Button(page7, bg="#1A1A1A", width=4, height=3, command=lambda: [set_color(26, 26, 26), receipt("Metropolis", "BK083")])
            Metropolis_button.grid(row=5, column=12, padx=1, pady=2)
            NightShadow_button = tk.Button(page7, bg="#1C1C1C", width=4, height=3, command=lambda: [set_color(28, 28, 28), receipt("Night Shadow", "BK084")])
            NightShadow_button.grid(row=5, column=13, padx=1, pady=2)
            OffBlack_button = tk.Button(page7, bg="#595652", width=4, height=3, command=lambda: [set_color(89, 86, 82), receipt("Off Black", "BK085")])
            OffBlack_button.grid(row=6, column=0, padx=1, pady=2)
            DarkRaisin_button = tk.Button(page7, bg="#1A0F0F", width=4, height=3, command=lambda: [set_color(26, 15, 15), receipt("Dark Raisin", "BK086")])
            DarkRaisin_button.grid(row=6, column=1, padx=1, pady=2)
            TeaBag_button = tk.Button(page7, bg="#161311", width=4, height=3, command=lambda: [set_color(22, 19, 17), receipt("Tea Bag", "BK087")])
            TeaBag_button.grid(row=6, column=2, padx=1, pady=2)
            ElectricBlack_button = tk.Button(page7, bg="#292929", width=4, height=3, command=lambda: [set_color(41, 41, 41), receipt("Electric Black", "BK088")])
            ElectricBlack_button.grid(row=6, column=3, padx=1, pady=2)
            TechBlack_button = tk.Button(page7, bg="#0D0E0E", width=4, height=3, command=lambda: [set_color(13, 14, 14), receipt("Tech Black", "BK089")])
            TechBlack_button.grid(row=6, column=4, padx=1, pady=2)
            DullBlack_button = tk.Button(page7, bg="#161616", width=4, height=3, command=lambda: [set_color(22, 22, 22), receipt("Dull Black", "BK090")])
            DullBlack_button.grid(row=6, column=5, padx=1, pady=2)
            DarkBlack_button = tk.Button(page7, bg="#010203", width=4, height=3, command=lambda: [set_color(1, 2, 3), receipt("Dark Black", "BK091")])
            DarkBlack_button.grid(row=6, column=6, padx=1, pady=2)
            NaturalBlack_button = tk.Button(page7, bg="#07000B", width=4, height=3, command=lambda: [set_color(7, 0, 11), receipt("Natural Black", "BK092")])
            NaturalBlack_button.grid(row=6, column=7, padx=1, pady=2)
            RetroBlack_button = tk.Button(page7, bg="#1F201F", width=4, height=3, command=lambda: [set_color(31, 32, 31), receipt("Retro Black", "BK093")])
            RetroBlack_button.grid(row=6, column=8, padx=1, pady=2)
            BlackGreenRAL_button = tk.Button(page7, bg="#303D3A", width=4, height=3, command=lambda: [set_color(48, 61, 58), receipt("Black Green RAL", "BK094")])
            BlackGreenRAL_button.grid(row=6, column=9, padx=1, pady=2)
            DeepBlack_button = tk.Button(page7, bg="#050203", width=4, height=3, command=lambda: [set_color(5, 2, 3), receipt("Deep Black", "BK095")])
            DeepBlack_button.grid(row=6, column=10, padx=1, pady=2)
            RefreshBlack_button = tk.Button(page7, bg="#111212", width=4, height=3, command=lambda: [set_color(17, 18, 18), receipt("Refresh Black", "BK096")])
            RefreshBlack_button.grid(row=6, column=11, padx=1, pady=2)
            RusticBlack_button = tk.Button(page7, bg="#1B1A16", width=4, height=3, command=lambda: [set_color(27, 26, 22), receipt("Rustic Black", "BK097")])
            RusticBlack_button.grid(row=6, column=12, padx=1, pady=2)
            RoseEbony_button = tk.Button(page7, bg="#674846", width=4, height=3, command=lambda: [set_color(103, 72, 70), receipt("Rose Ebony", "BK098")])
            RoseEbony_button.grid(row=6, column=13, padx=1, pady=2)
            Liver_button = tk.Button(page7, bg="#534B4F", width=4, height=3, command=lambda: [set_color(83, 75, 79), receipt("Liver", "BK099")])
            Liver_button.grid(row=7, column=0, padx=1, pady=2)
            PurpleTaupe_button = tk.Button(page7, bg="#50404D", width=4, height=3, command=lambda: [set_color(80, 64, 77), receipt("Purple Taupe", "BK100")])
            PurpleTaupe_button.grid(row=7, column=1, padx=1, pady=2)
            BlackPearl_button = tk.Button(page7, bg="#0E161A", width=4, height=3, command=lambda: [set_color(14, 22, 26), receipt("Black Pearl", "BK101")])
            BlackPearl_button.grid(row=7, column=2, padx=1, pady=2)
            BlackRussian_button = tk.Button(page7, bg="#24252B", width=4, height=3, command=lambda: [set_color(36, 37, 43), receipt("Black Russian", "BK102")])
            BlackRussian_button.grid(row=7, column=3, padx=1, pady=2)
            AestheticBlack_button = tk.Button(page7, bg="#1C1C1E", width=4, height=3, command=lambda: [set_color(28, 28, 30), receipt("Aesthetic Black", "BK103")])
            AestheticBlack_button.grid(row=7, column=4, padx=1, pady=2)
            SignalBlackRAL_button = tk.Button(page7, bg="#2B2B2C", width=4, height=3, command=lambda: [set_color(43, 43, 44), receipt("Signal Black RAL", "BK104")])
            SignalBlackRAL_button.grid(row=7, column=5, padx=1, pady=2)
            CafeNoir_button = tk.Button(page7, bg="#4B3621", width=4, height=3, command=lambda: [set_color(75, 54, 33), receipt("Cafe Noir", "BK105")])
            CafeNoir_button.grid(row=7, column=6, padx=1, pady=2)
            LuxuryBlack_button = tk.Button(page7, bg="#060D0D", width=4, height=3, command=lambda: [set_color(6, 13, 13), receipt("Luxury Black", "BK106")])
            LuxuryBlack_button.grid(row=7, column=7, padx=1, pady=2)
            BrightBlack_button = tk.Button(page7, bg="#222024", width=4, height=3, command=lambda: [set_color(34, 32, 36), receipt("Bright Black", "BK107")])
            BrightBlack_button.grid(row=7, column=8, padx=1, pady=2)
            BlackBlueRAL_button = tk.Button(page7, bg="#1A1E28", width=4, height=3, command=lambda: [set_color(26, 30, 40), receipt("Black Blue RAL", "BK108")])
            BlackBlueRAL_button.grid(row=7, column=9, padx=1, pady=2)
            GlossyBlack_button = tk.Button(page7, bg="#252324", width=4, height=3, command=lambda: [set_color(37, 35, 36), receipt("Glossy Black", "BK109")])
            GlossyBlack_button.grid(row=7, column=10, padx=1, pady=2)
            IvoryBlack_button = tk.Button(page7, bg="#231F20", width=4, height=3, command=lambda: [set_color(35, 31, 32), receipt("Ivory Black", "BK110")])
            IvoryBlack_button.grid(row=7, column=11, padx=1, pady=2)
            PastelBlack_button = tk.Button(page7, bg="#1D1C1A", width=4, height=3, command=lambda: [set_color(29, 28, 26), receipt("Pastel Black", "BK111")])
            PastelBlack_button.grid(row=7, column=12, padx=1, pady=2)
            FashionBlack_button = tk.Button(page7, bg="#060403", width=4, height=3, command=lambda: [set_color(6, 4, 3), receipt("Fashion Black", "BK112")])
            FashionBlack_button.grid(row=7, column=13, padx=1, pady=2)
            GraphiteBlackRAL_button = tk.Button(page7, bg="#27292B", width=4, height=3, command=lambda: [set_color(39, 41, 43), receipt("Graphite Black RAL", "BK113")])
            GraphiteBlackRAL_button.grid(row=8, column=0, padx=1, pady=2)
            BlackGray_button = tk.Button(page7, bg="#303234", width=4, height=3, command=lambda: [set_color(48, 50, 52), receipt("Black Gray", "BK114")])
            BlackGray_button.grid(row=8, column=1, padx=1, pady=2)
            BlackHole_button = tk.Button(page7, bg="#060605", width=4, height=3, command=lambda: [set_color(6, 6, 5), receipt("Black Hole", "BK115")])
            BlackHole_button.grid(row=8, column=2, padx=1, pady=2)
            Kokushoku_button = tk.Button(page7, bg="#171412", width=4, height=3, command=lambda: [set_color(23, 20, 18), receipt("Kokushoku", "BK116")])
            Kokushoku_button.grid(row=8, column=3, padx=1, pady=2)
            Kurotobi_button = tk.Button(page7, bg="#351E1C", width=4, height=3, command=lambda: [set_color(53, 30, 28), receipt("Kurotobi", "BK117")])
            Kurotobi_button.grid(row=8, column=4, padx=1, pady=2)
            Void_button = tk.Button(page7, bg="#010207", width=4, height=3, command=lambda: [set_color(1, 2, 7), receipt("Void", "BK118")])
            Void_button.grid(row=8, column=5, padx=1, pady=2)
            WetSuit_button = tk.Button(page7, bg="#080706", width=4, height=3, command=lambda: [set_color(8, 7, 6), receipt("Wet Suit", "BK119")])
            WetSuit_button.grid(row=8, column=6, padx=1, pady=2)
            YachtClubBlack_button = tk.Button(page7, bg="#222627", width=4, height=3, command=lambda: [set_color(34, 38, 39), receipt("Yacht Club Black", "BK120")])
            YachtClubBlack_button.grid(row=8, column=7, padx=1, pady=2)
            YoungNight_button = tk.Button(page7, bg="#232323", width=4, height=3, command=lambda: [set_color(35, 35, 35), receipt("Young Night", "BK121")])
            YoungNight_button.grid(row=8, column=8, padx=1, pady=2)
            BlackstrapMolasses_button = tk.Button(page7, bg="#2B2523", width=4, height=3, command=lambda: [set_color(43, 37, 35), receipt("Blackstrap Molasses", "BK122")])
            BlackstrapMolasses_button.grid(row=8, column=9, padx=1, pady=2)
            CarbonBlack_button = tk.Button(page7, bg="#0C0A00", width=4, height=3, command=lambda: [set_color(12, 10, 0), receipt("Carbon Black", "BK123")])
            CarbonBlack_button.grid(row=8, column=10, padx=1, pady=2)
            CynicalBlack_button = tk.Button(page7, bg="#171717", width=4, height=3, command=lambda: [set_color(23, 23, 23), receipt("Cynical Black", "BK124")])
            CynicalBlack_button.grid(row=8, column=11, padx=1, pady=2)
            BlackPlum_button = tk.Button(page7, bg="#362B32", width=4, height=3, command=lambda: [set_color(54, 43, 50), receipt("Black Plum", "BK125")])
            BlackPlum_button.grid(row=8, column=12, padx=1, pady=2)
            ReversedGray_button = tk.Button(page7, bg="#080808", width=4, height=3, command=lambda: [set_color(8, 8, 8), receipt("Reverxsed Gray", "BK126")])
            ReversedGray_button.grid(row=8, column=13, padx=1, pady=2)
            Stout_button = tk.Button(page7, bg="#0F0B0A", width=4, height=3, command=lambda: [set_color(15, 11, 10), receipt("Stout", "BK127")])
            Stout_button.grid(row=9, column=0, padx=1, pady=2)
            TornadoCloud_button = tk.Button(page7, bg="#121213", width=4, height=3, command=lambda: [set_color(18, 18, 19), receipt("Tornado Cloud", "BK128")])
            TornadoCloud_button.grid(row=9, column=1, padx=1, pady=2)
            WalnutHull_button = tk.Button(page7, bg="#1B1813", width=4, height=3, command=lambda: [set_color(27, 24, 19), receipt("Walnut Hull", "BK129")])
            WalnutHull_button.grid(row=9, column=2, padx=1, pady=2)
            TapShoe_button = tk.Button(page7, bg="#2A2B2D", width=4, height=3, command=lambda: [set_color(42, 43, 45), receipt("Tap Shoe", "BK130")])
            TapShoe_button.grid(row=9, column=3, padx=1, pady=2)
            Woodsmoke_button = tk.Button(page7, bg="#2B3230", width=4, height=3, command=lambda: [set_color(43, 50, 48), receipt("Wood Smoke", "BK131")])
            Woodsmoke_button.grid(row=9, column=4, padx=1, pady=2)
            BlackRed_button = tk.Button(page7, bg="#3D2022", width=4, height=3, command=lambda: [set_color(61, 32, 34), receipt("Black Red", "BK132")])
            BlackRed_button.grid(row=9, column=5, padx=1, pady=2)
            WindCave_button = tk.Button(page7, bg="#1F2024", width=4, height=3, command=lambda: [set_color(31, 32, 36), receipt("Wind Cave", "BK133")])
            WindCave_button.grid(row=9, column=6, padx=1, pady=2)
            HeavyGray_button = tk.Button(page7, bg="#050505", width=4, height=3, command=lambda: [set_color(5, 5, 5), receipt("Heavy Gray", "BK134")])
            HeavyGray_button.grid(row=9, column=7, padx=1, pady=2)
            TapShoe_button = tk.Button(page7, bg="#2A2B2D", width=4, height=3, command=lambda: [set_color(42, 43, 45), receipt("Tap Shoe", "BK130")])
            TapShoe_button.grid(row=9, column=8, padx=1, pady=2)
            Woodsmoke_button = tk.Button(page7, bg="#2B3230", width=4, height=3, command=lambda: [set_color(43, 50, 48), receipt("Wood Smoke", "BK131")])
            Woodsmoke_button.grid(row=9, column=9, padx=1, pady=2)
            BlackRed_button = tk.Button(page7, bg="#3D2022", width=4, height=3, command=lambda: [set_color(61, 32, 34), receipt("Black Red", "BK132")])
            BlackRed_button.grid(row=9, column=10, padx=1, pady=2)
            WindCave_button = tk.Button(page7, bg="#1F2024", width=4, height=3, command=lambda: [set_color(31, 32, 36), receipt("Wind Cave", "BK133")])
            WindCave_button.grid(row=9, column=11, padx=1, pady=2)
            HeavyGray_button = tk.Button(page7, bg="#050505", width=4, height=3, command=lambda: [set_color(5, 5, 5), receipt("Heavy Gray", "BK134")])
            HeavyGray_button.grid(row=9, column=12, padx=1, pady=2)

            # GreenSeries
            ForestGreen_button = tk.Button(page4, bg="#0B6623", width=4, height=3, command=lambda: [set_color(11, 102, 35), receipt("ForestGreen", "GR001")])
            ForestGreen_button.grid(row=0, column=0, padx=1, pady=2)

            Olive_button = tk.Button(page4, bg="#708238", width=4, height=3, command=lambda: [set_color(112, 130, 56), receipt("Olive", "GR002")])
            Olive_button.grid(row=0, column=1, padx=1, pady=2)

            HunterGreen_button = tk.Button(page4, bg="#3F704D", width=4, height=3, command=lambda: [set_color(63, 112, 77), receipt("HunterGreen", "GR003")])
            HunterGreen_button.grid(row=0, column=2, padx=1, pady=2)

            ArtichokeGreen_button = tk.Button(page4, bg="#8F9779", width=4, height=3, command=lambda: [set_color(143, 151, 121), receipt("ArtichokeGreen", "GR004")])
            ArtichokeGreen_button.grid(row=0, column=3, padx=1, pady=2)

            JungleGreen_button = tk.Button(page4, bg="#29AB87", width=4, height=3, command=lambda: [set_color(41, 171, 135), receipt("JungleGreen", "GR005")])
            JungleGreen_button.grid(row=0, column=4, padx=1, pady=2)

            TropicalRainforest_button = tk.Button(page4, bg="#00755E", width=4, height=3, command=lambda: [set_color(0, 117, 94), receipt("TropicalRainforest", "GR006")])
            TropicalRainforest_button.grid(row=0, column=5, padx=1, pady=2)

            Amazon_button = tk.Button(page4, bg="#3B7A57", width=4, height=3, command=lambda: [set_color(59, 122, 87), receipt("Amazon", "GR007")])
            Amazon_button.grid(row=0, column=6, padx=1, pady=2)

            DeepJungleGreen_button = tk.Button(page4, bg="#004B49", width=4, height=3, command=lambda: [set_color(0, 75, 73), receipt("DeepJungleGreen", "GR008")])
            DeepJungleGreen_button.grid(row=0, column=7, padx=1, pady=2)

            MediumJungleGreen_button = tk.Button(page4, bg="#1C352D", width=4, height=3, command=lambda: [set_color(28, 53, 45), receipt("MediumJungleGreen", "GR009")])
            MediumJungleGreen_button.grid(row=0, column=8, padx=1, pady=2)

            DarkJungleGreen_button = tk.Button(page4, bg="#1A2421", width=4, height=3, command=lambda: [set_color(26, 36, 33), receipt("DarkJungleGreen", "GR010")])
            DarkJungleGreen_button.grid(row=0, column=9, padx=1, pady=2)

            MossGreen_button = tk.Button(page4, bg="#8A9A5B", width=4, height=3, command=lambda: [set_color(138, 154, 91), receipt("MossGreen", "GR011")])
            MossGreen_button.grid(row=0, column=10, padx=1, pady=2)

            MyrtleGreen_button = tk.Button(page4, bg="#317873", width=4, height=3, command=lambda: [set_color(49, 120, 115), receipt("MyrtleGreen", "GR012")])
            MyrtleGreen_button.grid(row=0, column=11, padx=1, pady=2)

            PineGreen_button = tk.Button(page4, bg="#01796F", width=4, height=3, command=lambda: [set_color(1, 121, 111), receipt("PineGreen", "GR013")])
            PineGreen_button.grid(row=0, column=12, padx=1, pady=2)

            PersianGreen_button = tk.Button(page4, bg="#00A693", width=4, height=3, command=lambda: [set_color(0, 166, 147), receipt("PersianGreen", "GR014")])
            PersianGreen_button.grid(row=0, column=13, padx=1, pady=2)

            EmeraldGreen_button = tk.Button(page4, bg="#50C878", width=4, height=3, command=lambda: [set_color(80, 200, 120), receipt("EmeraldGreen", "GR015")])
            EmeraldGreen_button.grid(row=1, column=0, padx=1, pady=2)

            NeonGreen_button = tk.Button(page4, bg="#39FF14", width=4, height=3, command=lambda: [set_color(57, 255, 20), receipt("NeonGreen", "GR016")])
            NeonGreen_button.grid(row=1, column=1, padx=1, pady=2)

            SacramentoGreen_button = tk.Button(page4, bg="#043927", width=4, height=3, command=lambda: [set_color(4, 57, 39), receipt("SacramentoGreen", "GR017")])
            SacramentoGreen_button.grid(row=1, column=2, padx=1, pady=2)

            SeaGreen_button = tk.Button(page4, bg="#2E8B57", width=4, height=3, command=lambda: [set_color(46, 139, 87), receipt("SeaGreen", "GR018")])
            SeaGreen_button.grid(row=1, column=3, padx=1, pady=2)

            SageGreen_button = tk.Button(page4, bg="#9DC183", width=4, height=3, command=lambda: [set_color(157, 193, 131), receipt("SageGreen", "GR019")])
            SageGreen_button.grid(row=1, column=4, padx=1, pady=2)

            LimeGreen_button = tk.Button(page4, bg="#C7EA46", width=4, height=3, command=lambda: [set_color(199, 234, 70), receipt("LimeGreen", "GR020")])
            LimeGreen_button.grid(row=1, column=5, padx=1, pady=2)

            JadeGreen_button = tk.Button(page4, bg="#00A86B", width=4, height=3, command=lambda: [set_color(0, 168, 107), receipt("JadeGreen", "GR021")])
            JadeGreen_button.grid(row=1, column=6, padx=1, pady=2)

            FernGreen_button = tk.Button(page4, bg="#4F7942", width=4, height=3, command=lambda: [set_color(79, 121, 66), receipt("FernGreen", "GR022")])
            FernGreen_button.grid(row=1, column=7, padx=1, pady=2)

            LaurelGreen_button = tk.Button(page4, bg="#A9BA9D", width=4, height=3, command=lambda: [set_color(169, 186, 157), receipt("LaurelGreen", "GR023")])
            LaurelGreen_button.grid(row=1, column=8, padx=1, pady=2)

            MintGreen_button = tk.Button(page4, bg="#98FB98", width=4, height=3, command=lambda: [set_color(152, 251, 152), receipt("MintGreen", "GR024")])
            MintGreen_button.grid(row=1, column=9, padx=1, pady=2)

            Tea_Green_button = tk.Button(page4, bg="#D0F0C0", width=4, height=3, command=lambda: [set_color(208, 240, 192), receipt("Tea_Green", "GR025")])
            Tea_Green_button.grid(row=1, column=10, padx=1, pady=2)

            ArmyGreen_button = tk.Button(page4, bg="#4B5320", width=4, height=3, command=lambda: [set_color(75, 83, 32), receipt("ArmyGreen", "GR026")])
            ArmyGreen_button.grid(row=1, column=11, padx=1, pady=2)

            KellyGreen_button = tk.Button(page4, bg="#4CBB17", width=4, height=3, command=lambda: [set_color(76, 187, 23), receipt("KellyGreen", "GR027")])
            KellyGreen_button.grid(row=1, column=12, padx=1, pady=2)

            RussianGreen_button = tk.Button(page4, bg="#679267", width=4, height=3, command=lambda: [set_color(103, 146, 103), receipt("RussianGreen", "GR028")])
            RussianGreen_button.grid(row=1, column=13, padx=1, pady=2)

            ParisGreen_button = tk.Button(page4, bg="#50C878", width=4, height=3, command=lambda: [set_color(80, 200, 120), receipt("ParisGreen", "GR029")])
            ParisGreen_button.grid(row=2, column=0, padx=1, pady=2)

            PakistanGreen_button = tk.Button(page4, bg="#006600", width=4, height=3, command=lambda: [set_color(0, 102, 0), receipt("PakistanGreen", "GR030")])
            PakistanGreen_button.grid(row=2, column=1, padx=1, pady=2)

            MidnightGreen_button = tk.Button(page4, bg="#004953", width=4, height=3, command=lambda: [set_color(0, 73, 83), receipt("MidnightGreen", "GR031")])
            MidnightGreen_button.grid(row=2, column=2, padx=1, pady=2)

            IndiaGreen_button = tk.Button(page4, bg="#138808", width=4, height=3, command=lambda: [set_color(19, 136, 8), receipt("IndiaGreen", "GR032")])
            IndiaGreen_button.grid(row=2, column=3, padx=1, pady=2)

            HunterGreen_button = tk.Button(page4, bg="#355E3B", width=4, height=3, command=lambda: [set_color(53, 94, 59), receipt("HunterGreen", "GR033")])
            HunterGreen_button.grid(row=2, column=4, padx=1, pady=2)

            CeladonGreen_button = tk.Button(page4, bg="#ACE1AF", width=4, height=3, command=lambda: [set_color(172, 225, 175), receipt("CeladonGreen", "GR034")])
            CeladonGreen_button.grid(row=2, column=5, padx=1, pady=2)

            Avocado_button = tk.Button(page4, bg="#568203", width=4, height=3, command=lambda: [set_color(86, 130, 3), receipt("Avocado", "GR035")])
            Avocado_button.grid(row=2, column=6, padx=1, pady=2)

            Harlequin_button = tk.Button(page4, bg="#3FFF00", width=4, height=3, command=lambda: [set_color(63, 255, 0), receipt("Harlequin", "GR036")])
            Harlequin_button.grid(row=2, column=7, padx=1, pady=2)

            Spring_button = tk.Button(page4, bg="#00F0A8", width=4, height=3, command=lambda: [set_color(0, 240, 168), receipt("Spring", "GR037")])
            Spring_button.grid(row=2, column=8, padx=1, pady=2)

            Kaitoke_button = tk.Button(page4, bg="#004830", width=4, height=3, command=lambda: [set_color(0, 72, 48), receipt("Kaitoke", "GR038")])
            Kaitoke_button.grid(row=2, column=9, padx=1, pady=2)

            ScreaminGreen_button = tk.Button(page4, bg="#76FF7A", width=4, height=3, command=lambda: [set_color(118, 255, 122), receipt("ScreaminGreen", "GR039")])
            ScreaminGreen_button.grid(row=2, column=10, padx=1, pady=2)

            Chateau_button = tk.Button(page4, bg="#48A860", width=4, height=3, command=lambda: [set_color(72, 168, 96), receipt("Chateau", "GR040")])
            Chateau_button.grid(row=2, column=11, padx=1, pady=2)

            DarkMossGreen_button = tk.Button(page4, bg="#4A5D23", width=4, height=3, command=lambda: [set_color(74, 93, 35), receipt("DarkMossGreen", "GR041")])
            DarkMossGreen_button.grid(row=2, column=12, padx=1, pady=2)

            Swamp_button = tk.Button(page4, bg="#A8C090", width=4, height=3, command=lambda: [set_color(168, 192, 144), receipt("Swamp", "GR042")])
            Swamp_button.grid(row=2, column=13, padx=1, pady=2)

            Mantis_button = tk.Button(page4, bg="#74C365", width=4, height=3, command=lambda: [set_color(116, 195, 101), receipt("Mantis", "GR043")])
            Mantis_button.grid(row=3, column=0, padx=1, pady=2)

            Fun_button = tk.Button(page4, bg="#007848", width=4, height=3, command=lambda: [set_color(0, 120, 72), receipt("Fun", "GR044")])
            Fun_button.grid(row=3, column=1, padx=1, pady=2)

            PantoneArtichokeGreen_button = tk.Button(page4, bg="#4B6F44", width=4, height=3, command=lambda: [set_color(75, 111, 68), receipt("Pantone Artichoke Green", "GR045")])
            PantoneArtichokeGreen_button.grid(row=3, column=2, padx=1, pady=2)

            Viridian_button = tk.Button(page4, bg="#609078", width=4, height=3, command=lambda: [set_color(96, 144, 120), receipt("Viridian", "GR046")])
            Viridian_button.grid(row=3, column=3, padx=1, pady=2)

            ResedaGreen_button = tk.Button(page4, bg="#6C7C59", width=4, height=3, command=lambda: [set_color(108, 124, 89), receipt("Reseda Green", "GR047")])
            ResedaGreen_button.grid(row=3, column=4, padx=1, pady=2)

            Chetwode_button = tk.Button(page4, bg="#F0FFF0", width=4, height=3, command=lambda: [set_color(240, 255, 240), receipt("Chetwode", "GR048")])
            Chetwode_button.grid(row=3, column=5, padx=1, pady=2)

            ShamrockGreen_button = tk.Button(page4, bg="#009E60", width=4, height=3, command=lambda: [set_color(0, 158, 96), receipt("Shamrock Green", "GR049")])
            ShamrockGreen_button.grid(row=3, column=6, padx=1, pady=2)

            Verdun_button = tk.Button(page4, bg="#487800", width=4, height=3, command=lambda: [set_color(72, 120, 0), receipt("Verdun", "GR050")])
            Verdun_button.grid(row=3, column=7, padx=1, pady=2)

            CastletonGreen_button = tk.Button(page4, bg="#00563B", width=4, height=3, command=lambda: [set_color(0, 86, 59), receipt("Castleton Green", "GR051")])
            CastletonGreen_button.grid(row=3, column=8, padx=1, pady=2)

            Gin_button = tk.Button(page4, bg="#D8E4BC", width=4, height=3, command=lambda: [set_color(216, 228, 188), receipt("Gin", "GR052")])
            Gin_button.grid(row=3, column=9, padx=1, pady=2)

            GrannySmithApple_button = tk.Button(page4, bg="#A8E4A0", width=4, height=3, command=lambda: [set_color(168, 228, 160), receipt("Granny Smith Apple", "GR053")])
            GrannySmithApple_button.grid(row=3, column=10, padx=1, pady=2)

            BitterLime_button = tk.Button(page4, bg="#BFFF00", width=4, height=3, command=lambda: [set_color(191, 255, 0), receipt("Bitter Lime", "GR054")])
            BitterLime_button.grid(row=3, column=11, padx=1, pady=2)

            BrightMint_button = tk.Button(page4, bg="#4FFFB0", width=4, height=3, command=lambda: [set_color(79, 255, 176), receipt("Bright Mint", "GR055")])
            BrightMint_button.grid(row=3, column=12, padx=1, pady=2)

            BottleGreen_button = tk.Button(page4, bg="#006A4E", width=4, height=3, command=lambda: [set_color(0, 106, 78), receipt("Bottle Green", "GR056")])
            BottleGreen_button.grid(row=3, column=13, padx=1, pady=2)

            CadmiumGreen_button = tk.Button(page4, bg="#006B3C", width=4, height=3, command=lambda: [set_color(0, 107, 60), receipt("Cadmium Green", "GR057")])
            CadmiumGreen_button.grid(row=4, column=0, padx=1, pady=2)

            CamouflageGreen_button = tk.Button(page4, bg="#78866B", width=4, height=3, command=lambda: [set_color(120, 134, 107), receipt("Camouflage Green", "GR058")])
            CamouflageGreen_button.grid(row=4, column=1, padx=1, pady=2)

            Pear_button = tk.Button(page4, bg="#D1E231", width=4, height=3, command=lambda: [set_color(209, 226, 49), receipt("Pear", "GR059")])
            Pear_button.grid(row=4, column=2, padx=1, pady=2)

            DollarBill_button = tk.Button(page4, bg="#85BB65", width=4, height=3, command=lambda: [set_color(133, 187, 101), receipt("Dollar Bill", "GR060")])
            DollarBill_button.grid(row=4, column=3, padx=1, pady=2)

            Inchworm_button = tk.Button(page4, bg="#B2EC5D", width=4, height=3, command=lambda: [set_color(178, 236, 93), receipt("Inchworm", "GR061")])
            Inchworm_button.grid(row=4, column=4, padx=1, pady=2)

            Asparagus_button = tk.Button(page4, bg="#87A96B", width=4, height=3, command=lambda: [set_color(135, 169, 107), receipt("Asparagus", "GR062")])
            Asparagus_button.grid(row=4, column=5, padx=1, pady=2)

            CaribbeanGreen_button = tk.Button(page4, bg="#00CC99", width=4, height=3, command=lambda: [set_color(0, 204, 153), receipt("Caribbean Green", "GR063")])
            CaribbeanGreen_button.grid(row=4, column=6, padx=1, pady=2)

            GOGreen_button = tk.Button(page4, bg="#00AB66", width=4, height=3, command=lambda: [set_color(0, 171, 102), receipt("GO Green", "GR064")])
            GOGreen_button.grid(row=4, column=7, padx=1, pady=2)

            PhthaloGreen_button = tk.Button(page4, bg="#123524", width=4, height=3, command=lambda: [set_color(18, 53, 36), receipt("Phthalo Green", "GR065")])
            PhthaloGreen_button.grid(row=4, column=8, padx=1, pady=2)

            NapierGreen_button = tk.Button(page4, bg="#2A8000", width=4, height=3, command=lambda: [set_color(42, 128, 0), receipt("Napier Green", "GR066")])
            NapierGreen_button.grid(row=4, column=9, padx=1, pady=2)

            Feldgrau_button = tk.Button(page4, bg="#4D5D53", width=4, height=3, command=lambda: [set_color(77, 93, 83), receipt("Feldgrau", "GR067")])
            Feldgrau_button.grid(row=4, column=10, padx=1, pady=2)

            GreenYellow_button = tk.Button(page4, bg="#ADFF2F", width=4, height=3, command=lambda: [set_color(173, 255, 47), receipt("Green Yellow", "GR068")])
            GreenYellow_button.grid(row=4, column=11, padx=1, pady=2)

            Malachite_button = tk.Button(page4, bg="#0BDA51", width=4, height=3, command=lambda: [set_color(11, 218, 81), receipt("Malachite", "GR069")])
            Malachite_button.grid(row=4, column=12, padx=1, pady=2)

            RifleGreen_button = tk.Button(page4, bg="#444C38", width=4, height=3, command=lambda: [set_color(68, 76, 56), receipt("Rifle Green", "GR070")])
            RifleGreen_button.grid(row=4, column=13, padx=1, pady=2)

            Volt_button = tk.Button(page4, bg="#CEFF00", width=4, height=3, command=lambda: [set_color(206, 255, 0), receipt("Volt", "GR071")])
            Volt_button.grid(row=5, column=0, padx=1, pady=2)

            BritishRacingGreen_button = tk.Button(page4, bg="#004225", width=4, height=3, command=lambda: [set_color(0, 66, 37), receipt("British Racing Green", "GR072")])
            BritishRacingGreen_button.grid(row=5, column=1, padx=1, pady=2)

            Thyme_button = tk.Button(page4, bg="#5EDC1F", width=4, height=3, command=lambda: [set_color(94, 220, 31), receipt("Thyme", "GR073")])
            Thyme_button.grid(row=5, column=2, padx=1, pady=2)

            Chartreuse_button = tk.Button(page4, bg="#7FFF00", width=4, height=3, command=lambda: [set_color(127, 255, 0), receipt("Chartreuse", "GR074")])
            Chartreuse_button.grid(row=5, column=3, padx=1, pady=2)

            CornGreen_button = tk.Button(page4, bg="#71A92C", width=4, height=3, command=lambda: [set_color(113, 169, 44), receipt("Corn Green", "GR075")])
            CornGreen_button.grid(row=5, column=4, padx=1, pady=2)

            ShrekGreen_button = tk.Button(page4, bg="#C4D300", width=4, height=3, command=lambda: [set_color(196, 211, 0), receipt("Shrek Green", "GR076")])
            ShrekGreen_button.grid(row=5, column=5, padx=1, pady=2)

            ChristmasGreen_button = tk.Button(page4, bg="#00873E", width=4, height=3, command=lambda: [set_color(0, 135, 62), receipt("Christmas Green", "GR077")])
            ChristmasGreen_button.grid(row=5, column=6, padx=1, pady=2)

            IrishGreen_button = tk.Button(page4, bg="#009A44", width=4, height=3, command=lambda: [set_color(0, 154, 68), receipt("Irish Green", "GR078")])
            IrishGreen_button.grid(row=5, column=7, padx=1, pady=2)

            RoadSignGreen_button = tk.Button(page4, bg="#01735C", width=4, height=3, command=lambda: [set_color(1, 115, 92), receipt("Road Sign Green", "GR079")])
            RoadSignGreen_button.grid(row=5, column=8, padx=1, pady=2)

            LightsaberGreen_button = tk.Button(page4, bg="#2FF924", width=4, height=3, command=lambda: [set_color(47, 249, 36), receipt("Lightsaber Green", "GR080")])
            LightsaberGreen_button.grid(row=5, column=9, padx=1, pady=2)

            GirlScoutGreen_button = tk.Button(page4, bg="#00AE58", width=4, height=3, command=lambda: [set_color(0, 174, 88), receipt("Girl Scout Green", "GR081")])
            GirlScoutGreen_button.grid(row=5, column=10, padx=1, pady=2)

            TennisCourtGreen_button = tk.Button(page4, bg="#6C935C", width=4, height=3, command=lambda: [set_color(108, 147, 92), receipt("Tennis Court Green", "GR082")])
            TennisCourtGreen_button.grid(row=5, column=11, padx=1, pady=2)

            SpringBud_button = tk.Button(page4, bg="#A7FC00", width=4, height=3, command=lambda: [set_color(167, 252, 0), receipt("Spring Bud", "GR083")])
            SpringBud_button.grid(row=5, column=12, padx=1, pady=2)

            ChineseGreen_button = tk.Button(page4, bg="#D0DB61", width=4, height=3, command=lambda: [set_color(208, 219, 97), receipt("Chinese Green", "GR084")])
            ChineseGreen_button.grid(row=5, column=13, padx=1, pady=2)

            ArcticLime_button = tk.Button(page4, bg="#D0FF14", width=4, height=3, command=lambda: [set_color(208, 255, 20), receipt("Arctic Lime", "GR085")])
            ArcticLime_button.grid(row=6, column=0, padx=1, pady=2)

            Nyanza_button = tk.Button(page4, bg="#E9FFDB", width=4, height=3, command=lambda: [set_color(233, 255, 219), receipt("Nyanza", "GR086")])
            Nyanza_button.grid(row=6, column=1, padx=1, pady=2)

            DarkLemonLime_button = tk.Button(page4, bg="#76BA1B", width=4, height=3, command=lambda: [set_color(118, 186, 27), receipt("Dark Lemon Lime", "GR087")])
            DarkLemonLime_button.grid(row=6, column=2, padx=1, pady=2)

            CrayolaYellowGreen_button = tk.Button(page4, bg="#ACDF87", width=4, height=3, command=lambda: [set_color(172, 223, 135), receipt("Crayola Yellow Green", "GR088")])
            CrayolaYellowGreen_button.grid(row=6, column=3, padx=1, pady=2)

            MaximumGreen_button = tk.Button(page4, bg="#4C9A2A", width=4, height=3, command=lambda: [set_color(76, 154, 42), receipt("Maximum Green", "GR089")])
            MaximumGreen_button.grid(row=6, column=4, padx=1, pady=2)

            VividLimeGreen_button = tk.Button(page4, bg="#A4DE02", width=4, height=3, command=lambda: [set_color(164, 222, 2), receipt("Vivid Lime Green", "GR090")])
            VividLimeGreen_button.grid(row=6, column=5, padx=1, pady=2)

            Pistachio_button = tk.Button(page4, bg="#93C572", width=4, height=3, command=lambda: [set_color(147, 197, 114), receipt("Pistachio", "GR091")])
            Pistachio_button.grid(row=6, column=6, padx=1, pady=2)

            MediumSpringGreen_button = tk.Button(page4, bg="#00FA9A", width=4, height=3, command=lambda: [set_color(0, 250, 154), receipt("Medium Spring Green", "GR092")])
            MediumSpringGreen_button.grid(row=6, column=7, padx=1, pady=2)

            SheenGreen_button = tk.Button(page4, bg="#8FD400", width=4, height=3, command=lambda: [set_color(143, 212, 0), receipt("Sheen Green", "GR093")])
            SheenGreen_button.grid(row=6, column=8, padx=1, pady=2)

            LaSalleGreen_button = tk.Button(page4, bg="#087830", width=4, height=3, command=lambda: [set_color(8, 120, 48), receipt("LaSalle Green", "GR094")])
            LaSalleGreen_button.grid(row=6, column=9, padx=1, pady=2)

            SpanishViridian_button = tk.Button(page4, bg="#007F5C", width=4, height=3, command=lambda: [set_color(0, 127, 92), receipt("Spanish Viridian", "GR095")])
            SpanishViridian_button.grid(row=6, column=10, padx=1, pady=2)

            DartmouthGreen_button = tk.Button(page4, bg="#00703C", width=4, height=3, command=lambda: [set_color(0, 112, 60), receipt("Dartmouth Green", "GR096")])
            DartmouthGreen_button.grid(row=6, column=11, padx=1, pady=2)

            PineNeedleColor_button = tk.Button(page4, bg="#454D32", width=4, height=3, command=lambda: [set_color(69, 77, 50), receipt("Pine Needle Color", "GR097")])
            PineNeedleColor_button.grid(row=6, column=12, padx=1, pady=2)

            OliveDrab_button = tk.Button(page4, bg="#6B8E23", width=4, height=3, command=lambda: [set_color(107, 142, 35), receipt("Olive Drab", "GR098")])
            OliveDrab_button.grid(row=6, column=13, padx=1, pady=2)

            LawnGreen_button = tk.Button(page4, bg="#7CFC00", width=4, height=3, command=lambda: [set_color(124, 252, 0), receipt("Lawn Green", "GR099")])
            LawnGreen_button.grid(row=7, column=0, padx=1, pady=2)

            Xanadu_button = tk.Button(page4, bg="#738678", width=4, height=3, command=lambda: [set_color(115, 134, 120), receipt("Xanadu", "GR100")])
            Xanadu_button.grid(row=7, column=1, padx=1, pady=2)

            DarkOliveGreen_button = tk.Button(page4, bg="#556B2F", width=4, height=3, command=lambda: [set_color(85, 107, 47), receipt("Dark Olive Green", "GR101")])
            DarkOliveGreen_button.grid(row=7, column=2, padx=1, pady=2)

            DarkSeaGreen_button = tk.Button(page4, bg="#8FBC8F", width=4, height=3, command=lambda: [set_color(143, 188, 143), receipt("Dark Sea Green", "GR102")])
            DarkSeaGreen_button.grid(row=7, column=3, padx=1, pady=2)

            GreenMunsell_button = tk.Button(page4, bg="#00A877", width=4, height=3, command=lambda: [set_color(0, 168, 119), receipt("Green Munsell", "GR103")])
            GreenMunsell_button.grid(row=7, column=4, padx=1, pady=2)

            MughalGreen_button = tk.Button(page4, bg="#306030", width=4, height=3, command=lambda: [set_color(48, 96, 48), receipt("Mughal Green", "GR104")])
            MughalGreen_button.grid(row=7, column=5, padx=1, pady=2)

            JohnDeereGreen_button = tk.Button(page4, bg="#367C2B", width=4, height=3, command=lambda: [set_color(54, 124, 43), receipt("John Deere Green", "GR105")])
            JohnDeereGreen_button.grid(row=7, column=6, padx=1, pady=2)

            OfficeGreen_button = tk.Button(page4, bg="#008000", width=4, height=3, command=lambda: [set_color(0, 128, 0), receipt("Office Green", "GR106")])
            OfficeGreen_button.grid(row=7, column=7, padx=1, pady=2)

            Limerick_button = tk.Button(page4, bg="#9DC209", width=4, height=3, command=lambda: [set_color(157, 194, 9), receipt("Limerick", "GR107")])
            Limerick_button.grid(row=7, column=8, padx=1, pady=2)

            MaximumGreenYellow_button = tk.Button(page4, bg="#D9E650", width=4, height=3, command=lambda: [set_color(217, 230, 80), receipt("Maximum Green Yellow", "GR108")])
            MaximumGreenYellow_button.grid(row=7, column=9, padx=1, pady=2)

            FrenchLime_button = tk.Button(page4, bg="#9EFD38", width=4, height=3, command=lambda: [set_color(158, 253, 56), receipt("French Lime", "GR109")])
            FrenchLime_button.grid(row=7, column=10, padx=1, pady=2)

            MediumSpringBud_button = tk.Button(page4, bg="#C9DC87", width=4, height=3, command=lambda: [set_color(201, 220, 135), receipt("Medium Spring Bud", "GR110")])
            MediumSpringBud_button.grid(row=7, column=11, padx=1, pady=2)

            UFOGreen_button = tk.Button(page4, bg="#3CD070", width=4, height=3, command=lambda: [set_color(60, 208, 112), receipt("UFO Green", "GR111")])
            UFOGreen_button.grid(row=7, column=12, padx=1, pady=2)

            AcidGreen_button = tk.Button(page4, bg="#B0BF1A", width=4, height=3, command=lambda: [set_color(176, 191, 26), receipt("Acid Green", "GR112")])
            AcidGreen_button.grid(row=7, column=13, padx=1, pady=2)

            ChlorophyllGreen_button = tk.Button(page4, bg="#4AFF00", width=4, height=3,  command=lambda: [set_color(74, 255, 0), receipt("Chlorophyll Green", "GR113")])
            ChlorophyllGreen_button.grid(row=8, column=0, padx=1, pady=2)

            GreenLizard_button = tk.Button(page4, bg="#A7F432", width=4, height=3,  command=lambda: [set_color(167, 244, 50), receipt("Green Lizard", "GR114")])
            GreenLizard_button.grid(row=8, column=1, padx=1, pady=2)

            IguanaGreen_button = tk.Button(page4, bg="#71BC78", width=4, height=3, command=lambda: [set_color(113, 188, 120), receipt("Iguana Green", "GR115")])
            IguanaGreen_button.grid(row=8, column=2, padx=1, pady=2)

            KombuGreen_button = tk.Button(page4, bg="#354230", width=4, height=3, command=lambda: [set_color(53, 66, 48), receipt("Kombu Green", "GR116")])
            KombuGreen_button.grid(row=8, column=3, padx=1, pady=2)

            MiddleGreen_button = tk.Button(page4, bg="#4D8C57", width=4, height=3,  command=lambda: [set_color(77, 140, 87), receipt("Middle Green", "GR117")])
            MiddleGreen_button.grid(row=8, column=4, padx=1, pady=2)

            PaoloVeroneseGreen_button = tk.Button(page4, bg="#009B7D", width=4, height=3, command=lambda: [set_color(0, 155, 125), receipt("Paolo Veronese Green", "GR118")])
            PaoloVeroneseGreen_button.grid(row=8, column=5, padx=1, pady=2)

            PullmanGreen_button = tk.Button(page4, bg="#3B331C", width=4, height=3,command=lambda: [set_color(59, 51, 28), receipt("Pullman Green", "GR119")])
            PullmanGreen_button.grid(row=8, column=6, padx=1, pady=2)

            GreenScreen_button = tk.Button(page4, bg="#00B140", width=4, height=3,command=lambda: [set_color(0, 177, 64), receipt("Green Screen", "GR120")])
            GreenScreen_button.grid(row=8, column=7, padx=1, pady=2)

            AndroidGreen_button = tk.Button(page4, bg="#A4C639", width=4, height=3, command=lambda: [set_color(164, 198, 57), receipt("Android Green", "GR121")])
            AndroidGreen_button.grid(row=8, column=8, padx=1, pady=2)

            BitterLemon_button = tk.Button(page4, bg="#CAE00D", width=4, height=3, command=lambda: [set_color(202, 224, 13), receipt("Bitter Lemon", "GR122")])
            BitterLemon_button.grid(row=8, column=9, padx=1, pady=2)

            WageningenGreen_button = tk.Button(page4, bg="#34B233", width=4, height=3, command=lambda: [set_color(52, 178, 51), receipt("Wageningen Green", "GR123")])
            WageningenGreen_button.grid(row=8, column=10, padx=1, pady=2)

            SapGreen_button = tk.Button(page4, bg="#507D2A", width=4, height=3, command=lambda: [set_color(80, 125, 42), receipt("Sap Green", "GR124")])
            SapGreen_button.grid(row=8, column=11, padx=1, pady=2)

            OldMossGreen_button = tk.Button(page4, bg="#867E36", width=4, height=3, command=lambda: [set_color(134, 126, 54), receipt("Old Moss Green", "GR125")])
            OldMossGreen_button.grid(row=8, column=12, padx=1, pady=2)

            SlimyGreen_button = tk.Button(page4, bg="#299617", width=4, height=3, command=lambda: [set_color(41, 150, 23), receipt("Slimy Green", "GR126")])
            SlimyGreen_button.grid(row=8, column=13, padx=1, pady=2)

            VeryLightMalachiteGreen_button = tk.Button(page4, bg="#64E986", width=4, height=3, command=lambda: [set_color(100, 233, 134), receipt("Very Light Malachite Green", "GR127")])
            VeryLightMalachiteGreen_button.grid(row=9, column=0, padx=1, pady=2)

            DarkSpringGreen_button = tk.Button(page4, bg="#177245", width=4, height=3, command=lambda: [set_color(23, 114, 69), receipt("Dark Spring Green", "GR128")])
            DarkSpringGreen_button.grid(row=9, column=1, padx=1, pady=2)

            GuppieGreen_button = tk.Button(page4, bg="#00FF7F", width=4, height=3, command=lambda: [set_color(0, 255, 127), receipt("Guppie Green", "GR129")])
            GuppieGreen_button.grid(row=9, column=2, padx=1, pady=2)

            AppleGreen_button = tk.Button(page4, bg="#8DB600", width=4, height=3, command=lambda: [set_color(141, 182, 0), receipt("Apple Green", "GR130")])
            AppleGreen_button.grid(row=9, column=3, padx=1, pady=2)

            DeepGreen_button = tk.Button(page4, bg="#056608", width=4, height=3, command=lambda: [set_color(5, 102, 8), receipt("Deep Green", "GR131")])
            DeepGreen_button.grid(row=9, column=4, padx=1, pady=2)

            HookerGreen_button = tk.Button(page4, bg="#49796B", width=4, height=3, command=lambda: [set_color(73, 121, 107), receipt("Hooker Green", "GR132")])
            HookerGreen_button.grid(row=9, column=5, padx=1, pady=2)

            MediumSeaGreen_button = tk.Button(page4, bg="#3CB371", width=4, height=3, command=lambda: [set_color(60, 179, 113), receipt("Medium Sea Green", "GR133")])
            MediumSeaGreen_button.grid(row=9, column=6, padx=1, pady=2)

            TurquoiseGreen_button = tk.Button(page4, bg="#A0D6B4", width=4, height=3,command=lambda: [set_color(160, 214, 180), receipt("Turquoise Green", "GR134")])
            TurquoiseGreen_button.grid(row=9, column=7, padx=1, pady=2)

            def set_color(r, g, b):
                cv2.setTrackbarPos("Red", "Color Selection", r)
                cv2.setTrackbarPos("Green", "Color Selection", g)
                cv2.setTrackbarPos("Blue", "Color Selection", b)

            cv2.namedWindow("Color Selection")
            cv2.resizeWindow("Color Selection", 0, 0)

            cv2.createTrackbar("Red", "Color Selection", 0, 255, empty)
            cv2.createTrackbar("Green", "Color Selection", 0, 255, empty)
            cv2.createTrackbar("Blue", "Color Selection", 0, 255, empty)
            cv2.createTrackbar("BW <-> Color", "Color Selection", 1, 1, empty)

            while True:
                _, image = cap.read()
                finalimageoriginal = image.copy()
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                faces = detector(gray_image)
                b = cv2.getTrackbarPos("Blue", "Color Selection")
                g = cv2.getTrackbarPos("Green", "Color Selection")
                r = cv2.getTrackbarPos("Red", "Color Selection")

                if cv2.getTrackbarPos("BW <-> Color", "Color Selection"):
                    finalmakeup = finalimageoriginal
                else:
                    finalmakeup = cv2.cvtColor(finalimageoriginal, cv2.COLOR_BGR2GRAY)
                    finalmakeup = cv2.cvtColor(finalmakeup, cv2.COLOR_GRAY2BGR)

                gotFace = False

                for face in faces:
                    gotFace = True
                    x1, y1 = face.left(), face.top()
                    x2, y2 = face.right(), face.bottom()
                    landmarks = predictor(gray_image, face)
                    for n in range(68):
                        x = landmarks.part(n).x
                        y = landmarks.part(n).y
                        landmarkspoints.append([x, y])
                    landmarkspointsArr = np.array(landmarkspoints)
                    lipmask = np.zeros_like(image)
                    lipimage = cv2.fillPoly(lipmask, [landmarkspointsArr[48:70]], (255, 255, 255))
                    lipimagecolor = np.zeros_like(lipimage)
                    landmarkspoints = []
                    lipimagecolor[:] = b, g, r
                    lipimagecolor = cv2.bitwise_and(lipimage, lipimagecolor)
                    lipimagecolor = cv2.GaussianBlur(lipimagecolor, (7, 7), 10)
                    finalimage = cv2.addWeighted(finalmakeup, 1, lipimagecolor, 0.6, 0)

                if gotFace:
                    img = Image.fromarray(cv2.cvtColor(finalimage, cv2.COLOR_BGR2RGB))
                else:
                    img = Image.fromarray(cv2.cvtColor(finalmakeup, cv2.COLOR_BGR2RGB))

                img = img.resize((1200, 960))
                img_tk = ImageTk.PhotoImage(image=img)
                x = 0  # Adjust the x-coordinate according to your desired position
                y = 0  # Adjust the y-coordinate according to your desired position
                canvas.create_image(x, y, anchor=tk.NW, image=img_tk)
                canvas.image = img_tk

                window.update()

                if cv2.waitKey(1) == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()


        window1frame = Frame(window1)
        window1frame.pack(side=BOTTOM)


        def save_file():
            file = filedialog.asksaveasfilename(filetypes=[('PNG', '*.png')],
                                                defaultextension='.png')

            if file:
                screenshot = ImageGrab.grab()
                screenshot.save(file)

        start_button = tk.Button(window1frame, text="Open Camera", command=apply_makeup)
        start_button.grid(row=0, column=1, padx=20, pady=20)

        save_button = tk.Button(window1frame, text="Save The Picture", command=save_file)
        save_button.grid(row=0, column=2, padx=20, pady=20)

        window1.mainloop()


window = Tk()
window.title("Welcome To UMP Lipstick Cooperative")
window.geometry('1000x700+300+50')
window.resizable(0,0)

firstname=StringVar()
lastname=StringVar()
pnumber=StringVar()

user_info_frame = Frame(window, bd=6, relief=RIDGE, padx=10, pady=10)
user_info_frame.pack(side=TOP)

image1 = Image.open('bg1.png')     # Import image and set as window background
bck_end = ImageTk.PhotoImage(image1)
lbl = Label(window, image=bck_end)
lbl.pack(side=TOP)

image2 = Image.open('LogoUMP.png')      # Import image
resize_image1 = image2.resize((200,200))
img1 = ImageTk.PhotoImage(resize_image1)
Label1 = tk.Label(image=img1)
Label1.image = img1
Label1.place(x=25, y=25)

image3 = Image.open('Lipstick.jpeg')      # Import image
resize_image2 = image3.resize((255,240))
img2 = ImageTk.PhotoImage(resize_image2)
Label2 = tk.Label(image=img2)
Label2.image = img2
Label2.place(x=740, y=0)

user_info_frame = LabelFrame(user_info_frame, text="USER INFORMATION", font=('arial', 20, 'bold'),fg='Red4')
user_info_frame.pack(side=LEFT)

first_name_label = Label(user_info_frame, text="First Name", font=('arial', 18, 'bold'))
first_name_label.grid(row=0, column=0, sticky=W)
last_name_label = Label(user_info_frame, text="Last Name", font=('arial', 18, 'bold'))
last_name_label.grid(row=1, column=0, sticky=W)

first_name_entry = Entry(user_info_frame, font=('arial', 18, 'bold'), textvariable=firstname)
last_name_entry = Entry(user_info_frame, font=('arial', 18, 'bold'), textvariable=lastname)
first_name_entry.grid(row=0, column=1)
last_name_entry.grid(row=1, column=1)

phone = Label(user_info_frame, text="Phone Number", font=('arial', 18, 'bold'))
phone.grid(row=2, column=0, sticky=W)
phone_entry = Entry(user_info_frame, font=('arial', 18, 'bold'), textvariable=pnumber)
phone_entry.grid(row=2, column=1)

button = Button(user_info_frame, text="Enter Data", font=('arial', 18, 'bold'), command=information_user)
button.grid(row=5, column=1, sticky="news", padx=20, pady=10)

window.mainloop()