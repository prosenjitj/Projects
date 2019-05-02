import argparse
from OrderProcessingController import OrderProcessingController


def main():
    arg_parser = argparse.ArgumentParser(description='Process Daily Orders')
    arg_parser.add_argument('-m', '--menu', help='Path to Menu dump file', required=True)
    arg_parser.add_argument('-o', '--order', help='Path to Order dump file', required=True)
    arg_parser.add_argument('-t', '--temp', help='Path to Memory dump file', required=True)
    arg_parser.add_argument('-n', '--num', help='Number of parallel process', required=True)

    args = arg_parser.parse_args()

    OrderProcessingController(menuTxtFile=args.menu,
                    orderTxtFile=args.order,
                    tempFolder=args.temp,
                    numOfParallel=int(args.num)).dataProcessing()



if __name__ == '__main__':
    main()
