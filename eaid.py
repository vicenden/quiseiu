import json

# assume dict_all is your edges dictionary
with open('edges.json', 'w') as f:
    json.dump(dict_all, f)
