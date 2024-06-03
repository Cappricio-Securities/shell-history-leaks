#!/usr/bin/env python

"""
 * shell-history-leaks
 * shell-history-leaks Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */


"""
import getpass
username = getpass.getuser()


def display_help():
    help_banner = f"""

👋 Hey \033[96m{username}
   \033[92m                                                                          v1.0
         __         ____      __    _      __                         __           __
   _____/ /_  ___  / / /     / /_  (_)____/ /_____  _______  __      / /__  ____ _/ /_______
  / ___/ __ \/ _ \/ / /_____/ __ \/ / ___/ __/ __ \/ ___/ / / /_____/ / _ \/ __ `/ //_/ ___/
 (__  ) / / /  __/ / /_____/ / / / (__  ) /_/ /_/ / /  / /_/ /_____/ /  __/ /_/ / ,< (__  )
/____/_/ /_/\___/_/_/     /_/ /_/_/____/\__/\____/_/   \__, /     /_/\___/\__,_/_/|_/____/
                                                      /____/                                                                                     
                              \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1mshell-history-leaks : Bug scanner for WebPentesters and Bugbounty Hunters

\x1b[31;1m$ \033[92mshell-history-leaks\033[0m [option]

Usage: \033[92mshell-history-leaks\033[0m [options]

Options:
  -u, --url     URL to scan                                shell-history-leaks -u https://target.com
  -i, --input   <filename> Read input from txt             shell-history-leaks -i target.txt
  -o, --output  <filename> Write output in txt file        shell-history-leaks -i target.txt -o output.txt
  -c, --chatid  Creating Telegram Notification             shell-history-leaks --chatid yourid
  -b, --blog    To Read about shell-history-leaks Bug      shell-history-leaks -b
  -h, --help    Help Menu
    """
    print(help_banner)


def banner():
    help_banner = f"""
    \033[94m
👋 Hey \033[96m{username}
      \033[92m                                                                      v1.0
         __         ____      __    _      __                         __           __
   _____/ /_  ___  / / /     / /_  (_)____/ /_____  _______  __      / /__  ____ _/ /_______
  / ___/ __ \/ _ \/ / /_____/ __ \/ / ___/ __/ __ \/ ___/ / / /_____/ / _ \/ __ `/ //_/ ___/
 (__  ) / / /  __/ / /_____/ / / / (__  ) /_/ /_/ / /  / /_/ /_____/ /  __/ /_/ / ,< (__  )
/____/_/ /_/\___/_/_/     /_/ /_/_/____/\__/\____/_/   \__, /     /_/\___/\__,_/_/|_/____/
                                                      /____/
                                                      
                              \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1mshell-history-leaks : Bug scanner for WebPentesters and Bugbounty Hunters

\033[0m"""
    print(help_banner)
