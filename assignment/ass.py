def group_by_owners(files):
    ownerdict = {}
    for key,value in files.items():
        if value in ownerdict:
         ownerdict[value].append(key)
        else:
          ownerdict[value] = [key]
        return ownerdict

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))
