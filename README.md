# **iFastaFromAccID**

Extract interested fasta sequences based on the accession number list !

## **Background :**
A virus is a living organism only if we consider it associated with its host. Viruses of the same family can infect a wide range of hosts. Identifying the host organism(s) is therefore essential, because features like virus-cell interactions and post-translational modifications depend mostly on the host. (UniProt)

## **Usage :**
```
python iFastaFromAccID.py -i yourseq.fasta -id idlist.txt -o output.fasta
```
You need to give two inputs to run host-separation.py. ID list of host (file in .txt format), sequence data (file in .fasta format)
## **Caution :**
This code was used for ID match and extract for data downloaded from NCBI Taxonomy. Be careful when if you have data from another databases. Because standard ID annotation may differ. For NCBI:

accessionID.1 | definition
