from Sistem_Toko_Database import SistemDataBase
import pandas as pd


def total_bayar(data: list[tuple[str, int]], df: pd.DataFrame) -> int:
    """
    Menghitung Total Yang Harus Dibayar

    Args:
        data (list[tuple[str, int]]): Data Dari Hasil Input User Produk
        df (pd.DataFrame): DataFrame Dari DataBase

    Returns:
        int: Total Harga
    """
    total = 0
    
    for x, y in data:
        total += df.at[x, 'harga'] * y
    
    return total

def save_data(data: list[tuple[str, int]], database: SistemDataBase, df:pd.DataFrame) -> None:
    """
    Menyimpan Data Hasil Input User Ke DataBase

    Args:
        data (list[tuple[str, int]]): Data Dari Hasil Input User Produk
        database (SistemDataBase): Class SistemDatabase Dari File 'Sistem_Toko_DataBase'
        df (pd.DataFrame): DataFrame Dari DataBase
    """
    
    for x, y in data:
        database.stock(x, (df.at[x, 'stock'] - y))
        database.save_data()

def visual_awal():
    """
    Tampilan Awal Untuk User
    """
    print("\n"+"*"*50)
    print("\n"+"Toko Quintet".center(50)+"\n")
    print("*"*50+"\n")

def visual_akhir(data:list[tuple[str, int]], database: SistemDataBase, df: pd.DataFrame, uang: int):
    """
    Tampilan Akhir Untuk User

    Args:
        data (list[tuple[str, int]]): Data Dari Hasil Input User Produk
        database (SistemDataBase): Class SistemDatabase Dari File 'Sistem_Toko_DataBase'
        df (pd.DataFrame): DataFrame Dari DataBase
        uang (int): Data Dari Hasil Input User Uang
    """
    if uang - total_bayar(data, df) >= 0:
        print("-"*50)
        print("Struk Belanja".center(50))
        print("-"*50)
        
        for x, y in data:
            print(f"{x} {y}   {df.at[x, 'harga'] * y}".rjust(50))
        print("------------------".rjust(50))
        
        print(f'TUNAI   Rp.{uang:_}'.rjust(50))
        print(f'TOTAL HARGA   Rp.{total_bayar(data, df):_}'.rjust(50))
        print(f'KEMBALIAN   Rp.{uang - total_bayar(data, df):_}'.rjust(50))
        
        save_data(data, database, df)
    else:
        print("="*50)
        print(f'TUNAI   Rp.{uang:_}'.center(50))
        print(f'TOTAL HARGA   Rp.{total_bayar(data, df):_}'.center(50))
        print("--- Uang Anda Tidak Cukup ---".center(50))
        print("="*50)

def input_user_produk() -> tuple[str, int]:
    """
    Input User Untuk Produk

    Returns:
        tuple[str, int]: Data Yang Dihasilkan Dari User
    """
    try:
        nama_produk = input("Masukkan Nama Produk: ").lower().strip()
        jumlah = int(input("Masukkan Jumlah Yang Dibeli: ").strip())
        return nama_produk, jumlah
    except ValueError:
        print("\n--- Tolong Masukkan Jumlah Dengan Angka Bulat ---")
        print("Contoh: 1, 2, 3, 4, ...\n")
        quit()

def input_user_uang() -> int:
    """
    Input User Untuk Uang

    Returns:
        int: Data Yang Dihasilkan Dari User
    """
    try:
        uang = int(input("Masukkan Uang Anda Rp.").strip())
        return uang
    except ValueError:
        print("\n--- Tolong Masukkan Uang Dengan Angka Bulat ---")
        print("Contoh: 10000, 20000, 30000, 40000, ...\n")
        quit()

def input_user_lanjut() -> bool:
    """
    Input User Untuk Lanjut Atau Tidak

    Returns:
        bool: Data Yang Dihasilkan Dari User
    """
    return True if input("Lanjut (y/n): ").lower().strip() == 'n' else False

def sistem_utama():
    """
    Sistem Utama Dari Projek Kasir Toko Quintet
    """
    database = SistemDataBase()
    df = database.return_data()
    
    visual_awal()
    
    uang = input_user_uang()
    data = []
    
    print("\n")
    
    while True:
        nama, jumlah = input_user_produk()
        
        if nama in df["nama"] and jumlah > 0:
            data.append((nama, jumlah))
        else:
            print("\n"+"--- Produk Tidak Ditemukan ---".center(50))
        
        print("\n")
        
        if input_user_lanjut():
            print("\n")
            break
        
    
    visual_akhir(data, database, df, uang)

def main(): 
    sistem_utama()

if __name__ == "__main__":
    main()