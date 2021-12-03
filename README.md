# **Coalign2Split**

Extract interested fasta sequences based on indicating the host accessions in a ID list or identify the host sequence looking to name of the host species in the header.

## **Background :**
A virus is a living organism only if we consider it associated with its host. Viruses of the same family can infect a wide range of hosts. Identifying the host organism(s) is therefore essential, because features like virus-cell interactions and post-translational modifications depend mostly on the host. 

## **Usage :**
There 2 ways to use the tool:

1- Define the name of host species found in the fasta headers.
```
python Coalign2Split.py -i yourseq.fasta -ho "Homo sapiens" -o output.fasta
```
2- Give an IDlist that has accession ID's of the relevant sequences.
```
python Coalign2Split.py -s -i yourseq.fasta -id idlist.txt -o output.fasta
```
You need to give two inputs to run Coalign2Split.py. ID list of host (file in .txt format), sequence data (file in .fasta format)
## **Caution :**
This code was used for ID match and extract for data downloaded from NCBI Taxonomy. Be careful when if you have data from another databases. Because standard ID annotation may differ. For NCBI:

accessionID.1 | definition
