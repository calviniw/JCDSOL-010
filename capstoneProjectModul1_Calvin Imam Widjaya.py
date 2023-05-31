from tabulate import tabulate as tbl
import os

# Membersihkan tampilan pada saat running
os.system('cls')

# Isi informasi karyawan disimpan menggunakan data collection Dictionary di dalam List agar mudah dimodifikasi
employee =[
     {"NIK":"SM01","Nama":"Agung Hermawan","Gender":"Pria","Umur":28,"Jabatan":"Direktur Utama"},
     {"NIK":"FA02","Nama":"Lia Sirait","Gender":"Wanita","Umur":24,"Jabatan":"Finance Manager"},
     {"NIK":"HR02","Nama":"Pratama Arhan","Gender":"Pria","Umur":29,"Jabatan":"HRGA Manager"}]

# Menampilkan data secara menarik menggunakan library tabulate
def showData():
    print(tbl(employee, headers="keys", tablefmt="fancy_grid"))

# Menampilkan Menu Utama menggunakan f-string dengan format rata tengah
def main_menu():
    print(f"{'Selamat Datang di':^60}")
    print(f"{'Employee Database System PT CFR':^60}")
    print("-"*60)
    print(f"{'Silakan Pilih Menu yang Ingin Diakses':^60}")
    print("-"*60)
    print('1. Melihat Informasi Data Karyawan')
    print('2. Menambahkan Informasi untuk Karyawan Baru')
    print('3. Melakukan Perubahan Informasi Karyawan')
    print('4. Menghapus Informasi Karyawan')
    print('5. Keluar')

# Submenu Read/Melihat Informasi Karyawan dengan menggunakan regular function, conditional statement, dan looping
def submenu_1():
    while True:
        print("-"*60)
        print(f"{'Menu Informasi Data Karyawan':^60}")
        print("-"*60)
        print('1. Melihat Seluruh Informasi Data Karyawan')
        print('2. Mencari Informasi Data Karyawan Berdasarkan Filter Tertentu')
        print('3. Kembali ke Menu Utama')
        print('\n')
        input_submenu_1 = input('Silakan pilih dan ketik angka menu yang diinginkan [1-3]: ')
        print("-"*60)
        if input_submenu_1 == "1":
            
            # Jika data karyawan tidak ada/kosong
            if employee== []:
                print("Maaf, Data Belum Tersedia. Silakan coba lagi")
                break
            else:
                showData()
        elif input_submenu_1 == "2":
            dataSpecific=input("Silakan masukkan NIK: ")
            for a in range(len(employee)):
                if dataSpecific in employee[a]["NIK"]:
                    # Fungsi \t seperti Tab di keyboard untuk merapikan
                    # Fungsi \n untuk membuat baris baru
                    print('''NIK\t\t|Nama\t\t|Gender\t\t|Umur\t\t|Jabatan\n''')
                    print("{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}\n".format(employee[a]["NIK"],employee[a]["Nama"],employee[a]["Gender"],employee[a]["Umur"],employee[a]["Jabatan"]))            
                    break
                elif a==max(range(len(employee))):
                    print("-"*60)
                    print(f"{'Maaf, NIK Tidak Terdaftar. Silakan Masukkan NIK yang terdaftar':^60}")
                    print("-"*60)
                    break
                else:
                    continue
        elif input_submenu_1 =="3":
            break
        else:
            continue

# Submenu Create/Menambah Informasi Karyawan menggunakan regular function, conditional statement, dan looping 
def submenu_2():
    while True:
        print('-'*60)
        print(f"{'Menu Informasi Karyawan Baru':^60}")
        print('-'*60)
        print("1. Menambahkan Informasi Karyawan Baru")
        print("2. Kembali ke Menu Utama")
        
        input_submenu_2=input("Silakan pilih dan ketik angka menu yang diinginkan [1-2]: ")
        if input_submenu_2=="1":
            nik=input("Masukkan NIK yang ingin diperbaharui: ")
            for a in range(len(employee)):
                if employee[a]["NIK"]==nik:
                    print("Maaf, Data Sudah Tersedia")
                    break
                elif a==max(range(len(employee))):
                    nama=input("Masukkan Nama Lengkap Karyawan: ")
                    gender=input("Masukkan Jenis Kelamin Karyawan [Pria/Wanita]: ")
                    umur=input("Masukkan Umur Karyawan: ")
                    jabatan=input("Masukkan Jabatan Karyawan: ")
                    while True:
                        askInput=input("Apakah sudah yakin informasi ini akan disimpan? (Y/N) : ")
                        if askInput=="Y" or askInput== "y":
                            employee.append({"NIK":nik,"Nama":nama,"Gender":gender,"Umur":umur,"Jabatan":jabatan})
                            print('-'*60)
                            print(f"{'Terima kasih! Informasi telah diperbaharui':^60}")
                            break
                        elif askInput=="N" or askInput== "n":
                            print('-'*60)
                            print(f"{'Okay. Data batal diperbaharui ya':^60}")
                            break
                        else:
                            continue
                else:
                    continue
                              
        elif input_submenu_2=="2":
            break
        else:
            continue

# Submenu Update/Merubah Informasi Karyawan menggunakan regular function, conditional statement, dan looping
def submenu_3():
    while True:
        print(f"{'Menu Perubahan Informasi Karyawan':^60}")
        print('-'*60)
        print('1. Merubah Informasi Karyawan')
        print('2. Kembali ke Menu Utama')
        input_menu_3 = (input('Silakan pilih dan ketik angka menu yang diinginkan [1-2]: '))
        if input_menu_3=="1":
            showData()
            nik=input("Silakan masukkan NIK yang ingin dilakukan perubahan: ")
            for a in range(len(employee)):
                if nik==employee[a]["NIK"]:
                    print('''NIK\t\t|Nama\t\t|Gender\t\t|Umur\t\t|Jabatan\n''')
                    print("{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}\n".format(employee[a]["NIK"],employee[a]["Nama"],employee[a]["Gender"],employee[a]["Umur"],employee[a]["Jabatan"]))    
                    while True:
                        askUpdate=input("Tekan 'Y' jika ingin melanjuti proses perubahan atau 'N' apabila tidak (Y/N) : ")
                        if askUpdate=="y" or askUpdate=="Y":
                            askUpdate2=input("Silakan ketik berdasarkan [Nama Kolom] yang ingin diubah: ")
                            if askUpdate2=="nama"or askUpdate2=="Nama":
                                nama=input("Silakan masukkan nama baru: ")
                                while True:
                                    askUpdate3=input("Apakah sudah yakin? (Y/N) : ")
                                    if askUpdate3=="y"or askUpdate3=="Y":
                                        employee[a]["Nama"]=nama
                                        print("Berhasil! Data telah tersimpan")
                                        break
                                    elif askUpdate3=="n"or askUpdate3=="N":
                                        print("Okay. Data batal disimpan ya")
                                        break
                                    else:
                                        continue
                            elif askUpdate2=="NIK"or askUpdate2=="NIK":
                                gender=input("Silakan masukkan NIK baru: ")
                                while True:
                                    askUpdate3=input("Apakah sudah yakin? (Y/N) : ")
                                    if askUpdate3=="y"or askUpdate3=="Y":                                
                                        employee[a]["NIK"]=gender
                                        print("Berhasil! Data telah tersimpan")
                                        break
                                    elif askUpdate3=="n"or askUpdate3=="N":
                                        print("Okay. Data batal disimpan ya")
                                        break
                                    else:
                                        continue
                            elif askUpdate2=="gender"or askUpdate2=="Gender":
                                gender=input("Silakan masukkan gender baru: ")
                                while True:
                                    askUpdate3=input("Apakah sudah yakin? (Y/N) : ")
                                    if askUpdate3=="y"or askUpdate3=="Y":                                
                                        employee[a]["Gender"]=gender
                                        print("Berhasil! Data telah tersimpan")
                                        break
                                    elif askUpdate3=="n"or askUpdate3=="N":
                                        print("Okay. Data batal disimpan ya")
                                        break
                                    else:
                                        continue
                            elif askUpdate2=="umur"or askUpdate2=="Umur":
                                umur=int(input("Silakan masukkan umur baru: "))
                                while True:
                                    askUpdate3=input("Apakah sudah yakin? (Y/N) : ")
                                    if askUpdate3=="y"or askUpdate3=="Y":                                
                                        employee[a]["Umur"]=umur
                                        print("Berhasil! Data telah tersimpan")
                                        break
                                    elif askUpdate3=="n"or askUpdate3=="N":
                                        print("Okay. Data batal disimpan ya")
                                        break
                                    else:
                                        continue
                            elif askUpdate2=="Jabatan"or askUpdate2=="jabatan":
                                jabatan=input("Silakan masukkan jabatan baru: ")
                                while True:
                                    askUpdate3=input("Apakah sudah yakin? (Y/N) : ")
                                    if askUpdate3=="y"or askUpdate3=="Y":                                
                                        employee[a]["Jabatan"]=jabatan
                                        print("Berhasil! Data telah tersimpan")
                                        break
                                    elif askUpdate3=="n"or askUpdate3=="N":
                                        print("Okay. Data batal disimpan ya")
                                        break
                                    else:
                                        continue
                            else:
                                print('-'*60)
                                print("Maaf, nama kolomnya keliru. Dicoba lagi ya. \nPerhatikan nama kolomnya [misal: Nama]")
                                print('-'*60)
                                break
                        elif askUpdate=="n"or askUpdate=="N":
                            break
                        else:
                            continue
                elif a==max(range(len(employee))):
                    print('-'*60)
                    print("Oops! Pastikan NIK nya terdaftar ya. \nNIK menggunakan kombinasi huruf kapital dan angka")
                    print('-'*60)
                    break
                else:
                    continue
        elif input_menu_3=="2":
            break
        else:
            continue

# Submenu Delete/Menghapus informasi karyawan menggunakan regular function, conditional statement, dan looping
def submenu_4():
    while True:
        print(f"{'Menu Hapus Informasi Karyawan':^60}")
        print('-'*60)
        print('1. Menghapus Informasi Karyawan')
        print('2. Kembali ke Menu Utama')
        input_menu_4 = (input('Silakan pilih dan ketik angka menu yang diinginkan [1-2]: '))
        if input_menu_4 == "1":
            showData()
            keyDel=input("Silakan masukkan NIK yang ingin dihapus: ")
            for x in range(len(employee)):
                if keyDel==employee[x]["NIK"]:
                    while True:
                        askDelete=input("Yakin ingin menghapus informasi karyawan ini? \nJika Sudah yakin, Silakan ketik 'Y' untuk menghapusnya, \ndan ketik 'N' Jika masih ragu: '")
                        if askDelete=="y"or askDelete=="Y":
                            for x in range(len(employee)):
                                if keyDel==employee[x]["NIK"]:
                                    employee.pop(x)
                                    print('*'*60)
                                    print(f"{'Selamat! Data Berhasil dihapus':^60}")
                                    print('*'*60)
                                    break
                                else:
                                    continue
                            break
                        elif askDelete=="n"or askDelete=="N":
                            print("Okay. Data Belum Dihapus ya")
                            print('-'*60)
                            break
                        else:
                            continue
                elif x == max(range(len(employee))):
                    print('-'*60)
                    print("Oops! Pastikan NIK nya terdaftar ya. \nNIK menggunakan kombinasi huruf kapital beserta angka")
                    print('-'*60)
                    break
                else:
                    continue
        elif input_menu_4=="2":
            break
        else:
            continue

# Menentukan langkah selanjutnya pada Menu Utama menggunakan conditional statement
while True:
    main_menu() 
    opsi=input("Silahkan Pilih dan Ketik Menu Berupa Angka [1-5] : ")
    if opsi=="1":
        submenu_1()
    elif opsi=="2":
        submenu_2()
    elif opsi=="3":
        submenu_3()
    elif opsi=="4":
        submenu_4()
    elif opsi=="5":
        print("Terima kasih! Have a wonderful day!")
        break   
    else:
        print('-'*60)
        print("Oops! Pastikan masukkan Angka antara 1 hingga 5 saja ya")
        print('-'*60)