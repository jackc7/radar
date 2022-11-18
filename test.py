
with open("output.txt", 'r') as f:
    data = []
    for x, line in enumerate(f.readlines()):
        wl = line.strip()
        if len(wl) != 3:
            continue
        try:
            data.append(int(wl))
        except ValueError:
            pass

sr = 0.00058331354 # Seconds between samples
data = data[13250:13650]
with open("table.csv", 'w') as f:
    for i, x in enumerate(data):
        # print(f"{i}\t{x}")
        f.write(f"{i*sr},{x}\n")