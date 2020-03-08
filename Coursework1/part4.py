from mrjob.job import MRJob
import csv

def csv_readline(line):
    """Given a sting CSV line, return a list of strings."""
    for row in csv.reader([line]):
        return row
    


class MRTriplesOfURL(MRJob):
    def mapper(self,_, line):
        cell = csv_readline(line)
        for word in cell:
            yield word ,cell

    def reducer(self, key, string):
            yield key, list(string)
        
if __name__ == '__main__':
    MRTriplesOfURL.run()

