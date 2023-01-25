def main():
    earth_weight = float(input("What do you weigh on Earth? "))
    mercury_weight = format(earth_weight * 0.38, ".2f")
    jupiter_weight = format(earth_weight * 2.53, ".2f")
    print(
        '\nOn Mercury you would weigh', mercury_weight, 'pounds.\n'
        'On Jupiter you would weigh', jupiter_weight, 'pounds.'
    )


# NOTE: This means if the code is run as `python3 planets.py`, run the
# main function.  If the code is merely imported, don't do anything.
if __name__ == '__main__':
    main()
