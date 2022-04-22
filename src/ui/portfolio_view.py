from multiprocessing.spawn import old_main_modules
from sqlite3 import Row
from tkinter import Label, ttk, constants

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
    

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text=str(self.portfolio_services.get_logged_user() +"'s " + "portfolio is here:"))

       
        label_total_portfolio_worth = ttk.Label(master=self._frame, text="Total portfolio's worth")
        label_total_portfolio_worth_value = ttk.Label(master=self._frame,text=self.portfolio_services.total_portfolio_worth())
        
        label_capital = ttk.Label(master=self._frame, text= "Free capital")
        label_capital_value = ttk.Label(master=self._frame, text = self.portfolio_services.get_capital())
        
        label_total_capital = ttk.Label(master=self._frame, text= "Total capital")
        label_total_capital_value = ttk.Label(master=self._frame, text = self.portfolio_services.total_capital())
        
        label_profit = ttk.Label(master=self._frame, text= "Net profit")
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

        back_to_action_button.grid(row=5, column=0, padx=5, pady=5)
