#This program is running on python 3.5.0
def readData(fileName): #This converts the data from the .txt file into a list in python, doing this should speed up the process
    myFile = open(fileName,'r') #opens the .txt file and enters read only more
    myList = [] #list used to store contents of .txt file
    for eachLine in myFile: #loop for each line in the list
        depList = eachLine.split()  # splits the contents of the list
        department = depList[0] # stores the department as 'department'
        good = depList[1] # stores the value of good reviews
        fair = depList[2]   #stores the value of fair reviews
        poor = depList[3]   #stores the value of poor reviews
        header = [department,[good,fair,poor]]  #header used to assign format of list
        myList.append(header) #adds the line of content from the .txt file to list
    myFile.close # close .txt file
    return myList #returns list created

def menu(): #prints the menu for the different functions available to user
    print("""   0. Quit
    1. Display menu
    2. Display all survey information
    3. Search department, display number of participants and average result
    4. Display highest customer satisfaction
    5. Display lowest customer satisfaction
    6. Display departments with over 50% voted fair or poor
    7. Display departments with 60% or more voted good
    8. Display total participant and average value """)

def displayData(myList): #this program displays all data in the list
    for departments in myList: #loop for all items in the list then prints all information on screen
        print ('Department:',departments[0],'    Good:',departments[1][0],'  Fair:',departments[1][1],'  poor:', departments[1][2])
         
def calculateTotal(myList): #fucntion for calculating total participants
    total = 0   #total vairble used for total
    for departments in myList:  #creates loops for all departments in list
        for result in range(3): # loop for each results in survey
            total+= int(departments[1][result - 1]) #adds the results of survey to total
    return total #returns total

def calculateAverage(myList):  # calculate average response. formula: value of responce(1) * weight(1) + value of responce(2) * weight(2).../total
    good = 0
    fair = 0
    poor = 0
    for departments in myList: # loop for all departments in the list
        good += int(departments[1][0]) #adds the value of good revies to total good review
        fair += int(departments[1][1])  #adds the value of fair reviews to total fair reviews
        poor += int(departments[1][2])  #adds the value of poor reviews to total poor reviews
    average = float((good * 3) + (fair * 2) + (poor))/ int(calculateTotal(myList)) #calculates average reviews
    return average #returns average value

def calculateTotalByDepartment(myList,depName): #calculates total review participants based on given department
    valid =False #boolean varibale used to check is department exist
    total = 0
    for departments in myList: #loop of each department in the list
        if departments[0] == depName: #if the searched department is identival to department on list
            valid = True #turns valid boolean into true
            for result in range(3):
                total += int(departments[1][result - 1]) #adds each survey result to total
    if valid: # checks if department name entered is valid, if not error message is returned, if valid total is returned
        return total
    else:
        return 'error, department not found(check for gramatical/spelling errors)'

def calculateAverageByDepartment(myList,depName): #calculates average for a specific department entered
    valid = False
    for departments in myList:
        if departments[0] == depName: #if the searched department is identival to department on list
            valid = True
            average = float(int(departments[1][0])* 3+ int (departments[1][1])* 2+ int(departments[1][2]))/ int(calculateTotalByDepartment(myList,depName)) #calculates average using formula:  value of responce(1) * weight(1) + value of responce(2) * weight(2).../total
    if valid: #checks if department name entered is valid, if not error message is returned, if valid average is returned
        return average
    else:
        return 'Error calculating average(department not found)'

def displayHighest(myList): # finds department with the highest user review
    highestValue = -1 # this is a imposible value to guarantee a highest reviewed department is found
    for departments in myList:
        currentValue = calculateAverageByDepartment(myList,departments[0]) #calculates and sets average for the department using calculateAverageByDepartment function
        if float(currentValue) > highestValue: # if the current average value is greater than highest listed average value
            highestValue = currentValue #sets the highestvalue to current value of department
            highestDepartment = departments[0] #saves department name
    return highestDepartment #returns department name with highest reiviewed

def displayLowest(myList): # finds worst performing deparment with lowest reviews
    lowestValue = 4# this is a imposible value to guarantee a lowesrt reviewed department is found
    for departments in myList:
        currentValue = calculateAverageByDepartment(myList,departments[0]) #calculates and sets average for the department using calculateAverageByDepartment function
        if float(currentValue) < lowestValue: # if current value is lower than lowest recorded value
            lowestValue = currentValue #sets lowest value to curretn value
            lowestDepartment = departments[0] #stores name of department with lowest average review
    return lowestDepartment #returns department name

def displayPoorPerformance(myList): #this creates a list of departments with poor or fair reviews of greater than 50%
    poorPerformance = [] #list for all department poor and fair reviews greater than 50%
    for departments in myList:
        percentage = float(int(departments[1][1]) + int(departments[1][2]))/int(calculateTotalByDepartment(myList,departments[0])) #calculates percentage of reviews that are poor and fair
        if float(percentage) > .5: # if percentage is greater han 50%
            poorPerformance.append(departments[0]) #adds department to poor performance department list
    return poorPerformance #returns poor performance list

def displayExcellentPerformance(myList): # creates a list of best performing department based on customer reviews
    excellentPerformance = [] #list for best performing departments
    for departments in myList: 
        percentage = float(float(departments[1][0])/calculateTotalByDepartment(myList,departments[0])) #calculates the average based on no. good review/total participant for department
        if float(percentage) > .6: #if percentage of good reviews is greater than 60%
            excellentPerformance.append(departments[0]) #adds department to excellent performance list
    return excellentPerformance #returns excellent performance list


surveyList = readData("survey.txt") #creates a list using survey.txt data
print(menu()) #prints menu on launch for the benifit of the consumer
choice = 1
while int(choice) != 0: #ends loop when user enters 0
    choice = int(input("Enter your choice?(Enter the number corosponding the option)")) #allows the user to select which functions they want to access
    if choice == 1: # if users chooses 1, opens menu
        print(menu())
    elif choice == 2: #if user chooces 2 displayData function runs
        displayData(surveyList)
    elif choice ==3: #if user chooces 3 calculateTotalByDepartment function is run
        search = input("Enter the department?") #note, this program runs on python 3.5.0, if marking using 2.7.10 replace input into raw_input
        print ('total participants:',calculateTotalByDepartment(surveyList,search.capitalize()),".Average result:", calculateAverageByDepartment(surveyList,search.capitalize()))
    elif choice ==4: #if choice = 4 runs displayHighest function
        print(displayHighest(surveyList))
    elif choice ==5: #if choice = 5 runs displayLowest function
        print(displayLowest(surveyList)) 
    elif choice ==6: #if choice = 6 it runs  displaypoorperformance function
        print (displayPoorPerformance(surveyList))
    elif choice ==7: #if choice = 7 runs displayexcellentperformance function
        print (displayExcellentPerformance(surveyList))
    elif choice ==8: #if 8 is chosen then it runs the calculatetotal and calculateaverage then displays the message
        print ('total participants:', calculateTotal(surveyList),'. Avegrage:', calculateAverage(surveyList))
    elif choice == 0:
        ...
    else: #this is a error message if the user enters a invalid value
        print("Choice is invalid, try again")
print('Thank you for using our system,goodbye') #this is a goodbye message when the program is exited
