import unittest  	         	  

from Testing import testCard, testDeck, testMenu, testRandNumberSet  	         	  

suite = unittest.TestSuite()  	         	  

tests = (testCard.TestCard, testDeck.TestDeck, testMenu.TestMenu, testRandNumberSet.TestRandNumberSet)  	         	  
for test in tests:  	         	  
    suite.addTest(unittest.makeSuite(test))  	         	  

runner = unittest.TextTestRunner(verbosity=2)  	         	  
runner.run(suite)  	         	  
