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
        self.spawn("./restaurant").stdin('y').stdin('y').stdin('y').stdin('y').stdin('y').stdout("Total: \$21.00\n", "Total: \$21.00\n").exit(0)
    
    @check("compiles")
    def testgc(self):
        """Grilled cheese yields a bill of $5.00"""
        self.spawn("./restaurant").stdin('y').stdin('n').stdin('n').stdin('n').stdout("Total: \$5.00\n", "Total: \$5.00\n").exit(0)  
        
    @check("compiles")
    def testhd(self):
        """Hot dog yields a bill of $5.00"""
        self.spawn("./restaurant").stdin('n').stdin('y').stdin('n').stdin('n').stdout("Total: \$5.00\n", "Total: \$5.00\n").exit(0)
        
    @check("compiles")
    def testnachos(self):
        """nachos yields a bill of $4.00"""
        self.spawn("./restaurant").stdin('n').stdin('n').stdin('y').stdin('n').stdout("Total: \$4.00\n", "Total: \$4.00\n").exit(0)
        
    @check("compiles")
    def testhamburger(self):
        """Hamburger yields a bill of $6.00"""
        self.spawn("./restaurant").stdin('n').stdin('n').stdin('n').stdin('y').stdin('n').stdout("Total: \$6.00\n", "Total: \$6.00\n").exit(0)
        
    @check("compiles")
    def testcheeseburger(self):
        """Cheeseburger yields a bill of $7.00"""
        self.spawn("./restaurant").stdin('n').stdin('n').stdin('n').stdin('y').stdin('y').stdout("Total: \$7.00\n", "Total: \$7.00\n").exit(0)        
        
    @check("compiles")
    def test0(self):
        """n yields a bill of $0.00"""
        self.spawn("./restaurant").stdin('n').stdin('n').stdin('n').stdin('n').stdout("Total: \$0.00\n", "Total: \$0.00\n").exit(0)


    @check("compiles")
    def test_reject_empty_string(self):
        """rejects a non-numeric input of "" """
        self.spawn("./restaurant").stdin("").reject()
