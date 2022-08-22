import pprint
import re
import pickle 

with open('siccode.txt') as f:
    lines = f.readlines()

# pprint.pprint(lines)

sic_dict = {}
latest_division = "Agriculture, Forestry, And Fishing"
for line in lines:
    if line.strip():
        # print(line)
        division = re.search('(?<=Division .: ).+', line)
        if division != None and division.group(0) not in sic_dict:
            # print(division.group(0))
            sic_dict[division.group(0)] = {}
            latest_division = division.group(0)
        
        group_name = re.search('(?<=Group ..: ).+', line)
        if group_name != None:
            # print(group_name.group(0))
            group_no = re.search('(?<=Group )..', line)
            # print(group_no.group(0))
            sic_dict[latest_division][group_no.group(0)] = group_name.group(0)
        
with open('sic_dict.pkl', 'wb') as f:
    pickle.dump(sic_dict, f)