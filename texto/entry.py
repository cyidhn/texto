class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    print("""
TTTTTTTTTTTTTTTTTTTTTTTEEEEEEEEEEEEEEEEEEEEEEXXXXXXX       XXXXXXXTTTTTTTTTTTTTTTTTTTTTTT     OOOOOOOOO     
T:::::::::::::::::::::TE::::::::::::::::::::EX:::::X       X:::::XT:::::::::::::::::::::T   OO:::::::::OO   
T:::::::::::::::::::::TE::::::::::::::::::::EX:::::X       X:::::XT:::::::::::::::::::::T OO:::::::::::::OO 
T:::::TT:::::::TT:::::TEE::::::EEEEEEEEE::::EX::::::X     X::::::XT:::::TT:::::::TT:::::TO:::::::OOO:::::::O
TTTTTT  T:::::T  TTTTTT  E:::::E       EEEEEEXXX:::::X   X:::::XXXTTTTTT  T:::::T  TTTTTTO::::::O   O::::::O
        T:::::T          E:::::E                X:::::X X:::::X           T:::::T        O:::::O     O:::::O
        T:::::T          E::::::EEEEEEEEEE       X:::::X:::::X            T:::::T        O:::::O     O:::::O
        T:::::T          E:::::::::::::::E        X:::::::::X             T:::::T        O:::::O     O:::::O
        T:::::T          E:::::::::::::::E        X:::::::::X             T:::::T        O:::::O     O:::::O
        T:::::T          E::::::EEEEEEEEEE       X:::::X:::::X            T:::::T        O:::::O     O:::::O
        T:::::T          E:::::E                X:::::X X:::::X           T:::::T        O:::::O     O:::::O
        T:::::T          E:::::E       EEEEEEXXX:::::X   X:::::XXX        T:::::T        O::::::O   O::::::O
      TT:::::::TT      EE::::::EEEEEEEE:::::EX::::::X     X::::::X      TT:::::::TT      O:::::::OOO:::::::O
      T:::::::::T      E::::::::::::::::::::EX:::::X       X:::::X      T:::::::::T       OO:::::::::::::OO 
      T:::::::::T      E::::::::::::::::::::EX:::::X       X:::::X      T:::::::::T         OO:::::::::OO   
      TTTTTTTTTTT      EEEEEEEEEEEEEEEEEEEEEEXXXXXXX       XXXXXXX      TTTTTTTTTTT           OOOOOOOOO     
    """)
    print(f"{bcolors.WARNING}Projet en cours de développement...{bcolors.ENDC}")
    print(f"{bcolors.UNDERLINE}By @DemangeJeremy{bcolors.ENDC}")
    print("")

if __name__ == "__main__":
    # execute only if run as a script
    main()
