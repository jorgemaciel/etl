from pydoc import cli
from traceback import print_tb
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('firebird+fdb://SYSDBA:masterkey@localhost:3050//home/jorge/Downloads/ALUGUEL.GDB?charset=latin1')

ajuste = pd.read_sql(sql="SELECT * FROM AJUSTE", con=engine)
cliente = pd.read_sql(sql="SELECT * FROM CLIENTE", con=engine)
departamento = pd.read_sql(sql="SELECT * FROM DEPARTAMENTO", con=engine)
devolucao = pd.read_sql(sql="SELECT * FROM DEVOLUCAO", con=engine)
equipamento = pd.read_sql(sql="SELECT * FROM EQUIPAMENTO", con=engine)
equipamento2 = pd.read_sql(sql="SELECT * FROM EQUIPAMENTO2", con=engine)
mensagem = pd.read_sql(sql="SELECT * FROM MENSAGEM", con=engine)
movimento = pd.read_sql(sql="SELECT * FROM MOVIMENTO", con=engine)
orgao = pd.read_sql(sql="SELECT * ORGAO_CENTRALIZADOR", con=engine)
situacao = pd.read_sql(sql="SELECT * FROM SITUACAO", con=engine)
tipo = pd.read_sql(sql="SELECT * FROM TIPO", con=engine)


