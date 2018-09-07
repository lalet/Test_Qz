from functools import reduce
import argparse

#Split the string based on dot character and return the product
def findVal(str1,str2):
    str1_list = str1.split(".")
    str2_list =  str2.split(".")
    total1 = get_reduced_val(str1_list)
    total2 = get_reduced_val(str2_list)
    return total1,total2

#Function to find the product of all elements in a string
def get_reduced_val(in_list):
    return reduce(lambda x, y: int(x)*int(y), in_list)

def main():
    parser=argparse.ArgumentParser(description='Sting value comparison app')
    parser.add_argument('str1', action="store")
    parser.add_argument('str2', action="store")
    result=parser.parse_args()
    total1, total2 = findVal(result.str1,result.str2)
    print(total1,total2)
    if total1==total2:
        print("Values are equal")
    elif total1 > total2:
        print(str(total1) + "greater than" + str(total2))
    else:
        print(str(total2) + ":greater than:" + str(total1))


if __name__ == "__main__":
    main()




