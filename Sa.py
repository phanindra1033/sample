import csv

with open('G:/New folder (4)/csv1.csv','r') as csvinput: 
    with open('G:/New folder (4)/tsv1.tsv', 'w') as tsvoutput:
        csvinput = csv.reader(csvinput)
        tsvoutput = csv.writer(tsvoutput, delimiter='\t')

        for row in csvinput:	    
            tsvoutput.writerow(row)
