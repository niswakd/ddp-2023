import tkinter
from tkinter import ttk

def submit():
    # user Info
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    title = title_combobox.get()
    age = age_spinbox.get()
    religious = religious_combobox.get()
    jaminan = jaminan_combobox.get()
    cicilan = cicilan_combobox.get()
    notelp = notelp_entry.get()
    norek = norek_entry.get()

    #courses Info
    Bank = reg_status_var.get()
    nominal = nominal_spinbox.get()

    print(".......................................")
    print("Nama Lengkap : ",first_name, last_name)
    print("Status       : ", title)
    print("Umur         : ", age )
    print("Agama        : ",religious)
    print("No Telpon    :", notelp)
    print("=======================================")
    print("Nominal Uang : ", nominal, "Juta")
    print("Nama Bank    : ", Bank)
    print("Cicilan      : ", cicilan)
    print("Jaminan      :", jaminan)
    print("No Rekening  : ", norek)
    print(".......................................")


window = tkinter.Tk()
window.title("Data Pinjol")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="Informasi Peminjam")
user_info_frame.grid(row= 0, column= 0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="Nama Depan")
first_name_label.grid(row=0, column=0)
first_name_label = tkinter.Label(user_info_frame, text="Nama Belakang")
first_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Status")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Menikah", "Belum Menikah"])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text= "Umur")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to='infinity')
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

religious_label = tkinter.Label(user_info_frame, text="Agama")
religious_combobox = ttk.Combobox(user_info_frame, values=["Islam", "Kristen", "Hindu", "Buddha", "Konghucu"])
religious_label.grid(row=2, column=1)
religious_combobox.grid(row=3, column=1)

notelp_label = tkinter.Label(user_info_frame, text="Nomor Telp")
notelp_label.grid(row=2, column=2)
notelp_entry = tkinter.Entry(user_info_frame)
notelp_entry.grid(row=3, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Pilihan Bank")

reg_status_var = tkinter.StringVar(value="no")  
bca_check = tkinter.Checkbutton(courses_frame, text="BCA",
                                    variable = reg_status_var, onvalue= "BCA", offvalue="no")
btn_check = tkinter.Checkbutton(courses_frame, text="BTN",
                                    variable = reg_status_var, onvalue= "BTN", offvalue="no")
bri_check = tkinter.Checkbutton(courses_frame, text="BRI",
                                    variable = reg_status_var, onvalue= "BRI", offvalue="no")

registered_label.grid(row=0, column=0)
bca_check.grid(row=1, column=0)
btn_check.grid(row=2, column=0)
bri_check.grid(row=3, column=0)

nominal_label = tkinter.Label(courses_frame, text="Nominal Pinjaman")
nominal_spinbox = tkinter.Spinbox(courses_frame, from_=0, to= 'infinity')
nominal_label.grid(row=0, column=1)
nominal_spinbox.grid(row=1, column=1, padx=50)

cicilan_label = tkinter.Label(courses_frame, text="Cicilan")
cicilan_combobox = ttk.Combobox(courses_frame, values=["Setiap 1 bulan", "Setiap 3 bulan","Setiap 6 bulan","Setiap 12 bulan"])
cicilan_label.grid(row=2, column=1)
cicilan_combobox.grid(row=3, column=1)

jaminan_label = tkinter.Label(courses_frame, text="Jaminan")
jaminan_combobox = ttk.Combobox(courses_frame, values=["KTP", "Surat Tanah"])
jaminan_label.grid(row=0, column=2)
jaminan_combobox.grid(row=1, column=2)

norek_label = tkinter.Label(courses_frame, text="Nomor Rekening")
norek_label.grid(row=2, column=2)
norek_entry = tkinter.Entry(courses_frame)
norek_entry.grid(row=3, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Ketentuan")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

terms_label = tkinter.Label(terms_frame, text="Peminjaman diatas 10 Juta wajib memberikan jaminan Surat Tanah.")
terms_check = tkinter.Checkbutton(terms_frame, text="Kami paham dan menerima semua kebijakan yang berlaku.")
terms_check.grid(row=1, column=0)
terms_label.grid(row=0, column=0)

#button
button = tkinter.Button(frame, text="Kirim", command= submit)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()