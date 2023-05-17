# CONSTANTS
RESET_CLOCK_MINUTES_THRESHOLD = 720 # MINUTES_IN_HOUR * HOURS_IN_CLOCK
MINUTES_IN_HOUR = 60

## helper function to check if an array of int is an arithmetic sequence

def isArithSequence(arr):
    if len(arr) == 1:
        return True

    diff = arr[1] - arr[0]
    curTerm = arr[0]

    for i in range(1, len(arr)):
        if curTerm + diff != arr[i]:
            return False

        # update current term
        curTerm = arr[i]

    return True

## helper function to convert minutes to 12h clock digits as an array of int

def convertMinutesTo12HourClockDigits(minutesToAdd):
    # note: hours do not have leading zeros but minutes may have leading zeros
    # and the clock starts at 12:00 by default

    hour, minutes = 12, 0
    rtnVal = []

    quotient = minutesToAdd // MINUTES_IN_HOUR

    if quotient < 12 and quotient != 0:
        hour = quotient
    else:
        quotient = quotient - (quotient // 12) * 12
        if quotient != 0:
            hour = quotient

    # remainder is minutes
    minutes = minutesToAdd % MINUTES_IN_HOUR

    # add leading zero to minutes if is less than 10
    rtnVal = [int(d) for d in str(hour)] + [0] + [int(d) for d in str(minutes)] \
                if minutes < 10 else [int(d) for d in str(hour)] + [int(d) for d in str(minutes)]
    
    return rtnVal

def main(minutesToAdd):
    numArithSequencesFormed = 0
    curTimeInDigits = []

    # note every 720 min we reset to 12:00
    if minutesToAdd > RESET_CLOCK_MINUTES_THRESHOLD:
        numResets = minutesToAdd // RESET_CLOCK_MINUTES_THRESHOLD
    
        for minutes in range(RESET_CLOCK_MINUTES_THRESHOLD):
            curTimeInDigits = convertMinutesTo12HourClockDigits(minutes)

            if isArithSequence(curTimeInDigits):
                numArithSequencesFormed += 1

        numArithSequencesFormed = numArithSequencesFormed * numResets

    minutesRemaining = minutesToAdd % RESET_CLOCK_MINUTES_THRESHOLD

    # inclusive range
    for minutes in range(minutesRemaining + 1):
        curTimeInDigits = convertMinutesTo12HourClockDigits(minutes)

        if isArithSequence(curTimeInDigits):
            numArithSequencesFormed += 1

    return numArithSequencesFormed

# get input
n = int(input())

# print result
print(main(n))
