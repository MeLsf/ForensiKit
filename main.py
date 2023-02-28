import argparse
import utilities





def main():
    description = """
    Collect live forensics artifacts using open-source tools.
    ______                             _  _  __ _  _   
    |  ____|                           (_)| |/ /(_)| |  
    | |__  ___   _ __  ___  _ __   ___  _ | ' /  _ | |_ 
    |  __|/ _ \ | '__|/ _ \| '_ \ / __|| ||  <  | || __|
    | |  | (_) || |  |  __/| | | |\__ \| || . \ | || |_ 
    |_|   \___/ |_|   \___||_| |_||___/|_||_|\_\|_| \__|    
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-l', '--light', action='store_true', help='Collect light forensic artifacts')
    parser.add_argument('-m', '--memory', action='store_true', help='Collect memory forensic artifacts')
    parser.add_argument('-s', '--sensitive', action='store_true', help='Collect sensitive forensic artifacts')
    parser.add_argument('-u', '--utilities', action='store_true', help='Collect utilities forensic artifacts')
    parser.add_argument('-a', '--avz', action='store_true', help='Collect AVZ forensic artifacts')

    args = parser.parse_args()

    if not any(vars(args).values()):
        utilities.nirsoft_collector()
        return

    print('')
    if args.light:
        print('  * Light forensic artifacts')
    if args.memory:
        print('  * Memory forensic artifacts')
    if args.sensitive:
        print('  * Sensitive forensic artifacts')
    if args.utilities:
        utilities.nirsoft_collector()
    if args.avz:
        print('  * AVZ forensic artifacts')


if __name__ == '__main__':
    main()
