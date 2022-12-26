import random  	         	  


class RandNumberSet():  	         	  
    MIN_SIZE = 3  	         	  
    MAX_SIZE = 16  	         	  

    def __init__(self, nSize, nMax):  	         	  
        """  	         	  
        Create a number set that contains the segments used in the Bingo card 	         	  
        """

        # keep Bingo card size in range from 3 to 16
        self.__m_nSize = nSize
        if self.__m_nSize < RandNumberSet.MIN_SIZE:  	         	  
            self.__m_nSize = RandNumberSet.MIN_SIZE  	         	  

        if self.__m_nSize > RandNumberSet.MAX_SIZE:  	         	  
            self.__m_nSize = RandNumberSet.MAX_SIZE  	         	  

        # pick the larger of `nMax` or `nSize^2 * 2`
        self.__m_nMax = max(nMax, self.__m_nSize * self.__m_nSize * 2)
        self.__m_nRowPos = 0

        # when `len(RandNumberSet)` is not evenly divisible by `nSize`, there will be some numbers left over
        # distribute these extra numbers starting from segment #0, going up from there
        segments = []
        segment_size = self.__m_nMax // self.__m_nSize
        remainder = self.__m_nMax % self.__m_nSize
        low = 1  	         	  
        for segment in range(1, self.__m_nSize + 1):  	         	  
            high = low + segment_size
            if segment <= remainder:  	         	  
                high += 1
            segments.append(list(range(low, high)))
            low = high  	         	  
        self.segments = segments  	         	  

    def __len__(self):  	         	  
        return self.__m_nSize

    # allows a row in list form from the Bingo card to be chosen using an indexing operator []
    def __getitem__(self, n):
        if 0 <= n < self.__m_nSize:  	         	  
            row = []  	         	  
            for seg in self.segments:  	         	  
                row.append(seg[n])  	         	  
            return row  	         	  
        else:  	         	  
            raise IndexError  	         	  

    # randomize numbers so the first few will be used in the Bingo card; ensures no repeats
    def shuffle(self):  	         	  
        for seg in self.segments:
            random.shuffle(seg)  	         	  
        self.__m_nRowPos = 0  	         	  

    # returns a list of the next row of Bingo numbers
    def next_row(self):  	         	  
        if self.__m_nRowPos >= self.__m_nSize:
            return None  	         	  
        row = []  	         	  
        for seg in self.segments:  	         	  
            row.append(seg[self.__m_nRowPos])  	         	  
        self.__m_nRowPos += 1  	         	  
        return row  	         	  

    # if variable of type RandNumberSet is called, return a list of lists of Bingo rows
    def __str__(self):  	         	  
        strs = []  	         	  
        for seg in self.segments:  	         	  
            strs.append(str(seg))  	         	  
        return '\n'.join(strs)  	         	  
