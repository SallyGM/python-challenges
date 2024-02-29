import sys
# <summary >
# During your time at mountain warheouse you will often have to go bug fix your own ( and other peoples!) code.
# The following method should return the smallest value in the given array. If the array is empty then it should return 0.
# However, the last dev has made some bugs.  It seems it only works when the number "1" is the smallest value in the array - for all other cases the method fails
# 4 bugs have been identified within the code.
# See if you can find them all!
# </summary >
# <param name = "numbers" > </param >
# <returns > </returns >

def ReturnSmallestValueInArray(numbers):
    # min should be the minimum number in the array
    #min = -sys.maxsize-1

    # return when the array is empty
    if len(numbers) == 0: 
        return 0
    else:
        for i in range(len(numbers)):
            # gets the first number as the minimum instead
            if i == 0:
                min = numbers[i]
            # wrong comparison
            elif min > numbers[i]:
                min = numbers[i]
    # return min and not 1 for every single  case
    return min
