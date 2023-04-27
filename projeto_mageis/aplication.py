from tkinter import *
import customtkinter 
from tkinter import ttk #treeview(tabela de dados)
from funcoes import funcoes

customtkinter.set_appearance_mode('Light')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()

class app(funcoes):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame1()
        self.widgets_frame2()
        self.cria_bd()
        self.atualiza_tabela()
        root.mainloop()
        
    def tela(self):
        
        self.root.title('Otimizador de Investimentos')
        self.root.geometry('700x500')
        self.root.resizable(True,True) #responsividade
        self.root.maxsize(width=750,height=500)
        self.root.minsize(width=500, height=400)
        
    def frames(self):
        #frames
        self.frame1 = customtkinter.CTkFrame(self.root)
        self.frame1.place(relx = 0,rely = 0,relwidth = 1,relheight = 0.18)
        self.frame2 = customtkinter.CTkFrame(self.root)
        self.frame2.place(relx = 0,rely =0.18, relwidth = 1, relheight = 0.85)
    
    def widgets_frame1(self):
        #labels
        self.data = customtkinter.CTkLabel(self.frame1,text='Data')
        self.data.place(relx = 0.1, rely = 0.1)
        self.codigo = customtkinter.CTkLabel(self.frame1,text='Código')
        self.codigo.place(relx = 0.24, rely = 0.1)
        self.qtd = customtkinter.CTkLabel(self.frame1,text='Qtd.')
        self.qtd.place(relx = 0.38, rely = 0.1)
        self.valor_unit = customtkinter.CTkLabel(self.frame1,text='Valor unit. (R$)')
        self.valor_unit.place(relx = 0.48, rely = 0.1)
        #entrys
        self.data_entry = customtkinter.CTkEntry(self.frame1,width=90,placeholder_text='dd/mm/aaaa')
        self.data_entry.place(relx = 0.06, rely = 0.4)
        self.codigo_entry = customtkinter.CTkEntry(self.frame1, width=80,placeholder_text='AAAA00')
        self.codigo_entry.place(relx = 0.21, rely = 0.4)
        self.qtd_entry = customtkinter.CTkEntry(self.frame1, width=70)
        self.qtd_entry.place(relx = 0.35, rely = 0.4)
        self.valor_unit_entry = customtkinter.CTkEntry(self.frame1, width=80)
        self.valor_unit_entry.place(relx = 0.48, rely = 0.4)
        #botão 
        self.bt_add = customtkinter.CTkButton (self.frame1,text = 'Adicionar', width = 70,command=self.adiciona_dados)
        self.bt_add.place(relx = 0.8, rely = 0.2)
        self.bt_limpar = customtkinter.CTkButton (self.frame1,text = 'Limpar', width = 70,command=self.limpar_tela)
        self.bt_limpar.place(relx = 0.8, rely = 0.6)
        #radiobutton
        self.radio_valor = IntVar()
        self.compra =customtkinter.CTkRadioButton(self.frame1,text = 'Comprar', value=1,variable=self.radio_valor)
        self.compra.place(relx = 0.65, rely = 0.2)
        self.venda = customtkinter.CTkRadioButton(self.frame1,text = 'Vender',value=2,variable=self.radio_valor)
        self.venda.place(relx = 0.65, rely = 0.6) 
        
    def widgets_frame2(self):
        
        #tabela de dados
        self.tabela_dados = ttk.Treeview(self.frame2,height = 10,column = ('col1','col2','col3','col4','col5','col6','col7','col9','col10'))

        self.tabela_dados.heading('#0',text='')
        self.tabela_dados.heading('#1',text='Data')
        self.tabela_dados.heading('#2',text='Código')
        self.tabela_dados.heading('#3',text='Qtd.')
        self.tabela_dados.heading('#4',text='Valor Unit.')
        self.tabela_dados.heading('#5',text='C/V')
        self.tabela_dados.heading('#6',text='Valor Op.')
        self.tabela_dados.heading('#7',text='tx.Corret.')
        self.tabela_dados.heading('#8',text='tx.Imposto')
        self.tabela_dados.heading('#9',text='Valor Final')

        self.tabela_dados.column('#0',width=0)
        self.tabela_dados.column('#1',width=60)
        self.tabela_dados.column('#2',width=70)
        self.tabela_dados.column('#3',width=50)
        self.tabela_dados.column('#4',width=70)
        self.tabela_dados.column('#5',width=60)
        self.tabela_dados.column('#6',width=60)
        self.tabela_dados.column('#7',width=60)
        self.tabela_dados.column('#8',width=70)
        self.tabela_dados.column('#9',width=90)
       
        self.tabela_dados.place(relx = 0.01,rely = 0.01, relwidth=0.98, relheight=0.93)
        
        #barra de rolagem
        self.scrol_tab = customtkinter.CTkScrollbar(self.frame2,orientation='vertical')
        self.tabela_dados.configure(yscroll=self.scrol_tab.set)
        self.scrol_tab.place(relx=0.98,rely=0,relheight=0.94)

app()
