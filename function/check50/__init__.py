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
