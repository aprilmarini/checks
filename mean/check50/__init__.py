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
    def test15(self):
        """15 yields a mean of 15"""
        self.spawn("./mean").stdin("15").stdout("The mean is: 15\n", "15\n").exit(0)

    @check("compiles")
    def test_reject_empty_string(self):
        """rejects a non-numeric input of "" """
        self.spawn("./mean").stdin("").reject()
