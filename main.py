from rich import *
from rich.console import Console
import sys

cons = Console()

cons.print("[yellow] _   _  ____  _  _  ___  ____  ____  ____  ____ [/yellow]")
cons.print("[yellow]( )_( )( ___)( \/ )/ __)(  _ \(_  _)(  _ \( ___)[/yellow]")
cons.print("[yellow] ) _ (  )__)  )  ( \__ \ )___/ _)(_  )   / )__) [/yellow]")
cons.print("[yellow](_) (_)(____)(_/\_)(___/(__)  (____)(_)\_)(____)[/yellow]")
cons.print(" ")

cons.print("[yellow][1] Пробив по номеру телефона[/yellow]")
cons.print("[yellow][2] [/yellow]")
cons.print("[yellow][3] [/yellow]")
cons.print("[yellow][4] [/yellow]")
cons.print()
cons.print("[yellow][5] Закрыть утилиту[/yellow]")

def qwest():
    request = cons.input("[yellow]>> [/yellow]")
    if request == "1":
        cons.print("[yellow]Введите номер телефона +71234567890[/yellow]")
        cons.input("[yellow]>> [/yellow]")

    if request == "5":
        sys.exit()

qwest()