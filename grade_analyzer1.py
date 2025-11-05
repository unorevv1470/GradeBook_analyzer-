def func():
    dict = {}
    while(True):
        name = input("Enter the name or (done) for ending : ")
        if name == "done":
            break
        marks = int(input("Enter the marks : "))
        dict[name] = marks
    sum = 0 
    values = []
    for key , value in dict.items():
        sum+= value
        values.append(value)
    values.sort()
    average = sum/len(dict)
    lowest = values[0]
    highest = values[len(values) - 1]
    median = values[(len(values) - 1)//2]
    heighest_name  = ""
    lowest_name = ""
    for key , value in dict.items():
        if highest == value : 
            heighest_name = key
        elif lowest == value : 
            lowest_name = key

    print("AVERAGE : " , average)
    print("MEDIAN : " , median)
    print("HIGHEST : " , heighest_name , f"({highest})")
    print("LOWEST  : " ,lowest_name , f"({lowest_name})")
    passed = 0 
    failed = 0
    print("Name \t Marks \t Grade")
    print("------------------------")
    for key , value in dict.items():
        print(f"{key} \t {value} \t {"Pass" if value > 80 else "Fail"}")
        if value > 80 : 
            passed+=1
        else :
            failed+=1
    print(f"passed:{passed} failed:{failed}")
    continues = input("do you want to continue ? y or n")
    if continues == 'y' :
        func()
    else :
        return 
func()