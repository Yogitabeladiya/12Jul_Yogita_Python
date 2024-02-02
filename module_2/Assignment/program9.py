# write a python program smallest number in list 

def smallest():
    list=[4,8,2,3,5]
    min=list[0]
    for x in list:
        if x<min: 
            min=x   
    return min
print(smallest())










def second_smallest(numbers):
  if (len(numbers)<2):
    return
  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    return
  dup_items = set()
  uniq_items = []
  for x in numbers:
    if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x)
  uniq_items.sort()    
  return  uniq_items[1]   

print(second_smallest([1, 2, -8, -2, 0, -2]))




