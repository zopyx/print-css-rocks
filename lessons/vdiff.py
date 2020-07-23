import os
import shutil
import operator
from itertools import permutations

dirname = os.path.abspath(".")

filenames = os.listdir(dirname)
pdf_files = [fn for fn in filenames if fn.endswith('.pdf')]

perms = filter(lambda x: operator.le(x[0], x[1]), permutations(pdf_files, 2))
perms = list(perms)

diff_dir = os.path.join(dirname, 'diffs')
if os.path.exists(diff_dir):
    shutil.rmtree(diff_dir)
os.makedirs(diff_dir)

for fn1, fn2 in perms:
    bn1, ext = os.path.splitext(fn1)
    bn2, ext = os.path.splitext(fn2)
    diff_out = f"{bn1}-{bn2}.pdf"
    cmd = f'diff-pdf --output-diff "{diff_dir}/{diff_out}" "{dirname}/{fn1}" "{dirname}/{fn2}"'
    print(cmd)
    status = os.system(cmd)
