#2CB Interactive 3D Model: Groovy Colors
from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

# 1. Setup the molecule
smiles = "COc1cc(Br)cc(OC)c1CCN"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, randomSeed=42)
AllChem.MMFFOptimizeMolecule(mol)
mol_block = Chem.MolToMolBlock(mol)

# 2. Initialize viewer with dreamy background
view = py3Dmol.view(width=800, height=500)
view.addModel(mol_block, "mol")
view.setBackgroundColor("#FFF0F5")  # Lavender Blush (soft pink-white)

# 3. Ball-and-Stick Style with Childlike Happiness Colors
# Carbon: Sunny Yellow
view.setStyle({"elem": "C"}, {
    "stick": {"color": "#FFD700", "radius": 0.15},
    "sphere": {"color": "#FFD700", "scale": 0.3}
})

# Oxygen: Bubblegum Pink
view.setStyle({"elem": "O"}, {
    "stick": {"color": "#FF69B4", "radius": 0.18},
    "sphere": {"color": "#FF69B4", "scale": 0.35}
})

# Nitrogen: Orchid Purple
view.setStyle({"elem": "N"}, {
    "stick": {"color": "#DA70D6", "radius": 0.18},
    "sphere": {"color": "#DA70D6", "scale": 0.35}
})

# Bromine: Golden Orange
view.setStyle({"elem": "Br"}, {
    "stick": {"color": "#FFA500", "radius": 0.25},
    "sphere": {"color": "#FFA500", "scale": 0.45}
})

# Hydrogen: Soft White
view.setStyle({"elem": "H"}, {
    "stick": {"color": "#FFFFFF", "radius": 0.08},
    "sphere": {"color": "#FFFFFF", "scale": 0.2}
})

# 4. Animation for whimsical feel
view.zoomTo()
view.spin(True, speed=0.5)  # Gentle rotation

# Show the result
view.show()
