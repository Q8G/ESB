from colorama import init, Fore; import os
try:
    os.system("title Rwshny EXE Size Booster")
except Exception:
  pass
print(Fore.LIGHTGREEN_EX + r"""
      
      
      
                                ____               _                   _____ ____  ____  
                               |  _ \__      _____| |__  _ __  _   _  | ____/ ___|| __ ) 
                               | |_) \ \ /\ / / __| '_ \| '_ \| | | | |  _| \___ \|  _ \ 
                               |  _ < \ V  V /\__ \ | | | | | | |_| | | |___ ___) | |_) |
                               |_| \_\ \_/\_/ |___/_| |_|_| |_|\__, | |_____|____/|____/ 
                                                               |___/  
                                                            
                                                                               
      """)
try:
    init()
    while True:
        EXE = input(Fore.YELLOW + "                               [?] Exe Name (With .exe): " + Fore.RESET)
        if os.path.exists(EXE):
            break
        else:
            print(Fore.RED + "                               [!] File Not Found!" + Fore.RESET)
    while True:
        try:
            Size = int(input(Fore.YELLOW + "                               [?] How much do you want it to increase in size in MB?: " + Fore.RESET))
            if Size > 0:
                break
            else:
                print(Fore.RED + "                               [!] Please enter a positive number.")
        except ValueError:
            print(Fore.RED + "                               [!] Please enter a valid number.")
    size = Size * 1000
    sizeMB = 1024 * size
    with open(EXE, 'ab') as f:
        d = b'\0' * sizeMB
        f.write(d)
    print(Fore.LIGHTGREEN_EX + "                               [+] Done" + Fore.RESET)
except Exception:
    print(Fore.RED + "                               [!] An error occurred" + Fore.RESET)
