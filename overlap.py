""" Lines can either be separate or they are overlapping.
    With the help of greater than or equal to and less than operations we can find if lines
    overlap or not.
    Say lines are [5,10] and [8,15],
    if #END_OF_FIRST_LINE >= #START_OF_SECOND_LINE and #END_OF_SECOND_LINE >= #START_OF_FIRST_LINE:
    then lines overlap """

def overlapping(r,s):
    return (r[1]>=s[0] and s[1]>=r[0])

def main():
    print("Are lines overlapping ? ")
    print(overlapping([15,25],[10,20]))

if __name__ == "__main__":
    main()
