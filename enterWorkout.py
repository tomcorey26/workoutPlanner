def enterWorkout():
    i=0
    woutList =[]

    #while all workouts arent entered
    while i == 0:
        workout = input("Input exercise , enter done when all workouts are recorded")
        if (workout == "done"):
            i = 1
        else:
            woutList.append(workout)

    return woutList

def printFormat(workoutlist):
    for i in range(len(workoutlist)):
        print(workoutlist[i] + '\n')
    

def main():
    workoutList = enterWorkout()
    printFormat(workoutList)
