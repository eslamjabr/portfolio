def get_list():
    # Continuously prompt the user until valid input is provided
    while True:
        try:
            # Take input for the first list of numbers
            input_str1 = input("Enter a first list of numbers separated by spaces: ")
            # Take input for the second list of numbers
            input_str2 = input("Enter a second list of numbers separated by spaces: ")
            
            # Split the input strings into lists of numbers
            numbers_str1 = input_str1.split()
            numbers_str2 = input_str2.split()
            
            # Convert the lists of strings into lists of integers
            numbers1 = [int(num) for num in numbers_str1]
            numbers2 = [int(num) for num in numbers_str2]
            
            # Return the two lists of numbers if input is successfully processed
            return numbers1, numbers2
            
        except:
            # Catch any exception raised during input conversion and ask the user for valid input
            print("wrong input please input numbers")

def main():
    # Call the get_list function to get two lists of numbers
    list1, list2 = get_list()
    
    # Initialize a counter to count the number of matching elements between the two lists
    count = 0
    
    # Check if the two lists have the same length
    if len(list1) == len(list2):
        # Iterate through the elements of the first list
        for i in list1:
            # Iterate through the elements of the second list
            for n in list2:
                # Check if the elements match
                if n == i:
                    # Increment the count if a match is found
                    count += 1
    else:
        # If the lists have different lengths, print a message indicating they are not the same
        print("two lists are not the same as elements of first list != second list")
    
    # Check if the count of matching elements is equal to the length of the first list
    if count == len(list1):
        # If all elements of the first list match with elements of the second list, print a message indicating they are the same
        print("two lists are the same")
    else:
        # If not all elements match, print a message indicating they are not the same
        print("two lists are not the same")

# Call the main function to execute the program
main()