#!/usr/bin/env python3
# ╔══════════════════════════════════════════════════════════════════════╗
# ║  SALO CYBR — MultiTool                                               ║
# ║  Fresh build, written from scratch by SALO                           ║
# ║  • Data-driven menus (no copy-pasted menu blocks)                    ║
# ║  • Tool loop instead of recursion (no stack growth)                  ║
# ║  • Every tool runs in its own try/except — a crash never kills the   ║
# ║    panel, you just get dropped back into the menu                    ║
# ║  • DDoS Stress Test loads independently of the Helper import chain   ║
# ╚══════════════════════════════════════════════════════════════════════╝

import os
import sys
import time
import importlib.util

# ── bootstrap: run from this folder no matter how the file is launched ──────
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
if os.getcwd() != ROOT:
    os.chdir(ROOT)

# ── UTF-8 console so the banner never crashes on cp1252 ────────────────────
for _stream in (sys.stdout, sys.stderr):
    try:
        if _stream.encoding and _stream.encoding.lower() != "utf-8":
            _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# ── Helper chain ────────────────────────────────────────────────────────────
try:
    from Helper import *                      # all tool functions
    from Helper.Common.utils import *         # Fore, lc, new_title, get_tokens...
except ModuleNotFoundError as e:
    # Auto-heal: install missing deps into the running interpreter, then relaunch
    missing = getattr(e, "name", "?")
    print(f"[SALO] Missing dependency '{missing}' — installing requirements.txt (one-time)...")
    import subprocess
    r = subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(f"[SALO] pip install failed:\n{(r.stderr or r.stdout).strip()[-400:]}")
        try:
            input("Press Enter to exit...")
        except EOFError:
            pass
        sys.exit(1)
    # clean restart so module-level star-imports succeed
    os.execv(sys.executable, [sys.executable, os.path.abspath(__file__)])
except Exception as e:
    print(f"[SALO] Helper failed to load: {e}")
    try:
        input("Press Enter to exit...")
    except EOFError:
        pass
    sys.exit(1)

# ── DDoS module: independent loader, falls back to direct file load ────────
def _load_ddos():
    try:
        from Helper.Funcs.ddos import ddos_stress as _fn
        return _fn, "package"
    except Exception:
        pass
    path = os.path.join(ROOT, "Helper", "Funcs", "ddos.py")
    try:
        spec = importlib.util.spec_from_file_location("salocybr_ddos", path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules["salocybr_ddos"] = mod
        spec.loader.exec_module(mod)
        return mod.ddos_stress, "direct-file"
    except Exception:
        return None, "failed"

ddos_stress, ddos_load_mode = _load_ddos()

def ddos_unavailable():
    print(f"{Fore.LIGHTRED_EX}[SALO] DDoS module could not load — check Helper/Funcs/ddos.py{Fore.RESET}")
    time.sleep(2)

# ── theme ───────────────────────────────────────────────────────────────────
THEMES = {
    "1":  ("Light Magenta", Fore.LIGHTMAGENTA_EX),
    "2":  ("Light Blue",    Fore.LIGHTBLUE_EX),
    "3":  ("Light Red",     Fore.LIGHTRED_EX),
    "4":  ("Light Green",   Fore.LIGHTGREEN_EX),
    "5":  ("Light Cyan",    Fore.LIGHTCYAN_EX),
    "6":  ("Light Yellow",  Fore.LIGHTYELLOW_EX),
    "7":  ("Magenta",       Fore.MAGENTA),
    "8":  ("Blue",          Fore.BLUE),
    "9":  ("Red",           Fore.RED),
    "10": ("Green",         Fore.GREEN),
    "11": ("Cyan",          Fore.CYAN),
    "12": ("Yellow",        Fore.YELLOW),
}
color = Fore.LIGHTMAGENTA_EX

# ── menu data ───────────────────────────────────────────────────────────────
# (code, label, function) — bindings fixed where the original had wrong ones
PAGE1 = [
    ("1",  "Token Formater",        formater),
    ("2",  "Token Checker",         Token_checker),
    ("3",  "Token Sorter",          sort_tokens),
    ("4",  "Token Spammer",         token_spammer),
    ("5",  "Token Guild Checker",   check_tokens_guild),
    ("6",  "Token Guild Leaver",    token_leave_server),
    ("7",  "Remove Doubles",        remove_duplicates),
    ("8",  "Proxy Scraper",         Proxy_scraper),
    ("9",  "Proxy Checker",         check_proxys),
    ("10", "Webhook Tool",          Webhook_tool),
    ("11", "Faker Tool",            main_faker),
    ("12", "Obfuscator",            obfuscate),
    ("13", "Clear Output Folder",   clear_output),
    ("14", "Clear Input Folder",    clear_input),
    ("15", "Token Mail Verifier",   TokenMailverifier),
    ("16", "Token Pass Changer",    pass_changer),
    ("17", "Token Onliner",         online_tokens),
    ("18", "Token Status Rotator",  status_changer),
    ("19", "Token Nuker",           Token_nuker),
    ("20", "Token Editor",          token_editor),
    ("21", "Nitro Gift Checker",    check_codes),
    ("43", "DDoS Stress Test",      ddos_stress if ddos_stress else ddos_unavailable),
    ("44", "Port Scanner",          port_scanner),
    ("45", "MAC Changer",           mac_changer),
    ("46", "Botnet Lab C2",         lab_controller),
    ("47", "Lab Bot Client",        lab_bot),
    ("48", "Whois Lookup",          whois_lookup),
    ("49", "Local Net Scanner",     network_scanner),
    ("50", "WiFi Password Dump",    wifi_dump),
    ("51", "System Recon",          system_recon),
    ("52", "Username Tracker",      username_tracker),
    ("53", "Python Obfuscator",     python_obfuscator),
    ("54", "Email Lookup",          email_lookup),
    ("55", "Discord Bot Invite",    bot_invite),
    ("56", "HTTP Stress Lab",       http_stress_lab),
    ("57", "Search Database",       search_database),
    ("58", "Zip/Rar Crack",         zip_crack),
    ("59", "Instagram Lookup",      insta_lookup),
    ("60", "Steam Lookup",          steam_lookup),
]

PAGE2 = [
    ("22", "Discord Nuker",             Discord_nuker),
    ("23", "Get Own Token",             get_own_token),
    ("24", "Token Login",               token_login),
    ("25", "PC Cleaner",                Cleaner),
    ("26", "Youtube Downloader",        youtube_converter),
    ("27", "Id To Token",               id__token),
    ("28", "Avatar Scraper",            scrape_Avatars),
    ("29", "Gen Test Token",            gen_token),
    ("30", "Get Token Info",            fetch_user_details),
    ("31", "Simple Ip Lookup",          ip_lookup),
    ("32", "Simple Ip Grabber",         make_ip_grabber),
    ("33", "Serial Changer",            serial_changer),
    ("34", "Serial Checker",            check_serials),
    ("35", "Change Theme",              None),          # handled in-run (needs closure)
    ("36", "Token Watermarker",         token_wartermarker),
    ("37", "Token Huminazor",           procces_hm),
    ("38", "Token Payment Checker",     check_payments),
    ("39", "Token Leave Groups",        leave_groups),
    ("40", "Token Guild Count Checker", guild_count),
    ("41", "Token Message Everywhere",  meessage_everywhere_spam),
    ("42", "Discord Message Logger",    message_logger),
    ("43", "DDoS Stress Test",          ddos_stress if ddos_stress else ddos_unavailable),
]

PAGES = {1: PAGE1, 2: PAGE2}
SPECIALS = {
    "x1": ("Back To Page 1", None),
    "x2": ("Next Page",      None),
    "x3": ("Socials",        social_menu),
}

# ── rendering ───────────────────────────────────────────────────────────────
BANNER = f"""{color}
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║     S  A  L  O     C  Y  B  R      —      M u l t i T o o l              ║
║                     fresh build  •  43 tools  •  page {{pg}}                  ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝{Fore.RESET}"""


# category grouping for the new UI — codes stay identical, only the layout changed
CATEGORY_ORDER = ["TOKEN & DISCORD", "NETWORK", "SYSTEM & UTILS"]
CATEGORIES = {
    "TOKEN & DISCORD": ["1", "2", "3", "4", "5", "6", "7", "15", "16", "17", "18", "19", "20", "21",
                        "22", "23", "24", "27", "28", "29", "30", "36", "37", "38", "39", "40", "41", "42", "55"],
    "NETWORK":         ["8", "9", "10", "31", "32", "43", "44", "46", "47", "48", "49", "52", "54", "56", "59", "60"],
    "SYSTEM & UTILS":  ["11", "12", "13", "14", "25", "26", "33", "34", "35", "45", "50", "51", "53", "57", "58"],
}


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def _tool_lookup():
    """code -> (label, fn) from both pages combined."""
    table = {}
    for items in PAGES.values():
        for code, label, fn in items:
            table[code] = (label, fn)
    return table


def render_menu(page):
    """Grouped, boxed menu layout — totally different look, same codes."""
    print(BANNER.replace("{pg}", str(page)))
    table = _tool_lookup()
    for section in CATEGORY_ORDER:
        codes = CATEGORIES[section]
        print(f"{color}┌─{Fore.RESET}[ {Fore.LIGHTWHITE_EX}{section}{Fore.RESET} ]{color}"
              + "─" * max(2, 58 - len(section)) + f"┐{Fore.RESET}")
        for i in range(0, len(codes), 2):
            left = codes[i]
            right = codes[i + 1] if i + 1 < len(codes) else None
            def _cell(code):
                if code is None:
                    return " " * 37
                label, _fn = table[code]
                return (f"{color}│{Fore.RESET} {color}<<{Fore.RESET}{code:>3}{color}>>{Fore.RESET} "
                        f"{label:<26} ")
            print(f"{color}│{Fore.RESET}" + _cell(left) + (_cell(right) if right else "") + f"{color}│{Fore.RESET}")
        print(f"{color}└" + "─" * 74 + f"┘{Fore.RESET}")
    print()
    print(" " * 4 + f"{color}<<{Fore.RESET}x1{color}>>{Fore.RESET} Page 1   "
                      f"{color}<<{Fore.RESET}x2{color}>>{Fore.RESET} Page 2   "
                      f"{color}<<{Fore.RESET}x3{color}>>{Fore.RESET} Socials   "
                      f"{Fore.LIGHTBLACK_EX}type the code of any tool — it works from every page{Fore.RESET}")


def change_theme():
    global color
    clear()
    print(f"{color}{BANNER}{Fore.RESET}")
    for code, (name, _f) in THEMES.items():
        print(f"    {color}<<{Fore.RESET}{code:<3}{color}>>{Fore.RESET} [{Fore.RESET}{name}{Fore.RESET}]")
    choice = input(f"\n{Fore.RESET}[{color}>{Fore.RESET}] Theme: ").strip()
    theme = THEMES.get(choice)
    if theme:
        color = theme[1]
        print(f"{Fore.LIGHTGREEN_EX}Theme set to {theme[0]}.{Fore.RESET}")
        time.sleep(0.6)
    else:
        print("invalid choice")
        time.sleep(1)


def run_tool(fn):
    """Wrap every tool call — a crash inside a tool returns to the menu."""
    try:
        fn()
    except KeyboardInterrupt:
        print(f"\n{Fore.LIGHTCYAN_EX}[SALO] Tool interrupted — back to menu.{Fore.RESET}")
        time.sleep(0.8)
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}[SALO] Tool error: {e}{Fore.RESET}")
        time.sleep(1.5)


def main_loop():
    page = 1
    while True:
        clear()
        new_title(f"SALO CYBR │ Page {page}")
        render_menu(page)
        try:
            choice = input(f"{color}┌{Fore.RESET}[{Fore.LIGHTWHITE_EX}salo@cybr{Fore.RESET}{color}]{Fore.RESET}─[{Fore.LIGHTBLACK_EX}page {page}{Fore.LIGHTBLACK_EX}]{color}┐{Fore.RESET}\n  └─$ ").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n{Fore.LIGHTCYAN_EX}[SALO] Closed.{Fore.RESET}")
            break

        # page specials
        if choice == "x1":
            page = 1
            continue
        if choice == "x2":
            page = 2
            continue
        if choice == "x3":
            run_tool(social_menu)
            continue

        # find tool on current page
        match = next((item for item in PAGES[page] if item[0] == choice), None)
        if not match:
            # also search the other page so a right number always works
            other = 1 if page == 2 else 2
            match = next((item for item in PAGES[other] if item[0] == choice), None)
            if match:
                print(f"{Fore.LIGHTYELLOW_EX}[SALO] That tool is on Page {other} — switching...{Fore.RESET}")
                time.sleep(0.6)
                page = other

        if not match:
            print("invalid choice")
            time.sleep(0.8)
            continue

        code, label, fn = match
        if label == "Change Theme":
            change_theme()
        elif fn is not None:
            run_tool(fn)
        else:
            print("invalid choice")
            time.sleep(0.8)


# ── entry point ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    try:
        StartupTool()
        ddos_line = (f"{Fore.LIGHTCYAN_EX}[SALO] DDoS module loaded ({ddos_load_mode}) — menu code 43{Fore.RESET}"
                     if ddos_stress else
                     f"{Fore.LIGHTRED_EX}[SALO] DDoS module FAILED to load{Fore.RESET}")
        os.system("mode con cols=140 lines=32")
        clear()
        print(ddos_line)
        time.sleep(1.2)
        main_loop()
    except KeyboardInterrupt:
        clear()
        print(f"{Fore.LIGHTCYAN_EX}[SALO] Closed. Come back soon.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}[SALO] Fatal: {e}{Fore.RESET}")
    finally:
        try:
            input(f"{Fore.RESET}Press {Fore.LIGHTBLACK_EX}[Enter]{Fore.RESET} to exit...")
        except EOFError:
            pass
