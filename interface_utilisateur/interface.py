

class InterfaceUtilisateur:
    def __init__(self):
        self.points_passage = []

    def get_user_input(self):
        num_points = int(input("Nombre de points : "))

        for i in range(num_points):
            x = float(input(f"Point {i + 1} - x : "))
            y = float(input(f"Point {i + 1} - y : "))
            self.points_passage.append((x, y))

        return self.points_passage


