from check50 import *


class Calculating(Checks):

    @check()
    def exists(self):
        """restaurant.c exists"""
        self.require("restaurant.c")

    @check("exists")
    def compiles(self):
        """restaurant.c compiles"""
        self.spawn("clang -std=c11 -o restaurant restaurant.c -lcs50 -lm").exit(0)
        
    @check("compiles")
    def testy(self):
        """All y yields a bill of $21.00"""
        self.spawn("./restaurant").stdin('y').stdin('y').stdin('y').stdin('y').stdin('y').stdout("\nThe total for your food is $21.00.\n The total with 15% tip is $24.15.\n Thank you for your business!\n", "\nThe total for your food is $21.00.\n The total with 15% tip is $24.15.\n Thank you for your business!\n").exit(0)
        
    @check("compiles")
    def test0(self):
        """0 yields a mean of 0"""
        self.spawn("./restaurant").stdin("n").stdin("n").stdin("n").stdin("n").stdin("n").stdout("\nThe total for your food is $0.00.\n The total with 15% tip is $0.00.\n Thank you for your business!\n", "\nThe total for your food is $0.00.\n The total with 15% tip is $0.00.\n Thank you for your business!\n").exit(0)


    @check("compiles")
    def test_reject_empty_string(self):
        """rejects a non-numeric input of "" """
        self.spawn("./restaurant").stdin("").reject()
