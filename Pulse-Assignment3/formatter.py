def clean_output(data):
    clean = []

    for item in data:
        if item["Submodules"]:
            clean.append(item)

    return clean
