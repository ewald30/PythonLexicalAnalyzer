from HashTable import HashTable
from Scanner import Scanner

hashTable = HashTable()
pif = []

'''
    Please be sure the leave only one of the execute instructions uncommented
    HashTable and Pif are shared by the program!!!
'''

scanner = Scanner(hashTable, pif)
# scanner.execute("files/ex1.txt", 'files/PIF1.out', 'files/ST1.out')
# scanner.execute("files/ex2.txt", 'files/PIF2.out', 'files/ST2.out')
#scanner.execute("files/ex3.txt", 'files/PIF3.out', 'files/ST3.out')
scanner.execute("files/ex1err.txt", 'files/PIF_Err.out', 'files/ST_Err.out')
