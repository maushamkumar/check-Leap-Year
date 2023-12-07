def check_leap_year():
    years = []

    while True:
        year = int(input("Enter a year: "))
        if year % 4 == 0:
            print(f"{year} is a leap year")
            status = "leap year"
        else:
            print(f"{year} is not a leap year")
            status = "not a leap year"

        years.append((year, status)) 
        
        while True:
            try:
                option = input("Do you want to check more? (yes/no): ")
                if option.lower() == "no":
                    break
                elif option.lower() == "yes":
                    break
                else:
                    raise ValueError("Please enter only 'yes' or 'no'")
            except ValueError as e:
                print(e)

        if option.lower() == "no":
            break

    for entry in years:
        y, s = entry
        print(f"{y} is {s}")

check_leap_year()
