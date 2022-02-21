# Melakukan sorting array of points terurut membesar
# Algoritma yang digunakan untuk sorting adalah Merge Sort
def MergeSort(points):
  if len(points) > 1:
    idxMid = len(points) // 2
    leftArr = points[:idxMid]
    rightArr = points[idxMid:]

    # Pemanggilan rekursif
    MergeSort(leftArr)
    MergeSort(rightArr)

    # iterator
    i = 0
    j = 0
    k = 0

    while i < len(leftArr) and j < len(rightArr):
      if leftArr[i][0] <= rightArr[j][0]:
        points[k] = leftArr[i]
        i += 1
      else:
        points[k] = rightArr[j]
        j += 1
      
      k += 1
    
    while i < len(leftArr):
      points[k] = leftArr[i]
      i += 1
      k += 1
    
    while j < len(rightArr):
      points[k] = rightArr[j]
      j += 1
      k += 1
    



def myConvexHull(points):
  MergeSort(points)

  return points


