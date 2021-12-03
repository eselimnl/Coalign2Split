from Bio import SeqIO #requirement: pip install Bio
import argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument('-ho', '--host', dest="host", help='Specify which host you want to split.')
parser.add_argument('-i', '--input1', dest="input1", help='Absolute path to the aligned sequences file in FASTA format.')
parser.add_argument('-id', '--input2', dest="input2", help='Absolute path to the aligned sequences file in ID format.')
parser.add_argument('-o', '--output',dest="output", help='Absolute path to the output file.')
parser.add_argument('-s', '--sepID', dest="sepID", help='Call the function', action='store_true',required=False)        
args = parser.parse_args()

f1 = open(args.input1,'r') #fasta file that contains multiple-host sequence (input)
f3 = open(args.output,'a') #host spesific sequence (output)

if len(sys.argv) == 8:
    f2 = open(args.input2,'r') #accession ID of host-1 (input) 
    lineList = [line.rstrip('\n') for line in f2] #creates ID list of host  
    skip = 0 
    for line in f1: 
        if line[0] == '>': #selects ID line
            _splitline = line.split() 
            accessorIDWithArrow = _splitline[0] #takes accession and removes definition
            accessorID = accessorIDWithArrow[1:] #removes ">" symbol
            if accessorID in lineList: #compares if ID in fasta exists in the given host ID list  
                f3.write(line) #adds ID to output
                skip = 0 
            else:
                skip = 1 
        else:
            if not skip:
                f3.write(line) #adds sequence to output
else:
    for record in SeqIO.parse(f1, "fasta"):
        if args.host in record.description:
            SeqIO.write(record, f3, "fasta")  
                       
print(f'Results successfully saved at {args.output}')
sys.exit(0)
  










