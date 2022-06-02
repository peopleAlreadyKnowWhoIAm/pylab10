from transistor import Transistor, TransistorType

from transistorlist import TransistorList


def main():
    """main function of the program
    """
    tr_list = TransistorList()
    tr_list.push_back(Transistor(TransistorType.NPN, "2b2222", 30, 2))
    tr_list.push_back(Transistor(TransistorType.PNP, "2da1201y", 120, 0.8))
    tr_list.push_back(Transistor(TransistorType.NPN, "2DC4617SQ", 50, 0.15))
    tr_list.push_back(Transistor(TransistorType.PNP, "AC857BQ", 45, 0.1))
    tr_list.push_back(Transistor(TransistorType.NPN, "DXT697BK", 180, 0.5))
    tr_list.insert(Transistor(TransistorType.PNP, "DXT751Q", 60, 3), 0)
    print(tr_list)
    tr_list.sort_by_current()
    print(tr_list)

if __name__ == '__main__':
    main()
