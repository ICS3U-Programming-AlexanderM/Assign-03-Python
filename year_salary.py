#!/usr/bin/env python3

# Created by: Alexander Matheson
# Created on: Dec 9, 2021
# This program gets the user to input their
# yearly salary and years of service.
# It then determines if the user should get a bonus.
# If the user gets a bonus, the program will calculate the bonus.
import constants


# declare variables
salary = 0
years = 0


def set_variables():
    # input
    global salary
    global years
    # error checking
    try:
        salary = float(input("Enter your current yearly salary: $"))
    except Exception:
        print("Must be a number")
        main()
    # error checking
    try:
        years = int(input("Enter your current years of service: "))
    except Exception:
        print("Must be a number")
        main()
    print()


def calculate():

    global salary

    salary_extra = salary * constants.INCREASE
    salary = salary + salary_extra
    print("Your bonus is ${:.2f}.". format(salary_extra))
    print("Your new salary is ${:.2f}.". format(salary))


def not_quite():
    extra_years = constants.SERVICE + 1 - years
    print("You do not have enough years of service to receive a bonus.")
    if extra_years == 1:
        print("You need {} more year.". format(extra_years))

    else:
        print("You need {} more years.". format(extra_years))


def main():

    set_variables()

    global years

    # check years of service
    if years > constants.SERVICE:
        calculate()

    else:
        not_quite()

    # loop
    answer = input("Is there someone else who would like to try? (y/n) ")
    print()

    if answer == constants.YES:
        main()

    else:
        print('Goodbye.')
        quit()


if __name__ == "__main__":
    main()
