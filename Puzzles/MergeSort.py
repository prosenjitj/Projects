def merge(arr1 , arr2) :
       arr3 = []
       while len(arr1) > 0 and len(arr2) > 0 :
              if arr1[0] < arr2[0] :
                     arr3.append(arr1[0])
                     arr1.remove(arr1[0])
              else :
                     arr3.append(arr2[0])
                     arr2.remove(arr2[0])

       if len(arr1) > 0 :
              arr3.extend(arr1)
       if len(arr2) > 0 :
              arr3.extend(arr2)

       return arr3

def mergesort(arr) :
       if len(arr) < 2 :
              return arr

       mid = len(arr) // 2
       m1 = mergesort(arr[mid:])
       m2 = mergesort(arr[:mid])
       return merge(m1 , m2)


print(mergesort(arr))
