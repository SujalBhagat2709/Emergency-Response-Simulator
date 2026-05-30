import time

from incident import Incident

ambulances = 3
fire_trucks = 2
police_units = 4

print(
    "\n================================"
)

print(
    "EMERGENCY RESPONSE CENTER"
)

print(
    "================================"
)

for minute in range(1, 6):

    print(
        f"\n⏰ Minute {minute}"
    )

    incident = Incident()

    incident.display()

    print(
        "\nResources"
    )

    print(
        f"🚑 Ambulances: "
        f"{ambulances}"
    )

    print(
        f"🔥 Fire Trucks: "
        f"{fire_trucks}"
    )

    print(
        f"🚓 Police Units: "
        f"{police_units}"
    )

    choice = input(
        "\nDispatch Team? (y/n): "
    )

    if choice.lower() == "y":

        if incident.type == "Medical Emergency":

            if ambulances > 0:

                ambulances -= 1

                print(
                    "🚑 Ambulance Dispatched"
                )

        elif incident.type == "Building Fire":

            if fire_trucks > 0:

                fire_trucks -= 1

                print(
                    "🔥 Fire Truck Dispatched"
                )

        else:

            if police_units > 0:

                police_units -= 1

                print(
                    "🚓 Police Unit Dispatched"
                )

    time.sleep(2)

print(
    "\n🏁 Simulation Ended"
)