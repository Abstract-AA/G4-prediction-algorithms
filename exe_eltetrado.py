# use py3.9
import glob
import re
import os
import subprocess

f_list=glob.glob("../cif/*.cif.gz")

for f in f_list:
    tmp_f=f.split('/')[2]
    tmp_f_out="../eltetrado/" + tmp_f.replace('cif.gz','json')
    print(tmp_f_out)
    subprocess.call(['eltetrado', '--input', f, '--output', tmp_f_out])
                    
