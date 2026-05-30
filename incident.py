import random

class Incident:

    def __init__(self):

        incidents = [
            "Road Accident",
            "Building Fire",
            "Medical Emergency",
            "Gas Leak",
            "Flood Alert"
        ]

        self.type = random.choice(
            incidents
        )

        self.priority = random.randint(
            1,
            5
        )

    def display(self):

        print(
            f"\n🚨 Incident: "
            f"{self.type}"
        )

        print(
            f"Priority: "
            f"{self.priority}"
        )


if __name__ == "__main__":

    incident = Incident()

    incident.display()