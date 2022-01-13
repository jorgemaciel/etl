from pydoc import cli
from traceback import print_tb
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('firebird+fdb://SYSDBA:masterkey@localhost:3050//home/jorge/Downloads/ALUGUEL.GDB?charset=latin1')

clientes = pd.read_sql(sql="SELECT * FROM CLIENTE", con=engine)

