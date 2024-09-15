from Bio import PDB
import glob
import os

def get_residue_id(residue):
    if isinstance(residue.id, tuple):
        return residue.id[1]
    else:
        return residue.id

def remove_nucleotides(input_pdb, positions_to_remove, output_pdb):
        # Create a PDB parser
        pdb_parser = PDB.PDBParser(QUIET=True)

        # Load the structure from the PDB file
        structure = pdb_parser.get_structure("input", input_pdb)[0]

        #create a new structure for the output file
        new_structure = PDB.Structure.Structure("output")
                
        # Iterate through the structure to remove specified nucleotides
      #  new_chain = PDB.Chain.Chain(" ")
                
        for model in structure:
            new_model = PDB.Model.Model(0)
            for chain in model:
         #       new_model = PDB.Model.Model(0)
                new_chain = PDB.Chain.Chain(" ")
                print(chain.get_list())
                for residue in chain:
                    if get_residue_id(residue) not in positions_to_remove:
#                        print(residue.resname)
                        new_residue = residue.copy()
                        new_chain.add(new_residue)

            new_model.add(new_chain)

        new_structure.add(new_model)
                        
        # Save the modified structure to a new PDB file
        pdb_io = PDB.PDBIO()
        pdb_io.set_structure(structure)
        pdb_io.save(output_pdb)
        
# Specify the directory containing PDB files
pdb_directory = "/path/to/your/pdb/files/"

# Locate PDB files in the specified directory
pdb_files = glob.glob( "/home/user/XXX.pdb")

# Specify the positions to remove
positions_to_remove = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,29, 30, 31, 32, 33, 34, 35, 36,372] 

# Process each PDB file
for input_pdb_file in pdb_files:
    # Create an output file name based on the input file
    filename, extension = os.path.splitext(input_pdb_file)
    output_pdb_file = f"{filename}_modified{extension}"
    # Remove nucleotides and save the modified structure
    remove_nucleotides(input_pdb_file, positions_to_remove, output_pdb_file)                                                                              
