# Compute average
def average(array):
    array_set = set(array)
    array_sum = sum(array_set)
    array_length = len(array_set)
    avg = array_sum / array_length
    
    return avg

if __name__ == '__main__':
    n = int(input("Enter the size of n: "))
    arr = list(map(int, input("Enter the number of elements: ").split()))
    assert len(arr) == n, f"Expected {n} elements in arr, got {len(arr)}"
    result = average(arr)
    print(result)