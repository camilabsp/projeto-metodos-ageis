from tkinter import *
from datetime import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 

class funcoes:
    def __init__(self,data,ativo,qtd,valor_unit,c_v,taxa_corret=5.00):
        self.data = data    
        self.ativo = ativo
        self.qtd = qtd
        self.valor_unit = valor_unit
        self.c_v = c_v
        self.taxa_corret = taxa_corret

    def limpar_tela(self):
        self.data_entry.delete(0,END)
        self.ativo_entry.delete(0,END)
        self.qtd_entry.delete(0,END)
        self.valor_unit_entry.delete(0,END)

    def conecta_bd(self):
        self.conn = sqlite3.connect('bd.bd')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def cria_bd(self):
        self.conecta_bd()
        ##criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bd(
                data TEXT,
                ativo TEXT,
                qtd TEXT,
                valor_unit TEXT,
                c_v TEXT,
                valor_operacao REAL,
                tx_corret REAL,
                tx_b3 REAL,
                valor_total REAL,
                preco_medio REAL,
                lucro_prejuizo REAL
               
            );
        """)

        self.conn.commit();print('banco de dados criado')
        self.desconecta_bd

    def adiciona_dados(self):

        #try:
            self.data = str(self.data_entry.get())
            self.ativo = self.ativo_entry.get().upper()
            self.qtd = int(self.qtd_entry.get())
            self.valor_unit = float(self.valor_unit_entry.get())
            self.c_v = self.radio_valor.get()
        
            self.valor_operacao = round((self.qtd * self.valor_unit),2)
            self.tx_corret = 5.00
            self.tx_b3 = round((0.0003 * self.valor_operacao),2)

            if self.c_v == 1:
                self.c_v = 'C'
                self.valor_total = round((self.valor_operacao + self.tx_corret + self.tx_b3),2)
            elif self.c_v == 2:
                self.c_v = 'V'
                self.valor_total = round((self.valor_operacao - self.tx_corret - self.tx_b3),2)
                

            self.calculo_preco_medio()

            self.calculo_lucro_prejuizo()

            self.lp_carteira()

            self.conecta_bd()

            self.cursor.execute("""INSERT INTO bd(data,ativo,qtd,valor_unit,c_v,valor_operacao,tx_corret,tx_b3,valor_total,preco_medio,lucro_prejuizo)
            VALUES (?,?,?,?,?,?,?,?,?,?,?)""",(self.data,self.ativo,self.qtd,self.valor_unit,self.c_v,self.valor_operacao,self.tx_corret,self.tx_b3,self.valor_total,self.preco_medio,self.lucro_prejuizo)) 

            self.conn.commit()
            self.desconecta_bd()
            self.atualiza_tabela()
            self.limpar_tela()

        #except:
            #msg = 'Todos os campos devem ser preenchidos'
            #messagebox.showinfo('Otimizador de Investimentos',msg)

    def atualiza_tabela(self):
        self.tabela_dados.delete(*self.tabela_dados.get_children())
        self.conecta_bd()
        l = self.cursor.execute(""" SELECT data,ativo,qtd,valor_unit,c_v,valor_operacao,tx_corret,tx_b3,valor_total,preco_medio,lucro_prejuizo
            FROM bd ORDER BY DATE (data) ASC""")
        for i in l:
            self.tabela_dados.insert("",END,values=i)

        self.desconecta_bd()
    
    def buscar_ativo(self):

        self.conecta_bd()

        self.total_lp = 0

        self.tabela_dados.delete(*self.tabela_dados.get_children()) 
        

        self.filtrar_ativo_entry.insert(END,"%")
        filtrar_ativo = self.filtrar_ativo_entry.get()
        self.cursor.execute(
            """SELECT data,ativo,qtd,valor_unit,c_v,valor_operacao,tx_corret,tx_b3,valor_total,preco_medio,lucro_prejuizo FROM bd WHERE ativo LIKE '%s' ORDER BY DATE (data) ASC""" % filtrar_ativo)
        buscacodigo = self.cursor.fetchall()
        for i in buscacodigo:
            self.tabela_dados.insert("",END,values=i)
            self.total_lp = self.total_lp + i[10]
            self.tabela_soma.delete(*self.tabela_soma.get_children())
            self.tabela_soma.insert("", END, values=self.total_lp)

        print(self.total_lp)

        self.limpar_tela()
        self.desconecta_bd()

    def excluir_registro(self):
        
        selecao = self.tabela_dados.focus() # Obtem o item selecionado na Tabela de dados
        
        if selecao:
            
            valores = self.tabela_dados.item(selecao)['values'] # valores dos itens selecionados
            registro = valores[8]  

            self.conecta_bd()

            self.cursor.execute("DELETE FROM bd WHERE valor_total = ?", (registro,))
            self.conn.commit()

            self.desconecta_bd()

            self.tabela_dados.delete(selecao)

            self.limpar_tela()
            self.atualiza_tabela() # Atualiza tabela

    def calculo_preco_medio(self):

        cont = self.qtd
        self.preco_medio = round(self.valor_total/self.qtd,2)
        
        self.tabela_dados.delete(*self.tabela_dados.get_children())
        self.conecta_bd()
        d = self.cursor.execute(""" SELECT data,ativo,qtd,valor_unit,c_v,valor_operacao,tx_corret,tx_b3,valor_total,preco_medio,lucro_prejuizo
            FROM bd ORDER BY DATE (data) ASC""")
        for i in d:
            self.tabela_dados.insert("",END,values=i)

            if str(i[4]) == 'C':
                self.preco_medio = (int(i[8]) + (cont* self.preco_medio))/  (cont + int(i[2]))
                cont += int(i[2])
                
            elif str(i[4]) == 'V':
                cont = cont - int(i[2])
                
                
        self.limpar_tela()
        self.atualiza_tabela()
        self.desconecta_bd()

    def calculo_lucro_prejuizo(self):

        self.lucro_prejuizo = 0
        self.status = '-'

        self.tabela_dados.delete(*self.tabela_dados.get_children())
        self.conecta_bd()
        d = self.cursor.execute(""" SELECT data,ativo,qtd,valor_unit,c_v,valor_operacao,tx_corret,tx_b3,valor_total,preco_medio,lucro_prejuizo
            FROM bd ORDER BY DATE (data) ASC""")
        for i in d:
            self.tabela_dados.insert("",END,values=i)

            if self.c_v == 'V':
                self.lucro_prejuizo = round(self.valor_total - (int(i[2]) * i[9]),2)
            else:
                self.lucro_prejuizo = 0
                
     
        self.limpar_tela()
        self.atualiza_tabela()
        self.desconecta_bd()  

    def lp_carteira(self):

        self.soma = self.lucro_prejuizo
        
        self.tabela_dados.delete(*self.tabela_dados.get_children())
        
        self.conecta_bd()
        d = self.cursor.execute(""" SELECT data,ativo,qtd,valor_unit,c_v,valor_operacao,tx_corret,tx_b3,valor_total,preco_medio,lucro_prejuizo
            FROM bd ORDER BY DATE (data) ASC""")
        for i in d:
            self.tabela_dados.insert("",END,values=i)

            self.soma = self.soma + (i[10])
            self.tabela_soma.delete(*self.tabela_soma.get_children())
            self.tabela_soma.insert("", END, values=(round(self.soma,2)))

        print(self.soma)

        self.limpar_tela()
        self.atualiza_tabela()
        self.desconecta_bd()