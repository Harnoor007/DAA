import sqlite3

# Connect to the database (creates a new database if it doesn't exist)
db_connection = sqlite3.connect('csea2.db')
cursor = db_connection.cursor()

# Fetch IDs from the database
fetch_ids_query = "SELECT URN FROM students"
cursor.execute(fetch_ids_query)

ids_list = [row[0] for row in cursor.fetchall()]

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Calculate mid index to avoid integer overflow

        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Element not found


target_element = int(input("Enter the roll number to be found: "))
result = binary_search(ids_list, target_element)

if result != -1:
    print(f"Element {target_element} found")

    fetch_student_query = "SELECT * FROM students WHERE URN = ?"
    cursor.execute(fetch_student_query, (target_element,))
    student_details = cursor.fetchone()

    if student_details:
        print("Student Details:")
        print("URN:", student_details[0])  #the first column is the roll number
        print("Name:", student_details[1])  #the second column is the name
        print("Class:", student_details[2])
        print("CRN:", student_details[3])

else:
    print(f"Element {target_element} not found in the table")

db_connection.close()