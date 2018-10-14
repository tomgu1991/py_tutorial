#!/usr/bin/env python3
# Author Zuxing Gu

import yaml

f = open('ISpecLSample.yml', 'r')
spec = yaml.load_all(f.read())
for item in spec:
    print(item)
    content = item['SPEC']
    note = content['NOTES']
    mainF = content['MAINFUNCTION']
    print(note)
    print(mainF)
    print()

f.close()

fw = open('tem.yml', 'w')
data = {'SPEC': {'NOTES': 'note', 'TYPE': 'IMC'}}
fw.write(yaml.dump(data, default_flow_style=False, indent=4))
fw.flush()
fw.close()
