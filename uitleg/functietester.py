def handle_test(naam_test, verwacht, resultaat):
    if verwacht == resultaat:
        print(f"test {naam_test} is geslaagd.")
    else:
        print(f"test {naam_test} is niet geslaagd! verwacht: {verwacht} kreeg {resultaat}.")