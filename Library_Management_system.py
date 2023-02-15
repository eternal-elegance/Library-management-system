from Helper_Functions_module import *
from tkinter import *
from tkinter import ttk, messagebox
from crud_modules import *
import datetime



class LibraryManagementSystem1:

    w, h, x, y = get_screen_res()
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry(f'{self.w}x{self.h}+{self.x}+{self.y}')
        print(f'The width is {self.w} and height is {self.h} ')

        self.member_var = StringVar(self.root, '')
        self.prn_var = StringVar(self.root, '')
        self.id_var = StringVar(self.root, '')
        self.firstname_var = StringVar(self.root, '')
        self.lastname_var = StringVar(self.root, '')
        self.address1_var = StringVar(self.root, '')
        self.address2_var = StringVar(self.root, '')
        self.postcode_var = StringVar(self.root, '')
        self.mobile_var = StringVar(self.root, '')
        self.bookid_var = StringVar(self.root, '')
        self.booktitle_var = StringVar(self.root, '')
        self.author_var = StringVar(self.root, '')
        self.dateborrowed_var = StringVar(self.root, '')
        self.datedue_var = StringVar(self.root, '')
        self.daysonbook_var = StringVar(self.root, '')
        self.latereturnfine_var = StringVar(self.root, '')
        self.dateoverdue_var = StringVar(self.root, '')
        self.finalprice_var = StringVar(self.root, '')

        self.db = create_database("library.db")
        self.cr = get_cursor(self.db)
        attrs=dict(
        id='txt',
        member='txt',
        prn_no='txt',
        firstname='txt',
        lastname='txt',
        address1='txt',
        address2='txt',
        postcode='txt',
        mobile='txt',
        bookid='txt',
        book_title='txt',
        author='txt',
        issue_date='txt',
        due_date='txt',
        days_passed='txt',
        late_return_fine='txt',
        date_over_due='txt',
        actual_price='txt',
    )
        self.table_name='Member'
        create_table(self.db, self.cr, self.table_name, attrs, pk='id')

        self.ids=[]
        def valid_ids():
            self.ids=[]
            rows=show_func(self.cr, self.table_name)

            if len(rows)>0:
                for i in rows:
                    self.ids.append(str(i[0]))
        valid_ids()
















#   ---------------------------------------------main heading----------------------------------
        heading = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="red", bd=20, relief=RIDGE, font=('times new roman', 50, 'bold'), padx=2, pady=6)
        heading.pack(side=TOP, fill=X)
            










 # ----------------------------------------------main frame--------------------------------
        main_frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
        main_frame.place(x=0, y=self.h//6, width=self.w, height=self.h//2.05)

















# ----------------------------------------left membership info----------------------------
        inner_Frame_left = LabelFrame(main_frame, text='Library membership detais:', bg='powder blue', fg='green', bd=10, relief=RIDGE, font=('times new roman', 10, 'bold'), padx=0, pady=0)
        inner_Frame_left.place(x=0, y=0, width=round(((self.w//3)*1.75)), height=self.h//2.2)

        bgcol = 'powder blue' # to maintain consistency
        hf = Helper_functions(inner_Frame_left, bgcol)

        # adding widgets
            # member type - combobox
        member_type = Label(inner_Frame_left, bg=bgcol, text="Member Type: ", font=('times new roman', 12, 'bold'), padx=2, pady=6)
        member_type.grid(row=0, column=0, sticky=W)
        
        member_combo = ttk.Combobox(inner_Frame_left, font=('Ariel', 12, 'italic'),textvariable=self.member_var , width=20, state='readonly')
        member_combo['value'] = tuple('Admin Staff,Student,Lecturer'.split(','))
        member_combo.grid(row=0, column=1)
        
        # prnno - entry
        prnno_label = hf.create_label(text='PRN NO:', font_family='Ariel')
        prnno_label.grid(row=1, column=0, sticky=W)
        
        prnno_entry = hf.create_entry(textvariable=self.prn_var)
        hf.grid_it(prnno_entry, 1, 1, W)
        
        # title - entry
        id_label = hf.create_label(text='ID:', font_family='Ariel')
        hf.grid_it(id_label, 2, 0, W)
        
        id_entry = hf.create_entry(textvariable=self.id_var)
        hf.grid_it(id_entry, 2, 1, W)
        
        # first name - entry
        first_label = hf.create_label(text='First Name:', font_family='Ariel')
        hf.grid_it(first_label, 3, 0, W)
        
        first_entry = hf.create_entry(textvariable=self.firstname_var)
        hf.grid_it(first_entry, 3, 1, W)
        
        # last name - entry
        last_label = hf.create_label(text='Last Name:', font_family='Ariel')
        hf.grid_it(last_label, 4, 0, W)
        
        last_entry = hf.create_entry(textvariable=self.lastname_var)
        hf.grid_it(last_entry, 4, 1, W)
        
        # address1 - entry
        add1_label = hf.create_label(text='Address1:', font_family='Ariel')
        hf.grid_it(add1_label, 5, 0, W)
        
        add1_entry = hf.create_entry(textvariable=self.address1_var)
        hf.grid_it(add1_entry, 5, 1, W)
        
        # address2 - entry
        add2_label = hf.create_label(text='Address2:', font_family='Ariel')
        hf.grid_it(add2_label, 6, 0, W)
        
        add2_entry = hf.create_entry(textvariable=self.address2_var)
        hf.grid_it(add2_entry, 6, 1, W)
        
        # postcode - entry
        post_label = hf.create_label(text='Postcode:', font_family='Ariel')
        hf.grid_it(post_label, 7, 0, W)
        
        post_entry = hf.create_entry(textvariable=self.postcode_var)
        hf.grid_it(post_entry, 7, 1, W)
        
        # Mobile - entry
        mob_label = hf.create_label(text='Mobile:', font_family='Ariel')
        hf.grid_it(mob_label, 8, 0, W)
        
        mob_entry = hf.create_entry(textvariable=self.mobile_var)
        hf.grid_it(mob_entry, 8, 1, W)
        
        
        #==========================second col========================================
        # bookid - entry
        bookid_label = hf.create_label(text='Book ID:', font_family='Ariel')
        hf.grid_it(bookid_label, 0, 2, W)
        
        bookid_entry = hf.create_entry(textvariable=self.bookid_var)
        hf.grid_it(bookid_entry, 0, 3, W)
        
        
        # book_title - entry
        book_title_label = hf.create_label(text='Book Title:', font_family='Ariel')
        hf.grid_it(book_title_label, 1, 2, W)
        
        book_title_entry = hf.create_entry(textvariable=self.booktitle_var)
        hf.grid_it(book_title_entry, 1, 3, W)
        
        
        # author - entry
        author_label = hf.create_label(text='Author:', font_family='Ariel')
        hf.grid_it(author_label, 2, 2, W)
        
        author_entry = hf.create_entry(textvariable=self.author_var)
        hf.grid_it(author_entry, 2, 3, W)
        
        
        # issue_date - button
        issue_date_label = hf.create_label(text='Issue Date:', font_family='Ariel')
        hf.grid_it(issue_date_label, 3, 2, W)
        
        issue_date_entry = hf.create_entry(textvariable=self.dateborrowed_var)
        hf.grid_it(issue_date_entry, 3, 3, W)

            # due_date - entry
        due_date_label = hf.create_label(text='Due Date:', font_family='Ariel')
        hf.grid_it(due_date_label, 4, 2, W)
        
        due_date_entry = hf.create_entry(textvariable=self.datedue_var)
        hf.grid_it(due_date_entry, 4, 3, W)
        
        # due_button = hf.create_button(cmd=date_picker2, txt='Choose Date')
        # hf.grid_it(due_button, 4, 3, W)
        
        
        # days_passed - entry
        days_passed_label = hf.create_label(text='Days Passed:', font_family='Ariel')
        hf.grid_it(days_passed_label, 5, 2, W)
        
        days_passed_entry = hf.create_entry(textvariable=self.daysonbook_var)
        hf.grid_it(days_passed_entry, 5, 3, W)
        
        
        # late_fine - entry
        late_fine_label = hf.create_label(text='Late Return Fine:', font_family='Ariel')
        hf.grid_it(late_fine_label, 6, 2, W)
        
        late_fine_entry = hf.create_entry(textvariable=self.latereturnfine_var)
        hf.grid_it(late_fine_entry, 6, 3, W)
        
        
        # date_over - entry
        date_over_label = hf.create_label(text='Date Over Due:', font_family='Ariel')
        hf.grid_it(date_over_label, 7, 2, W)
        
        date_over_entry = hf.create_entry(textvariable=self.dateoverdue_var)
        hf.grid_it(date_over_entry, 7, 3, W)
        
        
        
        # actual_price - entry
        actual_price_label = hf.create_label(text='Actual Price:', font_family='Ariel')
        hf.grid_it(actual_price_label, 8, 2, W)
        
        actual_price_entry = hf.create_entry(textvariable=self.finalprice_var)
        hf.grid_it(actual_price_entry, 8, 3, W)

















# ----------------------------------------right book info---------------------------------
        inner_Frame_right = LabelFrame(main_frame, text='Book Database', bg='powder blue', fg='green', bd=10, relief=RIDGE, font=('times new roman', 10, 'bold'), padx=0, pady=0)
        inner_Frame_right.place(x=round(((self.w//3)*1.75)+10), y=0, width=round(((self.w//3)*1.15)), height=self.h//2.2)
        
        self.book_shelf = Text(inner_Frame_right, font=('Ariel', 12, 'bold'), width=32, height=20, padx=0, pady=0, state='normal')
        self.book_shelf.grid(row=0, column=2)
        
        book_shelf_scroll = Scrollbar(inner_Frame_right)
        book_shelf_scroll.grid(row=0, column=1, sticky='ns')
        
        book_list = ['All about Python', 'Abcd of python', 'all in one python', 'This that of python', 'Everything about python', 'Anything about Python',
                        'Python for everybody', 'python for all', 'Python understanding' 
                    ]

        book_details = {
            book_list[0]: {
                "bookid": "121D",
                "booktitle": book_list[0],
                "author": "Mr. X",
                "late_return_fine": "$50",
                "actual_price": "$600"
            },

            book_list[1]: {
                "bookid": "124D",
                "booktitle": book_list[1],
                "author": "Mr. P",
                "late_return_fine": "$90",
                "actual_price": "$900"
            }
        }


        def set_attrs1(book):
            self.bookid_var.set(book['bookid'])
            self.booktitle_var.set(book['booktitle'])
            self.author_var.set(book['author'])

            d1=datetime.datetime.today()
            d2=datetime.timedelta(days=20)
            d3=d1+d2
            d1=str(d1).split()[0]
            d3=str(d3).split()[0]

            self.dateborrowed_var.set(d1),
            self.datedue_var.set(d3),
            self.daysonbook_var.set(20),
            self.latereturnfine_var.set(book['late_return_fine']),
            self.dateoverdue_var.set("No"),
            self.finalprice_var.set(book['actual_price'])

        def selectbook(event=""):
            value=str(book_list_box.get(book_list_box.curselection()))
            if value == book_list[0]:
                book=book_details[value]
                set_attrs1(book)
                

            elif value == book_list[1]:
                book=book_details[value]
                set_attrs1(book)

            else:
                messagebox.showwarning("Warning", "sorry no data available")
                reset()

        
        book_list_box = Listbox(inner_Frame_right, font=('times new roman', 12, 'bold'), width=20, height=19)
        book_list_box.bind("<<ListboxSelect>>", selectbook)
        book_list_box.grid(row=0, column=0, padx=4)
        book_shelf_scroll.config(command=book_list_box.yview)
        
        for item in book_list:
            book_list_box.insert(END, item)















# ------------------------------------------Commands--------------------------------------------------------------------------
        def add_data():
            data=[
            self.id_var.get(),
            self.member_var.get(),
            self.prn_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get()
        ]
            if len(self.id_var.get())>0:
                insert_normal(self.db, self.cr, data, self.table_name)
                fetch_data()
                valid_ids()

        def reset():
            self.id_var.set(''),
            self.member_var.set(''),
            self.prn_var.set(''),
            self.firstname_var.set(''),
            self.lastname_var.set(''),
            self.address1_var.set(''),
            self.address2_var.set(''),
            self.postcode_var.set(''),
            self.mobile_var.set(''),
            self.bookid_var.set(''),
            self.booktitle_var.set(''),
            self.author_var.set(''),
            self.dateborrowed_var.set(''),
            self.datedue_var.set(''),
            self.daysonbook_var.set(''),
            self.latereturnfine_var.set(''),
            self.dateoverdue_var.set(''),
            self.finalprice_var.set('')
            self.book_shelf.delete("1.0", END)


        def fetch_data():
            rows = show_func(self.cr, self.table_name)

            if len(rows)>0:
                self.library_table.delete(*self.library_table.get_children())
                for i in rows:
                    self.library_table.insert("", END, values=i)
            self.db.commit()


        def get_focus(event=""):
            cursor_row=self.library_table.focus()
            contnt=self.library_table.item(cursor_row)
            rows=contnt['values']

            self.id_var.set(rows[0]),
            self.member_var.set(rows[1]),
            self.prn_var.set(rows[2]),
            self.firstname_var.set(rows[3]),
            self.lastname_var.set(rows[4]),
            self.address1_var.set(rows[5]),
            self.address2_var.set(rows[6]),
            self.postcode_var.set(rows[7]),
            self.mobile_var.set(rows[8]),
            self.bookid_var.set(rows[9]),
            self.booktitle_var.set(rows[10]),
            self.author_var.set(rows[11]),
            self.dateborrowed_var.set(rows[12]),
            self.datedue_var.set(rows[13]),
            self.daysonbook_var.set(rows[14]),
            self.latereturnfine_var.set(rows[15]),
            self.dateoverdue_var.set(rows[16]),
            self.finalprice_var.set(rows[17])


        def show():
            valid_ids()
            if self.id_var.get() in self.ids:
                self.book_shelf.delete("1.0", END)
                self.book_shelf.insert(END, f"ID:\t\t {self.id_var.get()}\n")
                self.book_shelf.insert(END, f"MEMBER TYPE:\t\t {self.member_var.get()}\n")
                self.book_shelf.insert(END, f"PRN NO:\t\t {self.prn_var.get()}\n")
                self.book_shelf.insert(END, f"FIRSTNAME:\t\t {self.firstname_var.get()}\n")
                self.book_shelf.insert(END, f"LASTNAME:\t\t {self.lastname_var.get()}\n")
                self.book_shelf.insert(END, f"ADDRESS1:\t\t {self.address1_var.get()}\n")
                self.book_shelf.insert(END, f"ADDRESS2:\t\t {self.address2_var.get()}\n")
                self.book_shelf.insert(END, f"POSTCODE:\t\t {self.postcode_var.get()}\n")
                self.book_shelf.insert(END, f"MOBILE:\t\t {self.mobile_var.get()}\n")
                self.book_shelf.insert(END, f"BOOK ID:\t\t {self.bookid_var.get()}\n")
                self.book_shelf.insert(END, f"BOOK TITLE:\t\t {self.booktitle_var.get()}\n")
                self.book_shelf.insert(END, f"AUTHOR:\t\t {self.author_var.get()}\n")
                self.book_shelf.insert(END, f"BORROWED DATE:\t\t {self.dateborrowed_var.get()}\n")
                self.book_shelf.insert(END, f"DUE DATE:\t\t {self.datedue_var.get()}\n")
                self.book_shelf.insert(END, f"DAYS:\t\t {self.daysonbook_var.get()}\n")
                self.book_shelf.insert(END, f"LATE FINE:\t\t {self.latereturnfine_var.get()}\n")
                self.book_shelf.insert(END, f"DAYS OVER DUE:\t\t {self.dateoverdue_var.get()}\n")
                self.book_shelf.insert(END, f"FINAL PRICE:\t\t {self.finalprice_var.get()}\n")

            else:
                messagebox.showerror("ID error", 'ID does not exists')

        def exit_it():
            ex=messagebox.askyesno("EXIT?", 'Do you really want to exit')
            if ex>0:
                self.root.destroy()
                return


        def update_system():

            valid_ids()
            
            if self.id_var.get() in self.ids:

                prepared= f"UPDATE {self.table_name} SET member='{self.member_var.get()}', prn_no='{self.prn_var.get()}', firstname='{self.firstname_var.get()}', lastname='{self.lastname_var.get()}', address1='{self.address1_var.get()}', address2='{self.address2_var.get()}', postcode='{self.postcode_var.get()}', mobile='{self.mobile_var.get()}' WHERE ID='{self.id_var.get()}' "
                # print(prepared)
                try:
                    self.cr.execute(prepared)
                except Exception as e:
                    print(e)
                finally:
                    self.db.commit()
                fetch_data()
                valid_ids()
            else:
                messagebox.showerror("ID error", 'ID does not exists')


        def delete_system():
            valid_ids()
            if self.id_var.get() in self.ids:
                prepared= f"DELETE FROM {self.table_name} WHERE ID={self.id_var.get()}"
                try:
                    self.cr.execute(prepared)
                except Exception as e:
                    print(e.with_traceback())
                finally:
                    self.db.commit()
                fetch_data()
                valid_ids()
                reset()
            else:
                messagebox.showerror("ID error", 'ID does not exists')
 











# ------------------------------------------Button Holder---------------------------------
        button_holder_frame = Frame(self.root, bd=12, relief=RIDGE, padx=15, bg='powder blue')
        button_holder_frame.place(x=0, y=self.h//1.5, width=self.w, height=self.h//13)

        btn = Helper_functions(button_holder_frame)
        # add button
        add_btn = btn.create_button(cmd=add_data, txt='Add', width=23, bg='powder blue', fg='black')
        btn.grid_it(add_btn, 0, 0)
        
        # show button
        show_btn = btn.create_button(cmd=show, txt='Show', width=23, bg='powder blue', fg='black')
        btn.grid_it(show_btn, 0, 1)
        
        # update button
        update_btn = btn.create_button(cmd=update_system, txt='Update', width=23, bg='powder blue', fg='black')
        btn.grid_it(update_btn, 0, 2)
        
        # delete button
        del_btn = btn.create_button(cmd=delete_system, txt='Delete', width=23, bg='powder blue', fg='black')
        btn.grid_it(del_btn, 0, 3)
        
        # reset button
        reset_btn = btn.create_button(cmd=reset, txt='Reset', width=23, bg='powder blue', fg='black')
        btn.grid_it(reset_btn, 0, 4)
        
        # exit button
        exit_btn = btn.create_button(cmd=exit_it, txt='Exit', width=23, bg='powder blue', fg='black')
        btn.grid_it(exit_btn, 0, 5)



















 # -----------------------------------------Display Frame-----------------------------------
        display_frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
        display_frame.place(x=0, y=self.h//1.35, width=self.w, height=190)
        


        w, h, x, y = get_screen_res()
        self.table_frame = Frame(display_frame, bd=6, relief=RIDGE, bg="powder blue")
        self.table_frame.place(x=0, y=2, width=w // 1.05, height=h // 7)


        xscroll=ttk.Scrollbar(self.table_frame, orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(self.table_frame, orient=VERTICAL)



        self.library_table = ttk.Treeview(self.table_frame, column=(
           "id", "membertype", 'prno', 'firstname', 'lastname', 'address1', 'address2', 'postid', 'mobile', 'bookid',
            'booktitle', 'author', 'dateborrowed', 'datedue', 'days', 'latereturnfine', 'dateoverdue', 'finalprice'
        ), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)


        self.library_table.heading('id', text='ID')
        self.library_table.heading('membertype', text='Member Type')
        self.library_table.heading('prno', text='PRN NO.')
        self.library_table.heading('firstname', text='Firstname')
        self.library_table.heading('lastname', text='Lastname')
        self.library_table.heading('address1', text='Address1')
        self.library_table.heading('address2', text='Address2')
        self.library_table.heading('postid', text='Post Id')
        self.library_table.heading('mobile', text='Mobile')
        self.library_table.heading('bookid', text='Book Id')
        self.library_table.heading('booktitle', text='Book Title')
        self.library_table.heading('author', text='Author')
        self.library_table.heading('dateborrowed', text='Date Borrowed')
        self.library_table.heading('datedue', text='Date Due')
        self.library_table.heading('days', text='Days on Book')
        self.library_table.heading('latereturnfine', text='Late Return Fine')
        self.library_table.heading('dateoverdue', text='Date over due')
        self.library_table.heading('finalprice', text='Final price')

        self.library_table['show']='headings'
        self.library_table.pack(fill=BOTH, expand=1)

        def set_column_width(obj, lst):
            for i in lst:
                obj.column(i, width=135)

        # setting width of all
        lst = ['id', "membertype", 'prno', 'firstname', 'lastname', 'address1', 'address2', 'postid', 'mobile', 'bookid',
            'booktitle', 'author', 'dateborrowed', 'datedue', 'days', 'latereturnfine', 'dateoverdue', 'finalprice']
        set_column_width(self.library_table, lst)

        self.library_table.bind("<ButtonRelease-1>", get_focus)
        fetch_data()


















if __name__ == '__main__':
    root = Tk()
    library = LibraryManagementSystem1(root)
    root.mainloop()