import tkinter
import webbrowser

mainWindow = tkinter.Tk()


mainWindow.title('Nikodem Mucha CV')
mainWindow.geometry('1680x960')
mainWindow.maxsize(1690, 960)
mainWindow.minsize(1690, 960)
mainWindow.configure(bg='black')

entry_text = '>Welcome to little submission of my life'


mainWindow.columnconfigure(0, weight=300)
mainWindow.columnconfigure(1, weight=500)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
mainWindow.columnconfigure(4, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)


def go(text, placement, counter=1):
    placement.config(text=text[:counter], bg='black', fg='green', font='times, 22', borderwidth=0)
    if counter < len(text):
        mainWindow.after(45, lambda: go(text, placement, counter+1))


def callback_and_hide(button, text, placement):
    go(text, placement)
    button.grid_forget()


def linkedin():
    webbrowser.open_new(r"https://www.linkedin.com/in/nikodem-mucha-338829229/")


def github():
    webbrowser.open_new(r"https://github.com/Vulpeslnculta")


start_button = tkinter.Button(mainWindow, text='>Begin the journey!',
                              command=lambda: callback_and_hide(start_button, entry_text, label),
                              background='black', foreground='black', borderwidth=0)
start_button.grid(rowspan=2, columnspan=2)
start_button.place(y=50, x=100000)


label = tkinter.Button(mainWindow)
label.grid(rowspan=2, columnspan=2)
label.place(x=50, y=50)

start_button.invoke()
# TEXTS

education_txt = '> I have completed Wislawa Szymborska high school no. IX in Sosnowiec' \
                ' at biochemistry specialisation in 2021,\n ' \
                '> after graduation I\'ve successfully qualified for AGH university of science on field of\n' \
                '> biomedical engineering, where I had my first contact with programming at all, and that\'s \n' \
                '> where it all begun. From the next academical year I want to start extramural studies on\n' \
                '> Computer Science to develop my skills and myself.'
aboutme_txt = '> Time to introduce myself.\n' \
        '> Hello!\n> I\'m Nikodem Mucha, I\'m 19 years old, and I\'m trying to put my first step into world of coding\n' \
        '> I\'m from Silesian Voivodeship, but currently I live in Cracow from beginning of July 2021.\n' \
        '> I feel quite confident about using English, I would place my abilities to operate in this language between\n' \
        '> C1 and C2, Polish is my native language.'

courses_txt = '> Throughout beginning of 2022 I have completed two courses since:\n' \
              '> Python Programming Masterclass by Tim Buchalka\n' \
              '> The Complete SQL Bootcamp 2022: Go from Zero to Hero by Jose Portilla\n' \
              '>\n' \
              '> Both of courses are available on Udemy and are certified. Both of my certificates are' \
              ' published on my LinkedIn\n' \
              '> I\'ve caught a glimpse of C and R language on university.'

passions_txt = '> Here is some of my passions and hobbies:\n' \
               '> Music: I was playing in a band for 4 years straight as a bassist, now I\'m learning how to use\n' \
               '> Ableton Live to create something on my own.\n' \
               '>\n' \
               '> Automotive: I\'m absolutely fascinated about everything with wheels and engine, currently \n' \
               '> I\'m a proud owner of a motorcycle, but I hope that my collection will thrive in few years\n' \
               '>\n' \
               '> IT: That\'s not just a thing that I wanna do, but also my great passion, and something I want to\n' \
               '> learn about and be as good as it\'s possible at it!'
expirience_txt = '> Unfortunately I don\'t have any experience in real programming work environment,\n' \
                 '> but I really hope that your company is the one who would give me a chance to blossom' \


label2 = tkinter.Label(mainWindow, bg='black')
label2.grid(rowspan=2, columnspan=2)
label2.place(x=200, y=350)

button1 = tkinter.Button(text='>My education', bg='black', fg='green', borderwidth=0,
                         command=lambda: callback_and_hide(start_button, education_txt, label2))
button1.grid(sticky='nw', rowspan=1)
button1.place(x=10, y=150)

button2 = tkinter.Button(text='>My courses and certificates', bg='black', fg='green', borderwidth=0,
                         command=lambda: callback_and_hide(start_button, courses_txt, label2))
button2.grid(sticky='sw', rowspan=1)
button2.place(x=10, y=200)

button3 = tkinter.Button(text='>My passions', bg='black', fg='green', borderwidth=0,
                         command=lambda: callback_and_hide(start_button, passions_txt, label2))
button3.grid(sticky='nw', rowspan=1)
button3.place(x=10, y=250)

button4 = tkinter.Button(text='>My work experience', bg='black', fg='green', borderwidth=0,
                         command=lambda: callback_and_hide(start_button, expirience_txt, label2))
button4.grid(sticky='sw', rowspan=1)
button4.place(x=10, y=300)

button5 = tkinter.Button(text='>About me', bg='black', fg='green', borderwidth=0,
                         command=lambda: callback_and_hide(start_button, aboutme_txt, label2))
button5.grid(sticky='nw', rowspan=1)
button5.place(x=10, y=350)

button6 = tkinter.Button(text='>LinkedIn', bg='black', fg='green', borderwidth=0,
                         command=linkedin)
button6.grid(sticky='nw', rowspan=1)
button6.place(x=10, y=650)

button7 = tkinter.Button(text='>GitHub', bg='black', fg='green', borderwidth=0,
                         command=github)
button7.grid(sticky='nw', rowspan=1)
button7.place(x=10, y=700)

button8 = tkinter.Button(text='>Exit', bg='black', fg='green', borderwidth=0,
                         command=mainWindow.destroy)
button8.grid(sticky='nw', rowspan=1)
button8.place(x=1600, y=20)


mainWindow.mainloop()
