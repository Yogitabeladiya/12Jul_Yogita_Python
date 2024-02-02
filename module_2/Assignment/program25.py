# remove empy tuple from tuple 




def remove(tuples):
     for i in tuples:
          if (len(i)==0):
               tuples.remove(i)
     return tuples
tuples=[(),(2,3,4),(),(4,5),()]
print(remove(tuples))
