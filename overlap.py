import argparse

""" Lines can either be separate or they are overlapping.
    With the help of greater than or equal to and less than operations we can find if lines
    overlap or not.
    Say lines are [5,10] and [8,15],
    if #END_OF_FIRST_LINE >= #START_OF_SECOND_LINE and #END_OF_SECOND_LINE >= #START_OF_FIRST_LINE:
    then lines overlap """

def overlapping(r,s):
    return (int(r[1])>=int(s[0]) and int(s[1])>=int(r[0]))

def main():
    print("Sample syntax python overlap.py [15,25] [10,20]")
    parser=argparse.ArgumentParser(description='Overlapping lines')
    parser.add_argument('line1', action="store")
    parser.add_argument('line2', action="store")
    cmd_line=parser.parse_args()
    A = map(float, cmd_line.line1.strip('[]').split(','))
    B = map(float, cmd_line.line2.strip('[]').split(','))
    print("Are lines overlapping ?")
    print(overlapping(A,B))

if __name__ == "__main__":
    main()
