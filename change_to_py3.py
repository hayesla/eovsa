import glob
import subprocess

files = glob.glob('*.py')

for file in files:
	subprocess.call(['2to3', '-w', file])