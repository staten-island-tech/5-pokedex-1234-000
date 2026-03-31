wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}


staff = {}
for ward, staff in wards.items():
    print(ward,staff)
finder = input("Who? ")
for characters in staff:
    if finder == characters:
        print("works")


