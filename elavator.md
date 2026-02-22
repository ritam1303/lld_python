# 🏢 Elevator Scheduling System — Low Level Design Notes

---

# 📌 Problem Statement

Design a lift system that:

* Supports multiple lifts
* Accepts pickup and destination floors
* Assigns the most suitable lift
* Maintains lift routes dynamically
* Handles both upward and downward movement

The goal is to simulate a **real-world elevator dispatch system**.

---

# 🧱 System Components

## 1️⃣ LiftManager (State Store)

Responsible for maintaining the state of all lifts.

Acts like an in-memory database of elevators.

Stores:

* current floor
* direction
* route queue
* destination

---

## 2️⃣ Lift (Entity)

Responsible for:

* Creating lifts
* Registering them in LiftManager
* Setting initial state

Each lift starts at floor **1**, status **idle**.

---

## 3️⃣ Algorithm (Dispatcher / Scheduler)

Responsible for:

* Accepting requests
* Choosing best lift
* Updating routes
* Maintaining direction
* Simulating movement

This represents the **brain of the system**.

---

# 📊 UML Class Diagram

```
+-------------------+
|    LiftManager    |
+-------------------+
| - lifts : dict    |
+-------------------+

          1
          |
          | manages
          |
          *
+-------------------+
|       Lift        |
+-------------------+
| - current_floor   |
| - destination     |
| - status          |
| - track : list    |
+-------------------+

          ^
          |
          | uses
          |
+-------------------+
|     Algorithm     |
+-------------------+
| - lift_manager    |
+-------------------+
| + shortest_route()|
+-------------------+
```

---

# 🔄 Scheduling Logic

### UP Request

A lift can serve if:

* idle OR moving up
  AND
* below pickup floor

Track sorted ascending.

---

### DOWN Request

A lift can serve if:

* idle OR moving down
  AND
* above pickup floor

Track sorted descending.

---

# 🧠 Design Principles Used

* Separation of concerns
* Dispatcher pattern
* Route optimization
* Direction-based scheduling

Similar to **SCAN disk scheduling algorithm**.

---

# 💻 Full Implementation Code

```python
class LiftManager:
    def __init__(self):
        self.lifts = {}


class Algorithm:
    def __init__(self, lift_manager: LiftManager):
        self.lift_manager = lift_manager
    
    def shortest_route(self, current_floor: int, destination_floor: int):

        # ---------------- UP REQUEST ----------------
        if current_floor < destination_floor:
            for lift in self.lift_manager.lifts:
                lift_data = self.lift_manager.lifts[lift]

                if (
                    lift_data["status"] in ["idle", "up"]
                    and lift_data["current_floor"] <= current_floor
                ):
                    lift_data["status"] = "up"

                    if current_floor not in lift_data["track"]:
                        lift_data["track"].append(current_floor)

                    if destination_floor not in lift_data["track"]:
                        lift_data["track"].append(destination_floor)

                    lift_data["track"].sort()

                    print("Up track:", lift_data["track"])

                    lift_data["current_floor"] = lift_data["track"][0]
                    lift_data["destination_floor"] = lift_data["track"][-1]

                    if len(lift_data["track"]) > 1:
                        print(
                            f"Lift {lift} moving UP from {lift_data['current_floor']} to {lift_data['track'][1]}"
                        )

                    lift_data["track"].pop(0)
                    break
            else:
                print("No lift available")

        # ---------------- DOWN REQUEST ----------------
        else:
            for lift in self.lift_manager.lifts:
                lift_data = self.lift_manager.lifts[lift]

                can_serve = (
                    lift_data["status"] == "idle"
                    or (
                        lift_data["status"] == "down"
                        and lift_data["current_floor"] >= current_floor
                    )
                )

                if can_serve:
                    lift_data["status"] = "down"

                    if lift_data["status"] == "idle":
                        lift_data["track"] = [current_floor]

                    if current_floor not in lift_data["track"]:
                        lift_data["track"].append(current_floor)

                    if destination_floor not in lift_data["track"]:
                        lift_data["track"].append(destination_floor)

                    lift_data["track"].sort(reverse=True)

                    print("Down track:", lift_data["track"])

                    lift_data["current_floor"] = lift_data["track"][0]
                    lift_data["destination_floor"] = lift_data["track"][-1]

                    if len(lift_data["track"]) > 1:
                        print(
                            f"Lift {lift} moving DOWN from {lift_data['current_floor']} to {lift_data['track'][1]}"
                        )

                    lift_data["track"].pop(0)
                    break
            else:
                print("No lift available")


class Lift:
    def __init__(self, total_lifts: int, floors: int, manager: LiftManager):
        self.total_lifts = total_lifts
        self.floors = floors
        self.manager = manager

        for lift in range(1, total_lifts + 1):
            self.manager.lifts[lift] = {
                "current_floor": 1,
                "destination_floor": None,
                "status": "idle",
                "track": [1],
            }


# ---------- Usage ----------
manager = LiftManager()
building = Lift(3, 10, manager)

algo = Algorithm(manager)

algo.shortest_route(3, 5)
algo.shortest_route(5, 9)
algo.shortest_route(5, 7)

# Down requests
algo.shortest_route(9, 2)
algo.shortest_route(7, 1)
algo.shortest_route(1, 3)
algo.shortest_route(6, 3)
```

---

# 🎯 Interview Explanation (Use This)

> “I modeled the elevator system using a central LiftManager storing elevator states and a dispatcher Algorithm that assigns requests based on direction and proximity. Each lift maintains a sorted route queue, ensuring efficient movement similar to SCAN scheduling. The design separates state, entities, and logic, making it scalable and extensible.”

---

# 🚀 Possible Enhancements (Mention in Interviews)

* Distance-based lift selection
* Priority queues
* Async request handling
* Peak-hour zoning
* Load balancing
* Real-time simulation engine

---

# 🏁 Summary

This design demonstrates:

* Object-oriented modeling
* Scheduling optimization
* Dispatcher pattern
* Real-world system mapping

Strong example for:

* LLD interviews
* Backend design rounds
* Machine coding discussions

---
