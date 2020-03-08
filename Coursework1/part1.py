from mrjob.job import MRJob
import csv

def csv_readline(line):
    """Given a sting CSV line, return a list of strings."""
    for row in csv.reader([line]):
        return row

class MRMaxNumber(MRJob):
    def mapper(self,_, line):
        cell = csv_readline(line)
        for i in cell:
            yield "maximum:",i;
        
        
    def reducer(self, lable, numList):
        yield lable,max(numList)
        
if __name__ == '__main__':
    MRMaxNumber.run()
