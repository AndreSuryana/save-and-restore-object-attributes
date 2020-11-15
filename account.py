from oop.save_and_restore import Action

class Account:

    def __init__(self, username, passwd, nama, email, phone_num, tgl_lahir, address, grade):
        self.username = username
        self.passwd = passwd
        self.nama = nama
        self.email = email
        self.phone_num = phone_num
        self.tgl_lahir = tgl_lahir
        self.address = address
        self.grade = grade

    def show_profile(self):
        print("Username         :")
        print(self.username)
        print("Password         :")
        print(self.passwd)
        print("Nama             :")
        print(self.nama)
        print("Email            :")
        print(self.email)
        print("Phone            :")
        print(self.phone_num)
        print("Tanggal Lahir    :")
        print(self.tgl_lahir)
        print("Alamat           :")
        print(self.tgl_lahir)
        print("Grade            :")
        print(self.grade)