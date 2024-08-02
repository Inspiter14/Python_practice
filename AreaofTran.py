def process_Array(arr):
    i = 0
    while i < len(arr) - 1:
        # Check if the current and next elements are both single-digit numbers and not negative
        if 0 <= int(arr[i]) < 10 and 0 <= int(arr[i + 1]) < 10 and int(arr[i]) >= 0 and int(arr[i + 1]) >= 0:
            count = 1
            # Count the consecutive single-digit numbers
            while i + count < len(arr) and 0 <= int(arr[i + count]) < 10 and int(arr[i + count]) >= 0:
                count += 1

            # Replace the sequence with the last number in that sequence
            arr[i:i + count] = [arr[i + count - 1]]

        # Move to the next element in the array
        i += 1

    return ",".join(filter(lambda x: int(x) >= 0, arr))

# Example usage
input_num=input()
num = input_num.split(",")
new_array = process_Array(num)
print("Modified Array:", new_array)
