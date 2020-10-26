from tkinter import *
from tkinter import messagebox
from selenium import webdriver

def web():
    if var_1.get() == '1':
        search_text = var_2.get()
        begin = webdriver.Chrome() #使用Chrome webdriver
        begin.get('https://www.google.com') #Google首頁
        inputElement = begin.find_element_by_name("q") #尋找搜索框
        inputElement.send_keys(search_text) #輸入搜尋字元
        inputElement.submit()
        with open('record.txt', 'a') as a:
            search_record = var_2.get()
            a.write(search_record + '\n')
            text.append(a)
           
    if var_1.get() == '2':
        search_text = var_2.get()
        begin = webdriver.Firefox() #使用Firefox webdriver
        begin.get('https://www.google.com') #Google首頁
        inputElement = begin.find_element_by_name("q") #尋找搜索框
        inputElement.send_keys(search_text) #輸入搜尋字元
        inputElement.submit()
        with open('record.txt', 'a') as a:
            search_record = var_2.get()
            a.write(search_record + '\n')
            text.append(a)
def read():
    with open('record.txt', 'r') as readtext:
        readtext_1 = readtext.read()
        readtext_1
        label5['text'] = readtext_1
def clear_txt():
    try: 
        text_list = []
        with open('record.txt', 'r') as readtext:
            readtext_1 = readtext.read()
            for del_txt in readtext_1:
                text_list.append(del_txt)
                for del_txt1 in text_list[:]:
                    text_list.remove(del_txt1)
                    label5['text'] = text_list
                    with open('record.txt', 'w') as write_clear:
                        
                            if text_list == []:
                                text_list = ''
                            write_clear.write(str(text_list))
    except Exception:
        print()

def about():
    messagebox.showinfo('Search_V1.1', '內容:\n\n\
        更新GoogleDriver版本(86.0.4240.22)')

window = Tk()
window.geometry('310x250')
window.title('search 1.1')

menu = Menu(window)
window.config(menu=menu)

filemenu = Menu(menu, activebackground='green')
menu.add_cascade(label='選單', menu=filemenu)
filemenu.add_command(label='內容', command=about)
filemenu.add_separator()
filemenu.add_command(label='離開', command=window.destroy)

text = []

var_1 = StringVar()
var_1.set('1')
var_2 = StringVar()

label1 = Label(window, text='Search Launcher', bg='yellow', font='NotoSansTC-Thin 15 bold')
label1.grid(row=0, column=1, padx=2, pady=5)
label2 = Label(window, text='輸入搜尋字')
label2.grid(row=1)
label3 = Label(window, text='選擇搜尋引擎', font='NotoSansTC-Thin 10 bold')
label3.place(x=20, y=80)
label4 = Label(window, text='搜尋紀錄', font='NotoSansTC-Thin 10 bold')
label4.place(x=160, y=80)
label5 = Label(window, width=15, height=8, bg='Gainsboro', justify='left', relief='groove')
label5.place(x=140, y=110)

entry1 = Entry(window, textvariable=var_2)
entry1.grid(row=1, column=1)

btn1 = Button(window, text='Search', command=web)
btn1.grid(row=1, column=2)
btn2 = Button(window, text='History', command=read)
btn2.place(x=255, y=110)
btn3 = Button(window, text='Clear', command=clear_txt)
btn3.place(x=260, y=140)

rb1 = Radiobutton(window, text='Chrome', variable=var_1, value='1')
rb1.place(x=30, y=100)
rb2 = Radiobutton(window, text='Firefox', variable=var_1, value='2')
rb2.place(x=30, y=120)

window.mainloop()