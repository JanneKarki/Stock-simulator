from tkinter import ttk, constants
from services.stock_actions import stock_actions

class ActionView:
    def __init__(self, root, handle_hello, handle_portfolio, stock_actions, portfolio_services):
        self._root = root
        self._handle_hello = handle_hello
        self._handle_portfolio = handle_portfolio
        self._frame = None
        self.stock_actions = stock_actions
        self.portfolio_services = portfolio_services

    
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_buy(self):
        print("Buy")

    def _handle_sell(self):
        print("Sell")
        
    def _handle_portfolio_click(self):
        self._handle_portfolio(self.stock_actions, self.portfolio_services)


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Logged in")

        buy_stock_button = ttk.Button(
            master=self._frame,
            text="Buy Stock",
            command=self._handle_buy
        )

        sell_stock_button = ttk.Button(
            master=self._frame,
            text="Sell stock",
            command=self._handle_sell
        )

        portfolio_button = ttk.Button(
            master=self._frame,
            text="Portofolio",
            command=self._handle_portfolio_click
        )
        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._handle_hello
        )

        label.grid(row=0, column=0)
        buy_stock_button.grid(row=1, column=0)
        sell_stock_button.grid(row=2, column=0)
        portfolio_button.grid(row=3, column=0)
        logout_button.grid(row=4, column=0)
