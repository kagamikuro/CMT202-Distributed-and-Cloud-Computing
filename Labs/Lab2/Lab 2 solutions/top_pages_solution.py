"""Find Vroots with more than 400 visits.

This program will take a CSV data file and output tab-seperated lines of

    Vroot -> number of visits

To run:

    python top_pages_solution.py anonymous-msweb.data

To store output:

    python top_pages_solution.py anonymous-msweb.data > top_pages.out
"""

from mrjob.job import MRJob
import csv

def csv_readline(line):
    """Given a sting CSV line, return a list of strings."""
    for row in csv.reader([line]):
        return row

class TopPages(MRJob):

    def mapper(self, line_no, line):
        """Extracts the Vroot that was visited"""
        cell = csv_readline(line)
        if cell[0] == 'V':
            yield cell[1], 1 

    def reducer(self, vroot, visit_counts):
        """Sumarizes the visit counts by adding them together.  If total visits
        is more than 400, yield the results"""
        total = sum(visit_counts) # How do we calculate the total visits from the visit_counts?
        if total > 400:
            yield vroot, total
        
if __name__ == '__main__':
    TopPages.run()