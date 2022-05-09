from curses.ascii import EM
from tkinter import E, W, Scrollbar, ttk, constants, StringVar, Text, WORD
import webbrowser
from numpy import pad
from repositories.stock_repository import StockNotInPortfolioError, TooLargeSellOrderError
from repositories.user_repository import NotEnoughMoneyError
from services.stock_actions import InvalidAmountError, stock_actions, SymbolNotFoundError, EmptyInputError



class ActionView:
    """Käyttöliittymäluokka, joka vastaa osakkeiden osto- ja myyntinäkymästä.
    """
    def __init__(self, root, handle_login, handle_portfolio, stock_actions, portfolio_services):
        """Luokan konstruktori, joka luo näkymän, jossa osakkeiden osto ja myynti tapahtuu.

        Args:
            root (tkinter.TK): Graafisen käyttöliittymän moduuli.
            handle_login (method): Metodi joka siirtää Login-näkymään.
            handle_portfolio (method): Metodi joka siirtää Portfolio-näkymään.
            stock_actions (class): Osakkeiden toiminnoista vastaava luokka.
            portfolio_services (class): Portfolion toiminnoista vastaava luokka.
        """
        self._root = root
        self._handle_login = handle_login
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
        """Määrittää ikkunan geometrian.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Sulkee nykyisen näkymän
        """
        self._frame.destroy()

    def _show_error(self, message):
        """Asettaa virheviestin näkyville.

        Args:
            message (str): Näytettävä virheviesti.
        """
        self._error_variable.set(message)
        self._error_label.grid()

    def _show_price(self, price):
        """Asettaa osakkeen hinnan näkyville.

        Args:
            price (float): Näytettävä hinta.
        """
        self._get_price_variable.set(price)
        self._get_price_label.grid()

    def _show_info(self, info):
        """Asettaa yritystiedon näkyille tekstilaatikkoon.

        Args:
            info (str): Näytettävä info-teksti
        """
        self._text_info.insert(1.0, info)
        self._text_info.grid()

    def _show_name(self, name):
        """Näyttää osakkeen nimen.

        Args:
            nimi (str): Näytettävän osakkeen nimi.
        """
        self._get_name_variable.set(name)
        self._get_name_label.grid()

    def _hide_error(self):
        """Piilottaa näytetyn virheviestin.
        """
        self._error_label.grid_remove()

    def _hide_price(self):
        """Piilottaa näytetyn osakkeen hinnan.
        """
        self._get_price_label.grid_remove()
    
    def _hide_name(self):
        """Piilottaa näytetyn osakkeen nimen.
        """
        self._get_name_label.grid_remove()

    def _handle_get_price_and_name(self):
        """Hakee osakkeen hinnan ja nimen kutsumalla StockActions-luokan metodeita,
        ja asettaa ne ikkunaan näkyviin.
        """
        self._hide_price()
        self._hide_error()
        self._hide_name()
        
        symbol_entry = self._symbol_entry.get()


        try:
            latest_price = self._stock_actions.get_latest_price(symbol_entry)
            stock_name = self._stock_actions.get_stock_name(symbol_entry)

            self._show_price(latest_price)
            self._show_name(stock_name)

        except SymbolNotFoundError:
            self._show_error("Symbol not found")


    def _handle_get_info(self):
        """Hakee yrityksen esittelytekstin kutsumalla StockActions-luokan get_stock_info-metodia,
        ja asettaa sen tekstilaatikkoon näkyviin.
        """
        self._hide_error()

        symbol = self._symbol_entry.get()

        try:
            info = self._stock_actions.get_stock_info(symbol)
            self._show_info(info)

        except SymbolNotFoundError:
            self._show_error("Symbol not found")


    def _handle_buy(self):
        """Käsittelee ostotapahtuman kutsumalla StockActions-luokan buy_stock-metodia.
        """
        self._hide_error()
        self._hide_price()
        self._hide_name()
        symbol = self._symbol_entry.get()
        amount = self._amount_entry.get()
            
        try:
            self._stock_actions.buy_stock(symbol, amount)
        except SymbolNotFoundError:
            self._show_error('Symbol not found')
        except NotEnoughMoneyError:
            self._show_error('Not enough money')
        except EmptyInputError:
            self._show_error('Inputs cannot be empty')
        except InvalidAmountError:
            self._show_error('Invalid amount')

        self._symbol_entry.delete(0, constants.END)
        self._amount_entry.delete(0, constants.END)

        self._initialize

    def _handle_sell(self):
        """Käsittelee myyntitapahtuman kutsumalla StockActions-luokan sell_stock-metodia.
        """
        self._hide_error()
        self._hide_name()
        self._hide_price()

        symbol = self._symbol_entry.get()
        amount = self._amount_entry.get()

        try:
            self._stock_actions.sell_stock(symbol, amount)
        except SymbolNotFoundError:
            self._show_error('Symbol not found')
        except StockNotInPortfolioError:
            self._show_error('Stock not owned')
        except TooLargeSellOrderError:
            self._show_error('Too large sell order')
        except InvalidAmountError:
            self._show_error('Invalid amount')
        except EmptyInputError:
            self._show_error('Inputs cannot be empty')

        self._symbol_entry.delete(0, constants.END)
        self._amount_entry.delete(0, constants.END)

    def _handle_portfolio_click(self):
        """Siirtää sovelluksen portfolio-näkymään.
        """
        self._handle_portfolio(self._stock_actions, self._portfolio_services)

    def _initialize(self):
        """Alustaa StockActions-näkymän.
        """
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(0, weight=0, minsize=30)
        self._set_labels()
        self._set_buttons()
        self._set_textbox()
        self._set_up_entries()

    def callback(self,url):
            webbrowser.open_new(url)

    def _set_labels(self):
        """Määrittelee ja asettaa näkymään Labelit.
        """
        label_user = ttk.Label(master=self._frame, text=str(
            self._portfolio_services.get_logged_user()) + " is logged")
        label_symbol = ttk.Label(master=self._frame, text="Symbol:")
        label_amount = ttk.Label(master=self._frame, text="Amount:")
        label_capital = ttk.Label(master=self._frame, text="Free capital:")
        label_capital_value = ttk.Label(
            master=self._frame, text=self._portfolio_services.get_capital())
        label_dollar = ttk.Label(master=self._frame, text="$")

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
        #Label positions
        label_user.grid(row=0, column=0)
        label_dollar.grid(row=5, column=2, sticky=constants.W)
        label_symbol.grid(row=1, column=0, padx=5, pady=5, sticky=E)
        label_amount.grid(row=3, column=0, padx=5, pady=5, sticky=E)
        label_capital.grid(row=5, column=0, padx=5, pady=5, sticky=E)
        label_capital_value.grid(row=5, column=1, padx=5, pady=5, sticky=E)
        self._get_price_label.grid(row=0, column=1, )
        self._get_name_label.grid(row=0, column=2, )
        self._error_label.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

    def _set_buttons(self):
        """Määrittelee ja asettaa näkymään Button-painikkeet.
        """
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
            command=self._handle_login
        )
        #Button positions
        get_price_button.grid(row=2, column=1, padx=5, pady=5, sticky=E)
        buy_stock_button.grid(row=4, column=1, padx=5, pady=5, sticky=E)
        sell_stock_button.grid(row=4, column=2, padx=5, pady=5, sticky=W)
        get_info_button.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        portfolio_button.grid(row=6, column=1, padx=5, pady=5, sticky=E)
        logout_button.grid(row=6, column=2, padx=5, pady=5, sticky=W)

    def _set_textbox(self):
        """Määrittelee ja asettaa näkymään info-tekstilaatikon ja sille scroll-barin.
        """
        self._text_info = Text(self._frame, wrap=WORD, height=15,
                               width=65, padx=5, pady=5,
                               bg="lightgrey")
        scroll_bar_info = Scrollbar(self._frame, orient='vertical')
        scroll_bar_info.config(command=self._text_info.yview)
        scroll_bar_info.grid(row=9, column=3, sticky=(
            'ns', constants.E), padx=10, pady=12)
        self._text_info.grid(row=9, column=0, columnspan=4,
                             padx=20, pady=10, sticky=(constants.W, constants.E))
        self._text_info.config(yscrollcommand=scroll_bar_info.set)


    def _set_up_entries(self):
        """Määrittelee ja asettaa näkymään "Symbol"- ja "Amount"-syötteiden Entry-kentät.
        """

        self._amount_entry = ttk.Entry(master=self._frame, width=40)
        self._symbol_entry = ttk.Entry(master=self._frame, width=40)
        
        #Entry positions
        self._symbol_entry.grid(
            row=1, column=1, columnspan=2,  padx=5, pady=5, sticky=W)
        self._amount_entry.grid(
            row=3, column=1, columnspan=2,  padx=5, pady=5, sticky=W)