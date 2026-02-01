class Factory:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f"object details are: 1.material: {self.material}, 2.zips: {self.zips}, 3.pockets: {self.pockets}")

skybags = Factory("leather", 2, 3)

campus = Factory("nylon", 2, 5)

skybags.show()
campus.show()