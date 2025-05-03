#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: May, 2025
# The program generates a sine table from 1 up to a number entered by the user (between 1 and 360)
# It asks if the user wants to start, handles invalid inputs, and uses nested loops
import math  # Helps us to use the sin fuction


def main():
    print("Welcome!")  # Welcome message
    print(
        "In this program we will help you generate the sin table for each degree (0 to 360)"
    )
    while True:
        answer = input(
            "Do you want to start? (please answer with a 'yes' or 'no'): "
        ).lower()
        # Start question and using lower
        if answer == "no":
            print("Have a nice day!")
            break
        elif answer == "yes":  # start of the actual program
            counter = 0

            while True:
                user_num = input("Enter a number between 1 and 360: ")

                try:  # TryCatch
                    num_int = int(user_num)

                    if num_int <= 0 or num_int > 360:
                        # Restriction on numbers
                        retry = input(
                            "Number should be between 1 and 360. Do you want to try again? (yes/no): "
                        ).lower()
                        # another question so we can restart the program from the top
                        # retry = answer_redo in flowchart
                        if retry != "yes":
                            print("Thank you for using this program.")
                            break  # end of the program
                        continue

                    # Nested loop
                    while counter < num_int:
                        counter += 1  # add 1 to the counter
                        result = math.sin(counter)
                        print(f"sin({counter}) = {result}")  # show results

                    print("Thanks for using this program.")
                    break  # End the inner while loop after successful completion

                except ValueError:
                    retry = input(
                        "Input is not an integer. Do you want to try again? (yes/no): "
                    ).lower()
                    # ask for a integer
                    if retry != "yes":
                        print("Thank you for using this program.")
                        break  # end the program
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")
            # start all over again


if __name__ == "__main__":
    main()
