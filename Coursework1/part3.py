from mrjob.job import MRJob
import csv

def csv_readline(line):
    """Given a sting CSV line, return a list of strings."""
    for row in csv.reader([line]):
        return row
    


class MRTriplesOfURL(MRJob):
    def mapper(self,_, line):
        cell = csv_readline(line)
        yield cell[1],(cell[0],cell[1])
        yield cell[0],(cell[0],cell[1])
        
    def reducer(self, key, URLRelations):
        lists_URLRelations = list(URLRelations)
        if len(lists_URLRelations)>1 :
            for i in range(0,len(lists_URLRelations)):
                index = i+1;
                for j in range(index,len(lists_URLRelations)):
                    if lists_URLRelations[i][1] == lists_URLRelations[j][0]:
                        yield key,(lists_URLRelations[i][0],lists_URLRelations[i][1],lists_URLRelations[j][1])
                    if lists_URLRelations[j][1] == lists_URLRelations[i][0]:
                        yield key,(lists_URLRelations[j][0],lists_URLRelations[j][1],lists_URLRelations[i][1])
                        
                
        #yield key,lists_URLRelations
        
if __name__ == '__main__':
    MRTriplesOfURL.run()
000000
