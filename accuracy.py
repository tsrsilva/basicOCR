# Install dependencies
# python-Levenshtein

# Import libraries
from Levenshtein import distance

# Define path to ground values
ground_value = r'BRASIL: MG, Viçosa , Mata do Seu Nico 745m 20°47`54.4``S - 42°50`53.2``W 13.iv.2012. Schmidt,F.A.; Rezende,F.;Jesus,R. col Floresta Estacional Semidecidual Formação primária Pitfall hipogéico Ponto:19 Estrato: H PitfallÇ 1 H/P : 50 cm ANTWEB 1008097"'
ocr_value = r'BRASIMS Vicoss 13E 35 Seu Nco Zasm 2004754.4s 42*5053zw 13.1v.2012 SchmidFA; Rezende. F: Jesus R coi'

print(distance(ground_value, ocr_value))