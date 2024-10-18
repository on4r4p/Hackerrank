

from random import randint

class TestDataEmptyArray():
    @staticmethod
    def get_array():
        return []

class TestDataUniqueValues():
    _seq = []
    @staticmethod
    def get_array():
        random = randint(3,11)
        TestDataUniqueValues._seq = [i for i in range(0,random)]
        return TestDataUniqueValues._seq
        
    @staticmethod
    def get_expected_result():
         return TestDataUniqueValues._seq.index(min(TestDataUniqueValues._seq))
           
class TestDataExactlyTwoDifferentMinimums():
    _seq = []
    @staticmethod
    def get_array():
        random = randint(3,11)
        TestDataExactlyTwoDifferentMinimums._seq = [i for i in range(0,random)]
        TestDataExactlyTwoDifferentMinimums._seq.insert(0,TestDataExactlyTwoDifferentMinimums._seq[0])
        return TestDataExactlyTwoDifferentMinimums._seq
    @staticmethod
    def get_expected_result():
        diff2 = TestDataExactlyTwoDifferentMinimums._seq
        return diff2.index(min(diff2))
        

