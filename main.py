from datetime import date

def main():
    try:
        year = int(input("Enter year of birth (YYYY): "))
        claimed_age = int(input("Enter claimed age: "))
        
        current_year = date.today().year
        actual_age = current_year - year
        
        if actual_age == claimed_age:
            print("The claimed age is valid.")
        else:
            print("The claimed age does NOT match.")
            print(f"Actual age should be about: {actual_age}")
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()