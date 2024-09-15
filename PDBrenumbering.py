from Bio import PDB

def read_rna_sequence(fasta_file):
    with open(fasta_file, 'r') as f:
        sequence = "".join(line.strip() for line in f if not line.startswith('>'))
    return sequence

# Input PDB and FASTA file paths
pdbfile = '/home/user/template.pdb' #this line is where the template for rosetta is going to be fetched
new_num=[1,2,4,5,7,8,10,11]

#Parse the PDB file
pdb_parser = PDB.PDBParser(QUIET=True)
structure = pdb_parser.get_structure(" ", pdbfile)
print(structure)

# Get the number of residues in the chain
#num_residues = sum(1 for model in structure for chain in model for residue in chain.get_residues())

# Generate the new_num list automatically
#new_num = list(range(1, num_residues + 1))


'''
# Read RNA sequence from the FASTA file
rna_sequence = read_rna_sequence(fastafile)

# Update the residue numbering in the PDB structure
new_resnums = [i for i in range(len(rna_sequence))]
'''
for model in structure:
    for chain in model:
        for i, residue in enumerate(chain.get_residues()):
#            print(i)

            if i < len(new_num):
                res_id = list(residue.id)
                res_id[1] = res_id[1] + 1000 
                residue.id = tuple(res_id)


for model in structure:
    for chain in model:
        for i, residue in enumerate(chain.get_residues()):
            print(i)

            if i < len(new_num):
                res_id = list(residue.id)
                res_id[1] = new_num[i] 
                residue.id = tuple(res_id)




# Save the modified structure as a new PDB file
pdb_io = PDB.PDBIO()
pdb_io.set_structure(structure)
pdb_io.save(pdbfile + "_re.pdb")
