from tkinter import Scrollbar, ttk, constants, Listbox

class PortfolioView:
    """Käyttöliittymäluokka, joka vastaa portfolionäkymästä.
    """

    def __init__(self, root, handle_action, stock_actions, portfolio_services):
        """Luokan konstruktori, joka luo portfolionäkymän.


        Args:
            root (tkinter.TK): Graafisen käyttöliittymän moduuli.
            handle_action (method): Metodi joka siirtää ActionView-näkymään.
            stock_actions (class): Osakkeiden toiminnoista vastaava luokka.
            portfolio_services (class): Portfolion toiminnoista vastaava luokka.
        """
        self._root = root
        self._handle_action = handle_action
        self._frame = None
        self.stock_actions = stock_actions
        self.portfolio_services = portfolio_services

        self._initialize()

    def pack(self):
        """Määrittää ikkunan geometrian.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Sulkee nykyisen näkymän.
        """
        self._frame.destroy()

    def _handle_back_to_action_click(self):
        """Siirtää sovelluksen StockActions-näkymään.
        """
        self._handle_action(self.stock_actions, self.portfolio_services)

    def _set_stocks_listbox(self):
        """Lisää osakkeet listbox-widgettiin ja palauttaa sen.

        Returns:
            tKinter.Listbox: Palauttaa listboxiin, johon on lisätty käyttäjän omistamat osakkeet, niiden määrät ja
                keskimääräiset hankintahinnnat.
        """
        portfolio = self.portfolio_services.get_portfolio()

        listbox = Listbox(self._frame, height=10,
                          width=30,
                          bg="lightgrey",
                          activestyle='dotbox',
                          fg="Black")
        
        for count, item in enumerate(portfolio):
            symbol = str(item[0])
            avg_price = str(item[1])
            amount = str(item[2])
            text_row = amount + " shares of " + symbol + " at $" + avg_price
            listbox.insert(count, text_row)
        return listbox

    def _set_rank_listbox(self):
        """Järjestää osakkeet tuotonmukaiseen järjestykseen kutsumalla PortfolioServices-luokan metodia
            ja syöttää ne järjestyksessä listbox-widgettiin, jonka se palauttaa.

        Returns:
            tKinter.Listbox: Palauttaa listboxiin, johon on lisätty osakkeet tuotonmukaisessa järjestyksessä.
        """

        ranked_list = self.portfolio_services.rank_investments()

        ranked_list_box = Listbox(self._frame, height=10,
                                  width=30,
                                  bg="lightgrey",
                                  activestyle='dotbox',
                                  fg="Black")
        for count, item in enumerate(ranked_list):
            ranked_list_box.insert(count, item)

        return ranked_list_box

    def _initialize(self):
        """Alustaa Portfolio-näkymän.
        """

        self._frame = ttk.Frame(master=self._root)
        self._set_labels()
        self._set_listboxes()
        self._set_buttons()
        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_rowconfigure(0, weight=1)

    def _set_labels(self):
        """Määrittelee ja asettaa näkymän teksti-labelit.
        """

        label_portfolio = ttk.Label(master=self._frame, text='Portfolio')
        label_rank_list = ttk.Label(master=self._frame, text="Rank List")
        label_total_portfolio_worth = ttk.Label(
            master=self._frame, text="Portfolio's worth:")
        label_total_portfolio_worth_value = ttk.Label(
            master=self._frame, text=self.portfolio_services.total_portfolio_worth())
        label_capital = ttk.Label(master=self._frame, text="Free capital:")
        label_capital_value = ttk.Label(
            master=self._frame, text=self.portfolio_services.get_capital())
        label_total_capital = ttk.Label(
            master=self._frame, text="Total capital:")
        label_total_capital_value = ttk.Label(
            master=self._frame, text=self.portfolio_services.total_capital())
        label_profit = ttk.Label(
            master=self._frame, text="Open profit:", foreground='black')
        label_profit_value = ttk.Label(
            master=self._frame, text=self.portfolio_services.total_win_loss())

        label_starting_capital = ttk.Label(
            master=self._frame, text="Starting capital:")

        label_starting_capital_value = ttk.Label(
            master=self._frame, text=self.portfolio_services.get_starting_capital())

        label_net_result = ttk.Label(
            master=self._frame, text="Net result:")

        label_net_result_value = ttk.Label(
            master=self._frame, text=self.portfolio_services.get_net_result())

        label_dollar_1 = ttk.Label(self._frame, text="$")
        label_dollar_2 = ttk.Label(self._frame, text="$")
        label_dollar_3 = ttk.Label(self._frame, text="$")
        label_dollar_4 = ttk.Label(self._frame, text="$")
        label_dollar_5 = ttk.Label(self._frame, text="$")
        label_dollar_6 = ttk.Label(self._frame, text="$")
        # Label positions
        label_portfolio.grid(row=0, column=0, padx=5, pady=5)
        label_rank_list.grid(row=0, column=3)
        label_total_portfolio_worth.grid(
            row=2, column=0, padx=5, pady=5, sticky=constants.E)
        label_total_portfolio_worth_value.grid(
            row=2, column=1, padx=5, pady=5, sticky=constants.E)
        label_profit.grid(row=3, column=0, padx=5, pady=5, sticky=constants.E)
        label_profit_value.grid(row=3, column=1, padx=5,
                                pady=5, sticky=constants.E)
        label_capital.grid(row=4, column=0, padx=5, pady=5, sticky=constants.E)
        label_capital_value.grid(
            row=4, column=1, padx=5, pady=5, sticky=constants.E)
        label_total_capital.grid(
            row=5, column=0, padx=5, pady=5, sticky=constants.E)
        label_total_capital_value.grid(
            row=5, column=1, padx=5, pady=5, sticky=constants.E)

        label_starting_capital.grid(
            row=6, column=0, padx=5, pady=5, sticky=constants.E)
        label_starting_capital_value.grid(
            row=6, column=1, padx=5, pady=5, sticky=constants.E)

        label_net_result.grid(
            row=7, column=0, padx=5, pady=5, sticky=constants.E)
        label_net_result_value.grid(
            row=7, column=1, padx=5, pady=5, sticky=constants.E)
        
        label_dollar_1.grid(row=2, column=2)
        label_dollar_2.grid(row=3, column=2)
        label_dollar_3.grid(row=4, column=2)
        label_dollar_4.grid(row=5, column=2)
        label_dollar_5.grid(row=6, column=2)
        label_dollar_6.grid(row=7, column=2)
    def _set_listboxes(self):
        """Määrittelee ja asettaa näkymän listboxit.
        """
        listbox_stocks = self._set_stocks_listbox()
        listbox_rank = self._set_rank_listbox()

        scroll_bar_for_stock_list = Scrollbar(self._frame, orient='vertical')
        scroll_bar_for_rank_list = Scrollbar(self._frame, orient='vertical')

        listbox_stocks.config(yscrollcommand=scroll_bar_for_stock_list.set)
        scroll_bar_for_stock_list.config(command=listbox_stocks.yview)
        listbox_rank.config(yscrollcommand=scroll_bar_for_rank_list.set)
        scroll_bar_for_rank_list.config(command=listbox_rank.yview)
        listbox_stocks.configure(background="white")
        listbox_rank.configure(background="white")
        # Positions
        listbox_stocks.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        scroll_bar_for_stock_list.grid(row=1, column=2, sticky=(
            'ns', constants.E), padx=5, pady=7)
        listbox_rank.grid(row=1, column=3, columnspan=2, padx=5, pady=5)
        scroll_bar_for_rank_list.grid(row=1, column=4, sticky=(
            'ns', constants.E), padx=5, pady=7)

    def _set_buttons(self):
        """Määrittelee ja asettaa näkymään button-painikkeet.
        """

        back_to_action_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back_to_action_click
        )
        # Button position
        back_to_action_button.grid(
            row=10, column=0, columnspan=5, padx=10, pady=20)
