import json

def fjsonencode(dictobj, filename):
    with open(filename, 'w') as f:
        json.dump(dictobj, f, indent=3)

def fjsondecode(filename) -> dict:
    with open(filename) as f:
        return json.load(f)

if __name__ == "__main__":
    pass