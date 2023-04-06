from tkinter import *

root = Tk()

# COLORS
bg_clr = "#F5F5F5"
primary_clr = "#2196F3"
btn_clr = "#FF5722"

# FONTS
title_font = ("open sans", 24, "bold")
body_font = ("Georgia", 12)
btn_font = ("Lato", 14, "bold")

# GENERAL SETUP
root.title('Gestion Clients')
root.geometry('900x600+150+50')
root.resizable(False, False)
root.iconbitmap('customer.ico')

# Header Frame
# bd = border
header = Frame(root, bg=primary_clr)
header.pack(side=TOP, fill=X)

# footer
footer = Frame(root, bg=primary_clr)
footer.pack(side=BOTTOM, fill=X)
# login and signup frame
login = Frame(root)
sign_up = Frame(root)
admin = Frame(root)


def to_login():
    login.pack(fill='both', expand=1)
    sign_up.pack_forget()
    body.pack_forget()


def to_signup():
    sign_up.pack(fill='both', expand=1)
    login.pack_forget()
    body.pack_forget()


def to_home():
    body.pack(fill='both', expand=1)
    sign_up.pack_forget()
    login.pack_forget()
    # admin.pack_forget()


# c1
def show_password():
    if textCheck.get() == 1:
        text_Password.config(show='')
    else:
        text_Password.config(show='*')


# c2
def check_p():
    if loginCheck.get() == 1:
        login_password.config(show='')
    else:
        login_password.config(show='*')


def signup():
    with open('clients', 'a') as file:
        file.write(f'\nCode: {textCode.get()} | nom : {textNom.get()} | prenom : {textPrenom.get()} | ville : {textVille.get()} | gmail : {textGmail.get()} | password : {textPassword.get()} | genre : {textGenre.get()}')
    to_login()


def check_login():
    with open('clients', 'r') as file:
        lines = file.readlines()
    for line in lines:
        data = line.strip().split(' | ')
        email = data[4].split(': ')[1]
        password = data[5].split(': ')[1]

        if email == loginGmail.get() and password == loginPassword.get():
            to_home()
        else:
            to_signup()


# header
logo_button = Button(header, text="Gestion Client", bg=primary_clr, fg="#fff", font=body_font, cursor='hand2', bd=0, activebackground=primary_clr, activeforeground="#fff", command=to_home)
logo_button.pack(side=LEFT, padx=10, pady=10)

signup_button = Button(header, text="Sign Up", bg=primary_clr, command=to_signup, fg="#fff", font=body_font, cursor='hand2', bd=0, activebackground=primary_clr, activeforeground="#fff")
signup_button.pack(side=RIGHT, padx=10, pady=10)

login_button = Button(header, text="Login", bg=primary_clr, command=to_login, fg="#fff", font=body_font, cursor='hand2', bd=0, activebackground=primary_clr, activeforeground="#fff")
login_button.pack(side=RIGHT, padx=10, pady=10)

home_button = Button(header, text="Home", bg=primary_clr, command=to_home, fg="#fff", font=body_font, cursor='hand2', bd=0, activebackground=primary_clr, activeforeground="#fff")
home_button.pack(side=RIGHT, padx=10, pady=10)

# footer
logo_button = Label(footer, text="Created By : Ayoub Mouhssine", bg=primary_clr, fg="#fff", font=body_font, bd=0, activebackground=primary_clr, activeforeground="#fff")
logo_button.pack(side=LEFT, padx=10, pady=10)

login_button = Label(footer, text="2023 - 2024", bg=primary_clr, fg="#fff", font=body_font, bd=0, activebackground=primary_clr, activeforeground="#fff")
login_button.pack(side=RIGHT, padx=10, pady=10)

signup_button = Label(footer, text="All Right Reserved", bg=primary_clr, fg="#fff", font=body_font, bd=0, activebackground=primary_clr, activeforeground="#fff")
signup_button.pack(side=RIGHT, padx=10, pady=10)


# signup frame
lbl_title = Label(sign_up, text="Signup Page", font=title_font, fg=primary_clr)
lbl_title.pack()

lbl_code = Label(sign_up, text="Code :", font=body_font, width=8, height=1, bg='lightBlue', fg='black')
lbl_code.place(x=50, y=40)

lbl_nom = Label(sign_up, text="Nom:", font=body_font, width=8, height=1, bg='lightBlue', fg='black')
lbl_nom.place(x=50, y=80)

lbl_prenom = Label(sign_up, text="Prenom:", font=body_font, width=8, height=1, bg='lightBlue', fg='black')
lbl_prenom.place(x=50, y=120)

lbl_ville = Label(sign_up, text="Ville :", font=body_font, width=8, height=1, bg='lightBlue', fg='black')
lbl_ville.place(x=50, y=160)

lbl_ville = Label(sign_up, text="Gmail :", font=body_font, width=8, height=1, bg='lightBlue', fg='black')
lbl_ville.place(x=50, y=200)

lbl_ville = Label(sign_up, text="Password :", font=body_font, width=8, height=1, bg='lightBlue', fg='black')
lbl_ville.place(x=50, y=240)

lbl_login = Label(sign_up, text='Vous avez déjà un compte?', font=body_font, width=25, height=1, bg='lightBlue', fg='black')
lbl_login.place(x=50, y=400)

lbl_genre = Label(sign_up, text="Genre :", font=body_font, width=8, height=1, bg='lightBlue', fg='black')
lbl_genre.place(x=50, y=320)

# signup Entry
textCode = IntVar()
textNom = StringVar()
textPrenom = StringVar()
textVille = StringVar()
textGmail = StringVar()
textPassword = StringVar()
textGenre = StringVar()
textCheck = IntVar(value=0)

text_code = Entry(sign_up, textvariable=textCode, font=body_font, width=25,)
text_code.place(x=200, y=40)

text_nom = Entry(sign_up, textvariable=textNom, font=body_font, width=25, )
text_nom.place(x=200, y=80)

text_prenom = Entry(sign_up, textvariable=textPrenom, font=body_font, width=25, )
text_prenom.place(x=200, y=120)

text_ville = Entry(sign_up, textvariable=textVille, font=body_font, width=25, )
text_ville.place(x=200, y=160)

text_Gmail = Entry(sign_up, textvariable=textGmail, font=body_font, width=25, )
text_Gmail.place(x=200, y=200)

text_Password = Entry(sign_up, textvariable=textPassword, font=body_font, width=25, show='*')
text_Password.place(x=200, y=240)

# signup radio Buttons
rdBtn_femme = Radiobutton(sign_up, text='Femme', value='femme', variable=textGenre, font=body_font, )
rdBtn_femme.place(x=200, y=320)

rdBtn_homme = Radiobutton(sign_up, text='Homme', value='Homme', variable=textGenre, font=body_font, )
rdBtn_homme.place(x=350, y=320)

# signup : show password
c1 = Checkbutton(sign_up, text='Show Password', variable=textCheck, onvalue=1, offvalue=0, command=show_password)
c1.place(x=200, y=280)

#  button : login and sign up button's
btn_sign = Button(sign_up, text='Sign Up', font=body_font, bg='lightGreen', fg='red', width=25, command=signup)
btn_sign.place(x=200, y=360)

btn_logIn = Button(sign_up, text='Log In', font=body_font, bg='lightGreen', fg='red', width=25, command=check_login)
btn_logIn.place(x=200, y=440)

# login frame
loginGmail = StringVar()
loginPassword = StringVar()
loginCheck = IntVar(value=0)

lbl_title = Label(login, text="Login In Page", font=title_font, fg=primary_clr)
lbl_title.pack()

lbl_gmail = Label(login, text="Gmail :", font=body_font, width=9, height=1, bg='lightBlue', fg='black')
lbl_gmail.place(x=50, y=100)

lbl_password = Label(login, text="Password :", font=body_font, width=9, height=1, bg='lightBlue', fg='black')
lbl_password.place(x=50, y=140)

login_gmail = Entry(login, textvariable=loginGmail, font=body_font, width=25, )
login_gmail.place(x=220, y=100)

login_password = Entry(login, textvariable=loginPassword, font=body_font, width=25, show='*')
login_password.place(x=220, y=140)


c2 = Checkbutton(login, text='Show Password', variable=loginCheck, onvalue=1, offvalue=0, command=check_p)
c2.place(x=220, y=180)

# buttons
btn_ajouter = Button(login, text='Log In', font=body_font, bg='lightGreen', fg='red', width=13, command=check_login)
btn_ajouter.place(x=200, y=240)

# frame : body
body = Frame(root, width=900, height=600)
body.pack()

# frame : back_img
left_body = Frame(body, width=450, height=600)
left_body.place(x=0, y=0)

back_img = PhotoImage(file='imgs/Bookshop-bro.png')

back = Label(left_body, image=back_img, bg='white')
back.place(x=0, y=0, width=450, height=600)

# frame : back_txt
right_body = Frame(body, width=450, height=600)
right_body.place(x=450, y=0)

welcome_txt = Label(right_body, text="Gestion Clients\n is an application that helps\n users efficiently manage client data.", font=('Courier', 15))
welcome_txt.place(x=0, y=30)

# social media
profile = PhotoImage(file='imgs/logo-m.png')
face = PhotoImage(file='imgs/facebook.png')
insta = PhotoImage(file='imgs/insta.png')
git = PhotoImage(file='imgs/github.png')

def facebook():
    import webbrowser
    url = 'https://www.facebook.com/ayoub.mouhssine.75/'
    webbrowser.open(url)

def instagram():
    import webbrowser
    url = 'https://www.instagram.com/mouhssineayoub/'
    webbrowser.open(url)


def github():
    import webbrowser
    url = 'https://github.com/AyoubMouhssine'
    webbrowser.open(url)


side_title2 = Label(right_body, text='Social Media', fg='black', font=('Courier', 15))
side_title2.place(x=25, y=150)

b2 = Button(right_body, text='facebook', cursor='hand2', image=face, bg='whiteSmoke', compound=TOP, width=130, bd=0, relief=RIDGE, command=facebook)
b2.place(x=20, y=200)

b3 = Button(right_body, text='instagram', cursor='hand2', image=insta, bg='whiteSmoke', compound=TOP, width=130, bd=0, relief=RIDGE, command=instagram)
b3.place(x=150, y=200)

b4 = Button(right_body, text='github', cursor='hand2', image=git , bg='whiteSmoke', compound=TOP, width=130, bd=0, relief=RIDGE, command=github)
b4.place(x=280, y=200)

# our team
side_title3 = Label(right_body, text='Our Team', fg='black', font=('Courier', 15))
side_title3.place(x=25, y=330)

b1 = Button(right_body, text='Ayoub Mouhssine', image=profile,bg='whiteSmoke', compound=TOP, cursor='hand2', bd=0, relief=RIDGE, width=120)
b1.place(x=25, y=380)

root.mainloop()