# Extracts a collection of birth dates from the user and determines
# if each individual is at least 32 years of age.
from date import Date

def main():
    # Date before which a person must have been born to be 32 or older.
    bornBofore = Date(1984, 5, 2)

    # Extract birth dates from the user and determine if 32 or older
    date = promptAndExtractDate()
    while date is not None:
        if date <= bornBofore:
            print("Is at least 32 years of age: ", date)
        date = promptAndExtractDate()


# Prompts for and extracts the Gregorian date components. Return a
# Date object or None when user has finished entering dates.
def promptAndExtractDate():
    print("Enter a birth date.")
    year = int(input("year (0 to quit): "))
    if year == 0:
        return None
    else:
        month = int(input("month: "))
        day = int(input("day: "))
        return Date(year, month, day)

main()
