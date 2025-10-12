from Input_Output_DataBase import InputOutputDatabase
import pandas as pd

class SistemDataBase():
    """
    Merubah Nama, Harga, Stock Produk Pada Tabel Dan Disimpan Ke DataBase
    """
    def __init__(self):
        self.database_sql = InputOutputDatabase()
        self.df = self.database_sql.output_database().set_index('nama', drop=False)
    
    def stock(self, nama: str, stock:int):
        """
        Merubah Stock Produk Pada DataBase
        
        Args:
            nama (str): Nama Produk
            stock (int): Jumlah Stock Terbaru
        """
        self.df.at[nama, 'stock'] = stock
    
    def harga(self, nama: str, harga:int):
        """
        Merubah Harga Produk Pada DataBase
        
        Args:
            nama (str): Nama Produk
            harga (int): Harga Produk Terbaru
        """
        self.df.at[nama, 'harga'] = harga
    
    def nama(self, nama_lama: str, nama_baru:str):
        """
        Mengubah Nama Produk
        
        Args:
            nama_lama (str): Nama Lama Produk
            nama_baru (str): Nama Baru Produk
        """
        self.df['nama'] = [nama_baru if i == nama_lama else i for i in self.df['nama']]
    
    def save_data(self):
        """
        Menyimpan Data Yang Diubah Ke DataBase
        """
        self.database_sql.input_database(self.df.set_index('index'))
    
    def return_data(self) -> pd.DataFrame:
        """Mengambil DataFrame Dari DataBase

        Returns:
            pd.DataFrame: Data Yang Dihasilkan Dari DataBase
        """
        return self.df

def main():
    # test = SistemDataBase()
    # print(test.df)
    # test.harga('kimbab', 15_000)
    # test.stock('kimbab', 50)
    # test.nama("kimbab", "bakmi")
    # test.nama('donut', 'donat')
    # test.save_data()
    # print(test.df)
    pass

if __name__ == "__main__":
    main()