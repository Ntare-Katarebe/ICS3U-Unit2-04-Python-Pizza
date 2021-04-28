#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: April 2021
# This program calculates the cost of making a pizza
#    with diameter inputted from the user

import constants


def main():
    # This function calculates the cost of making a pizza

    # input
    diameter = int(
        input("Enter the diameter of the pizza you would" + "like (inch): ")
    )

    # process
    sub_cost = (
        constants.LABOR + constants.RENT + (constants.MATERIALS * diameter))
    cost = sub_cost + (sub_cost * constants.HST)
    # output
    print("")
    print(" The cost for a {} inch pizza is: ${}".format(diameter, cost))
    print("\nDone.")


if __name__ == "__main__":
    main()
