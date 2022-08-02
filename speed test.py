from tkinter import *
import speedtest

window = Tk()
window.geometry("360x600") 
window.config(bg="#49dbdb")
window.title("Internet Speed Test")
icon_photo = PhotoImage(file = "logo.png")
window.iconphoto(False,icon_photo)
window.resizable(False,False)

def click():
    test = speedtest.Speedtest()
    download_update = round(test.download()/(1024*1024),2)
    upload_update = round(test.upload()/(1024*1024),2)
    server = []
    test.ger_servers(server)
    ping_update = round(test.results.ping/(1024*1024),2)
    ping.config(text=ping_update)
    download.config(text=download_update)
    Upload.config(text=upload_update)
    Download_1.config(text=download_update)

        
Top_image = PhotoImage(file="top.png")
Top = Label(window, image=Top_image, bg="#49dbdb")
Top.pack()

main_image = PhotoImage(file="main.png")
main = Label(window, image=main_image, bd=0, bg="#49dbdb")
main.pack(pady=(30,0))

button_image = PhotoImage(file="button.png")
button = Button(window, image=button_image, bg="#49dbdb", bd=0, activebackground="#49dbdb", command=click(), cursor="hand2")
button.pack(pady=20)

ping = Label(window, text="PING", font="arial 10 bold", bg="#49dbdb", fg="white")
ping.place(x=50, y=0)

download = Label(window, text="DOWNLOAD", font="arial 10 bold", bg="#49dbdb", fg="white")
download.place(x=140, y=0)

Upload = Label(window, text="UPLOAD", font="arial 10 bold", bg="#49dbdb", fg="white")
Upload.place(x=265, y=0)

MS = Label(window, text="MS", font="arial 10 bold", bg="#49dbdb", fg="white")
MS.place(x=51,y=75)

mbps = Label(window, text="MBPS", bg="#49dbdb", fg="white", font="arial 10 bold")
mbps.place(x=159,y=75)

mbps_2 = Label(window, text="MBPS", bg="#49dbdb", fg="white", font="arial 10 bold")
mbps_2.place(x=275,y=75)

Download_1 = Label(window, text="DOWLOAD", font="Arial 15 bold", bg="#49dbdb", fg="white")
Download_1.place(x=130,y=280)

mbps_3 = Label(window, text="MBPS", bg="#49dbdb", fg="white", font="arial 15 bold")
mbps_3.place(x=150,y=380)

ping_2= Label(window, text="00", font="arial 15 bold", bg="#49dbdb", fg="white")
ping_2.place(x=65,y=60, anchor="center")

download_1= Label(window, text="00", font="arial 15 bold", bg="#49dbdb", fg="white")
download_1.place(x=180,y=60, anchor="center")

upload_1= Label(window, text="00", font="arial 15 bold", bg="#49dbdb", fg="white")
upload_1.place(x=295,y=60, anchor="center")

Download_1 = Label(window, text="00", font="arial 40 bold", bg="#49dbdb", fg="#000")
Download_1.place(x=185,y=340, anchor="center")


window.mainloop()