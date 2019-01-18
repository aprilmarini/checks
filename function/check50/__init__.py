from check50 import *


class Calculating(Checks):

    @check()
    def exists(self):
        """function.c exists"""
        self.require("function.c")

    @check("exists")
    def compiles(self):
        """function.c compiles"""
        self.spawn("clang -std=c11 -o function function.c -lcs50 -lm").exit(0)
        
    @check("compiles")
    def test1(self):
        """All y yields a bill of $21.00"""
        self.spawn("./function").stdout("Square Function!\n").stdin(2).stdout("2 squared is 4\n").stdout("\n").stdout("Minimum Function!\n").stdin(1).stdin(2).stdin(3).stdout("The minimum of the three numbers is: 1\n").stdout("\n").stdout("Quadratic Formula Function!\n").stdin(1).stdin(15).stdin(1).stdout("x = -0.066966, -14.933034\n").exit(0)
