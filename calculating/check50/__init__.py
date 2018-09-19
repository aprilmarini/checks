from check50 import *


class Calculating(Checks):

    @check()
    def exists(self):
        """mean.c exists"""
        self.require("mean.c")

    @check("exists")
    def compiles(self):
        """mean.c compiles"""
        self.spawn("clang -std=c11 -o mean mean.c -lcs50 -lm").exit(0)
        
    @check("compiles")
    def test37(self):
        """37 degrees Celsius yields 98.6 degrees Fahrenheit"""
        self.spawn("./mean").stdin("15").stdout(number(15), "15\n").exit(0)

    @check("compiles")
    def test_reject_empty_string(self):
        """rejects a non-numeric input of "" """
        self.spawn("./mean").stdin("").reject()
