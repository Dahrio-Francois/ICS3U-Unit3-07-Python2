#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: April 2022
# This program lets you know if you can date
# a grandma's grandchild, if you are rich or handsome


def main():
    # this function creates the program

    # input
    financial_status = input("What is your financial status? Are you rich? : ")
    attractiveness_status = input(
        "What about your attractiveness? Are you handsome? : "
    )
    print("")

    # process & output
    if financial_status == "yes" or attractiveness_status == "yes":
        print("You may date my grandchild.")
    elif financial_status == "no" and attractiveness_status == "no":
        print("I don't want to see you around my grandchild again.")
    else:
        print("Please answer with yes or no.")


if __name__ == "__main__":
    main()
