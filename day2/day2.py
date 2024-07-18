RED = 12
GREEN = 13
BLUE = 14

def read_file(file_path:str)-> list:
    with open(file_path, 'r') as file:
        return file.readlines()

def sumValidIDs(file_path:str)-> int:
    lines = read_file(file_path)
    sumOfGameIDs = 0
    powerSet = []
    for i, line in enumerate(lines):
        line = line.split(":")[1]
        subsets = line.split(";")
        subsets[-1] = subsets[-1].strip()
        lineFlag = False
        maxRed = 0
        maxGreen = 0
        maxBlue = 0
        for subset in subsets:
            smallerSets = subset.split(",")
            for elem in smallerSets:
                elem = elem.strip()
                if "red" in elem:
                    elemRed = int(elem.split(" ")[0])
                    if elemRed > maxRed:
                        maxRed = elemRed
                    if elemRed > RED:
                        lineFlag = True
                        continue
                if "green" in elem:
                    elemGreen = int(elem.split(" ")[0])
                    if elemGreen > maxGreen:
                        maxGreen = elemGreen
                    if elemGreen > GREEN:
                        lineFlag = True
                        continue
                if "blue" in elem:
                    elemBlue = int(elem.split(" ")[0])
                    if elemBlue > maxBlue:
                        maxBlue = elemBlue
                    if elemBlue > BLUE:
                        lineFlag = True
                        continue
        
        powerSet.append(maxBlue*maxGreen*maxRed)
        if not lineFlag:
            sumOfGameIDs += i + 1
            
    return sumOfGameIDs, powerSet     
        

def sumList(powerSet: list)-> int:
    sum = 0
    for elem in powerSet:
        sum += elem
    return sum
        
        
        
        
def main():
    sumIds, powerSet = sumValidIDs("input.txt")
    print("PART 1")
    print("Sum of all valid game IDs is:", sumIds)
    
    sumPowerSet = sumList(powerSet)
    
    print("PART 2")
    print("Sum of the power of the minimum set of cubes that must have been present is :", sumPowerSet , "where power Set is : ", powerSet)
    
if __name__ == "__main__":
    main()
    