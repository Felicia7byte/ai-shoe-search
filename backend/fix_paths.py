import json

with open("shoe_paths.json", "r") as f:
    paths = json.load(f)

fixed_paths = []

for path in paths:
    filename = path.replace("\\", "/").split("/")[-1]
    fixed_paths.append(f"shoes/{filename}")

with open("shoe_paths.json", "w") as f:
    json.dump(fixed_paths, f, indent=2)

print(f"Fixed {len(fixed_paths)} paths")
