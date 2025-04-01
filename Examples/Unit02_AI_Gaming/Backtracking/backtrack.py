
def combination_sum(numbers, sum, running_sum=0, subset=[]):
    if len(numbers) == 0:
        return
    elif running_sum == sum:
        print(numbers)
        return
    elif running_sum > sum:
        return
    # Include Number
    num = numbers[0]
    subset.append(num)
    combination_sum(numbers, sum, running_sum + num, subset)
    subset.pop()

    # Don't include number
    combination_sum(numbers[1:], sum, running_sum, subset)
    
def place_1s(numbers, subset=[]):
    if len(numbers) == 1:
        subset.append(numbers[0])
        print(subset)
        return
    elif len(numbers) < 1:
        return
    copy_subset = []
    for i in range(len(subset)):
        copy_subset.append(subset[i])
   

    #Include number
    num = numbers[0]
    subset.append(num)
    subset.append(1)
    place_1s(numbers[1:], subset)

    #Dont Include number
        
    copy_subset.append(num)
    place_1s(numbers[1:], copy_subset)
    


          

            
    
        




place_1s([2,3,4])





            
            






