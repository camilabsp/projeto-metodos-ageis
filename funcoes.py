from tkinter import *
from datetime import *
from tkinter import messagebox
import sqlite3 

class funcoes:
    def __init__(self,data,codigo,qtd,valor_unit,c_v,taxa_corret=5.00):
        self.data = data    
        self.codigo = codigo
        self.qtd = qtd
        self.valor_unit = valor_unit
        self.c_v = c_v
        self.taxa_corret = taxa_corret

    def limpar_tela(self):
        self.data_entry.delete(0,END)
        self.codigo_entry.delete(0,END)
        self.qtd_entry.delete(0,END)
        self.valor_unit_entry.delete(0,END)

    def conecta_bd(self):
        self.conn = sqlite3.connect('newbd')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def cria_bd(self):
        self.conecta_bd()
        ##criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS newbd(
                data TEXT,
                codigo TEXT,
                qtd TEXT,
                valor_unit TEXT,
                c_v TEXT,
                valor_operacao REAL,
                tx_corret REAL,
                tx_imposto REAL,
                valor_final REAL
                
            );
        """)

        self.conn.commit();print('banco de dados criado')
        self.desconecta_bd

    def adiciona_dados(self):

        
            self.data = str(self.data_entry.get())
            self.codigo = self.codigo_entry.get().upper()
            self.qtd = int(self.qtd_entry.get())
            self.valor_unit = float(self.valor_unit_entry.get())
            self.c_v = self.radio_valor.get()
        
            self.valor_operacao = round((self.qtd * self.valor_unit),2)
            self.tx_corret = 5.00
            self.tx_imposto = round((0.0003 * self.valor_operacao),2)

            if self.c_v == 1:
                self.c_v = 'C'
                self.valor_final = round((self.valor_operacao + self.tx_corret + self.tx_imposto),2)
            elif self.c_v == 2:
                self.c_v = 'V'
                self.valor_final = round((self.valor_operacao - self.tx_corret - self.tx_imposto),2)
                

            self.conecta_bd()

            self.cursor.execute("""INSERT INTO newbd(data,codigo,qtd,valor_unit,c_v,valor_operacao,tx_corret,tx_imposto,valor_final)
            VALUES (?,?,?,?,?,?,?,?,?)""",(self.data,self.codigo,self.qtd,self.valor_unit,self.c_v,self.valor_operacao,self.tx_corret,self.tx_imposto,self.valor_final)) 

            self.conn.commit()
            self.desconecta_bd()
            self.atualiza_tabela()
            self.limpar_tela()

    def atualiza_tabela(self):
        self.tabela_dados.delete(*self.tabela_dados.get_children())
        self.conecta_bd()
        l = self.cursor.execute(""" SELECT data,codigo,qtd,valor_unit,c_v,valor_operacao,tx_corret,tx_imposto,valor_final
            FROM newbd ORDER BY data ASC""")
        for i in l:
            self.tabela_dados.insert("",END,values=i)

        self.desconecta_bd()
    
    def buscar_ativo(self):
        self.conecta_bd()
        self.tabela_dados.delete(*self.tabela_dados.get_children()) 

        self.filtrar_ativo_entry.insert(END,"%")
        filtrar_ativo = self.filtrar_ativo_entry.get()
        self.cursor.execute(
            """SELECT data,codigo,qtd,valor_unit,c_v,valor_operacao,tx_corret,tx_imposto,valor_final FROM newbd WHERE codigo LIKE '%s' ORDER BY data ASC""" % filtrar_ativo)
        buscacodigo = self.cursor.fetchall()
        for i in buscacodigo:
            self.tabela_dados.insert("",END,values=i)
        self.limpar_tela()
        self.desconecta_bd()
