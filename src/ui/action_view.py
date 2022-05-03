from tkinter import E, W, Scrollbar, ttk, constants, StringVar, Text, WORD
from services.stock_actions import stock_actions, SymbolNotFoundError

class ActionView:
    def __init__(self, root, handle_hello, handle_portfolio, stock_actions, portfolio_services):
        self._root = root
        self._handle_hello = handle_hello
        self._handle_portfolio = handle_portfolio
        self._frame = None
        self._stock_actions = stock_actions
        self._portfolio_services = portfolio_services
        self._get_price_variable = None
        self._get_price_label = None
        self._error_variable = None
        self._error_label = None
        self._get_info_variable = None
        self._get_info_label = None
        self._get_name_variable = None
        self._get_name_label = None
        self._get_info_text = None
        self._text_info = None
    
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
        print(info)
       # self._get_info_variable.set(info)
        #self._get_info_label.grid()
        self._text_info.insert(1.0,info)
        self._text_info.grid()
    
    def _show_name(self,price):
        self._get_name_variable.set(price)
        self._get_name_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()
    
    def _hide_price(self):
        self._get_price_label.grid_remove()

    def _handle_get_price_and_name(self):
        self._hide_price()
        symbol  = self._symbol_entry.get()

        try:
            price = self._stock_actions.get_latest_price(symbol)
            name = self._stock_actions.get_stock_name(symbol)
            self._show_price(price)
            self._show_name(name)

        except SymbolNotFoundError:
            self.show_error("Symbol not found")

    def _handle_get_info(self):
        symbol  = self._symbol_entry.get()
        try:
            info = self._stock_actions.get_stock_info(symbol)
            self._show_info(info)

        except SymbolNotFoundError:
            self._show_error("Symbol not found")


    def _handle_buy(self):
        print("Buy")
        symbol  = self._symbol_entry.get()
        amount = int(self._amount_entry.get())
        self._stock_actions.buy_stock(symbol,amount)

        self._symbol_entry.delete(0, constants.END)
        self._amount_entry.delete(0, constants.END)

        self._initialize
        

    def _handle_sell(self):
        print("Sell")
        symbol  = self._symbol_entry.get()
        amount = int(self._amount_entry.get())
        self._stock_actions.sell_stock(symbol,amount)

        self._symbol_entry.delete(0, constants.END)
        self._amount_entry.delete(0, constants.END)

       
    def _handle_portfolio_click(self):
        self._handle_portfolio(self._stock_actions, self._portfolio_services)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label_user = ttk.Label(master=self._frame, text=str(self._portfolio_services.get_logged_user())+ " is logged")

        label_symbol = ttk.Label(master=self._frame, text="Symbol:")
        self._symbol_entry = ttk.Entry(master=self._frame, width=40)

        amount_label = ttk.Label(master=self._frame, text="Amount:")
        self._amount_entry = ttk.Entry(master=self._frame, width=40)

        
        label_capital = ttk.Label(master=self._frame, text= "Free capital:")
        label_capital_value = ttk.Label(master=self._frame, text = self._portfolio_services.get_capital())
                
        label_dollar = ttk.Label(master=self._frame, text="$")
        label_empty = ttk.Label(master=self._frame, text=" afdsasfd")

        get_price_button = ttk.Button(
            master=self._frame,
            text="Get Price",
            command=self._handle_get_price_and_name
        )

        get_info_button = ttk.Button(
            master=self._frame,
            text="Get Info",
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

        self._text_info = Text(self._frame, wrap=WORD, height=15,
                                  width=65, padx=5, pady=5,
                                  bg="lightgrey")
        scroll_bar_info_test = Scrollbar(self._frame, orient='vertical')
        

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
      
        # Get name label
        self._get_name_variable = StringVar(self._frame)
        self._get_name_label = ttk.Label(
            master=self._frame,
            textvariable=self._get_name_variable,
            foreground="black"
        )


    #sticky=(
     #       constants.E, constants.W),
        label_user.grid(row=0, column=0)
        label_dollar.grid(row=5,column=2, sticky=constants.W)
        label_symbol.grid(row=1, column=0, padx=5, pady=5, sticky=E)
        self._symbol_entry.grid(row=1, column=1, columnspan=2,  padx=5, pady=5, sticky=W)

        amount_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
        self._amount_entry.grid(row=3, column=1, columnspan=2,  padx=5, pady=5, sticky=W)

        get_price_button.grid(row=2, column=1, padx=5, pady=5, sticky=E)
        self._get_price_label.grid(row=0,column=1, )
        self._get_name_label.grid(row=0,column=2, )

        get_info_button.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        #self._get_info_label.grid(row=7, column=3, padx=5, pady=5)

        #label_empty.grid(row=0, column=4)

        self._error_label.grid(row=0, column=0 ,padx=5, pady=5)

        buy_stock_button.grid(row=4, column=1,padx=5, pady=5, sticky=E)
        sell_stock_button.grid(row=4, column=2,padx=5, pady=5, sticky=W)
        #, sticky=constants.E
        label_capital.grid(row=5,column=0, padx=5, pady=5, sticky=E)
        label_capital_value.grid(row=5, column=1 ,padx=5, pady=5, sticky=E)

        portfolio_button.grid(row=6, column=1,padx=5, pady=5, sticky=E)
        logout_button.grid(row=6, column=2,padx=5, pady=5, sticky=W)

        self._text_info.grid(row=9, column=0, columnspan=4, padx=20, pady=10,sticky=(constants.W,constants.E))
        
        self._text_info.config(yscrollcommand=scroll_bar_info_test.set)

        scroll_bar_info_test.config(command=self._text_info.yview)
        scroll_bar_info_test.grid(row=9, column=3, sticky=(
            'ns', constants.E), padx=10, pady=12)

        self._frame.grid_columnconfigure(0, weight=0, minsize=30)