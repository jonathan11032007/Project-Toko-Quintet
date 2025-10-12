from Sistem_Toko_Database import SistemDataBase

def visual_awal_admin():
    """
    Tampilan Awal Dari Sistem Administrator
    """
    print("\n")
    print("*"*50)
    print("Administrator DataBase Kasir Toko Quintet".center(50))
    print("*"*50)
    print("\n")

def input_pilihan_admin() -> int:
    """
    Meminta Data Pilihan Dari Administrator

    Returns:
        int: Data Pilihan
    """
    try:
        pilihan = int(input("Masukkan pilihan Anda: "))
        return pilihan
    except ValueError:
        print("\n--- Tolong Masukkan Angka Saja ---")
        print("Contoh: 1, 2, 3\n")
        quit()

def input_lanjut() -> bool:
    """
    Meminta Data Lanjut Dari Administrator

    Returns:
        bool: Data Lanjut
    """
    return True if input("Lanjut? (y/n) ") == 'n' else False

def login_admin() -> bool:
    """
    Meminta Username Dan Password Beserta Memeriksanya 
    Untuk Memastikan Yang Menjalani Sistem Ini Hanya Administrator

    Returns:
        bool: Hasil Dari Pemeriksaan
    """
    data_admin = ['laper', 'quintet aja']
    username = input("Masukkan username anda: ").strip()
    password = input("Masukkan password: ").strip()
    return True if username == data_admin[0] and password == data_admin[1] else False

def visual_database_admin(database: SistemDataBase):
    """
    Tampilan DataBase Dalan Bentuk Pandas

    Args:
        database (SistemDataBase): DataBase Sistem Toko Quintet
    """
    print("\n")
    print("======== ======== ======== DataBase ========")
    print(database.return_data().to_string().center(50))
    print("======== ======== ======== ======== ========")
    print("\n")

def visual_pilihan_admin():
    """
    Tampilan Pilihan Untuk Administrator
    """
    print("""
        Pilih Salah Satu:
        
        (1) Mengubah Data 'Stock' Produk
        (2) Mengubah Data 'Harga' Produk
        (3) Mengubah Data 'Nama' Produk
        
        """)

def proses_pilihan_admin(database: SistemDataBase, pilihan: int):
    """
    Proses Lanjutan Dari Pilihan Yang Diberikan Oleh Administrator

    Args:
        database (SistemDataBase): _description_
        pilihan (int): _description_
    """
    nama_produk = database.return_data()["nama"]
    nama = input("Masukkan Nama Produk Yang Ingin Diubah: ")
    
    if nama in nama_produk:
        try:
            match pilihan:
                case 1:
                    stock = int(input("Masukkan Stock Produk Terbaru: "))
                    database.stock(nama, stock)
                case 2:
                    harga = int(input("Masukkan Harga Produk Terbaru: "))
                    database.harga(nama, harga)
                case 3:
                    nama_baru = input("Masukkan Nama Produk Terbaru: ")
                    database.nama(nama, nama_baru)
                case _:
                    print("\n--- Tolong Pilih 1, 2, 3 ---\n")
                    quit()
        except ValueError:
            print("\n--- Tolong Masukkan Dengan Benar! ---\n")
            quit()
    else:
        print("\n--- Nama Produk Tidak Ditemukan ---\n")
        quit()
    
    database.save_data()

def sistem_administrator():
    """
    Sistem Utama Administrator
    """
    database = SistemDataBase()
    visual_database_admin(database)
    visual_pilihan_admin()
    pilihan = input_pilihan_admin()
    proses_pilihan_admin(database, pilihan)
    visual_database_admin(database)

def main():
    if login_admin():
        while True:
            visual_awal_admin()
            sistem_administrator()
            
            if input_lanjut():
                print("="*50)
                print("Sistem Dimatikan".center(50))
                print("="*50)
                break
    else:
        print("\n--- Username Dan Password Anda Salah---\n")

if __name__ == "__main__":
    main()