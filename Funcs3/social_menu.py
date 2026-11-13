from Helper import *
from Helper.Common.utils import *

def link_start(link):
    os.system(f"start {link}")
    print("Opend Link!")
    time.sleep(1)
    social_menu()


def social_menu():
    new_title("SALO CYBR Socials")
    print(f"{Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}] SALO CYBR Discord")
    print(f"[{Fore.MAGENTA}2{Fore.RESET}] SALO CYBR")
    print(f"[{Fore.MAGENTA}3{Fore.RESET}] MultiTool Github")
    print(f"[{Fore.MAGENTA}4{Fore.RESET}] Youtube")
    print(f"[{Fore.MAGENTA}0{Fore.RESET}] Leave")
    choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Choice: ")
    if choice == "1":
        link_start("https://discord.gg/QxH952Rwn7")
    elif choice == "2":
        link_start("https://SALO CYBR")
    elif choice == "3":
        link_start("https://SALO CYBR")
    elif choice == "4":
        link_start("https://www.youtube.com/channel/UCDCi8zE2ReRp5cg2GBtJ2Pw")
    elif choice == "0":
        quit1()
    else:
        print("invalid choice")
        social_menu()