filenames = [
    "Last digit of integer",
    "Tens digit",
    "Sum of digits",
    "Fractional part",
    "First digit after decimal point",
    "Car route",
    "Digital clock",
    "Total cost",
    "Clock face - 1",
    "Clock face - 2"
]

for i, name in enumerate(filenames, start=1):
    filename = f"{i:02d} {name}.py"    # 01, 02, 03…
    with open(filename, "w") as f:
        pass  # create empty file

print("All numbered .py files created!")
