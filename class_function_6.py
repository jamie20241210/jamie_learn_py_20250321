class User:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def getWeight(self):
        print("getWeight", self.weight)
        return float(self.weight)


def TestFunc():
    print("TestFunc")
    str = "dasjsdsa"
    print(f"""
    aa = {str}
    """)

    return 1