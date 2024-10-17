# -*- coding: utf-8 -*-
import datetime
import random
import re
import smtplib
import sqlite3
import string
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.messagebox as msg
import uuid
import webbrowser
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
from tkinter.font import Font

import matplotlib.pyplot as plt
import mysql
import mysql.connector
import mysql.connector
import qrcode
from PIL import Image, ImageTk

mydb = mysql.connector.connect(
    host="localhost",
    user="admin", # a modifier
    password="admin", #a modifier
    database="register_login"
)


mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS register_login")
mydb.commit()


def accee():
    window.destroy()
    connector = sqlite3.connect('NEW_STUDENT_DATABASE.db')
    cursor = connector.cursor()

    class App:
        def __init__(self, master):

            self.master = master
            master.title('BIENVENUE CHEZ ENSAH SERVICES')
            master.geometry('1000x700')
            master.resizable(0, 0)

            self.headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
            self.labelfont = ('Garamond', 14)
            self.entryfont = ('Garamond', 12)

            menubar = Menu(master)

            menubar = Menu(master, background='white', foreground='black', font=('Arial', 12), relief='groove',
                           disabledforeground='gray', postcommand=self.post_menu, tearoffcommand=self.tearoff_menu)

            file_menu = Menu(menubar, tearoff=0, activebackground='light blue', activeforeground='white', bd=2,
                             background='white', foreground='black', font=('Magneto', 11), relief='groove',
                             disabledforeground='gray', postcommand=self.post_menu, tearoffcommand=self.tearoff_menu)
            file_menu.add_command(label="Quitter", command=self.quit_app, underline=0, compound="left")
            menubar.add_cascade(label="DECONNEXION", menu=file_menu)

            about_menu = Menu(menubar, tearoff=0, activebackground='light blue', activeforeground='white', bd=2,
                              background='white', foreground='black', font=('Magneto', 11), relief='groove',
                              disabledforeground='gray', postcommand=self.post_menu, tearoffcommand=self.tearoff_menu)
            about_menu.add_command(label="À propos de nous", command=self.about_us, underline=0, compound="left")
            menubar.add_cascade(label="A PROPOS DE NOUS", menu=about_menu)

            captcha_menu = Menu(menubar, tearoff=0, activebackground='light blue', activeforeground='white', bd=2,
                                background='white', foreground='black', font=('Magneto', 11), relief='groove',
                                disabledforeground='gray', postcommand=self.post_menu, tearoffcommand=self.tearoff_menu)
            captcha_menu.add_command(label="Générer Code Bar Captcha", command=self.generate_qr_code, underline=0,
                                     compound="left")
            menubar.add_cascade(label="Code Bar Captcha", menu=captcha_menu)

            master.config(menu=menubar)

            self.border_canvas = Canvas(master, highlightthickness=0, width=1000, height=700)
            self.border_canvas.place(x=0, y=0)

            self.border_canvas.create_line(0, 50, 1000, 50, fill='green', smooth=True, width=3)
            self.border_canvas.create_line(0, 70, 1000, 70, fill='green', smooth=True, width=3)

            master.configure(bg="#f2f2f2")

            self.lf_bg = "#808080"
            self.left_frame = Frame(master, bg=self.lf_bg, bd=1, relief=SOLID)
            self.left_frame.place(x=260, y=30, relheight=1, relwidth=0.5)

            self.left_frame.config(highlightthickness=1, highlightbackground="#bfbfbf", highlightcolor="#bfbfbf")

            self.search_frame = ttk.Frame(master, borderwidth=2, relief="groove", style="Search.TFrame")
            self.search_frame.place(relx=0.5, rely=0.15, anchor="center")

            s = ttk.Style()
            s.theme_use('default')
            s.configure('Search.TFrame', borderwidth=0, bordercolor="#EFEFEF", background="#F0F0F0", padding=5,
                        relief="solid",
                        borderradius=10)

            s = ttk.Style()
            s.configure('My.TLabel', foreground='black')

            self.search_frame = ttk.Frame(master, borderwidth=2, relief="groove", style="Search.TFrame")
            self.search_frame.place(relx=0.5, rely=0.15, anchor=CENTER)

            self.search_label = ttk.Label(self.search_frame, text="Recherche :", background='silver', style="My.TLabel")
            self.search_label.pack(side="left", padx=10)

            search_icon = Image.open("images/18.png")
            search_icon = search_icon.resize((20, 20), Image.ANTIALIAS)
            search_icon = ImageTk.PhotoImage(search_icon)

            icon_label = ttk.Label(self.search_frame, image=search_icon)
            icon_label.image = search_icon
            icon_label.pack(side="left")

            self.search_entry = ttk.Entry(self.search_frame, font=('Garamond', 12), width=20, style="Search.TEntry")
            self.search_entry.pack(side="left", padx=10, pady=5)

            s.configure('Search.TEntry', borderwidth=0, background="#EFEFEF", foreground="#333333", padding=5,
                        relief="solid", bordercolor="black", bordertype="cut", borderradius=10)

            s.configure('Search.TFrame', background="#F0F0F0", borderwidth=0, bordercolor="#F0F0F0")

            self.search_button = ttk.Button(self.search_frame, text="Rechercher",
                                            command=self.search_click,
                                            style="Search.TButton")
            self.search_button.pack(side="left", padx=10, pady=5)

            s.configure('Search.TButton', borderwidth=0, background="#ADD8E6", foreground="#FFFFFF", padding=5,
                        relief="groove", borderradius=10,
                        focuscolor="#ADD8E6", focusthickness=2)

            self.lf_bg = '#808080'
            self.left_frame = Frame(master, bg=self.lf_bg)
            self.left_frame.place(x=260, y=200, relheight=1, relwidth=0.5)

            photo1 = Image.open('images/7.png')
            photo1 = photo1.resize((400, 400), resample=Image.LANCZOS)
            self.photo1 = ImageTk.PhotoImage(photo1)

            photo3 = Image.open('images/6.png')
            photo3 = photo3.resize((400, 400), resample=Image.LANCZOS)
            self.photo3 = ImageTk.PhotoImage(photo3)

            photo4 = Image.open('images/8.jpg')
            photo4 = photo4.resize((400, 400), resample=Image.LANCZOS)
            self.photo4 = ImageTk.PhotoImage(photo4)

            self.photo_frame = Frame(self.left_frame, bg='white', width=500, height=200)
            self.photo_frame.pack(pady=10)

            self.photo_label1 = Label(self.photo_frame, image=self.photo1)
            self.photo_label1.pack()

            self.current_photo = 1
            self.slideshow()

            self.background_image = Image.open("images/13.png")
            self.resized_image = self.background_image.resize((1000, 700), resample=Image.LANCZOS)
            self.background_image = ImageTk.PhotoImage(self.resized_image)
            self.background_label = Label(master, image=self.background_image)
            self.background_label.place(x=-730, y=30, relwidth=1, relheight=1)

            self.emp_button = Button(master, text="Emploi du temps", font=self.labelfont, command=self.emp_click,
                                     bg='#c0c0c0', fg='black', activebackground='#1E90FF', activeforeground='white',
                                     borderwidth=2)
            self.emp_button.place(x=50, y=100, height=50, width=200)

            self.cours_button = Button(master, text="Cours", font=self.labelfont, command=self.cours_click,
                                       bg='#868686',
                                       activebackground='black', activeforeground='white', borderwidth=2)
            self.cours_button.place(x=50, y=200, height=50, width=200)

            self.notes_button = Button(master, text="Affichage des notes", font=self.labelfont,
                                       command=self.notes_click,
                                       bg='#222', fg='white', activebackground='#444', activeforeground='white',
                                       borderwidth=2)
            self.notes_button.place(x=50, y=300, height=50, width=200)

            self.profil_button = Button(master, text="Profil", font=self.labelfont, command=self.profil_click,
                                        bg='#add8e6',
                                        activebackground='#F5F5F5', activeforeground='black', borderwidth=2)
            self.profil_button.place(x=50, y=500, height=50, width=200)

            self.demande_button = Button(master, text="Nouvelle demande", font=self.labelfont,
                                         command=self.show_demande,
                                         bg="#799ba1", fg='white', padx=10, activebackground="#6495ED",
                                         activeforeground="white", borderwidth=2)
            self.demande_button.place(x=50, y=400, height=50, width=200)

            self.personnel_button = Button(master, text="Personnel", font=self.labelfont, command=self.show_professeurs,
                                           bg="#effdff", fg='black', padx=10, activebackground="#6495ED",
                                           activeforeground="black", borderwidth=2)
            self.personnel_button.place(x=50, y=600, height=50, width=200)

            history_font = ("Bodoni MT Black", 12, "bold", "underline",)

            self.history_label = Label(master, text="Historique", bg='blue', fg='#4EF500', font=history_font,
                                       justify='center')
            self.history_label.place(x=780, y=100, height=50, width=200)

            self.history_listbox = Listbox(master, font=self.entryfont, width=30)
            self.history_listbox.configure(bg='white', fg='black')
            self.history_listbox.place(x=780, y=150, height=300, width=200)

            master.style = ttk.Style()
            master.style.configure('my.TButton',
                                   background='#5c4e4d',
                                   foreground='white',
                                   font=('Arial', 9, 'bold'),
                                   padding=5,
                                   relief='flat',
                                   borderwidth=0,
                                   width=15,
                                   anchor='center')


            master.style.map('my.TButton',
                             background=[('active', '#a2938d')],
                             foreground=[('active', 'white')])

            self.extrascolaires_button = ttk.Button(master, text="ACTIVITÉS EXTRASCOLAIRES", command=self.show_clubs,
                                                    style="my.TButton")
            self.extrascolaires_button.place(x=780, y=550, height=50, width=200)

            self.joined_clubs = []
            self.available_clubs = []

            self.stats_button = ttk.Button(master, text="STATISTIQUES", command=self.show_stats, style="my.TButton")
            self.stats_button.place(x=780, y=610, height=50, width=200)
            self.stats = []

            master.style.map("my.TButton",
                             foreground=[("pressed", "green"), ("active", "white")],
                             background=[("pressed", "!disabled", "#5c4e4d"), ("active", "#a2938d")],
                             bordercolor=[("pressed", "!disabled", "blue"), ("active", "blue")],
                             borderwidth=[("pressed", 1), ("active", 1)],
                             relief=[("pressed", "solid"), ("active", "groove")])

            s = ttk.Style()
            s.configure('my.TButton', borderwidth=0, background="lightblue", foreground="black", padding=5,
                        relief="groove", borderradius=10,
                        focuscolor="#ADD8E6", focusthickness=2)

            footer = Label(master, text="E-SERVICES © Copyright 2023 - Développée par O.HAI-J.BACHIRI-F.CHAKIR.",
                           font=("Helvetica", 12, "italic"), bg='white')
            footer.pack(side=BOTTOM, fill=X)

            self.demande_frame = None
            self.filepath = StringVar()

            self.demande_email = "email" # a modifier
            self.etudiant_email = "votre-email@ensah.ma" #a modifier

            history_font = ("Castellar", 10, "bold", "underline",)
            self.last_consultation_label = Label(master, text="", font=history_font, bg='blue', fg='white')
            self.last_consultation_label.place(x=780, y=460, height=50, width=200)
            self.update_last_consultation()

            def create_animated_welcome_label(master):
                static_label = Label(master, text="E-service ENSAH", font=("Arial", 14, "bold"), bg='blue')
                static_label.pack(side=TOP, fill=X)

                welcome_text = Label(master, text="", font=("Arial", 12, "bold italic"), fg="#0091D0")
                welcome_text.config(relief=SOLID)
                welcome_text.config(highlightbackground="#0091D0", highlightthickness=2)
                welcome_text.place(x=300, y=40)

                text = "Bienvenue sur la plateforme de consultation ENSAH  "

                def animate_text():
                    nonlocal text
                    text = text[-1] + text[:-1]
                    welcome_text.config(text=text)
                    welcome_text.after(90, animate_text)

                animate_text()

            create_animated_welcome_label(master)

        def generate_qr_code(self):

            mydb = mysql.connector.connect(host="localhost", port=3306, user="admin", password="admin",
                                           database='register_login')
            mycursor = mydb.cursor()
            mycursor.execute(
                "CREATE TABLE IF NOT EXISTS etudiant (name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, genre VARCHAR(255) NOT NULL, phone INT NOT NULL, birthday DATE NOT NULL, filier VARCHAR(50) NOT NULL, password VARCHAR(255) NOT NULL, qrcode VARCHAR(255) )")
            qr_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            mycursor.execute("SELECT * FROM new_student_database WHERE password = %s", (p,))
            etudiant = mycursor.fetchone()
            sql = "INSERT INTO etudiant (name, email, phone, genre, birthday, filier, password, qrcode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (
                etudiant[0], etudiant[1], etudiant[2], etudiant[3], etudiant[4], etudiant[5], etudiant[6], qr_text)
            mycursor.execute(sql, val)
            mydb.commit()

            qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5
            )
            qr.add_data(qr_text)
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color="black", back_color="white")


            file_name = f"{etudiant[1]}_{etudiant[2]}images/1.png"
            qr_image.save(file_name)


            self.master.destroy()
            k = tk.Tk()
            k.geometry("300x300")
            k.title("qr code")
            k.configure(bg="#272A37")

            img = PhotoImage(file=file_name)
            label = Label(k, image=img)
            label.pack()
            k.mainloop()

        def show_stats(self):
            self.mydb = mysql.connector.connect(host='localhost', port=3306, user='admin', password='admin',
                                                database='register_login')
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute("select username from login")
            users = self.mycursor.fetchall()
            conn_per_user = {user[0]: 0 for user in users}
            for user in users:
                self.mycursor.execute("select count(*) from login where  username=%s", (user[0],))
                count = self.mycursor.fetchone()[0]
                conn_per_user[user[0]] = count
            fig, ax = plt.subplots()
            ax.bar(list(conn_per_user.keys()), list(conn_per_user.values()))
            ax.set_xlabel('Utilisateur')
            ax.set_ylabel('Nombre de connexions')
            ax.set_title('Nombre de connexions des utilisateurs à l\'application')
            plt.show()

        def on_closing(self, window):
            if messagebox.askokcancel("Quit", "Voulez vous quitter?"):
                window.destroy()

        def show_clubs(self):
            def join_club():
                selected_item = clubs_table.focus()
                if selected_item:
                    club_info = clubs_table.item(selected_item)['values']
                    start_date = datetime.date(2022, 10, 1)
                    end_date = datetime.date(2022, 11, 15)
                    days_diff = (end_date - start_date).days
                    random_days = random.randint(0, days_diff)
                    adhesion_date = start_date + datetime.timedelta(days=random_days)
                    adhesion_date_str = adhesion_date.strftime('%Y/%m/%d')

                    self.joined_clubs.append({
                        'nom': club_info[0],
                        'description': club_info[1],
                        'adhesion': adhesion_date_str
                    })


                    messagebox.showinfo('Bienvenue', f"Bienvenue au club {club_info[0]} !")

                    clubs_table.item(selected_item, values=(club_info[0], club_info[1], adhesion_date_str))

            clubs_window = Toplevel(self.master)
            clubs_window.title("Liste des clubs")
            clubs_window.attributes('-topmost', True)
            clubs_window.geometry("900x500+500+200")
            clubs_window.resizable(False, False)
            clubs_window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(clubs_window))


            clubs_window_style = ttk.Style()
            clubs_window_style.configure('Custom.Toplevel', background='skyblue', borderwidth=0, highlightthickness=0)
            clubs_window.style = clubs_window_style
            clubs_window.style.theme_use('default')

            scrollbar = ttk.Scrollbar(clubs_window, orient='vertical')
            scrollbar.pack(side='right', fill='y')


            clubs_table_style = ttk.Style()
            clubs_table_style.configure('Custom.Treeview', background='#F0F0F0', rowheight=80, font=('Arial', 10),
                                        borderwidth=0, highlightthickness=0)
            clubs_table_style.configure('Custom.Treeview.Heading', background='#1E90FF', foreground='white',
                                        font=('Arial', 12, 'bold'))
            clubs_table_style.configure('Custom.Treeview', fieldbackground='#F0F0F0')
            clubs_table = ttk.Treeview(clubs_window, style='Custom.Treeview')
            clubs_table['columns'] = ('nom', 'description', 'adhesion')
            clubs_table.column('#0', width=0, stretch=NO)
            clubs_table.column('nom', anchor=CENTER, width=200)
            clubs_table.column('description', anchor=CENTER, width=500)
            clubs_table.column('adhesion', anchor=CENTER, width=200)
            clubs_table.heading('#0', text='', anchor=W)
            clubs_table.heading('nom', text='Nom')
            clubs_table.heading('description', text='Description')
            clubs_table.heading('adhesion', text='Adhésion')
            clubs_table.tag_configure('oddrow', background='#FFFFFF')
            clubs_table.tag_configure('evenrow', background='#F0F0F0')
            clubs_table.bind('<Double-1>', lambda e: join_club())
            clubs = [
                {'nom': '01',
                 'description': 'l\'objectif commun est de dynamiser la scène événementielle informatique , améliorer les compétences personnelles et professionnelles des étudiants en programmant plusieurs activités (formations, workshops et compétitions....). Le club a marqué sa présence aussi par l\'organisation de "TECH EXPERIENCE" qui est le plus grand évènement d’IT au nord du Royaume , organisé à L’ENSAH- Ecole Nationale des Sciences Appliqués d’Al Hoceima',
                 'adhesion': 'JOIN'},
                {'nom': 'DATA',
                 'description': "Le club scolaire Data a pour but d'initier les élèves aux fondamentaux de la science des données et de leur apprendre à analyser et à interpréter les données. Les membres du club participent à des activités telles que des ateliers, des projets et des compétitions pour améliorer leurs compétences en analyse de données. L'objectif ultime du club est de préparer les élèves à une carrière réussie dans le domaine des données.",
                 'adhesion': 'JOIN'},
                {'nom': 'CHESS',
                 'description': "Le club scolaire CHESS a pour but de promouvoir le jeu d'échecs auprès des étudiants. Il organise des sessions d'entraînement et des compétitions pour les joueurs débutants et avancés. Le club vise à améliorer les compétences de raisonnement et de prise de décision des étudiants tout en leur offrant un environnement social agréable.",
                 'adhesion': 'JOIN'},
                {'nom': 'JLM',
                 'description': "Le club scolaire JLM est une association qui vise à promouvoir la culture et les arts au sein de l'établissement. Il organise régulièrement des événements artistiques tels que des expositions, des spectacles de musique et de danse, ainsi que des ateliers de création. Le club est ouvert à tous les élèves qui souhaitent s'impliquer dans la vie culturelle de l'école.",
                 'adhesion': ""},
                {'nom': 'ENACTUS',
                 'description': "ENACTUS est un club étudiant international qui encourage les étudiants à utiliser l'entrepreneuriat pour créer des projets sociaux durables. Le club vise à résoudre les problèmes locaux en utilisant des solutions innovantes et durables. Rejoignez-nous pour apprendre à devenir un leader du changement social !",
                 'adhesion': ''},
                {'nom': 'CCT',
                 'description': "Le Club Culturel et Technologie (CCT) est un club étudiant axé sur la promotion de la culture et de la technologie à travers divers événements et activités pour les membres de la communauté étudiante. Les membres peuvent participer à des ateliers, des conférences et des compétitions pour développer leurs compétences en culture et en technologie.",
                 'adhesion': ''},
                {'nom': 'G.CIVIL',
                 'description': "Le club G.CIVIL est dédié aux étudiants en génie civil et permet de développer des compétences techniques et pratiques. Les membres organisent des événements, des ateliers et des visites de sites et chantiers pour approfondir leur compréhension du domaine et élargir leur réseau professionnel. Rejoindre le club G.CIVIL offre une opportunité unique de se connecter avec d'autres étudiants passionnés et de découvrir de nouvelles perspectives dans le domaine du génie civil.",
                 'adhesion': ''},
                {'nom': 'PRESS CLUB',
                 'description': "Le Press Club est un club dédié au journalisme et à la communication, offrant une plateforme pour les étudiants passionnés par l'actualité et l'écriture pour s'exprimer et améliorer leurs compétences. Le club organise des événements, des ateliers et des conférences pour encourager l'engagement des étudiants dans les médias et les affaires publiques.",
                 'adhesion': ''},
                {'nom': 'CLUB VOYAGE',
                 'description': "Le club VOYAGE de l'ENSAH est dédié à l'organisation de voyages et d'excursions. Il offre des opportunités de découvrir de nouvelles cultures et de nouvelles destinations à travers des événements et des activités enrichissantes. Rejoignez-nous pour explorer le monde ensemble !",
                 'adhesion': ''},
                {'nom': 'CLUB SPORT',
                 'description': "Le club sportif de l'ENSAH est une organisation étudiante qui organise des tournois sportifs, des événements et des activités pour promouvoir un style de vie sain et actif. Les membres participent à différentes activités sportives et travaillent ensemble pour organiser des compétitions passionnantes pour les étudiants.",
                 'adhesion': ''},
            ]

            import random
            import datetime
            max_length = 95


            for club in clubs:

                start_date = datetime.date(2022, 10, 1)
                end_date = datetime.date(2022, 11, 15)
                days_diff = (end_date - start_date).days
                random_days = random.randint(0, days_diff)
                adhesion_date = start_date + datetime.timedelta(days=random_days)
                adhesion_date_str = adhesion_date.strftime('%Y/%m/%d')

                description = club['description']
                if len(description) > max_length:
                    new_text = ""
                    words = description.split()
                    line_length = 0
                    for word in words:
                        if line_length + len(word) + 1 > max_length:
                            new_text += "\n"
                            line_length = 0
                        new_text += word + " "
                        line_length += len(word) + 1
                    club['description'] = new_text


                values = (club['nom'], club['description'], adhesion_date_str)
                clubs_table.insert(parent='', index='end', values=values)

            bg_image9 = Image.open("images/20.jpg")
            resized_image = bg_image9.resize((1000, 108), resample=Image.LANCZOS)
            bg_image9 = ImageTk.PhotoImage(resized_image)

            bg_label = tk.Label(clubs_window, image=bg_image9)
            bg_label.image = bg_image9
            bg_label.place(x=0, y=0)


            join_button = ttk.Button(clubs_window, text='Rejoindre', command=join_club, style='Join.TButton')
            join_button.pack(side='top', padx=10, pady=10)

            my_clubs_button = ttk.Button(clubs_window, text="Mes clubs", style='MyClubs.TButton')
            my_clubs_button.pack(side='top', padx=10, pady=20)

            clubs_table.pack()

            clubs_window.style = ttk.Style()

            clubs_window.style.configure('Join.TButton',
                                         background='blue',
                                         foreground='white',
                                         font=('Arial', 12, 'bold'),
                                         padding=5,
                                         relief='flat',
                                         borderwidth=0,
                                         width=15,
                                         anchor='center')

            clubs_window.style.configure('MyClubs.TButton',
                                         background='red',
                                         foreground='white',
                                         font=('Arial', 12, 'bold'),
                                         padding=5,
                                         relief='flat',
                                         borderwidth=0,
                                         width=15,
                                         anchor='center')

            clubs_window.style.map('Join.TButton',
                                   background=[('active', '#0066cc')],
                                   foreground=[('active', 'white')])
            clubs_window.style.map('MyClubs.TButton',
                                   background=[('active', '#cc0000')],
                                   foreground=[('active', 'white')])

        def about_us(self):
            main_frame = Frame(self.master, bg='white')
            main_frame.pack(fill=BOTH, expand=True)

            img_frame = Frame(main_frame, bg='white')
            img_frame.pack(side=TOP, padx=50, pady=0)

            img = Image.open("images/9.png")
            img = img.resize((120, 120), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            img_label = Label(img_frame, image=img, bg='white')
            img_label.image = img
            img_label.pack()

            about_frame = Frame(self.master, bg='white')
            about_frame.pack(fill=BOTH, expand=True)

            about_title_font = Font(family="Helvetica", size=30, weight="bold", underline=True)
            about_title = Label(about_frame, text="L'application ENSAH-Services de l'ENSAH", bg='white', fg='blue',
                                font=about_title_font, bd=3, relief='groove')
            about_title.pack(pady=0)

            about_text = "ENSAH-Services est une application Desktop conçue à l'Ecole Nationale des Sciences Appliquées par Omar HAI, Jawad BACHIRI , Fatima Zahra CHAKIR, pour offrir un point d'accès unique aux étudiants et au personnel de l'établissement pour trouver les informations, outils et services numériques nécessaires pour leurs activités pédagogiques ou administratives. \n\n L'application a été initialement créée pour simplifier les procédures d'inscription et les demandes d'attestations administratives. Elle a été améliorée au fil du temps pour couvrir de plus en plus de fonctionnalités, divisées en deux parties : la partie interne du système (Scolarité) et la partie accessible aux étudiants et aux enseignants (Partie front). Les fonctionnalités de l'application incluent la gestion des étudiants, des inscriptions, réinscriptions, ainsi que la centralisation de l'accès à l'actualité, le catalogue de la bibliothèque, les emplois du temps et d'autres ressources. \n\n Les utilisateurs peuvent également gérer les demandes envoyées aux services de l'administration, notamment le service de scolarité, et les fonctionnalités liées à l'internat, telles que la gestion des cartes du restaurant, la réservation et la base de données des résidents. L'application est développée en Python et SQL, sans l'utilisation d'un framework. Omar HAI, élève-ingénieur en Ingénierie des Données à l'Ecole Nationale des Sciences Appliquées d'Al Hoceima, est le développeur de l'application. Les contributions et les propositions pour améliorer l'application sont les bienvenues. Les étudiants de l'informatique intéressés peuvent contacter Omar HAI par e-mail à omar.hai@etu.uae.ac.ma. Une FAQ et des guides d'utilisation sont également disponibles pour les utilisateurs qui ont des questions. \n\nÀ propos du développeur Omar HAI, Eleve  Ingénieur en Ingénierie Des Données.\nEcole Nationale des Sciences Appliquées - Al HOCEIMA ."

            about_label = Label(about_frame, text=about_text, wraplength=900, justify=LEFT, font=self.entryfont,
                                bg='white',
                                cursor='arrow', takefocus=True)
            about_label.pack(padx=20, pady=3)

            phone_number = "+212707868252"
            whatsapp_url = f"https://wa.me/{phone_number}"
            about_label_phone = Label(about_frame, text=f"Whatsapp: {phone_number}", fg='blue', font=self.entryfont,
                                      bg='white',
                                      cursor='hand2', takefocus=True)
            about_label_phone.pack(padx=15, pady=3)
            about_label_phone.bind("<Button-1>", lambda event: webbrowser.open_new(whatsapp_url))

            linkedin_url = "https://www.linkedin.com/in/jawad-bachiri-b51797221/"
            about_label_linkedin = Label(about_frame, text="LinkdIn Account ", fg="blue", cursor="hand2",
                                         font=self.entryfont,
                                         bg="white")
            about_label_linkedin.pack(pady=3)
            about_label_linkedin.bind("<Button-1>", lambda event: webbrowser.open_new(linkedin_url))

            pdf_path = "FAQ.pdf"
            about_label_faq = Label(about_frame, text="FAQ", fg="blue", cursor="hand2", font=self.entryfont,
                                    bg="white")
            about_label_faq.pack(pady=5)
            about_label_faq.bind("<Button-1>", lambda event: webbrowser.open_new(pdf_path))

            back_button1 = tk.Button(about_frame, text="Retour",
                                     command=lambda: [self.master.deiconify(), about_frame.destroy()], bd=3, bg='green',
                                     fg='white')
            back_button1.pack(side=tk.BOTTOM)

        def quit_app(self):
            if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter?"):
                self.master.destroy()

        def post_menu(self):
            print("Menu posted")

        def tearoff_menu(self):
            print("Tearoff menu")

        def update_last_consultation(self):

            now = datetime.datetime.now()
            date_string = now.strftime("%Y-%m-%d %H:%M:%S")
            self.last_consultation_label.config(text="Last consultation: \n" + date_string)

        def slideshow(self):
            if self.current_photo == 1:
                self.photo_label1.configure(image=self.photo4)
                self.current_photo = 2
            elif self.current_photo == 2:
                self.photo_label1.configure(image=self.photo3)
                self.current_photo = 3
            else:
                self.photo_label1.configure(image=self.photo1)
                self.current_photo = 1

            self.master.after(5000, self.slideshow)

        def show_professeurs(self):
            new_window = Toplevel(self.master)
            new_window.title("Liste des Professeurs")


            table = ttk.Treeview(new_window, columns=('Nom', 'Prénom', 'Email académique', 'Photo'))

            data = [('NOM_PROF', 'PRENOM_PROF', 'EMAIL', 'IMG'),
                   ] # Ajouter plus



            table_frame = Frame(new_window, bg='white', padx=10, pady=10, relief='groove', bd=2)
            table_frame.pack(fill='both', expand=True)

            table = ttk.Treeview(table_frame, selectmode='browse',
                                 columns=('Nom', 'Prénom', 'Email académique', 'Photo'),
                                 show='headings')

            style = ttk.Style()
            style.configure('Treeview', foreground='blue', rowheight=150)
            style.configure('Treeview.Heading', foreground='blue', rowheight=150,
                            font=('Arial', 12, 'bold'))

            table = ttk.Treeview(table_frame, selectmode='browse',
                                 columns=('Nom', 'Prénom', 'Email académique', 'Photo'),
                                 show='headings', style='Treeview')
            table.heading('#0', text='ID', anchor='center')
            table.heading('Nom', text='Nom', anchor='center')
            table.heading('Prénom', text='Prénom', anchor='center')
            table.heading('Email académique', text='Email académique', anchor='center')
            table.heading('Photo', text='Photo', anchor='center')

            table.tag_configure('Treeview.Heading', background='gray')


            table.column('#0', width=50)
            table.column('Nom', width=150)
            table.column('Prénom', width=150)
            table.column('Email académique', width=200)
            table.column('Photo', width=100)


            for i, (nom, prenom, email, photo) in enumerate(data):
                table.insert(parent='', index='end', iid=i, text=i, values=(nom, prenom, email, photo))


            table.pack(fill='both', expand=True)


            table.tag_configure('table', background='black', font=('Arial', 12))
            table.tag_configure('headings', background='green', font=('Arial', 12, 'bold'))
            table.tag_bind('headings', '<Button-1>', lambda e: print('Clicked headings'))

            table_frame.configure(background='green', bd=2, relief='groove', padx=10, pady=10)

        def show_demande(self):
            demande_window = Toplevel(self.master)
            demande_window.geometry("1500x600")
            demande_window.title("Formulaire de demande")
            demande_window.configure(bg="#ADD8E6")

            demande_frame = Frame(demande_window, borderwidth=2, relief="groove", bg="#F0F0F0")
            demande_frame.pack(side=TOP, fill=BOTH, padx=10, pady=10)

            demande_label = Label(demande_frame, text="Service Scolarité", font=("Helvetica", 24), fg="#FFFFFF",
                                  bg="#2C3E50", bd=2, relief="groove", padx=10, pady=10)
            demande_label.pack(side=TOP, padx=10, pady=10)

            demande_label.config(highlightthickness=2, highlightbackground="#34495E", highlightcolor="#34495E")

            demande_menu_label = Label(demande_frame, text="Sélectionnez le type de demande :", font=self.labelfont)
            demande_menu_label.pack(side=TOP, padx=10, pady=10)

            demande_menu = Listbox(demande_frame, font=self.entryfont, selectmode=SINGLE, height=13, width=55)
            image_path = "images/21.png"
            image = Image.open(image_path)
            width, height = image.size
            max_size = 200
            if width > max_size or height > max_size:
                if width > height:
                    new_width = max_size
                    new_height = int(height * (max_size / width))
                else:
                    new_height = max_size
                    new_width = int(width * (max_size / height))
                image = image.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(image)


            image_label = Label(demande_frame, image=photo)
            image_label.image = photo
            image_label.pack(side=BOTTOM, padx=10, pady=10)

            demande_options = ["[S.Scolarité] RELEVE DE NOTES",
                               "[S.Scolarité] ATTESTATION DE RÉUSSITE",
                               "[S.Scolarité] PARCOURS D'ÉTUDES",
                               "[S.Scolarité] DEMANDE DE RECTIFICATION DES DONNEES",
                               "[S.Scolarité] ATTESTATION DE POURSUITE D'ÉTUDES",
                               "[S.Scolarité] SCANNE DES DIPLOME",
                               "[S.Scolarité] RECLAMATION BOURSES",
                               "[S.Scolarité] ATTESTATION D'OBTENTION DU NIVEAU B2",
                               "[S.Scolarité] AUTRE DEMANDE AU SERVICE SCOLARITE",
                               "[La Secrétaire du Directeur] CONVENTION ET DEMANDE DE STAGE",
                               "[la Secrétaire du Directeur] ATTESTATION D'ASSURANCE",
                               "[la Secrétaire du Directeur] AUTRE DEMANDE SECRETAIRE DE DIRECTION"]

            for option in demande_options:
                demande_menu.insert(END, option)

            demande_menu.pack(side=LEFT, padx=10)

            demande_import_label = Label(demande_frame, text="Importer des fichiers (PDF) :", font=self.labelfont)
            demande_import_label.pack(side=LEFT, padx=10)

            self.filepath_button = Button(demande_frame, text="Choisir un fichier", font=self.labelfont,
                                          command=self.choose_file, bg="#ADD8E6", padx=10,
                                          activebackground="#6495ED", activeforeground="white")
            self.filepath_button.pack(side=LEFT, padx=10)

            demande_details_label = Label(demande_frame, text="Détails de la demande :", font=self.labelfont)
            demande_details_label.pack(side=TOP, padx=10, pady=10)

            demande_details_entry = Entry(demande_frame, font=self.entryfont, width=50)
            demande_details_entry.pack(side=TOP, padx=20)

            self.demande_send_button = Button(demande_frame, text="Envoyer", font=self.labelfont,
                                              command=self.send_demande, bg="#ADD8E6", padx=10,
                                              activebackground="#6495ED", activeforeground="white")
            self.demande_send_button.pack(side=LEFT, padx=10, pady=10)

            self.demande_cancel_button = Button(demande_frame, text="Annuler", font=self.labelfont,
                                                command=self.cancel_demande, bg="#ADD8E6", padx=10,
                                                activebackground="#6495ED", activeforeground="white")
            self.demande_cancel_button.pack(side=LEFT, padx=10, pady=10)

            self.demande_email = "email" # a modifier
            self.etudiant_email = "votre-email@ensah.ma"

        def choose_file(self):
            filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                  filetypes=[("PDF Files", "*.pdf")])
            if filename:
                self.filepath.set(filename)
                messagebox.showinfo("Fichier importé", "Le fichier a été importé avec succès !")

        def cancel_demande(self):
            self.demande_menu.current(0)
            self.demande_details_entry.delete(0, END)
            self.filepath.set("")
            messagebox.showinfo("Demande annulée", "Votre demande a été annulée avec succès !")

        def send_demande(self):
            demande = self.demande_menu.get()
            details = self.demande_details_entry.get()
            filepath = self.filepath.get()

            if not demande:
                messagebox.showerror("Erreur", "Veuillez sélectionner un type de demande.")
                return
            elif not details:
                messagebox.showerror("Erreur", "Veuillez saisir les détails de votre demande.")
                return
            elif not filepath:
                messagebox.showerror("Erreur", "Veuillez importer un fichier.")
                return


            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("email", "key") # a modifier

            msg = MIMEMultipart()
            msg['From'] = "email"# a modifier
            msg['To'] = "email" # a modifier
            msg['Subject'] = "Nouvelle demande de {} - {}".format(demande, self.etudiant_email)

            body = "Type de demande: {}\nDétails: {}\n".format(demande, details)
            msg.attach(MIMEText(body, 'plain'))

            with open(filepath, "rb") as f:
                attach = MIMEApplication(f.read(), _subtype="pdf")
                attach.add_header('Content-Disposition', 'attachment', filename=str(filepath))

            msg.attach(attach)
            text = msg.as_string()
            server.sendmail("email", "email", text) # a modifier

            server.quit()

            messagebox.showinfo("Demande envoyée", "Votre demande a été envoyée avec succès !")

        def emp_click(self):
            filiere_window = Toplevel(self.master)
            filiere_window.geometry('300x300')
            filiere_window.title('Filière')
            filiere_window.configure(bg="#f2f2f2")

            self.img = PhotoImage(file=r"images/14.png")
            image_label = Label(filiere_window, image=self.img)
            image_label.pack()

            filiere_label = Label(filiere_window, text="Entrez votre filière:", font=self.labelfont)
            filiere_label.pack(pady=10)
            filiere_entry = Entry(filiere_window, font=self.entryfont)
            filiere_entry.pack(pady=10)


            submit_button = Button(filiere_window, text="Valider", font=self.labelfont,
                                   command=lambda: self.download_pdf(filiere_entry.get(), filiere_window))
            submit_button.pack(pady=10)


            filiere_window.option_add("*Button.background", "#5cb85c")
            filiere_window.option_add("*Button.foreground", "#ffffff")
            filiere_window.option_add("*Button.font", self.labelfont)
            filiere_window.option_add("*Entry.background", "#e6e6e6")
            filiere_window.option_add("*Entry.foreground", "#333333")
            filiere_window.option_add("*Entry.font", self.entryfont)

        def download_pdf(self, filiere, filiere_window):
            filename = ''
            if filiere == 'id1':
                filename = 'votre_fichier.pdf'
            elif filiere == 'gm1':
                filename = 'votre_fichier.pdf'
            elif filiere == 'cp2':
                filename = 'votre_fichier.pdf'
            elif filiere == 'gi2':
                filename = 'votre_fichier.pdf'

            if filename != '':
                url = 'file:emploi id1/' + filename
                webbrowser.open(url, new=2)
                messagebox.showinfo("Téléchargement réussi", "Le fichier a été téléchargé avec succès.")
            else:

                image_path = 'images/3.png'
                alert_window = tk.Toplevel(filiere_window)
                alert_window.geometry('400x250')
                alert_window.title('Alerte')

                alert_image = tk.PhotoImage(file='images/2.png')
                alert_label = tk.Label(alert_window, image=alert_image)
                alert_label.place(x=50, y=10)

                alert_text = tk.Label(alert_window,
                                      text="La filière que vous avez sélectionnée est incorrecte.",
                                      font=("Arial", 11, "bold"), fg="red")
                alert_text.place(x=10, y=220)

                alert_window.mainloop()

            filiere_window.destroy()

        def cours_click(self):
            filiere_window = Toplevel(self.master)
            filiere_window.geometry('300x300')
            filiere_window.title('Filière')
            filiere_window.configure(bg="#f2f2f2")

            self.img = PhotoImage(file=r"images/14.png")
            image_label = Label(filiere_window, image=self.img)
            image_label.pack()


            filiere_label = Label(filiere_window, text="Entrez votre filière:", font=self.labelfont)
            filiere_label.pack(pady=10)
            filiere_entry = Entry(filiere_window, font=self.entryfont)
            filiere_entry.pack(pady=10)

            submit_button = ttk.Button(filiere_window, text="Valider",
                                       command=lambda: self.display_cours(filiere_entry.get(), filiere_window))
            submit_button.pack(pady=10)
            button_style = ttk.Style()
            button_style.configure('TButton', font=self.labelfont, background='#4CAF50', foreground='#FFFFFF')


            filiere_window.option_add("*Button.background", "#4CAF50")
            filiere_window.option_add("*Button.font", self.labelfont)
            filiere_window.option_add("*Entry.background", "#e6e6e6")
            filiere_window.option_add("*Entry.foreground", "#333333")
            filiere_window.option_add("*Entry.font", self.entryfont)

        def display_cours(self, filiere, filiere_window):
            modules = {
                'id1': {
                    'Analyse numérique': [
                        'cours id1\\analyse numerique\\votre_fichier.pdf',
                        'cours id1\\analyse numerique\\votre_fichier.pdf',
                        "cours id1\\analyse numerique\\votre_fichier.pdf"],
                    'Java': [
                        'cours id1\\java\\votre_fichier.pdf',
                        'cours id1\\java\\votre_fichier.pdf',
                        'cours id1\\java\\votre_fichier.pdf'],
                    'Data Mining': [
                        'cours id1\\data mining\\votre_fichier.pdf',
                        'cours id1\\data mining\\votre_fichier.pdf'],
                    'Base du web': [
                        'cours id1\\base du web\\votre_fichier.pdf',
                        'cours id1\\base du web\\votre_fichier.pdf',
                        'cours id1\\base du web\\votre_fichier.pdf'],
                    'Statistique inférentielle': [
                        'cours id1\\statistique inferentiel\\votre_fichier.pdf',
                        'cours id1\\statistique inferentiel\\votre_fichier.pdf',
                        'cours id1\\statistique inferentiel\\votre_fichier.pdf'],
                    'Optimisation de base de données': [
                        'cours id1\\ADMINISTRATION ET OPTIMISATION DE BASE DE DONNÉES\\votre_fichier.pdf',
                        'cours id1\\ADMINISTRATION ET OPTIMISATION DE BASE DE DONNÉES\\votre_fichier.pdf',
                        'cours id1\\ADMINISTRATION ET OPTIMISATION DE BASE DE DONNÉES\\votre_fichier.pdf']
                }
            }

            if filiere in modules:
                module_window = Toplevel(self.master)
                module_window.geometry('600x400')
                module_window.title('Modules')
                module_window.configure(bg="#FFFFFF")


                style = ttk.Style()
                style.configure("TLabel", background="#FFFFFF", foreground="#000000", font=("Arial", 14, "bold"))
                style.configure("TButton", background="#bfbfbf", foreground="#000000", font=("Arial", 12))
                style.configure("TFrame", background="#FFFFFF")


                button_frame = ttk.Frame(module_window)


                canvas = Canvas(button_frame, bg="#FFFFFF", highlightthickness=0)
                scrollbar = ttk.Scrollbar(button_frame, orient="horizontal", command=canvas.xview)
                canvas.configure(xscrollcommand=scrollbar.set)
                scrollbar.pack(side="bottom", fill="x")
                canvas.pack(side="left", fill="both", expand=True)


                background_image1 = Image.open("images/13.png")
                resized_image1 = background_image1.resize((1000, 1000), resample=Image.LANCZOS)
                self.background_image1 = ImageTk.PhotoImage(resized_image1)
                background_label1 = ttk.Label(canvas, image=self.background_image1)
                background_label1.place(x=700, y=0, relwidth=1, relheight=1)


                frame = ttk.Frame(canvas)
                canvas.create_window((0, 0), window=frame, anchor='nw')
                cours_count = 1
                for module in modules[filiere]:
                    module_label = ttk.Label(frame, text=module, style="TLabel")
                    module_label.pack(padx=10, pady=10)

                    cours_frame = ttk.Frame(frame)
                    cours_frame.pack(side="top", fill="x")

                    for i in range(len(modules[filiere][module])):
                        cours_button = ttk.Button(cours_frame, text=f"Cours {cours_count}", style="TButton",
                                                  command=lambda url=modules[filiere][module][i]: webbrowser.open(url))
                        cours_button.pack(side="left", padx=5, pady=5)
                        cours_count += 1


                frame.update_idletasks()
                canvas.config(scrollregion=canvas.bbox("all"))


                button_frame.pack(fill="both", expand=True)
                module_window.update_idletasks()
                button_frame.pack_configure(expand=True,
                                            padx=(module_window.winfo_width() - button_frame.winfo_width()) // 2,
                                            pady=(module_window.winfo_height() - button_frame.winfo_height()) // 2)

                filiere_window.destroy()

            else:
                error_window = Toplevel(self.master)
                error_window.geometry('300x150')
                error_window.title('Erreur')
                error_window.configure(bg="#f2f2f2")

                error_label = Label(error_window, text="Filière non trouvée.", font=self.labelfont)
                error_label.pack(pady=30)

                ok_button = Button(error_window, text="OK", font=self.labelfont, command=error_window.destroy)
                ok_button.pack(pady=10)

        def notes_click(self):

            filiere_window = Toplevel(self.master)
            filiere_window.geometry('300x300')
            filiere_window.title('Filière')
            filiere_window.configure(bg="#f2f2f2")

            self.img = PhotoImage(file=r"images/14.png")
            image_label = Label(filiere_window, image=self.img)
            image_label.pack()


            filiere_label = Label(filiere_window, text="Entrez votre filière:", font=self.labelfont)
            filiere_label.pack(pady=10)
            filiere_entry = Entry(filiere_window, font=self.entryfont)
            filiere_entry.pack(pady=10)


            submit_button = Button(filiere_window, text="Valider", font=self.labelfont, bg="green", fg="white",
                                   command=lambda: self.display_notes(filiere_entry.get(), filiere_window))
            submit_button.pack(pady=10)


            filiere_window.option_add("*Button.background", "#5cb85c")
            filiere_window.option_add("*Button.foreground", "#ffffff")
            filiere_window.option_add("*Button.font", self.labelfont)
            filiere_window.option_add("*Entry.background", "#e6e6e6")
            filiere_window.option_add("*Entry.foreground", "#333333")
            filiere_window.option_add("*Entry.font", self.entryfont)

        def display_notes(self, filiere, filiere_window):
            global id1_window
            filiere_window.destroy()

            if filiere == "cp2":
                cp2_window = tk.Toplevel(self.master)
                cp2_window.geometry('1300x1300')
                cp2_window.title('CP2')
                cp2_window.configure(bg='sky blue')
                photo = Image.open("images/19.png")
                photo = photo.resize((700, 750))
                photo = ImageTk.PhotoImage(photo)

                photo_label = ttk.Label(cp2_window, image=photo)
                photo_label.place(x=700, y=0)

                welcome_text3 = tk.Label(cp2_window, text="", font=("Arial", 15, "bold italic"), fg="#0091D0", width=50)
                welcome_text3.config(relief="solid")
                welcome_text3.config(highlightbackground="#0091D0", highlightthickness=5)
                welcome_text3.place(x=50, y=500)

                text = "Wishing you success in your exams dear students!   "

                def animate_text():
                    nonlocal text
                    text = text[-1] + text[:-1]
                    welcome_text3.config(text=text)
                    welcome_text3.after(90, animate_text)

                animate_text()


                style = ttk.Style()
                style.configure('Custom.TButton', font=('Helvetica', 16))

                def create_algebra_button():
                    algebra_button = ttk.Button(cp2_window, text="Algebre Quadratique", style='Custom.TButton',
                                                command=lambda: webbrowser.open_new_tab(
                                                    "affichage cp2\\votre_fichier.pdf"))
                    algebra_button.grid(row=0, column=0, padx=10, pady=10, sticky='nsw')

                def create_lang_comm_button():
                    lang_comm_button = ttk.Button(cp2_window, text="Langue et Communication", style='Custom.TButton',
                                                  command=lambda: webbrowser.open_new_tab(
                                                      "affichage cp2\\votre_fichier.pdf"))
                    lang_comm_button.grid(row=1, column=0, padx=10, pady=10, sticky='nsw')

                def create_multivar_button():
                    multivar_button = ttk.Button(cp2_window, text="Fonction a plusieurs variables",
                                                 style='Custom.TButton',
                                                 command=lambda: webbrowser.open_new_tab(
                                                     "affichage cp2\\votre_fichier.pdf"))
                    multivar_button.grid(row=2, column=0, padx=10, pady=10, sticky='nsw')

                def create_prog_c_button():
                    prog_c_button = ttk.Button(cp2_window, text="Programmation C", style='Custom.TButton',
                                               command=lambda: webbrowser.open_new_tab(
                                                   "affichage cp2\\votre_fichier.pdf"))
                    prog_c_button.grid(row=3, column=0, padx=10, pady=10, sticky='nsw')

                def create_electro_button():
                    electro_button = ttk.Button(cp2_window, text="Electrocenitique & Electromagnétisme",
                                                style='Custom.TButton',
                                                command=lambda: webbrowser.open_new_tab(
                                                    "votre_fichier.pdf"))
                    electro_button.grid(row=4, column=0, padx=10, pady=10, sticky='nsw')

                def create_thermo_button():
                    thermo_button = ttk.Button(cp2_window, text="Thermodynamique & Statique des fluides",
                                               style='Custom.TButton',
                                               command=lambda: webbrowser.open_new_tab(
                                                   "affichage cp2\\votre_fichier.pdf"))
                    thermo_button.grid(row=5, column=0, padx=10, pady=10, sticky='nsw')

                def create_stats_button():
                    stats_button = ttk.Button(cp2_window,
                                              text="Probabilités et statistiques descriptives & Analyse numérique",
                                              style='Custom.TButton',
                                              command=lambda: webbrowser.open_new_tab(
                                                  "affichage cp2\\votre_fichier.pdf"))
                    stats_button.grid(row=6, column=0, padx=10, pady=10, sticky='nsw')

                def create_informatique_button():
                    informatique_button = ttk.Button(cp2_window, text="Outils informatique",
                                                     style='Custom.TButton',
                                                     command=lambda: webbrowser.open_new_tab(
                                                         "affichage cp2\\votre_fichier.pdf"))
                    informatique_button.grid(row=7, column=0, padx=10, pady=10, sticky='nsw')

                create_algebra_button()
                create_lang_comm_button()
                create_multivar_button()
                create_prog_c_button()
                create_electro_button()
                create_thermo_button()
                create_stats_button()
                create_informatique_button()

            if filiere == "id1":
                id1_window = tk.Toplevel(self.master)
                id1_window.geometry('1300x1300')
                id1_window.title('ID1')
                id1_window.configure(bg='sky blue')

                photo8 = Image.open("images/19.png")
                photo8 = photo8.resize((1300, 750))
                photo8 = ImageTk.PhotoImage(photo8)

                image_label = ttk.Label(id1_window, image=photo8)
                image_label.place(x=500, y=0)

                welcome_text4 = tk.Label(id1_window, text="", font=("Arial", 15, "bold italic"), fg="#0091D0", width=50)
                welcome_text4.config(relief="solid")
                welcome_text4.config(highlightbackground="#0091D0", highlightthickness=5)
                welcome_text4.place(x=50, y=500)

                text2 = "Wishing you success in your exams dear students!   "

                def animate_text2():
                    nonlocal text2
                    text2 = text2[-1] + text2[:-1]
                    welcome_text4.config(text=text2)
                    welcome_text4.after(90, animate_text2)

                animate_text2()

            theorie_button = tk.Button(id1_window, text="THEORIE DE LANGAGE ET DE COMPILATION", font=self.labelfont,
                                       command=lambda: webbrowser.open_new_tab(
                                           "affichage id1\\votre_fichier.pdf"),
                                       bg='blue')
            theorie_button.place(x=10, y=20)

            archi_button = tk.Button(id1_window, text="ARCHITECTURE DES ORDINATEURS ET SYSTEME D’EXPLOITATION",
                                     font=self.labelfont,
                                     command=lambda: webbrowser.open_new_tab(
                                         "affichage id1\\votre_fichier.pdf"),
                                     bg='blue')
            archi_button.place(x=10, y=70)

            BDD_button = tk.Button(id1_window, text="SYSTEME D’INFORMATION ET BASE DE DONNÉES", font=self.labelfont,
                                   command=lambda: webbrowser.open_new_tab(
                                       "affichage id1\\votre_fichier.pdf"),
                                   bg='blue')
            BDD_button.place(x=10, y=120)

            algo_button = tk.Button(id1_window, text="ALGORITHMIQUE AVANCÉES ET STRUCTURE DE DONNÉES",
                                    font=self.labelfont,
                                    command=lambda: webbrowser.open_new_tab(
                                        "affichage id1\\votre_fichier.pdf"),
                                    bg='blue')
            algo_button.place(x=10, y=170)

        def search_click(self):
            search_term = self.search_entry.get()

            main_frame = self.master.winfo_children()[0]


            search_results = []


            for child in main_frame.winfo_children():

                if search_term in str(child):

                    if child not in search_results:

                        search_results.append(child)


            search_results_frame = Frame(self.master)
            search_results_frame.pack(fill=BOTH, expand=True)


            result_count_label = Label(search_results_frame,
                                       text=f"{len(search_results)} résultats de recherche trouvés pour '{search_term}'")
            result_count_label.pack()


            if search_results:
                for result in search_results:
                    result.pack(fill=BOTH, expand=True)
            else:

                no_results_label = Label(search_results_frame,
                                         text=f"Aucun résultat de recherche trouvé pour '{search_term}'")
                no_results_label.pack(fill=BOTH, expand=True)


            back_button = Button(search_results_frame, text="Retour", command=lambda: search_results_frame.destroy())
            back_button.pack(side=BOTTOM)


            self.history_listbox.insert(END, search_term)

        def profil_click(self):
            self.profil_window = Toplevel(self.master)
            self.profil_window.title('Profil')
            self.profil_window.geometry('400x400')
            self.profil_window.resizable(0, 0)
            mydb = mysql.connector.connect(
                host="localhost",
                user="admin",
                password="admin",
                database="register_login")
            mycursor = mydb.cursor()
            mycursor.execute("select * from NEW_STUDENT_DATABASE where name=%s and password=%s", (u, p))
            row = mycursor.fetchone()
            a = row[0]
            b = row[1]
            c = row[2]
            d = row[3]
            e = row[4]
            f = row[5]

            bg_img = Image.open('images/13.png')
            bg_photo = ImageTk.PhotoImage(bg_img)


            bg_label = Label(self.profil_window, image=bg_photo)
            bg_label.image = bg_photo
            bg_label.place(x=0, y=0)



            bg_label.lower()


            logo_img = Image.open('images/9.png')
            t1_img = Image.open('images/21.png')
            logo_photo = ImageTk.PhotoImage(logo_img.resize((40, 40)))
            t1_photo = ImageTk.PhotoImage(t1_img.resize((40, 40)))

            logo_label = Label(self.profil_window, image=logo_photo)
            logo_label.image = logo_photo
            logo_label.place(x=340, y=10)

            t1_label = Label(self.profil_window, image=t1_photo)
            t1_label.image = t1_photo
            t1_label.place(x=10, y=10)


            label_style = ttk.Style()
            label_style.configure('TLabel', background='black', font=self.labelfont, foreground='sky blue')


            entry_style = ttk.Style()
            entry_style.configure('TEntry', font=self.entryfont)


            radio_style = ttk.Style()
            radio_style.configure('TRadiobutton', background='#F0F0F0', font=self.labelfont)



            self.name_label = ttk.Label(self.profil_window, text='Name:', style='TLabel')
            self.name_label.place(x=50, y=60)

            self.contact_label = ttk.Label(self.profil_window, text='Contact Number:', style='TLabel')
            self.contact_label.place(x=50, y=110)

            self.email_label = ttk.Label(self.profil_window, text='Email Address:', style='TLabel')
            self.email_label.place(x=50, y=160)

            self.gender_label = ttk.Label(self.profil_window, text='Gender:', style='TLabel')
            self.gender_label.place(x=50, y=210)

            self.dob_label = ttk.Label(self.profil_window, text='Birthday:', style='TLabel')
            self.dob_label.place(x=50, y=260)

            self.filiere_label = ttk.Label(self.profil_window, text='Filiere:', style='TLabel')
            self.filiere_label.place(x=50, y=310)

            self.name_strvar = StringVar()
            self.name_strvar.set(a)

            self.name_entry = ttk.Entry(self.profil_window, textvariable=self.name_strvar, width=30)
            self.name_entry.place(x=200, y=60)

            self.contact_strvar = StringVar()
            self.contact_strvar.set(c)
            self.contact_entry = ttk.Entry(self.profil_window, textvariable=self.contact_strvar, width=30)
            self.contact_entry.place(x=200, y=110)

            self.email_strvar = StringVar()
            self.email_strvar.set(b)
            self.email_entry = ttk.Entry(self.profil_window, textvariable=self.email_strvar, width=30)
            self.email_entry.place(x=200, y=160)

            self.gender_strvar = StringVar()
            self.gender_strvar.set(d)

            self.gender_entry = ttk.Entry(self.profil_window, textvariable=self.gender_strvar, width=30)
            self.gender_entry.place(x=200, y=210)

            self.dob_strvar = StringVar()
            self.dob_strvar.set(e)
            self.dob_entry = ttk.Entry(self.profil_window, textvariable=self.dob_strvar, width=30)
            self.dob_entry.place(x=200, y=260)

            self.filiere_strvar = StringVar()
            self.filiere_strvar.set(f)
            self.filiere_entry = ttk.Entry(self.profil_window, textvariable=self.filiere_strvar, width=30)
            self.filiere_entry.place(x=200, y=310)

    root = Tk()
    app = App(root)
    root.mainloop()


def full():
    global window
    window = Tk()
    height = 650
    width = 1300

    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 4) - (height // 4)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    window.configure(bg="#525561")

    def login_user():
        mydb = mysql.connector.connect(host='localhost', port=3306, user='admin', password='admin',
                                       database='register_login')
        mycursor = mydb.cursor()
        global u, p
        u = username_entry.get()
        p = password_entry.get()
        mycursor.execute("select * from NEW_STUDENT_DATABASE where name=%s and password=%s", (u, p))
        c = 0
        for i in mycursor:
            c += 1
        if username_entry.get() == "" or password_entry.get() == "":
            msg.showerror("Error", "No informations!!")
        elif c == 1:

            new_id = uuid.uuid4()
            id_str = str(new_id)
            mycursor.execute("""
                            CREATE TABLE IF NOT EXISTS login (
                                id VARCHAR(50) PRIMARY KEY,
                                username VARCHAR(50) NOT NULL,
                                password VARCHAR(50) NOT NULL
                            )
                        """)
            mycursor.execute("insert into login values(%s, %s, %s)", (id_str, u, p))
            mydb.commit()
            accee()
        elif c > 1:
            msg.showerror("login details", "Name alreday existe!")
        else:
            msg.showerror("login details", " Invalid username or password")

    def recover_password():
        def search_email():
            import random
            import string

            def generate_password(length):
                letters = string.ascii_letters + string.digits
                return ''.join(random.choice(letters) for i in range(length))

            global passw
            passw = generate_password(10)

            if email_new == '':

                msg.showerror("Error", "please fill the field")
            else:

                mydb = mysql.connector.connect(
                    host="localhost",
                    user="admin",
                    password="admin",
                    database="register_login"
                )

                mycursor = mydb.cursor()
                E = email_new.get()
                mycursor.execute("SELECT * FROM NEW_STUDENT_DATABASE WHERE email=%s", (E,))
                row = mycursor.fetchone()
                if row is not None:
                    global key, Fi
                    key = row[6]
                    Fi = row[5]

                if row == None:
                    msg.showerror("Error", "Incorrect username", parent=win)
                else:

                    from email.message import EmailMessage
                    import smtplib
                    import ssl


                    smtp_username = 'email'# modifier
                    smtp_password = 'key' # modifier
                    user = email_new.get()

                    to_email = user
                    subject = 'New Password'
                    body = f'Your new password is: {passw}'
                    em = EmailMessage()
                    em['From'] = smtp_username
                    em['To'] = to_email
                    em['Subject'] = subject
                    em.set_content(body)
                    context = ssl.create_default_context()

                    # Send the email
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
                        server.login(smtp_username, smtp_password)
                        server.sendmail(smtp_username, to_email, em.as_string())
                    msg.showinfo("Success", "Verify your email")
                    win.destroy()

            def update_pass():
                if new_password_entry.get() == '' or confirm_password_entry.get() == '':

                    msg.showerror("Error", "All fields requiered")
                elif new_password_entry.get() != confirm_password_entry.get() != passw:
                    msg.showerror("Error", "password  and confirmed password are not matching")
                else:
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="admin",
                        password="admin",
                        database="register_login"
                    )


                    mycursor = mydb.cursor()

                    mycursor.execute("SELECT * FROM NEW_STUDENT_DATABASE WHERE password=%s", (key,))

                    row = mycursor.fetchall()

                    if row == None:
                        msg.showerror("Error", "Incorrect email")

                    else:
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="admin",
                            password="admin",
                            database="register_login"
                        )


                        mycursor = mydb.cursor()

                        mycursor.execute("UPDATE NEW_STUDENT_DATABASE SET password=%s WHERE password=%s", (passw, key))
                        mycursor.execute("UPDATE etudiant SET password=%s WHERE password=%s", (passw, key))
                        mycursor.execute("UPDATE login SET password=%s WHERE password=%s", (passw, key))
                        mycursor.execute(f"UPDATE {Fi} SET password=%s WHERE password=%s", (passw, key))

                        mydb.commit()
                        mydb.close()
                        msg.showinfo("Success", "Password is reset, please login with the new password")

            wi = Tk()
            window_width = 350
            window_height = 450
            screen_width = wi.winfo_screenwidth()
            screen_height = wi.winfo_screenheight()
            position_top = int(screen_height / 4 - window_height / 4)
            position_right = int(screen_width / 2 - window_width / 2)
            wi.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

            wi.title('reset password')

            wi.configure(background='#272A37')
            wi.resizable(False, False)
            text = Label(wi, text='Please enter the new password \n that we have sent\n via your email (:',
                         fg="#FFFFFF", bg='#272A37',
                         font=("yu gothic ui", 14, 'bold'))

            text.place(x=30, y=50)

            global new_password_entry
            new_password_entry = Entry(wi, bg="#3D404B", font=("yu gothic ui semibold", 12),
                                       highlightthickness=1,
                                       bd=0)
            new_password_entry.place(x=40, y=180, width=256, height=50)
            new_password_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
            new_password_label = Label(wi, text='• New Password', fg="#FFFFFF", bg='#272A37',
                                       font=("yu gothic ui", 11, 'bold'))
            new_password_label.place(x=40, y=150)

            global confirm_password_entry
            confirm_password_entry = Entry(wi, bg="#3D404B", font=("yu gothic ui semibold", 12),
                                           highlightthickness=1,
                                           bd=0)
            confirm_password_entry.place(x=40, y=280, width=256, height=50)
            confirm_password_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
            confirm_password_label = Label(wi, text='• Confirm Password', fg="#FFFFFF", bg='#272A37',
                                           font=("yu gothic ui", 11, 'bold'))
            confirm_password_label.place(x=40, y=250)


            update_butt = Button(
                wi,
                text="Update",
                font=("yu gothic ui", 13, "bold"),
                bg="#4EF500",
                bd=0,
                borderwidth=0,
                highlightthickness=0,
                relief="flat",
                activebackground="#272A37",
                cursor="hand2",
                command=lambda: [update_pass(), wi.destroy()])

            update_butt.place(x=40, y=360, width=256, height=45)
            wi.mainloop()

        win = Toplevel()
        window_width = 350
        window_height = 450
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        position_top = int(screen_height / 4 - window_height / 4)
        position_right = int(screen_width / 2 - window_width / 2)
        win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        win.title('Forgot Password')

        win.configure(background='#272A37')
        win.resizable(False, False)

        texx = Label(win, text='Enter your email!', fg="#FFFFFF", bg='#272A37',
                     font=("yu gothic ui", 17, 'bold'))
        texx.place(x=65, y=50)
        # ====== email====================
        global email_new
        email_new = Entry(win, bg="#3D404B", font=("white", 12), highlightthickness=1,
                          bd=0)
        email_new.place(x=40, y=150, width=256, height=50)
        email_new.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
        email_new_label = Label(win, text='• Email', fg="#FFFFFF", bg='#272A37',
                                font=("yu gothic ui", 11, 'bold'))
        email_new_label.place(x=40, y=120)

        # ======submit Button ============
        update_pass = Button(
            win,
            text="Submit",
            font=("yu gothic ui", 13, "bold"),
            bg="#4EF500",
            bd=0,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            activebackground="#272A37",
            cursor="hand2",
            command=search_email)

        update_pass.place(x=40, y=360, width=256, height=45)

    def creat_account():
        window.destroy()
        f = Tk()
        height = 650
        width = 1240
        x = (f.winfo_screenwidth() // 2) - (width // 2)
        y = (f.winfo_screenheight() // 4) - (height // 4)
        f.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        f.configure(bg="#525561")
        global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar, password_strvar
        name_strvar = StringVar()
        email_strvar = StringVar()
        contact_strvar = StringVar()
        gender_strvar = StringVar()
        stream_strvar = StringVar()
        dob = StringVar()
        password_strvar = StringVar()

        def reset_fields():
            for i in ['name_strvar', 'email_strvar', 'contact_strvar', 'gender_strvar', 'stream_strvar',
                      'password_strvar', 'dob']:
                exec(f"{i}.set('')")

        def add_record():
            mydb = mysql.connector.connect(
                host="localhost",
                user="admin",
                password="admin",
                database="register_login")

            mycursor = mydb.cursor()
            mycursor.execute(
                "CREATE TABLE IF NOT EXISTS NEW_STUDENT_DATABASE (NAME VARCHAR(255) primary key, EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")

            name = name_strvar.get()
            email = email_strvar.get()
            contact = contact_strvar.get()
            gender = gender_strvar.get()
            DOB = dob.get()
            stream = stream_strvar.get()
            password = password_strvar.get()

            if not name or not email or not contact or not gender or not DOB or not stream or not password:
                mb.showerror('Error!', "Please fill all the missing fields!!")
            else:
                if not name.isalpha():
                    mb.showerror('Error!', "Invalid name entered. Please enter a name containing only letters.")
                else:
                    phone_regex = re.compile(r"^(07|06)\d{8}$")
                    if not phone_regex.match(contact):
                        mb.showerror('Error!', "Invalid phone number Please enter a number in the format XXX-XXX-XXXX")
                    else:
                        pattern = r"^[a-zA-Z0-9]+@gmail\.com$"
                        match = re.match(pattern, email)
                        if not match:
                            mb.showerror('Error!', "Invalid email address entered. Please enter a valid gmail address.")
                        else:
                            if len(password) < 8 or (not re.search("[a-zA-Z]", password)) or (
                                    not re.search("[0-9]", password)) or (not re.search("[@#$%^&+=]", password)):
                                mb.showerror('Error!',
                                             "Invalid password entered. Please enter a password with at least 8 characters, including letters, numbers, and special characters (@#$%^&+=).")
                            else:
                                mycursor.execute("SELECT * FROM NEW_STUDENT_DATABASE WHERE name=%s OR email =%s",
                                                 (name, password))

                                result = mycursor.fetchone()
                                if result is None:
                                    mycursor.execute(
                                        "insert into NEW_STUDENT_DATABASE values(%s, %s, %s, %s, %s, %s, %s)",
                                        (name, email, contact, gender, DOB, stream, password))
                                    if stream == "CP1":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS CP1 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into CP1 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    elif stream == "CP2":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS CP2 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into CP2 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    elif stream == "ID1":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS ID1 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into ID1 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    elif stream == "ID2":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS ID2 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into ID2 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    elif stream == "ID3":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS ID3 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into ID3 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    elif stream == "GI1":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS GI1 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into GI1 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    elif stream == "GI2":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS GI2 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into GI2 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    elif stream == "GI3":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS GI3 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into GI3 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    elif stream == "GC1":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS GC1 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into GC1 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    elif stream == "GC2":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS GC2 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into GC2 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    elif stream == "GC3":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS GC3 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into GC3 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    elif stream == "GEE1":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS GEE1 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into GEE1 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    elif stream == "GEE2":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS GEE2 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into GEE2 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    elif stream == "GEE3":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS GEE3 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into GEE3 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    elif stream == "GEER1":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS GEER1 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into GEER1 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    elif stream == "GEER2":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS GEER2 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into GEER2 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))

                                    elif stream == "GEER3":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS GEER3 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into GEER3 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    elif stream == "GM1":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS GM1 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into GM1 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    elif stream == "GM2":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS GM2 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into GM2 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    elif stream == "GM3":
                                        mycursor.execute(
                                            "CREATE TABLE IF NOT EXISTS GM3 (NAME VARCHAR(255), EMAIL VARCHAR(255), PHONE_NO VARCHAR(255), GENDER VARCHAR(10), DOB DATE, STREAM VARCHAR(255), PASSWORD VARCHAR(255))")
                                        mycursor.execute(
                                            "insert into GM3 values(%s, %s, %s, %s, %s, %s, %s)",
                                            (name, email, contact, gender, DOB, stream, password))
                                    mydb.commit()
                                    mb.showinfo('Record added', f"Record of {name} was successfully added")

                                    reset_fields()
                                else:
                                    msg.showerror("login details", " already have account")

        # ================Background Image ====================
        backgroundImage = PhotoImage(file="images/16.png")
        bg_image = Label(
            f,
            image=backgroundImage,
            bg="#525561"
        )
        bg_image.place(x=120, y=28)

        # ================ Header Text Left ====================

        headerText1 = Label(
            bg_image,
            text="ENSAH Services!",
            fg="#FFFFFF",
            font=("yu gothic ui bold", 50 * -1),
            bg="#272A37"
        )
        headerText1.place(x=110, y=38)

        # ================ CREATE ACCOUNT HEADER ====================
        createAccount_header = Label(
            bg_image,
            text="Create new account",
            fg="#FFFFFF",
            font=("yu gothic ui Bold", 28 * -1),
            bg="#272A37"
        )
        createAccount_header.place(x=75, y=121)

        # ================ ALREADY HAVE AN ACCOUNT TEXT ====================
        text = Label(
            bg_image,
            text="Already a member?",
            fg="#FFFFFF",
            font=("yu gothic ui Regular", 15 * -1),
            bg="#272A37"
        )
        text.place(x=75, y=187)

        # ==================retour================
        def retour():
            f.destroy()
            full()

        # ================ GO TO LOGIN ====================
        switchLogin = Button(
            bg_image,
            text="Login",
            fg="#4EF500",
            font=("yu gothic ui Bold", 15 * -1),
            bg="#272A37",
            bd=0,
            cursor="hand2",
            activebackground="#272A37",
            activeforeground="#ffffff",
            command=retour
        )
        switchLogin.place(x=230, y=185, width=50, height=35)

        # =================variables de stockage=================
        name_strvar = StringVar()
        email_strvar = StringVar()
        contact_strvar = StringVar()
        gender_strvar = StringVar()
        stream_strvar = StringVar()
        dob = StringVar()
        password_strvar = StringVar()

        # ================ Username Section ====================
        firstName_image = PhotoImage(file="images/15.png")
        firstName_image_Label = Label(
            bg_image,
            image=firstName_image,
            bg="#272A37"
        )
        firstName_image_Label.place(x=80, y=242)

        firstName_text = Label(
            firstName_image_Label,
            text="Username",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        firstName_text.place(x=25, y=0)

        firstName_entry = Entry(
            firstName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
            textvariable=name_strvar
        )
        firstName_entry.place(x=8, y=17, width=140, height=27)

        # ================ phone Section ====================
        lastName_image = PhotoImage(file="images/15.png")
        phone_Label = Label(
            bg_image,
            image=lastName_image,
            bg="#272A37"
        )
        phone_Label.place(x=293, y=242)

        phone_text = Label(
            phone_Label,
            text="Phone number",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B",

        )
        phone_text.place(x=25, y=0)

        phone_entry = Entry(
            phone_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
            textvariable=contact_strvar
        )
        phone_entry.place(x=8, y=17, width=140, height=27)

        # ================ Email Name Section ====================
        emailName_image = PhotoImage(file="images/4.png")
        emailName_image_Label = Label(
            bg_image,
            image=emailName_image,
            bg="#272A37"
        )
        emailName_image_Label.place(x=80, y=311)

        emailName_text = Label(
            emailName_image_Label,
            text="Email account",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        emailName_text.place(x=25, y=0)

        emailName_entry = Entry(
            emailName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
            textvariable=email_strvar
        )
        emailName_entry.place(x=8, y=17, width=354, height=27)

        # ================ Password Name Section ====================
        passwordName_image = PhotoImage(file="images/15.png")
        passwordName_image_Label = Label(
            bg_image,
            image=passwordName_image,
            bg="#272A37"
        )
        passwordName_image_Label.place(x=80, y=380)

        passwordName_text = Label(
            passwordName_image_Label,
            text="Password",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        passwordName_text.place(x=25, y=0)

        passwordName_entry = Entry(
            passwordName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
            textvariable=password_strvar,
            show="*", )

        passwordName_entry.place(x=8, y=17, width=140, height=27)

        # ================ filiereSection ====================
        filiere_image = PhotoImage(file="images/15.png")
        filiere_image_Label = Label(
            bg_image,
            image=filiere_image,
            bg="#272A37"
        )
        filiere_image_Label.place(x=293, y=380)

        filiere_text = Label(
            filiere_image_Label,
            text="Filière",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        filiere_text.place(x=25, y=0)

        filiere_entry = OptionMenu(filiere_image_Label, stream_strvar, 'CP1', 'CP2', 'ID1', 'ID2', 'ID3', 'GI1', 'GI2',
                                   'GI3', 'GC1', 'GC2',
                                   'GC3',
                                   'GEE1',
                                   'GEE2', 'GEE3', 'GEER1', 'GEER2', 'GEER3', 'GM1', 'GM2', 'GM3')
        filiere_entry.config(bg="#3D404B", bd=0, highlightthickness=0, font=("yu gothic ui SemiBold", 16 * -1))
        filiere_entry.place(x=12, y=18, width=170, height=27)

        # ================ Gender Section ====================
        gender_image = PhotoImage(file="images/15.png")
        gender_image_Label = Label(
            bg_image,
            image=gender_image,
            bg="#272A37"
        )
        gender_image_Label.place(x=80, y=450)

        gender_text = Label(
            gender_image_Label,
            text="Gender",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        gender_text.place(x=25, y=0)

        gender_strvar = StringVar()

        gender_entry = OptionMenu(
            gender_image_Label,
            gender_strvar,
            "Female", "Male"
        )
        gender_entry.config(bg="#3D404B", bd=0, highlightthickness=0, font=("yu gothic ui SemiBold", 16 * -1))
        gender_entry.place(x=12, y=17, width=170, height=27)

        # ================ Birthday Section ====================
        birthday_image = PhotoImage(file="images/15.png")
        birthday_image_Label = Label(
            bg_image,
            image=birthday_image,
            bg="#272A37"
        )
        birthday_image_Label.place(x=293, y=450)

        birthday_text = Label(
            birthday_image_Label,
            text="Birthday",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        birthday_text.place(x=25, y=0)

        dob_entry = Entry(
            birthday_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 13 * -1),
            textvariable=dob
        )
        dob_entry.place(x=8, y=17, width=140, height=27)

        # =============== Submit Button ====================

        submit_button = Button(
            bg_image,
            text="Submit",
            font=("yu gothic ui", 13, "bold"),
            bg="#4EF500",
            bd=0,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            activebackground="#272A37",
            cursor="hand2",
            command=add_record
        )
        submit_button.place(x=210, y=570, width=150, height=40)

        f.resizable(False, False)
        f.mainloop()

    def contact():

        win = Toplevel(window)
        win.geometry("500x500")
        win.configure(background='#272A37')
        win.resizable(False, False)

        whatsapp_label = Label(win, text="WhatsApp : +212 676 618 872", font=("yu gothic ui", 11, 'bold'), bg='#272A37',
                               fg="#FFFFFF")
        whatsapp_label.pack(pady=10)

        whatsapp_button = Button(win, text="Ouvrir WhatsApp", bg="#4EF500", font=("yu gothic ui", 11, 'bold'),
                                 command=lambda: webbrowser.open("https://wa.me/212707868252"))
        whatsapp_button.pack(pady=5)

        email_label = Label(win, text="Email : bchjawad123@gmail.com", fg='#4EF500', bg="#272A37",
                            font=("yu gothic ui", 11, 'bold'))
        email_label.pack(pady=10)

        email_link = Label(win, text="Envoyer un e-mail", font=("yu gothic ui", 11, 'bold'), fg="blue", cursor="hand2")
        email_link.pack(pady=5)
        email_link.bind("<Button-1>", lambda event: webbrowser.open("mailto:bchjawad123@gmail.com"))

    # ================Background Image ====================
    Login_backgroundImage = PhotoImage(file="images/13.png")
    bg_imageLogin = Label(
        window,
        image=Login_backgroundImage,
        bg="#525561"
    )
    bg_imageLogin.place(x=120, y=28)

    Login_headerText1 = Label(
        bg_imageLogin,
        text="ENSAH Services",
        fg="#FFFFFF",
        font=("yu gothic ui bold", 50 * -1),
        bg="#272A37"
    )
    Login_headerText1.place(x=110, y=35)

    # ================ LOGIN TO ACCOUNT HEADER ====================
    loginAccount_header = Label(
        bg_imageLogin,
        text="Login to continue",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 28 * -1),
        bg="#272A37"
    )
    loginAccount_header.place(x=75, y=121)

    # ================ NOT A MEMBER TEXT ====================
    loginText = Label(
        bg_imageLogin,
        text="Not a member?",
        fg="#FFFFFF",
        font=("yu gothic ui Regular", 15 * -1),
        bg="#272A37"
    )
    loginText.place(x=75, y=187)

    # ================ GO TO SIGN UP ====================
    switchSignup = Button(
        bg_imageLogin,
        text="Sign Up",
        fg="#4EF500",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37",
        bd=0,
        cursor="hand2",
        activebackground="#272A37",
        activeforeground="#ffffff",
        command=lambda: creat_account()
    )
    switchSignup.place(x=220, y=185, width=70, height=35)

    about = Button(
        bg_imageLogin,
        text="About us",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#4EF500",
        bd=0,
        cursor="hand2",
        command=contact

    )
    about.place(x=750, y=530)

    # ================ username Name Section ====================
    Login_emailName_image = PhotoImage(file="images/4.png")
    Login_emailName_image_Label = Label(
        bg_imageLogin,
        image=Login_emailName_image,
        bg="#272A37"
    )
    Login_emailName_image_Label.place(x=76, y=242)

    Login_emailName_text = Label(
        Login_emailName_image_Label,
        text="Name",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    Login_emailName_text.place(x=25, y=0)

    Login_emailName_icon = PhotoImage(file="images/5.png")
    Login_emailName_icon_Label = Label(
        Login_emailName_image_Label,
        image=Login_emailName_icon,
        bg="#3D404B"
    )
    Login_emailName_icon_Label.place(x=370, y=15)

    username_entry = Entry(
        Login_emailName_image_Label,
        bd=0,
        bg="#3D404B",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    username_entry.place(x=8, y=17, width=354, height=27)

    # ================ Password Name Section ====================
    Login_passwordName_image = PhotoImage(file="images/4.png")
    Login_passwordName_image_Label = Label(
        bg_imageLogin,
        image=Login_passwordName_image,
        bg="#272A37"
    )
    Login_passwordName_image_Label.place(x=80, y=330)

    Login_passwordName_text = Label(
        Login_passwordName_image_Label,
        text="Password",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    Login_passwordName_text.place(x=25, y=0)

    Login_passwordName_icon = PhotoImage(file="images/17.png")
    Login_passwordName_icon_Label = Label(
        Login_passwordName_image_Label,
        image=Login_passwordName_icon,
        bg="#3D404B"
    )
    Login_passwordName_icon_Label.place(x=370, y=15)

    password_entry = Entry(
        Login_passwordName_image_Label,
        bd=0,
        bg="#3D404B",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    password_entry.place(x=8, y=17, width=354, height=27)

    # =============== Submit Button ====================
    Login_button_1 = Button(bg_imageLogin, text="Submit", font=("yu gothic ui", 13, "bold"), bg="#4EF500", bd=0,
                            command=login_user)

    Login_button_1.place(x=210, y=445, width=150, height=40)

    # ================ Forgot Password ====================
    forgotPassword = Button(
        bg_imageLogin,
        text="Forgot Password?",
        fg="#4EF500",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37",
        bd=0,
        activebackground="#272A37",
        activeforeground="#ffffff",
        cursor="hand2",
        command=recover_password,
    )
    forgotPassword.place(x=210, y=400, width=150, height=35)

    window.resizable(False, False)
    window.mainloop()


def deb():
    def database():
        admin.destroy()
        students = Tk()
        height = 550
        width = 920
        students.title('Students database')
        x = (students.winfo_screenwidth() // 2) - (width // 2)
        y = (students.winfo_screenheight() // 4) - (height // 4)
        students.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        students.configure(bg="#525561")
        image = PhotoImage(file="images/16.png")
        label = Label(students, image=image)
        label.place(x=0, y=30)
        static_label = Label(students, text="ESPACE ETUDIANT", font=("Arial", 14, "bold"), bg='gray')
        static_label.pack(side=TOP, fill=X)

        def retourn():
            students.destroy()
            deb()

        def table(T: str):
            mydb = mysql.connector.connect(
                host="localhost",
                user="admin",
                password="admin",
                database="register_login")
            global mycursor
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT * FROM {T}")
            rows = mycursor.fetchall()
            global table1
            table1 = ttk.Treeview(students)
            table1["columns"] = ("NAME", "EMAIL", "PHONE_NO", "GENDER", "DOB", "STREAM", "PASSWORD")
            table1.column("#0", width=0, stretch=tk.NO)
            table1.column("NAME", anchor=tk.W, width=90)
            table1.column("EMAIL", anchor=tk.CENTER, width=180)
            table1.column("PHONE_NO", anchor=tk.CENTER, width=90)
            table1.column("GENDER", anchor=tk.W, width=50)
            table1.column("DOB", anchor=tk.W, width=70)
            table1.column("STREAM", anchor=tk.W, width=40)
            table1.column("PASSWORD", anchor=tk.W, width=100)

            table1.heading("NAME", text="NAME")
            table1.heading("EMAIL", text="EMAIL")
            table1.heading("PHONE_NO", text="PHONE_NO")
            table1.heading("GENDER", text="GENDER")
            table1.heading("DOB", text="DOB")
            table1.heading("STREAM", text="STREAM")
            table1.heading("PASSWORD", text="PASSWORD")

            for row in rows:
                table1.insert(parent="", index="end", text="",
                              values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

            table1.pack()

        def vider_la_table():
            selected_item = table1.focus()
            select_filiere = table1.item(selected_item)['values'][5]
            confirmed = messagebox.askyesno("Confirmation", "vous voulez vraiment supprimer tous les enregistrements?")
            if confirmed:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="admin",
                    password="admin",
                    database="register_login"
                )
                mycursor = mydb.cursor()
                sql = "DELETE FROM NEW_STUDENT_DATABASE WHERE STREAM = %s"
                val = (select_filiere,)
                mycursor.execute(sql, val)
                mycursor.execute(f"DELETE FROM {select_filiere}")
                msg.showinfo("suppression", "successfully!")
                mydb.commit()
            students.destroy()
            deb()

        delete_button = tk.Button(students, text="SUPPRIMER TOUS", command=vider_la_table, bg="#46CD07", width=20,
                                  height=2, font=("Arial", 14, "bold"))
        delete_button.place(x=30, y=300)

        def suprimer_record():
            selected_item = table1.focus()
            confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to delete this record?")
            if confirmed:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="admin",
                    password="admin",
                    database="register_login"
                )
                password = table1.item(selected_item)['values'][6]
                filiere = table1.item(selected_item)['values'][5]


                mycursor = mydb.cursor()
                sql = "DELETE FROM NEW_STUDENT_DATABASE WHERE PASSWORD = %s"
                val = (password,)
                mycursor.execute(sql, val)
                sql = f"DELETE FROM {filiere} WHERE PASSWORD = %s"
                val = (password,)
                mycursor.execute(sql, val)
                mydb.commit()
                table1.delete(selected_item)

        delete1_button = tk.Button(students, text="SUPPRIMER", command=suprimer_record, bg="#46CD07", width=20,
                                   height=2, font=("Arial", 14, "bold"))
        delete1_button.place(x=315, y=300)
        retour_button = tk.Button(students, text="<<--", command=retourn, bg="#FFFFFF", width=5)
        retour_button.place(x=0, y=0)

        def modifier_record():
            selected_item = table1.focus()
            global values
            values = table1.item(selected_item)["values"]
            tb = table1.item(selected_item)['values'][5]

            modifier = Tk()
            modifier.geometry("400x400")
            static_label = Label(modifier, text="Modification ", font=("Arial", 14, "bold"), bg='gray')
            static_label.pack(side=TOP, fill=X)

            global name_entry, email_entry, phone_no_entry, gender_entry, dob_entry, stream_entry, password_entry
            name_label = tk.Label(modifier, text="NAME:")
            name_label.place(x=50, y=60)
            name_entry = tk.Entry(modifier, width=30)
            name_entry.insert(tk.END, values[0])
            name_entry.place(x=150, y=60)

            email_label = tk.Label(modifier, text="EMAIL:")
            email_label.place(x=50, y=90)
            email_entry = tk.Entry(modifier, width=30)
            email_entry.insert(tk.END, values[1])
            email_entry.place(x=150, y=90)

            phone_no_label = tk.Label(modifier, text="PHONE:")
            phone_no_label.place(x=50, y=120)
            phone_no_entry = tk.Entry(modifier, width=30)
            phone_no_entry.insert(tk.END, values[2])
            phone_no_entry.place(x=150, y=120)

            gender_label = tk.Label(modifier, text="GENDER:")
            gender_label.place(x=50, y=150)
            gender_entry = tk.Entry(modifier, width=30)
            gender_entry.insert(tk.END, values[3])
            gender_entry.place(x=150, y=150)

            dob_label = tk.Label(modifier, text="DOB:")
            dob_label.place(x=50, y=180)
            dob_entry = tk.Entry(modifier, width=30)
            dob_entry.insert(tk.END, values[4])
            dob_entry.place(x=150, y=180)

            stream_label = tk.Label(modifier, text="Filiere:")
            stream_label.place(x=50, y=210)
            stream_entry = tk.Entry(modifier, width=30)
            stream_entry.insert(tk.END, values[5])
            stream_entry.place(x=150, y=210)

            password_label = tk.Label(modifier, text="PASSWORD:")
            password_label.place(x=50, y=240)
            password_entry = tk.Entry(modifier, width=30)
            password_entry.insert(tk.END, values[6])
            password_entry.place(x=150, y=240)

            def enregistrer():
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="admin",
                    password="admin",
                    database="register_login"
                )
                mycursor = mydb.cursor()
                tables = ["new_student_database", tb, "etudiant"]
                for t in tables:
                    sql = f"UPDATE {t} SET name=%s,email=%s,phone_no=%s,gender=%s,dob=%s,stream=%s,password=%s WHERE password=%s"
                    val = (
                        name_entry.get(), email_entry.get(), phone_no_entry.get(), gender_entry.get(), dob_entry.get(),
                        stream_entry.get(), password_entry.get(), values[6])
                    mycursor.execute(sql, val)
                    mydb.commit()
                msg.showinfo("modification", " record modified")
                modifier.destroy()
                students.destroy()
                deb()

            submit_button = Button(modifier, text="ENREGISTRER", command=enregistrer, font=("Arial", 10, "bold"),
                                   bg="#46CD07", width=12)
            submit_button.place(x=155, y=330)
            modifier.mainloop()

        modifier_button = tk.Button(students, text="MODIFIER", command=modifier_record, bg="#46CD07", width=20,
                                    height=2, font=("Arial", 14, "bold"))
        modifier_button.place(x=610, y=300)

        def cp1():
            T = "CP1"
            table(T)

        def cp2():
            T = "CP2"
            table(T)

        def id1():
            T = "ID1"
            table(T)

        def id2():
            T = "ID2"
            table(T)

        def id3():
            T = "ID3"
            table(T)

        def gi1():
            T = "GI1"
            table(T)

        def gi2():
            T = "GI2"
            table(T)

        def gi3():
            T = "GI3"
            table(T)

        def gc1():
            T = "GC1"
            table(T)

        def gc2():
            T = "GC2"
            table(T)

        def gc3():
            T = "GC3"
            table(T)

        def gee1():
            T = "GEE1"
            table(T)

        def gee2():
            T = "GEE2"
            table(T)

        def gee3():
            T = "GEE3"
            table(T)

        def geer1():
            T = "GEER1"
            table(T)

        def geer2():
            T = "GEER2"
            table(T)

        def geer3():
            T = "GEER3"
            table(T)

        def gm1():
            T = "GM1"
            table(T)

        def gm2():
            T = "GM2"
            table(T)

        def gm3():
            T = "GM3"
            table(T)

        cp1_button = tk.Button(students, text="CP1", command=cp1, bg="#808080", width=10)
        cp1_button.place(x=10, y=520)
        cp2_button = tk.Button(students, text="CP2", command=cp2, bg="#808080", width=10)
        cp2_button.place(x=100, y=520)
        id1_button = tk.Button(students, text="ID1", command=id1, bg="#808080", width=10)
        id1_button.place(x=190, y=520)
        id2_button = tk.Button(students, text="ID2", command=id2, bg="#808080", width=10)
        id2_button.place(x=280, y=520)
        id3_button = tk.Button(students, text="ID3", command=id3, bg="#808080", width=10)
        id3_button.place(x=370, y=520)
        gi1_button = tk.Button(students, text="GI1", command=gi1, bg="#808080", width=10)
        gi1_button.place(x=460, y=520)
        gi2_button = tk.Button(students, text="GI2", command=gi2, bg="#808080", width=10)
        gi2_button.place(x=550, y=520)
        gi3_button = tk.Button(students, text="GI3", command=gi3, bg="#808080", width=10)
        gi3_button.place(x=640, y=520)
        gc1_button = tk.Button(students, text="GC1", command=gc1, bg="#808080", width=10)
        gc1_button.place(x=730, y=520)
        gc2_button = tk.Button(students, text="GC2", command=gc2, bg="#808080", width=10)
        gc2_button.place(x=820, y=520)
        gc3_button = tk.Button(students, text="GC3", command=gc3, bg="#808080", width=10)
        gc3_button.place(x=10, y=480)
        gee1_button = tk.Button(students, text="GEE1", command=gee1, bg="#808080", width=10)
        gee1_button.place(x=100, y=480)
        gee2_button = tk.Button(students, text="GEE2", command=gee2, bg="#808080", width=10)
        gee2_button.place(x=190, y=480)
        gee3_button = tk.Button(students, text="GEE3", command=gee3, bg="#808080", width=10)
        gee3_button.place(x=280, y=480)
        geer1_button = tk.Button(students, text="GEER1", command=geer1, bg="#808080", width=10)
        geer1_button.place(x=370, y=480)
        geer2_button = tk.Button(students, text="GEER2", command=geer2, bg="#808080", width=10)
        geer2_button.place(x=460, y=480)
        geer3_button = tk.Button(students, text="GEER3", command=geer3, bg="#808080", width=10)
        geer3_button.place(x=550, y=480)
        gm1_button = tk.Button(students, text="GM1", command=gm1, bg="#808080", width=10)
        gm1_button.place(x=640, y=480)
        gm2_button = tk.Button(students, text="GM2", command=gm2, bg="#808080", width=10)
        gm2_button.place(x=730, y=480)
        gm3_button = tk.Button(students, text="GM3", command=gm3, bg="#808080", width=10)
        gm3_button.place(x=820, y=480)
        students.mainloop()

    def messagerie():
        admin.destroy()
        messagerie = tk.Tk()
        messagerie.geometry("700x500")
        messagerie.configure(bg="#272A37")
        static_label = Label(messagerie, text="ESPACE ADMIN", font=("Arial", 14, "bold"), bg='blue')
        static_label.place(x=0, y=0, relwidth=1)

        var1 = tk.BooleanVar()
        var2 = tk.BooleanVar()
        var3 = tk.BooleanVar()
        var4 = tk.BooleanVar()
        var5 = tk.BooleanVar()
        var6 = tk.BooleanVar()
        var7 = tk.BooleanVar()
        var8 = tk.BooleanVar()
        var9 = tk.BooleanVar()
        var10 = tk.BooleanVar()
        var11 = tk.BooleanVar()
        var12 = tk.BooleanVar()
        var13 = tk.BooleanVar()
        var14 = tk.BooleanVar()
        var15 = tk.BooleanVar()
        var16 = tk.BooleanVar()
        var17 = tk.BooleanVar()
        var18 = tk.BooleanVar()
        var19 = tk.BooleanVar()
        var20 = tk.BooleanVar()

        cb1 = tk.Checkbutton(messagerie, text="CP1", variable=var1, width=5)
        cb2 = tk.Checkbutton(messagerie, text="CP2", variable=var2, width=5)
        cb3 = tk.Checkbutton(messagerie, text="ID1", variable=var3, width=5)
        cb4 = tk.Checkbutton(messagerie, text="ID2", variable=var4, width=5)
        cb5 = tk.Checkbutton(messagerie, text="ID3", variable=var5, width=5)
        cb6 = tk.Checkbutton(messagerie, text="GI1", variable=var6, width=5)
        cb7 = tk.Checkbutton(messagerie, text="GI2", variable=var7, width=5)
        cb8 = tk.Checkbutton(messagerie, text="GI3", variable=var8, width=5)
        cb9 = tk.Checkbutton(messagerie, text="GC1", variable=var9, width=5)
        cb10 = tk.Checkbutton(messagerie, text="GC2", variable=var10, width=5)
        cb11 = tk.Checkbutton(messagerie, text="GC3", variable=var11, width=5)
        cb12 = tk.Checkbutton(messagerie, text="GM1", variable=var12, width=5)
        cb13 = tk.Checkbutton(messagerie, text="GM2", variable=var13, width=5)
        cb14 = tk.Checkbutton(messagerie, text="GM3", variable=var14, width=5)
        cb15 = tk.Checkbutton(messagerie, text="GEE1", variable=var15, width=5)
        cb16 = tk.Checkbutton(messagerie, text="GEE2", variable=var16, width=5)
        cb17 = tk.Checkbutton(messagerie, text="GEE3", variable=var17, width=5)
        cb18 = tk.Checkbutton(messagerie, text="GEER1", variable=var18, width=5)
        cb19 = tk.Checkbutton(messagerie, text="GEER2", variable=var19, width=5)
        cb20 = tk.Checkbutton(messagerie, text="GEER3", variable=var20, width=5)

        cb1.place(x=225, y=100)
        cb2.place(x=275, y=100)
        cb3.place(x=325, y=100)
        cb4.place(x=375, y=100)
        cb5.place(x=425, y=100)
        cb6.place(x=225, y=130)
        cb7.place(x=275, y=130)
        cb8.place(x=325, y=130)
        cb9.place(x=375, y=130)
        cb10.place(x=425, y=130)
        cb11.place(x=225, y=160)
        cb12.place(x=275, y=160)
        cb13.place(x=325, y=160)
        cb14.place(x=375, y=160)
        cb15.place(x=425, y=160)
        cb16.place(x=225, y=190)
        cb17.place(x=275, y=190)
        cb18.place(x=325, y=190)
        cb19.place(x=375, y=190)
        cb20.place(x=425, y=190)

        subject_label = tk.Label(messagerie, text='<<SUJET>>')
        subject_label.place(x=225, y=250)

        subject_entry = tk.Entry(messagerie)
        subject_entry.place(x=300, y=250, width=200)

        body_label = tk.Label(messagerie, text='<<MESSAGE>>')
        body_label.place(x=325, y=290)

        body_entry = tk.Text(messagerie, height=8)
        body_entry.place(x=100, y=320, width=500)

        def retourl():
            messagerie.destroy()
            deb()

        def email(variable):
            mydb = mysql.connector.connect(
                host="localhost",
                user="admin",
                password="admin",
                database="register_login"
            )
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT EMAIL FROM {variable}")
            rows = mycursor.fetchall()
            email_list = [row[0] for row in rows]
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            smtp_username = "email"  # adresse e-mail de l'expéditeur
            smtp_password = "key"  # mot de passe de l'expéditeur
            smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
            smtp_connection.starttls()
            smtp_connection.login(smtp_username, smtp_password)
            subject = subject_entry.get()
            body = body_entry.get("1.0", "end-1c")
            message = f"Subject: {subject}\n\n{body}"
            for email_address in email_list:
                smtp_connection.sendmail(smtp_username, email_address, message)
            smtp_connection.quit()

        def show_checked():
            mydb = mysql.connector.connect(
                host="localhost",
                user="admin",
                password="admin",
                database="register_login"
            )
            mycursor = mydb.cursor()
            if var1.get():
                V = "CP1"
                email(V)
            if var2.get():
                V = "CP2"
                email(V)
            if var3.get():
                V = "ID1"
                email(V)
            if var4.get():
                V = "ID2"
                email(V)
            if var5.get():
                V = "ID3"
                email(V)
            if var6.get():
                V = "GI1"
                email(V)
            if var7.get():
                V = "GI2"
                email(V)
            if var8.get():
                V = "GI3"
                email(V)
            if var9.get():
                V = "GC1"
                email(V)
            if var10.get():
                V = "GC2"
                email(V)
            if var11.get():
                V = "GC3"
                email(V)
            if var12.get():
                V = "GM1"
                email(V)
            if var13.get():
                V = "GM2"
                email(V)
            if var14.get():
                V = "GM3"
                email(V)
            if var15.get():
                V = "GEE1"
                email(V)
            if var16.get():
                V = "GEE2"
                email(V)
            if var17.get():
                V = "GEE3"
                email(V)
            if var18.get():
                V = "GEER1"
                email(V)
            if var19.get():
                V = "GEER2"
                email(V)
            if var20.get():
                V = "GEER3"
                email(V)
            mycursor.close()
            mydb.close()

        button_en = tk.Button(messagerie, text="ENVOYER", command=show_checked, bg="#46CD07", width=10,
                              font=("Arial", 14, "bold"))
        button_en.place(x=300,
                        y=460)  # Remplacez les numéros de ligne et de colonne par ceux que vous souhaitez utiliser
        button_re = tk.Button(messagerie, text="RETOUR", command=retourl)
        button_re.place(x=0, y=0)
        messagerie.mainloop()

    admin = Tk()
    height = 400
    width = 800
    admin.title("Admin")
    x = (admin.winfo_screenwidth() // 2) - (width // 2)
    y = (admin.winfo_screenheight() // 4) - (height // 4)
    admin.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    admin.configure(bg="#272A37")
    img1 = tk.PhotoImage(file="images/16.png")
    canvas1 = tk.Canvas(admin, width=800, height=400)
    canvas1.create_image(100, 100, image=img1)
    canvas1.place(x=0, y=0)

    def create_animated_welcome_label(admin):

        welcome_text = Label(admin, text="", font=("Arial", 12, "bold italic"), fg="#0091D0")
        welcome_text.config(relief=SOLID)
        welcome_text.config(highlightbackground="#0091D0", highlightthickness=2)
        welcome_text.place(x=200, y=40)


        text = "Bienvenue sur la plateforme de consultation ENSAH  "

        def animate_text():
            nonlocal text
            text = text[-1] + text[:-1]
            welcome_text.config(text=text)
            welcome_text.after(90, animate_text)

        animate_text()

    create_animated_welcome_label(admin)

    database_button = Button(admin, text="ENREGISTREMENT DES ETUDIANT", command=database, height=2,
                             font=("Arial", 12, "bold"), bg="#46CD07", width=30)
    database_button.place(x=250, y=150)

    messagerie_button = Button(admin, text="MESSAGERIE", command=messagerie, height=2, font=("Arial", 12, "bold"),
                               bg="#46CD07", width=16)
    messagerie_button.place(x=320, y=250)

    def retourm():
        admin.destroy()
        firstpage()

    retour_button = tk.Button(admin, text="déconnexion", command=retourm, bg="#46CD07", font=("Arial", 10, "bold"),
                              width=10)
    retour_button.place(x=0, y=350)
    admin.mainloop()


def secondpage():
    choix.destroy()
    conne = tk.Tk()
    conne.geometry("600x400")
    conne.configure(bg="#272A37")
    conne.title("Connexion")
    static_label = Label(conne, text="Admin connexion ", font=("Arial", 14, "bold"), bg='gray')
    static_label.pack(side=TOP, fill=X)

    img1 = tk.PhotoImage(file="images/3.png")
    canvas1 = tk.Canvas(conne, width=600, height=400)
    canvas1.create_image(100, 100, image=img1)
    canvas1.place(x=0, y=30)

    email_label = tk.Label(conne, text='Email :', font=('calibre', 10, 'bold'), bg="#808080", width=10)
    email_entry = tk.Entry(conne, width=30, font=('calibre', 10, 'normal'))
    password_label = tk.Label(conne, text='Password :', font=('calibre', 10, 'bold'), bg="#808080", width=10)
    password_entry = tk.Entry(conne, show='*', width=30, font=('calibre', 10, 'normal'))

    email_label.place(x=100, y=150)
    email_entry.place(x=200, y=150)
    password_label.place(x=100, y=200)
    password_entry.place(x=200, y=200)

    def connexion():
        email = email_entry.get()
        password = password_entry.get()
        if email == "email" and password == "password": # email et password pour la connexion
            conne.destroy()
            deb()
        else:
            msg.showerror("login deatils", "wrong register details!")

    connect_button = tk.Button(conne, text="SE CONNECTER", command=connexion, bg="#46CD07", width=15, height=1,
                               font=("Arial", 14, "bold"))
    connect_button.place(x=200, y=300)

    # Centrage de la fenêtre
    window_height = 400
    window_width = 600
    screen_width = conne.winfo_screenwidth()
    screen_height = conne.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    conne.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    conne.mainloop()


def firstpage():
    global choix
    choix = tk.Tk()
    choix.geometry("600x300")
    choix.title("Bienvenue")
    choix.configure(bg="#272A37")


    img1 = tk.PhotoImage(file="images/11.png")
    img2 = tk.PhotoImage(file="images/12.png")


    canvas1 = tk.Canvas(choix, width=200, height=200)
    canvas1.create_image(100, 100, image=img1)
    canvas1.grid(row=7, column=0, padx=50)

    canvas2 = tk.Canvas(choix, width=200, height=200)
    canvas2.create_image(100, 100, image=img2)
    canvas2.grid(row=7, column=4, padx=50)

    button1 = tk.Button(choix, text="ADMIN", width=10, bg="#46CD07", command=secondpage, font=("Arial", 14, "bold"))
    button1.grid(row=9, column=4)

    button2 = tk.Button(choix, text="ETUDIANT", bg="#46CD07", width=10, font=("Arial", 14, "bold"),
                        command=lambda: [choix.destroy(), full()])

    button2.grid(row=9, column=0)

    choix.mainloop()


firstpage()
