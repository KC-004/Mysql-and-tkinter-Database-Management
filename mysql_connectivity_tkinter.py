
from tkinter import *
from tkinter import messagebox
from mysql import connector


''' Functions '''

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def display_data():
    clear_window()
    mycursor = mydb.cursor()      #Connectig to mysql
    qry = "SELECT * FROM info"
    mycursor.execute(qry)

    tabel_label = Label(window, text='Table', compound="top")
    tabel_label.grid(row=0, columnspan=4)

    storage = []                  #Storing
    for items in mycursor:
        storage.append(items)
    print(storage)
    n = len(storage)
    i = 0
    for i in range(n):                    #Creating table
        for j in range(len(storage[i])):
            entry = Entry(window,
                          font=('futura', 12, 'bold'),
                          bg='black',
                          fg='white'
                          )
            entry.grid(column=j, row=i+1, pady=10, padx=10)
            entry.insert(END, storage[i][j])

    btn = Button(window,
                 text='Back',
                 command=home,
                 width=20
                 )
    btn.grid(row=i+2, columnspan=2, column=1)

def get_specific_data():

    def by_id():

        def display_by_id(id):

            clear_window()

            mycursor = mydb.cursor()  # Connectig to mysql
            qry = 'SELECT * FROM info WHERE id = %s'
            val = [id]
            mycursor.execute(qry, val)

            tabel_label = Label(window, text='Table')
            tabel_label.grid(row=0, columnspan=4)

            storage = []  # Storing
            for items in mycursor:
                storage.append(items)
            print(storage)
            n = len(storage)
            i=0
            for i in range(n):  # Creating table
                for j in range(len(storage[i])):
                    entry = Entry(window,
                                  font=('futura', 12, 'bold'),
                                  bg='black',
                                  fg='white'
                                  )
                    entry.grid(column=j, row=i + 1, pady=10, padx=10)
                    entry.insert(END, storage[i][j])
            btn = Button(window,
                         text='Back',
                         command=home,
                         width=20
                         )
            btn.grid(row=i + 2, columnspan=2, column=1)

        clear_window()
        title = Label(window,
                      text='Enter the Name:',
                      font=('futura', 20, 'italic')
                      )
        entry = Entry(window,
                      font=('futura', 20, 'italic'),
                      width=15
                      )
        get_data = Button(window,
                          text='Get Data',
                          font=('futura', 16),
                          width=20,
                          command=lambda: display_by_id(entry.get())
                          )
        btn = Button(window,
                     text='Back',
                     command=home,
                     width=20
                     )
        title.grid(row=0, padx=10, pady=10)
        entry.grid(row=1, padx=10, pady=10)
        get_data.grid(row=2, padx=10, pady=10)
        btn.grid(row=3, padx=10, pady=10)


    def by_name():

        def display_by_name(name):

            clear_window()

            mycursor = mydb.cursor()  # Connectig to mysql
            qry = 'SELECT * FROM info WHERE name = %s'
            val = [name]
            mycursor.execute(qry, val)

            tabel_label = Label(window, text='Table')
            tabel_label.grid(row=0, columnspan=4)

            storage = []  # Storing
            for items in mycursor:
                storage.append(items)
            print(storage)
            n = len(storage)
            i=0
            for i in range(n):  # Creating table
                for j in range(len(storage[i])):
                    entry = Entry(window,
                                    font=('futura', 12, 'bold'),
                                    bg='black',
                                    fg='white'
                                    )
                    entry.grid(column=j, row=i + 1, pady=10, padx=10)
                    entry.insert(END, storage[i][j])

            btn = Button(window,
                         text='Back',
                         command=home,
                         width=20
                         )
            btn.grid(row=i + 2, columnspan=2, column=1)

        clear_window()
        title = Label(window,
                      text='Enter the Name:',
                      font=('futura', 20, 'italic')
                      )
        entry = Entry(window,
                      font=('futura', 20, 'italic'),
                      width=15
                      )
        get_data = Button(window,
                             text='Get Data',
                             font=('futura', 16),
                             width=20,
                             command=lambda:display_by_name(entry.get())
                             )
        btn = Button(window,
                     text='Back',
                     command=home,
                     width=20
                     )
        title.grid(row=0, padx=10, pady=10)
        entry.grid(row=1, padx=10, pady=10)
        get_data.grid(row=2, padx=10, pady=10)
        btn.grid(row=3, padx=10, pady=10)


    def by_city():

        def display_by_city(city):


            clear_window()

            mycursor = mydb.cursor()  # Connectig to mysql
            qry = 'SELECT * FROM info WHERE city = %s'
            val = [city]
            mycursor.execute(qry, val)

            tabel_label = Label(window, text='Table')
            tabel_label.grid(row=0, columnspan=4)

            storage = []  # Storing
            for items in mycursor:
                storage.append(items)
            print(storage)
            n = len(storage)
            i = 0
            for i in range(n):  # Creating table
                for j in range(len(storage[i])):
                    entry = Entry(window,
                                  font=('futura', 12, 'bold'),
                                  bg='black',
                                  fg='white'
                                  )
                    entry.grid(column=j, row=i + 1, pady=10, padx=10)
                    entry.insert(END, storage[i][j])

            btn = Button(window,
                         text='Back',
                         command=home,
                         width=20
                         )
            btn.grid(row=i+2, columnspan=2, column=1)

        clear_window()
        title = Label(window,
                      text='Enter the Name:',
                      font=('futura', 20, 'italic')
                      )
        entry = Entry(window,
                      font=('futura', 20, 'italic'),
                      width=15
                      )
        get_data = Button(window,
                          text='Get Data',
                          font=('futura', 16),
                          width=20,
                          command=lambda: display_by_city(entry.get())
                          )
        btn = Button(window,
                     text='Back',
                     command=home,
                     width=20
                     )
        title.grid(row=0, padx=10, pady=10)
        entry.grid(row=1, padx=10, pady=10)
        get_data.grid(row=2, padx=10, pady=10)
        btn.grid(row=3, padx=10, pady=10)
    ''' _______________________________________'''
    clear_window()
    label = Label(window,
                  text='Get details by:',
                  font=('futura', 20, 'italic')
                  )
    by_id = Button(window,
                    text='Id',
                    font=('futura', 16),
                    width=20,
                    command=by_id
                    )
    by_name = Button(window,
                    text='Name',
                    font=('futura', 16),
                    width=20,
                    command=by_name
                    )
    by_city = Button(window,
                    text='City',
                    font=('futura', 16),
                    width=20,
                    command=by_city
                    )
    btn = Button(window,
                 text='Back',
                 command=home,
                 width=20
                 )
    btn.grid(row=3, padx=10, pady=10)

    label.grid(row=0, padx=10, pady=10)
    by_id.grid(row=1, padx=10, pady=10)
    by_name.grid(row=2, padx=10, pady=10)
    by_city.grid(row=3, padx=10, pady=10)
    btn.grid(row=4, padx=10, pady=10)

def add_data():

    def insert_data(id, name, city, phone):
        try:

            mycursor = mydb.cursor()
            qry = 'INSERT INTO INFO (id, name, city, phone) VALUES(%s, %s, %s, %s)'
            val = [id, name, city, phone]

            mycursor.execute(qry, val)
            print("Data successfully added!")
            messagebox.showinfo(title='Done', message='Added successfully!')


        except:
            messagebox.showerror(title='Error', message='Something went wrong.')
            home()


    clear_window()
    label = Label(window,
                  text='Insert Data',
                  font=('futura', 20, 'italic')
                  )
    id_label = Label(window,
                  text='Insert Id:',
                  font=('futura', 20, 'italic')
                   )
    id_entry = Entry(window,
                  font=('futura', 20, 'italic'),
                  width=15
                  )
    name_label = Label(window,
                     text='Insert Name:',
                     font=('futura', 20, 'italic')
                     )
    name_entry = Entry(window,
                     font=('futura', 20, 'italic'),
                     width=15
                     )
    city_label = Label(window,
                     text='Insert City:',
                     font=('futura', 20, 'italic')
                     )
    city_entry = Entry(window,
                     font=('futura', 20, 'italic'),
                     width=15
                     )
    phone_label = Label(window,
                     text='Insert Phone',
                     font=('futura', 20, 'italic')
                     )
    phone_entry = Entry(window,
                     font=('futura', 20, 'italic'),
                     width=15
                     )
    submit_btn = Button(window,
                    text='Submit',
                    font=('futura', 16),
                    width=20,
                    command=lambda:insert_data(id_entry.get(),
                                                name_entry.get(),
                                                city_entry.get(),
                                                phone_entry.get()
                                                )
                    )
    btn = Button(window,
                 text='Back',
                 command=home,
                 width=20
                 )

    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    id_label.grid(row=1, column=0, padx=10, pady=10)
    id_entry.grid(row=1, column=1, padx=10, pady=10)
    name_label.grid(row=2, column=0, padx=10, pady=10)
    name_entry.grid(row=2, column=1, padx=10, pady=10)
    city_label.grid(row=3, column=0, padx=10, pady=10)
    city_entry.grid(row=3, column=1,padx=10, pady=10)
    phone_label.grid(row=4, column=0,padx=10, pady=10)
    phone_entry.grid(row=4, column=1,padx=10, pady=10)
    submit_btn.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    btn.grid(row=6, column=0,padx=10, pady=10, columnspan=2)

def update_data():

    def update_name():
        def update(id, name):
            mycursor = mydb.cursor()
            gry = 'UPDATE info SET name = %s where id=%s'
            val = [name, id]
            try:
                mycursor.execute(gry, val)
                messagebox.showinfo(title='Done', message='Update successful.')
            except:
                messagebox.showerror(title='Error!', message='Error occurred!')
        clear_window()
        title = Label(window,
                      text='Update Name',
                      font=('futura', 20, 'italic')
                      )
        id_label = Label(window,
                         text='Enter the Id:',
                         font=('futura', 20, 'italic')
                         )
        id_entry= Entry(window,
                  font=('futura', 20, 'italic'),
                  width=15
                  )
        name_label = Label(window,
                           text='Enter the Name:',
                           font=('futura', 20, 'italic')
                           )
        name_entry = Entry(window,
                           font=('futura', 20, 'italic'),
                           width=15
                           )
        submit_btn = Button(window,
                    text='Submit',
                    font=('futura', 16),
                    width=20,
                    command=lambda:update(id_entry.get(), name_entry.get())
                    )
        btn = Button(window,
                     text='Back',
                     command=home,
                     width=20
                     )
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        id_label.grid(row=1, column=0, padx=10, pady=10)
        id_entry.grid(row=1, column=1, padx=10, pady=10)
        name_label.grid(row=2, column=0, padx=10, pady=10)
        name_entry.grid(row=2, column=1, padx=10, pady=10)
        submit_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        btn.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def update_city():
        def update(id, city):
            mycursor = mydb.cursor()
            gry = 'UPDATE info SET city = %s where id=%s'
            val = [city, id]
            try:
                mycursor.execute(gry, val)
                messagebox.showinfo(title='Done', message='Update successful.')
            except:
                messagebox.showerror(title='Error!', message='Error occurred!')
        clear_window()
        title = Label(window,
                      text='Update city',
                      font=('futura', 20, 'italic')
                      )
        id_label = Label(window,
                         text='Enter the Id:',
                         font=('futura', 20, 'italic')
                         )
        id_entry= Entry(window,
                  font=('futura', 20, 'italic'),
                  width=15
                  )
        city_label = Label(window,
                           text='Enter City:',
                           font=('futura', 20, 'italic')
                           )
        city_entry = Entry(window,
                           font=('futura', 20, 'italic'),
                           width=15
                           )
        submit_btn = Button(window,
                    text='Submit',
                    font=('futura', 16),
                    width=20,
                    command=lambda:update(id_entry.get(), city_entry.get())
                    )
        btn = Button(window,
                     text='Back',
                     command=home,
                     width=20
                     )
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        id_label.grid(row=1, column=0, padx=10, pady=10)
        id_entry.grid(row=1, column=1, padx=10, pady=10)
        city_label.grid(row=2, column=0, padx=10, pady=10)
        city_entry.grid(row=2, column=1, padx=10, pady=10)
        submit_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        btn.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def update_phone():
        def update(id, phone):
            mycursor = mydb.cursor()
            gry = 'UPDATE info SET phone = %s where id=%s'
            val = [phone, id]
            try:
                mycursor.execute(gry, val)
                messagebox.showinfo(title='Done', message='Update successful.')
            except:
                messagebox.showerror(title='Error!', message='Error occurred!')
        clear_window()
        title = Label(window,
                      text='Update phone',
                      font=('futura', 20, 'italic')
                      )
        id_label = Label(window,
                         text='Enter the Id:',
                         font=('futura', 20, 'italic')
                         )
        id_entry= Entry(window,
                  font=('futura', 20, 'italic'),
                  width=15
                  )
        phone_label = Label(window,
                           text='Enter phone no:',
                           font=('futura', 20, 'italic')
                           )
        phone_entry = Entry(window,
                           font=('futura', 20, 'italic'),
                           width=15
                           )
        submit_btn = Button(window,
                    text='Submit',
                    font=('futura', 16),
                    width=20,
                    command=lambda:update(id_entry.get(), phone_entry.get())
                    )
        btn = Button(window,
                     text='Back',
                     command=home,
                     width=20
                     )
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        id_label.grid(row=1, column=0, padx=10, pady=10)
        id_entry.grid(row=1, column=1, padx=10, pady=10)
        phone_label.grid(row=2, column=0, padx=10, pady=10)
        phone_entry.grid(row=2, column=1, padx=10, pady=10)
        submit_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        btn.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    clear_window()
    label = Label(window,
                  text='Update:',
                  font=('futura', 20, 'italic')
                  )
    by_name = Button(window,
                     text='Name',
                     font=('futura', 16),
                     width=20,
                     command=update_name
                     )
    by_city = Button(window,
                     text='City',
                     font=('futura', 16),
                     width=20,
                      command=update_city
                     )
    by_phone = Button(window,
                     text='Phone',
                     font=('futura', 16),
                     width=20,
                     command=update_phone
                     )
    btn = Button(window,
                 text='Back',
                 command=home,
                 width=20
                 )

    label.grid(row=0, padx=10, pady=10)
    by_name.grid(row=1, padx=10, pady=10)
    by_city.grid(row=2, padx=10, pady=10)
    by_phone.grid(row=3, padx=10, pady=10)
    btn.grid(row=4, padx=10, pady=10)

def delete_data():
    def delete(id):
        if messagebox.askokcancel(title='Warning', message='Confirm Deletion?'):
            mycursor = mydb.cursor()
            gry = 'DELETE FROM info where id=%s'
            val = [id]
            try:
                mycursor.execute(gry, val)
                messagebox.showinfo(title='Done', message='Deletion successful.')
            except:
                messagebox.showerror(title='Error!', message='Error occurred!')

    clear_window()
    title = Label(window,
                  text='Update phone',
                  font=('futura', 20, 'italic')
                  )
    id_label = Label(window,
                     text='Enter the Id:',
                     font=('futura', 20, 'italic')
                     )
    id_entry = Entry(window,
                     font=('futura', 20, 'italic'),
                     width=15
                     )
    submit_btn = Button(window,
                        text='Delete',
                        font=('futura', 16),
                        width=20,
                        command=lambda: delete(id_entry.get())
                        )
    btn = Button(window,
                 text='Back',
                 command=home,
                 width=20
                 )
    title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    id_label.grid(row=1, column=0, padx=10, pady=10)
    id_entry.grid(row=1, column=1, padx=10, pady=10)

    submit_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    btn.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

def home():
    clear_window()
    label = Label(window,
                  text='WELCOME',
                  font=('futura', 20, 'italic')
                  )
    display_btn = Button(window,
                         text='Display',
                         font=('futura', 16),
                         width=20,
                         command=display_data,
                         )
    get_specific_btn = Button(window,
                              text='Get Data',
                              font=('futura', 16),
                              width=20,
                              command=get_specific_data
                              )
    add_btn = Button(window,
                         text='Add Data',
                         font=('futura', 16),
                         width=20,
                         command=add_data
                         )
    update_btn = Button(window,
                        text='Update Data',
                        font=('futura', 16),
                        width=20,
                        command=update_data
                        )
    delete_btn = Button(window,
                        text='Delete Data',
                        font=('futura', 16),
                        width=20,
                        command=delete_data
                        )
    label.grid(row=0,padx=10,pady=10)
    display_btn.grid(row=1,padx=10,pady=10)
    get_specific_btn.grid(row=2,padx=10,pady=10)
    add_btn.grid(row=3, padx=10, pady=10)
    update_btn.grid(row=4,padx=10,pady=10)
    delete_btn.grid(row=5,padx=10,pady=10)


'''GUI'''

window = Tk()
window.title("Database Connectivity")

''' Connecting to my sql database '''
try:
    mydb = connector.connect(
        host='localhost',
        user='root',
        password='',
        database='kc_db'
    )
    home()

except:
    print('server down')
    window.destroy()


window.mainloop()



