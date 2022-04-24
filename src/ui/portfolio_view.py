from multiprocessing.spawn import old_main_modules
from sqlite3 import Row
from tkinter import BOTH, LEFT, NS, RIGHT, Y, Label, Scrollbar, ttk, constants, Listbox
import tkinter as tk

from numpy import pad
from services.portfolio_services import PortfolioServices

from services.stock_actions import StockActions


class PortfolioView:
    def __init__(self, root, handle_action, stock_actions, portfolio_services):
        self._root = root
        self._handle_action = handle_action
        self._frame = None
        self.stock_actions = stock_actions
        self.portfolio_services = portfolio_services
        #self.portfolio_services = 

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_back_to_action_click(self):
        self._handle_action(self.stock_actions, self.portfolio_services)

    def _stocks_in_listbox(self):
        portfolio = self.portfolio_services.get_portfolio()

        listbox = Listbox(self._frame,height = 10, 
                  width = 30, 
                  bg = "lightgrey",
                  activestyle = 'dotbox', 
                  fg = "Black")

        for count,item in enumerate(portfolio):
            listbox.insert(count,item)
        return listbox

    def _stocks_in_rank_listbox(self):
        ranked_list = self.portfolio_services.rank_investments()

        ranked_list_box = Listbox(self._frame,height = 10, 
                  width = 30, 
                  bg = "lightgrey",
                  activestyle = 'dotbox', 
                  fg = "Black")
        for count,item in enumerate(ranked_list):
            ranked_list_box.insert(count,item)
        return ranked_list_box
        
    

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text=str(self.portfolio_services.get_logged_user() +"'s " + "portfolio"))

        stocks_listbox = self._stocks_in_listbox()
        ranked_list_box = self._stocks_in_rank_listbox()

        scroll_bar_stock_list = Scrollbar(self._frame, orient='vertical')

        scroll_bar_ranked_list = Scrollbar(self._frame, orient='vertical')
       
        label_total_portfolio_worth = ttk.Label(master=self._frame, text="Total portfolio's worth")
        label_total_portfolio_worth_value = ttk.Label(master=self._frame,text=self.portfolio_services.total_portfolio_worth())
        
        label_capital = ttk.Label(master=self._frame, text= "Free capital")
        label_capital_value = ttk.Label(master=self._frame, text = self.portfolio_services.get_capital())
        
        label_total_capital = ttk.Label(master=self._frame, text= "Total capital")
        label_total_capital_value = ttk.Label(master=self._frame, text = self.portfolio_services.total_capital())
        
        label_profit = ttk.Label(master=self._frame, text= "Net profit", foreground='black')
        label_profit_value = ttk.Label(master=self._frame, text= self.portfolio_services.total_win_loss())

        back_to_action_button = ttk.Button(
            master=self._frame,
            text="Back_to_action",
            command=self._handle_back_to_action_click
        )

        label.grid(row=0, column=0,columnspan=2, padx=5, pady=5)

        label_total_portfolio_worth.grid(row=1, column=0,padx=5, pady=5 )
        label_total_portfolio_worth_value.grid(row=1,column=1, padx=5, pady=5)
        
        label_capital.grid(row=2,column=0, padx=5, pady=5)
        label_capital_value.grid(row=2, column=1, padx=5, pady=5)

        label_total_capital.grid(row=3,column=0, padx=5, pady=5)
        label_total_capital_value.grid(row=3, column=1, padx=5, pady=5)
        
        label_profit.grid(row=4,column=0, padx=5, pady=5)
        label_profit_value.grid(row=4, column=1, padx=5, pady=5)


        stocks_listbox.grid(row=1, column=2)
        scroll_bar_stock_list.grid(row=1,column=3)

        stocks_listbox.config(yscrollcommand=scroll_bar_stock_list.set)
        scroll_bar_stock_list.config(command=stocks_listbox.yview)

        ranked_list_box.grid(row=1, column=4)
        scroll_bar_ranked_list.grid(row=1,column=5)

        ranked_list_box.config(yscrollcommand=scroll_bar_ranked_list.set)
        scroll_bar_ranked_list.config(command=ranked_list_box.yview)

        back_to_action_button.grid(row=10, column=0, padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_rowconfigure(0, weight=1)