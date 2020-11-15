import os
import database.database as dbase
import account
import oop.save_and_restore as init

grade_list = ["TK", "SD", "SMP", "SMA", "Mahasiswa", "Lainnya"]

def header():
    print("=========================================")
    print("===        TUGAS INDIVIDU PBO         ===")
    print("===   MENYIMPAN STATUS SUATU OBJECT   ===")
    print("=========================================")
    print("Author : Andre Suryana")
    print("NIM    : 1908561103")
    print("=========================================\n")

def create_new_database_if_not_exists():
    db = dbase.Database("tugas_individu_akun_sekuy")
    db.set_host("localhost")
    db.set_username("root")
    db.set_password("")
    db.create_database()
    db.set_table_name("akun_pelajar")
    db.create_table()

def save_new_object():
    os.system("cls")
    print("       Add New Account to Database")
    print("=========================================\n")
    print("Username         :")
    username = input()
    print("Password         :")
    passwd = input()
    print("Nama             :")
    nama = input()
    print("Email            :")
    email = input()
    print("Phone            :")
    phone_num = input()
    print("Tanggal Lahir    :(yyyy-mm-dd)")
    tgl_lahir = input()
    print("Alamat           :")
    address = input()
    print("Grade            :")
    print("Pilih salah satu :")
    print("[1] TK")
    print("[2] SD")
    print("[3] SMP")
    print("[4] SMA")
    print("[5] Mahasiswa")
    print("[6] Lainnya")
    grade_index = int(input(">>> "))

    grade = grade_list[grade_index - 1]

    # Creating new Account :
    new_account = account.Account(username, passwd, nama, email, phone_num, tgl_lahir, address, grade)

    # Save Object Status to Database :
    s = init.Action()
    s.save(new_account.username, new_account.passwd, new_account.nama, new_account.email, new_account.phone_num, new_account.tgl_lahir, new_account.address, new_account.grade)
    
def restore_object():
    os.system("cls")
    print("     Restore Account from Database")
    print("=========================================\n")
    print("Search by Username:")
    username = input()

    # Getting Object Data from Database :
    r = init.Action()
    restored_data = r.restore(username)

    data = []

    for item in restored_data:
        for x in item:
            data.append(x)
    
    # Check Data is Empty :
    if not data:
        print("Error! Data tidak dapat ditemukan!")
        return

    # Creating New Object with Restored Data :
    restored_account = account.Account(data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])

    # Result :
    os.system("cls")
    print("\n              Restore Result")
    print("=========================================\n")
    restored_account.show_profile()

def main():
    # Check or Create Database :
    create_new_database_if_not_exists()

    while True:
        os.system("cls")
        header()
        print("Menu:")
        print("\t[1] Save New Object")
        print("\t[2] Restore Object")
        print("\t[3] Exit")
        menu = input(">>> ")
        
        if menu == '1':
            save_new_object()
        elif menu == '2':
            restore_object()
        elif menu == '3':
            print("Exit")
            break
        else:
            print("Input salah!")
        
        os.system("pause")

if __name__ == "__main__":
    main()