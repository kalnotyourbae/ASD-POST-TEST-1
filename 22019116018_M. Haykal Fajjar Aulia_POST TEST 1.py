import random
import os
import time
os.system("cls")

#menjelaskan bagian daripada proses partisi elemen
def partition(arr, low, high):
    #arr sebagai data, low sebagai element kiri, high sebagai element kanan
    print("\nPartisi Terkini : ", array)
    time.sleep(1)
    #pivot merupakan data element pertama, terakhir, atau tengah
    pivot = arr[high]
    i = low - 1
    #dibawah merupakan baris perintah melakukan proses pertukaran element kiri, kanan, dengan pedoman pada pivot
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

#penjelasan mengenai sorting menggunakan quicksort
def quicksort(arr, low, high):
    #pengkondisian apabila element low kurang dari element high ( )
    if low < high:
        pivot_index = partition(arr, low, high)
        print("Proses Mempartisi :",arr)
        quicksort(arr, low, pivot_index-1)
        quicksort(arr, pivot_index+1, high)

# List bilangan random yang akan di-sorting
array = [random.randint(1, 75) for i in range(10)]

# Menampilkan list awal
print("List sebelum sorting : ", array)
print()

# Memulai sorting
quicksort(array, 0, len(array)-1)

# Menampilkan list setelah sorting
print("\nList setelah sorting : ", array)
print()