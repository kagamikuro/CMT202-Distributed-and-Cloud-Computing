from mrjob.job import MRJob
import csv

def csv_readline(line):
    """Given a sting CSV line, return a list of strings."""
    for row in csv.reader([line]):
        return row
    
def mean(numList):
    sum = 0;
    len = 0;
    for i in numList:
        sum = sum + int(i)
        len = len +1
    return sum / len

class MRMeanOfNumbers(MRJob):
    def mapper(self,_, line):
        cell = csv_readline(line)
        for i in cell:
            yield "mean:",i;
        
        
    def reducer(self, lable, numList):
        yield lable,mean(numList)
        
if __name__ == '__main__':
    MRMeanOfNumbers.run()
