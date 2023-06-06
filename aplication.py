
from tkinter import *
import customtkinter 
from tkinter import ttk #treeview(tabela de dados)
from funcoes import funcoes

customtkinter.set_appearance_mode('Light')
customtkinter.set_default_color_theme('blue')

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
        self.buscar_ativo()
        self.excluir_registro()
        self.menus()
        root.mainloop()
        
    def tela(self):
        
        self.root.title('Otimizador de Investimentos')
        self.root.geometry('900x600')
        self.root.resizable(False,False) #responsividade
        self.root.maxsize(width=850,height=500)
        self.root.minsize(width=800, height=500)
        
    def frames(self):
        #frames
        self.frame1 = customtkinter.CTkFrame(self.root)
        self.frame1.place(relx = 0,rely = 0,relwidth = 1,relheight = 0.22)
        self.frame2 = customtkinter.CTkFrame(self.root)
        self.frame2.place(relx = 0,rely =0.20, relwidth = 1, relheight = 0.8)
    
    def widgets_frame1(self):
        #labels
        #self.filtrar_ativo = customtkinter.CTkLabel(self.frame1,text='Filtrar Ativo')
        #self.filtrar_ativo.place(relx = 0.05, rely = 0.1)
        self.data = customtkinter.CTkLabel(self.frame1,text='Data')
        self.data.place(relx = 0.075, rely = 0.1)
        self.ativo = customtkinter.CTkLabel(self.frame1,text='Ativo')
        self.ativo.place(relx = 0.2, rely = 0.1)
        self.qtd = customtkinter.CTkLabel(self.frame1,text='Qtd.')
        self.qtd.place(relx = 0.315, rely = 0.1)
        self.valor_unit = customtkinter.CTkLabel(self.frame1,text='Valor unit. (R$)')
        self.valor_unit.place(relx = 0.4, rely = 0.1)
        #self.tx_corret = customtkinter.CTkLabel(self.frame1,text='Tx.Corret. (R$)')
        #self.tx_corret.place(relx = 0.55, rely = 0.1)
        #entrys
        self.filtrar_ativo_entry = customtkinter.CTkEntry(self.frame1,width=60,placeholder_text='ABCD01')
        #self.filtrar_ativo_entry.place(relx = 0.15, rely = 0.1)
        self.data_entry = customtkinter.CTkEntry(self.frame1,width=90,placeholder_text='dd/mm/aaaa')
        self.data_entry.place(relx = 0.04, rely = 0.3)
        self.ativo_entry = customtkinter.CTkEntry(self.frame1, width=80,placeholder_text='AAAA00')
        self.ativo_entry.place(relx = 0.17, rely = 0.3)
        self.qtd_entry = customtkinter.CTkEntry(self.frame1, width=70)
        self.qtd_entry.place(relx = 0.29, rely = 0.3)
        self.valor_unit_entry = customtkinter.CTkEntry(self.frame1, width=80)
        self.valor_unit_entry.place(relx = 0.40, rely = 0.3)
        #botão 
        self.bt_add = customtkinter.CTkButton (self.frame1,text = 'Adicionar', width = 70,command=self.adiciona_dados)
        self.bt_add.place(relx = 0.8, rely = 0.15)
        self.bt_excluir = customtkinter.CTkButton (self.frame1,text = 'Excluir', width = 70,command=self.excluir_registro)
        self.bt_excluir.place(relx = 0.8, rely = 0.5)
        self.bt_buscar = customtkinter.CTkButton (self.frame1,text = 'Buscar', width = 70,command=self.buscar_ativo)
        #self.bt_buscar.place(relx = 0.25, rely = 0.1)
        #radiobutton
        self.radio_valor = IntVar()
        self.compra = customtkinter.CTkRadioButton(self.frame1,text = 'Comprar', value=1,variable=self.radio_valor)
        self.compra.place(relx = 0.65, rely = 0.15)
        self.venda = customtkinter.CTkRadioButton(self.frame1,text = 'Vender',value=2,variable=self.radio_valor)
        self.venda.place(relx = 0.65, rely = 0.4) 
      
    def widgets_frame2(self):
        
        #tabela de dados
        self.tabela_dados = ttk.Treeview(self.frame2,height = 11,column = ('col1','col2','col3','col4','col5','col6','col7','col9','col10','col11','col12','col13'))

        self.tabela_dados.heading('#0',text='')
        self.tabela_dados.heading('#1',text='Data')
        self.tabela_dados.heading('#2',text='Ativo')
        self.tabela_dados.heading('#3',text='Qtd.')
        self.tabela_dados.heading('#4',text='Valor Unit.')
        self.tabela_dados.heading('#5',text='C/V')
        self.tabela_dados.heading('#6',text='Valor Op.')
        self.tabela_dados.heading('#7',text='tx.Corret.')
        self.tabela_dados.heading('#8',text='taxa B3')
        self.tabela_dados.heading('#9',text='Valor Total')
        self.tabela_dados.heading('#10',text='Preço Médio')
        self.tabela_dados.heading('#11',text='LP')
        self.tabela_dados.heading('#12',text='Status')

        self.tabela_dados.column('#0',width=0)
        self.tabela_dados.column('#1',width=60)
        self.tabela_dados.column('#2',width=50)
        self.tabela_dados.column('#3',width=40)
        self.tabela_dados.column('#4',width=55)
        self.tabela_dados.column('#5',width=30)
        self.tabela_dados.column('#6',width=55)
        self.tabela_dados.column('#7',width=55)
        self.tabela_dados.column('#8',width=45)
        self.tabela_dados.column('#9',width=60)
        self.tabela_dados.column('#10',width=65)
        self.tabela_dados.column('#11',width=40)
        self.tabela_dados.column('#12',width=60)
       
        self.tabela_dados.place(relx = 0.01,rely = 0.01, relwidth=0.98, relheight=0.88)
        
        #barra de rolagem
        self.scrol_tab = customtkinter.CTkScrollbar(self.frame2,orientation='vertical')
        self.tabela_dados.configure(yscroll=self.scrol_tab.set)
        self.scrol_tab.place(relx=0.98,rely=0,relheight=0.9)

        #label
        #self.label_total_carteira = customtkinter.CTkLabel(self.frame2,text='Total L/P carteira:')
        #self.label_total_carteira.place(relx=0.7,rely=0.9)

        self.table1()

    def table1(self):

        self.tabela_soma = ttk.Treeview(self.frame2,height=1,columns=('col1'))
        self.tabela_soma['columns'] = ('soma')
        self.tabela_soma.heading('soma', text='Total L/P Carteira')
        
        self.tabela_soma.place(relx = 0.5,rely = 0.76)

    def table2(self):

        self.tabela_soma = ttk.Treeview(self.root2,height=1,columns=('col1'))
        self.tabela_soma['columns'] = ('total_lp')
        self.tabela_soma.heading('total_lp', text='Total L/P ')
        
        self.tabela_soma.place(relx = 0.48,rely = 0.8)


    def janela2(self):
        
        self.root2 = customtkinter.CTkToplevel()
        self.root2.title('Detalhamento por Ativo')
        self.root2.geometry('800x500')
        self.root2.resizable(True,True)
        self.root2.maxsize(width=800,height=500)
        self.root2.minsize(width=750, height=450)
        self.root2.transient(self.root)
        self.root2.focus_force()    

        self.widgets_janela2()
        
        self.tabela_dados = ttk.Treeview(self.root2,height = 11,column = ('col1','col2','col3','col4','col5','col6','col7','col9','col10','col11','col12','col13'))

        self.tabela_dados.heading('#0',text='')
        self.tabela_dados.heading('#1',text='Data')
        self.tabela_dados.heading('#2',text='Ativo')
        self.tabela_dados.heading('#3',text='Qtd.')
        self.tabela_dados.heading('#4',text='Valor Unit.')
        self.tabela_dados.heading('#5',text='C/V')
        self.tabela_dados.heading('#6',text='Valor Op.')
        self.tabela_dados.heading('#7',text='tx.Corret.')
        self.tabela_dados.heading('#8',text='taxa B3')
        self.tabela_dados.heading('#9',text='Valor Total')
        self.tabela_dados.heading('#10',text='Preço Médio')
        self.tabela_dados.heading('#11',text='LP')
        self.tabela_dados.heading('#12',text='Status')

        self.tabela_dados.column('#0',width=0)
        self.tabela_dados.column('#1',width=60)
        self.tabela_dados.column('#2',width=50)
        self.tabela_dados.column('#3',width=40)
        self.tabela_dados.column('#4',width=55)
        self.tabela_dados.column('#5',width=30)
        self.tabela_dados.column('#6',width=55)
        self.tabela_dados.column('#7',width=55)
        self.tabela_dados.column('#8',width=45)
        self.tabela_dados.column('#9',width=60)
        self.tabela_dados.column('#10',width=65)
        self.tabela_dados.column('#11',width=40)
        self.tabela_dados.column('#12',width=60)
       
        self.tabela_dados.place(relx = 0.01,rely = 0.2, relwidth=0.98, relheight=0.7)

        #self.label_total = customtkinter.CTkLabel(self.root2,text='Total L/P:')
        #self.label_total.place(relx=0.75,rely=0.92)

        self.table2()

    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def quit(): self.root.destroy()

        menubar.add_cascade(label='Opções',menu=filemenu)
        menubar.add_cascade(label='Detalhes',menu=filemenu2)

        filemenu.add_command(label='Sair',command=quit)
        filemenu2.add_command(label='Detalhamento por ativo',command=self.janela2)

    def widgets_janela2(self):
        #self.label_combobox = customtkinter.CTkLabel(self.root2,text='Filtrar Ativo')
        #self.label_combobox.place(relx=0.28,rely=0.095)

        #self.combobox_var = StringVar()
        #self.combobox = ttk.Combobox(self.root2,textvariable=self.combobox_var,values= ['ITSA4','PETR4','WEGE3'])
        #self.combobox.place(relx=0.4,rely=0.1)
        self.filtrar_ativo_label = customtkinter.CTkLabel(self.root2,text='Filtrar Ativo')
        self.filtrar_ativo_label.place(relx = 0.35, rely = 0.089)

        self.filtrar_ativo_entry = customtkinter.CTkEntry(self.root2,width=100,placeholder_text='ABCD01')
        self.filtrar_ativo_entry.place(relx = 0.45, rely = 0.089)

        self.filtrar = customtkinter.CTkButton (self.root2,text = 'Filtrar', width = 70, command= self.buscar_ativo)
        self.filtrar.place(relx = 0.6, rely = 0.09)


app()