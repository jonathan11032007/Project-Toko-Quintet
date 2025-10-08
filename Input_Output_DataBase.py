from sqlalchemy.engine import create_engine
import pandas as pd

class InputOutputDatabase:
    """
    Class Untuk Mengambil, Mengecek, Merubah Tabel Di DataBase 
    'table_produk_quintet'
    """
    def __init__(self) -> None:
        """
        Engine Dan DataBase Dalam Bentuk Tabel DataFrame
        """
        self.engine = create_engine(
            "mysql+pymysql://root:gemma@localhost:3306/database_toko_quintet"
            )
        self.df = pd.read_sql(
            "SELECT * FROM tabel_produk", 
            con=self.engine
            )
    
    def input_database(self, df: pd.DataFrame):
        """
        Mengubah DataBase 'tabel_produk_quintet' 
        Dengan DataFrame Terbaru
        (Mengubah Tabel)

        Args:
            df (pd.DataFrame): DataFrame Terbary
        """
        self.df = df
        self.df.to_sql(
            "tabel_produk", con=self.engine, if_exists="replace"
            )
    
    def cek_database(self) -> None:
        """
        Mengecek DataBase Dalam Bentuk DataFrame
        (Mengecek Tabel)
        """
        print(self.df)
    
    def output_database(self) -> pd.DataFrame:
        """
        Return DataFrame Dari DataBase 'tabel_produk_quintet'
        (Mengambil Tabel)
        Returns:
            pd.DataFrame: Data Dari DataBase
        """
        return self.df

def pembuatan_tabel_produk_baru():
    """
    Membuat Tabel Produk Baru (Mereset Tabel)
    """
    engine = create_engine(
        "mysql+pymysql://root:gemma@localhost:3306/database_toko_quintet"
        )
    data = {
        "nama":["kimbab", "donat"], "harga":[15_000, 15_000], "stock":[1500, 1500]
        }
    df = pd.DataFrame(data)
    df.to_sql(
        "tabel_produk", con=engine, if_exists="replace"
        )

def main():
    pembuatan_tabel_produk_baru()
    
    # data = {
    #     "nama":["kimbab", "donut"], "harga":[15_000, 15_000], "stock":[50, 50]
    #     }
    # df = pd.DataFrame(data)
    # test = InputOutputDatabase()
    # test.cek_database()
    # test.input_database(df)
    # test.cek_database()
    # print(test.output_database())
    pass

if __name__ == "__main__":
    main()