import glob
import fileinput
import os
import pypandoc

files = [f'yaml.md'] + sorted(glob.glob('Entradas/*.md'))
with open(f'.compile{os.sep}compiled.md', 'w') as fout:
	for line in fileinput.input(files=files):
		if fileinput.isfirstline() and fileinput.filename() != files[0]: fout.write(f'\n\\pagebreak\n\n# {os.path.splitext(os.path.basename(fileinput.filename()))[0]}\n\n')
		fout.write(line.replace('../Figuras', 'Figuras'))
	fout.write('\n\\pagebreak\n\n')
                               
os.system(f'pandoc .compile/compiled.md --filter pandoc-crossref --bibliography=referencias.bib --csl=.compile/ieee.csl --citeproc -o example.pdf --template eisvogel --listings')
