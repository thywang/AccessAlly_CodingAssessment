# thought process: greedy approach
# strategy 1: prioritize giving blood to the most restricted patients first
# strategy 2: prioritize taking the blood identical to theirs first

# CONSTANTS - blood type mappings to indexes
O_NEG = 0
O_POS = 1
A_NEG = 2
A_POS = 3
B_NEG = 4
B_POS = 5
AB_NEG = 6
AB_POS = 7

def main(unitsAvailable, unitsNeeded):
    ## helper function to find the maximum amount of blood of type t1 that can be given to patients needing type t2
    
    def getUnits(t1, t2):
        # we can only give as much blood of t1 as we have, so take the min
        units = min(unitsAvailable[t1], unitsNeeded[t2])

        # update amount of blood available and needed
        unitsAvailable[t1] = unitsAvailable[t1] - units
        unitsNeeded[t2] = unitsNeeded[t2] - units

        return units

    numReceivedBlood = 0

    # O- (take only O-)
    numReceivedBlood = getUnits(O_NEG, O_NEG)
    # O+ (take as much O+, then O-)
    numReceivedBlood = numReceivedBlood + getUnits(O_POS, O_POS) + getUnits(O_NEG, O_POS)
    # A- (take as much A-, then O-)
    numReceivedBlood = numReceivedBlood + getUnits(A_NEG, A_NEG) + getUnits(O_NEG, A_NEG)
    # A+ (take as much A+, then A-, then O+, then O-)
    numReceivedBlood = numReceivedBlood + getUnits(A_POS, A_POS) + getUnits(A_NEG, A_POS) + getUnits(O_POS, A_POS) + getUnits(O_NEG, A_POS)
    # B- (take as much B-, then O-)
    numReceivedBlood = numReceivedBlood + getUnits(B_NEG, B_NEG) + getUnits(O_NEG, B_NEG)
    # B+ (take as much B+, then B-, then O+, then O-)
    numReceivedBlood = numReceivedBlood + getUnits(B_POS, B_POS) + getUnits(B_NEG, B_POS) + getUnits(O_POS, B_POS) + getUnits(O_NEG, B_POS)
    # AB- (take as much AB-, then A-, then B-, then O-)
    numReceivedBlood = numReceivedBlood + getUnits(AB_NEG, AB_NEG) + getUnits(B_NEG, AB_NEG) + getUnits(A_NEG, AB_NEG) + getUnits(O_NEG, AB_NEG)
    # AB+ (take as much AB+, then AB-, then A+, then A-, then B+, then B-, then O+, then O-)
    numReceivedBlood = numReceivedBlood + getUnits(AB_POS, AB_POS) + getUnits(AB_NEG, AB_POS) + getUnits(A_POS, AB_POS) + getUnits(A_NEG, AB_POS) + getUnits(B_POS, AB_POS) + getUnits(B_NEG, AB_POS) + getUnits(O_NEG, AB_POS) + getUnits(O_POS, AB_POS)

    return numReceivedBlood

# get input
bloodAvailable = (input().split())
bloodNeeded = (input().split())

# convert to integers
for type in range(8):
    bloodAvailable[type] = int(bloodAvailable[type])
    bloodNeeded[type] = int(bloodNeeded[type])

# print result
print(main(bloodAvailable, bloodNeeded))