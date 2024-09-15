import json
import glob
import re
import os

# Get list of JSON files
f_list = glob.glob("/home/user/*.json") #this is where the input files directory should be

for f in f_list:
    print(f)
    
    with open(f) as fh:
        df = json.load(fh)
        
    seq_list = df['dotBracket']['sequence'].split('-')
    line1_list = df['dotBracket']['line1'].split('-')
    line2_list = df['dotBracket']['line2'].split('-')
    
    print(seq_list[0])
    print(line1_list[0])
    print(line2_list[0])
    
    m1 = re.finditer(r'[\(|\[|\{]', line1_list[0])
    m12 = re.finditer(r'[\)|\]|\}]', line1_list[0])
    m2 = re.finditer(r'[\(|\[|\{]', line2_list[0])
    m22 = re.finditer(r'[\)|\]|\}]', line2_list[0])
    
    m1_start = []
    m1_end = []
    m2_start = []
    m2_end = []
    
    for m in m1:
        m1_start.append(m.start())
        
    for m in m12:
        m1_end.append(m.start())
        
    for m in m2:
        m2_start.append(m.start())
        
    for m in m22:
        m2_end.append(m.start())
        
    m1_start.extend(m2_start)
    
    if m1_start:
        start = min(m1_start)
    else:
        start = 0
        
    m1_end.extend(m2_end)
    
    if m1_end:
        end = max(m1_end) + 1
    else:
        end = len(seq_list[0])
        
    print(f)
    print(start, end)
    print(seq_list[0][start:end])
    
    out_f = f.replace('json', 'g4seq')
    
    with open(out_f, "w") as o_fh:
        o_fh.write(seq_list[0][start:end])

