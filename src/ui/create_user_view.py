from tkinter import ttk, constants, Toplevel, Label, Button, StringVar
from services.user_services import user_services, EmptyInputError, CapitalInputError, UsernameExistsError


class CreateUserView:
    """Käyttöliittymäluokka, joka vastaa CreateUser-näkymästä
    """

    def __init__(self, root, handle_return):
        """Luokan konstruktori, joka luo näkymän, jossa osakkeiden uuden tunnuksen luonti tapahtuu.

        Args:
            root (tkinter.TK): Graafisen käyttöliittymän moduuli.
            handle_return (method): Metodi joka siirtää takaisin Login-näkymään.
        """
        self._root = root
        self._handle_return = handle_return
        self._frame = None
        self._error_variable = None
        self._error_label = None
        
        self._initialize()

    def pack(self):
        """Määrittää ikkunan geometrian.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Sulkee nykyisen näkymän.
        """
        self._frame.destroy()

    def _create_user_handler(self):
        """Käsittelee käyttäjän luomisen kutsumalla UserServices-luokan metodia.
        """
        username = self._username_entry.get()
        password = self._password_entry.get()
        capital = self._capital_entry.get()

        try:
            user_services.create_user(username, password, capital)
            self._open_ok_window()

        except EmptyInputError:
            self._show_error("Inputs cannot be empty")

        except UsernameExistsError:
            self._show_error("Username exists")

        except CapitalInputError:
            self._show_error("Invalid capital input")

    def _show_error(self, message):
        """Asettaa virheviestin näkyville.

        Args:
            message (str): Näytettävä virheviesti.
        """
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        """Piilottaa näytetyn virheviestin.
        """
        self._error_label.grid_remove()

    def _handle_ok_click(self):
        """Käsittelee "ok"-painikkeen klikkauksen.
        """
        self._handle_return()

    def _open_ok_window(self):
        """Avaa uuden "User Created"-ikkunan.
        """
        newWindow = Toplevel(self._frame)
        newWindow.title("User Created")
        newWindow.geometry("200x100")
        Label(newWindow, pady=10,
              text="User succesfully created!").pack()
        button = Button(newWindow,
                        text="OK",
                        command=self._handle_ok_click)
        button.pack(pady=3, padx=25)

    def _initialize(self):
        """Alustaa CreateUser-näkymän.
        """

        self._frame = ttk.Frame(master=self._root)

        self._frame.grid_columnconfigure(0, weight=1, minsize=150)

        self._hide_error()

    def _set_labels(self):
        """Määrittelee ja asettaa näkymän teksti-labelit.
        """

        heading_label = ttk.Label(master=self._frame, text="Create new user")
        username_label = ttk.Label(master=self._frame, text="Username:")
        password_label = ttk.Label(master=self._frame, text="Password:")
        capital_label = ttk.Label(master=self._frame, text="Capital:")
        # Error_label
        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )
        # Label positions
        heading_label.grid(row=0, column=0)
        self._error_label.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        password_label.grid(row=2, column=0, padx=5, pady=5)
        capital_label.grid(row=3, column=0, padx=5, pady=5)

    def _set_entries(self):
        """Määrittelee ja asettaa näkymään "username"-, "password"- "capital"-syötteiden entry-kentät.
        """

        self._username_entry = ttk.Entry(master=self._frame)
        self._password_entry = ttk.Entry(master=self._frame)
        self._capital_entry = ttk.Entry(master=self._frame)
        # Entries positions
        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._capital_entry.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def _set_buttons(self):
        """Määrittelee ja asettaa näkymään button-painikkeet.
        """

        create_button = ttk.Button(
            master=self._frame,
            text="Create",
            command=self._create_user_handler
        )
        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_return
        )
        # Button positions
        create_button.grid(row=4, column=0, padx=5, pady=25)
        back_button.grid(row=4, column=1, padx=5, pady=25)
