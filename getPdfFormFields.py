#!/usr/bin/env python

import os
import subprocess
import shlex

path = raw_input("Enter PDF directory path: ")
output = open("pdf_form_fields.txt", "w")
files = {}

for filename in os.listdir(path):
    if filename.endswith(".pdf"):
        file = os.path.join(path, filename)
        file = '"%s"' % file # wrap in quotes to handle files with spaces
        cmd = "pdftk " + file  + " dump_data_fields | grep -w FieldName"
        print filename
        try:
            files[filename] = subprocess.check_output(cmd, shell=True)
        except subprocess.CalledProcessError as exc:
            files[filename] = exc.output
        continue

count = 1
for name, data in files.items():
    output.write('----'+name+'----\n')
    output.write(data)
    output.write('\n\n')
    count = count + 1

output.write("\ntotal files processed\n")
output.write(str(count))
output.close()
