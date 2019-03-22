import HuskLogin
import HuskShell
import HuskDBClass
import HuskTableClass

def main():
    if not prompt(): exit()     # login checking

    # Husk Shell
    cmd = input(">")
    HuskCmd(cmd)


if __name__ == "__main__":
    main()
