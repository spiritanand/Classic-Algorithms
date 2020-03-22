from Collatz_Conjecture import CC1
from Sieve_of_Eratosthenes import SE1
from Sorting_It import Sort as S
while True:
    print("\t\t\tWelcome!!!\n"
          "\tWhich program do you want to execute\n"
          "\t\t1.Collatz_Conjecture (A cool way to reach '1')\n"
          "\t\t2.Sieve_of_Eratosthenes (An ancient and efficient way to calculate the"
          " all prime numbers up to limit n)\n"
          "\t\t3.Sorting (Sort any array of your choice)\n")
    choose = int(input("Enter the program's serial number :- "))
    if choose == 1:
        CC1.cc1()
    elif choose == 2:
        SE1.se1()
    elif choose == 3:
        while True:
            print("\t\tWhich sort do you want to perform on your array :\n"
                    "\t\t1.Bubble Sorting (A bit slow)\n"
                    "\t\t2.Merge Sorting (More efficient ,"
                    "but consumes a lot of memory)")
            sort_choose = int(input("Your input :- "))
            if sort_choose == 1:
                S.Bubble_Sorting()
                break
            elif sort_choose == 2:
                S.Merge_Sorting()
                break
            else:
                print("Please enter the correct number\n"
                                 "(Hint-Choose from 1 or 2)")
                continue
    else:
        print("Please enter the correct number\n"
                         "(Hint-Choose from 1, 2 or 3)")
        continue
    print("Hope you enjoyed your Experience and got your result\n"
          "Would you like to go again?")
    while True:
        go_choose = int(input("Enter 1.Yes or 2.No :- "))
        if go_choose == 1:
            for x in range(30):
                print("\n")
            print("Here we go again! XD")
            break
        elif go_choose == 2:
            print("\t\t\tThank You for using my program.")
            exit()
        else:
            print("Please enter the correct number\n"
                  "(Hint-Choose from 1 or 2)")
            continue
