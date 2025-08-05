"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        # Your code here
        num = float(input(f"Number {i+1}: "))  
        numbers.append(num)  
    
    # Display original list
    print(f"Original numbers: {numbers}")
    
    # Create filtered lists
    even_numbers = [n for n in numbers if n % 2 == 0] # Your code here
    odd_numbers = [n for n in numbers if n % 2 != 0] # Your code here
    
    # Calculate average
    total = sum(numbers)
    average = total / len(numbers) # Your code here
    above_average = [n for n in numbers if n > average]

    print(f"Even numbers: {even_numbers}")
    print(f"Odd numbers: {odd_numbers}")
    print(f"Numbers greater than average ({average}): {above_average}")
    print(f"Sum: {total}")
    print(f"Average: {average}")
    print(f"Min: {min(numbers)}")
    print(f"Max: {max(numbers)}")

if __name__ == "__main__":
    number_operations()