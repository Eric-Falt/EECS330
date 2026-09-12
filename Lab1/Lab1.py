def main():
    while True:
        
        # gets which task to be caculated by the user 
        whichTask = input("""Enter the specified number for the wanted task:\n
                          0 for task1A
                          1 for task1B
                          2 for task2
                          3 to exit
                          """)
        
        # 3 indicates the end of the program 
        if whichTask == 3:
            break
        
        # gets the array from the user 
        inputArr = input("Enter the unsorted array serperated by spaces: ").split()
        
        # calls the according function based on user input 
        match whichTask:
            case 0:
                print(taskOneA(inputArr))
            
            case 1: 
                print(taskOneB(inputArr))
            
            case 2: 
                print(taskTwo(inputArr))

# implements insertion sort with a second "sorted array"
def taskOneA(inputArr):
    
    # holds the sorted array 
    sortedArr = inputArr[0]
    
    # itterates through the input array, placing it where it should go 
    for number in range(1, len(inputArr)):
        for i, key in range(len(sortedArr)):
            if number >= key: 
                sortedArr[i + 1] = number
                break
            elif i == len(sortedArr) - 1:
                sortedArr[i] = number
    
    # returns the sorted array         
    return sortedArr

#implements insertion sort by shifting values in the input array 
def taskOneB(inputArr):
    
    sortedIndex = 0
    
    for value in range(1, len(inputArr)):
        for key in range(0, sortedIndex + 1):
            
    
    # returns the newly sorted input array 
    return inputArr
def taskTwo(inputArr):
    
    