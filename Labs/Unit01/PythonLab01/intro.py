def count_duplicate(arr):
    duplictes = 0
    for i in range(0, arr.length):
        for j in range(i + 1, arr.length):
            if arr[i] == arr[j]:
                duplictes += 1
    return duplictes

def famous_people():
    person1 = input("Famous Person: ")
    person2 = input("Famous Person: ")
    person3 = input("Famous Person: ")
    person4 = input("Famous Person: ")
    lst = [person1, person2, person3, person4]
    lst.pop
    lst.pop(1)
    lst.pop(person1)
    lst.pop
    print(lst)

def working_list():
    lst = ["doctor", "teacher", "plumber", "electrician"]
    lst.index(1)
    if "doctor" in lst:
        print("doctor")
    lst.append("farmer")
    lst.insert(0, "janitor")
    for job in lst:
        print(job)

def alpha_slices():
    lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    print(lst[0:3])
    print(lst[5:8])
    print(lst + lst[3:5])







