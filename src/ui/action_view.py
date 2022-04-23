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
        self._get_price_variable = None
        self._get_price_label = None
        self._error_variable = None
        self._error_label = None
        self._get_info_variable = None
        self._get_info_label = None


    
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _show_error(self,message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _show_price(self,price):
        self._get_price_variable.set(price)
        self._get_price_label.grid()

    def _show_info(self,info):
        self._get_info_variable.set(info)
        self._get_info_label.grid()


    def _hide_error(self):
        self._error_label.grid_remove()
    
    def _hide_price(self):
        self._get_price_label.grid_remove()

    def _handle_get_price(self):
        self._hide_price()
        symbol  = self._symbol_entry.get()

        try:
            price = self.stock_actions.get_latest_price(symbol)
            self._show_price(price)

        except SymbolNotFoundError:
            self.show_error("Symbol not found")

    def _handle_get_info(self):
        symbol  = self._symbol_entry.get()

        try:
            info = self.stock_actions.get_stock_info(symbol)
            self._show_info(info)

        except SymbolNotFoundError:
            self.show_error("Symbol not found")


    def _handle_buy(self):
        print("Buy")

    def _handle_sell(self):
        print("Sell")
        
    def _handle_portfolio_click(self):
        self._handle_portfolio(self.stock_actions, self.portfolio_services)


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text=str(self.portfolio_services.get_logged_user()) + " logged in")

        symbol_label = ttk.Label(master=self._frame, text="Symbol:")
        self._symbol_entry = ttk.Entry(master=self._frame)

        amount_label = ttk.Label(master=self._frame, text="Amount:")
        self._amount_entry = ttk.Entry(master=self._frame)

        
        
        get_price_button = ttk.Button(
            master=self._frame,
            text="Price",
            command=self._handle_get_price
        )

        get_info_button = ttk.Button(
            master=self._frame,
            text="Info",
            command=self._handle_get_info
        )
        
        buy_stock_button = ttk.Button(
            master=self._frame,
            text="Buy",
            command=self._handle_buy
        )

        sell_stock_button = ttk.Button(
            master=self._frame,
            text="Sell",
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

        # Error_label
        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )
        # Get price label
        self._get_price_variable = StringVar(self._frame)
        self._get_price_label = ttk.Label(
            master=self._frame,
            textvariable=self._get_price_variable,
            foreground="black"
        )
        # Get info label
        self._get_info_variable = StringVar(self._frame)
        self._get_info_label = ttk.Label(
            master=self._frame,
            textvariable=self._get_info_variable,
            foreground="black"
        )



        symbol_label.grid(row=1, column=0, padx=5, pady=5)
        self._symbol_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        amount_label.grid(row=3, column=0, padx=5, pady=5)
        self._amount_entry.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        get_price_button.grid(row=2, column=1,sticky=W, padx=5, pady=5)
        self._get_price_label.grid(row=0,column=1, )
        self._error_label.grid(row=0, column=1 ,columnspan=1 ,padx=5, pady=5)
        buy_stock_button.grid(row=4, column=1, sticky=W,padx=5, pady=5)
        sell_stock_button.grid(row=4, column=1,sticky=E,padx=5, pady=5)
        portfolio_button.grid(row=5, column=0,padx=5, pady=25)
        logout_button.grid(row=5, column=1,padx=5, pady=25)
        get_info_button.grid(row=2, column=1, sticky=E,)
        self._get_info_label.grid(row=0, column=2, padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=150)