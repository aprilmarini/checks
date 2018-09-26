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
        self.spawn("./restaurant").stdin('y').stdin('y').stdin('y').stdin('y').stdin('y').stdout("Total: \$21.00\n", "Total: \$21.00\n").stdout("Total with 15% tip: \$24.15\n", "Total with 15% tip: \$24.15\n").exit(0)
        
    @check("compiles")
    def test0(self):
        """n yields a bill of $0.00"""
        self.spawn("./restaurant").stdin('n').stdin('n').stdin('n').stdin('n').stdout("Total: \$0.00\n", "Total: \$0.00\n").exit(0)


    @check("compiles")
    def test_reject_empty_string(self):
        """rejects a non-numeric input of "" """
        self.spawn("./restaurant").stdin("").reject()
        
    def number(num):
        return "(^|[^\d]){}[^\d]".format(num)
