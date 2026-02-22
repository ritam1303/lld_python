class LiftManager:
    def __init__(self):
        self.lifts = {}


class Algorithm:
    def __init__(self, lift_manager: LiftManager):
        self.lift_manager = lift_manager
    
    def shortest_route(self, current_floor: int, destination_floor: int):
        if current_floor < destination_floor:
            # Lift going UP: pick lift that is idle or already going up, at or below pickup floor
            for lift in self.lift_manager.lifts:
                if (self.lift_manager.lifts[lift]["status"] == "idle" or self.lift_manager.lifts[lift]["status"] == "up") and self.lift_manager.lifts[lift]["current_floor"] <= current_floor:
                    self.lift_manager.lifts[lift]["status"] = "up"
                    if current_floor not in self.lift_manager.lifts[lift]["track"]:
                        self.lift_manager.lifts[lift]["track"].append(current_floor)
                    if destination_floor not in self.lift_manager.lifts[lift]["track"]:
                        self.lift_manager.lifts[lift]["track"].append(destination_floor)
                    self.lift_manager.lifts[lift]["track"].sort()
                    print("Up track:", self.lift_manager.lifts[lift]["track"])
                    self.lift_manager.lifts[lift]["current_floor"] = min(current_floor, self.lift_manager.lifts[lift]["track"][0])
                    self.lift_manager.lifts[lift]["destination_floor"] = max(self.lift_manager.lifts[lift]["track"])
                    if len(self.lift_manager.lifts[lift]["track"]) > 1:
                        print(f"Lift {lift} is moving up from {self.lift_manager.lifts[lift]['current_floor']} to {self.lift_manager.lifts[lift]['track'][1]}")
                    else:
                        print(f"Lift {lift} is moving up from {self.lift_manager.lifts[lift]['current_floor']} to {current_floor}")
                    self.lift_manager.lifts[lift]["track"].pop(0)
                    break
            else:
                print("No lift is available")
        else:
            # Lift going DOWN: pick lift that is idle or already going down, at or above pickup floor
            for lift in self.lift_manager.lifts:
                lift_data = self.lift_manager.lifts[lift]
                can_serve = (
                    lift_data["status"] == "idle"
                    or (lift_data["status"] == "down" and lift_data["current_floor"] >= current_floor)
                )
                if can_serve:
                    self.lift_manager.lifts[lift]["status"] = "down"
                    # Idle lift: start track from pickup floor; down lift: keep existing track
                    if lift_data["status"] == "idle":
                        self.lift_manager.lifts[lift]["track"] = [current_floor]
                    if current_floor not in self.lift_manager.lifts[lift]["track"]:
                        self.lift_manager.lifts[lift]["track"].append(current_floor)
                    if destination_floor not in self.lift_manager.lifts[lift]["track"]:
                        self.lift_manager.lifts[lift]["track"].append(destination_floor)
                    self.lift_manager.lifts[lift]["track"].sort(reverse=True)  # descending for down
                    print("Down track:", self.lift_manager.lifts[lift]["track"])
                    self.lift_manager.lifts[lift]["current_floor"] = max(current_floor, self.lift_manager.lifts[lift]["track"][0])
                    self.lift_manager.lifts[lift]["destination_floor"] = min(self.lift_manager.lifts[lift]["track"])
                    if len(self.lift_manager.lifts[lift]["track"]) > 1:
                        print(f"Lift {lift} is moving down from {self.lift_manager.lifts[lift]['current_floor']} to {self.lift_manager.lifts[lift]['track'][1]}")
                    else:
                        print(f"Lift {lift} is moving down from {self.lift_manager.lifts[lift]['current_floor']} to {current_floor}")
                    self.lift_manager.lifts[lift]["track"].pop(0)
                    break
            else:
                print("No lift is available")

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
                "track": [1]
            }
            


# ---------- Usage ----------
manager = LiftManager()
building = Lift(3, 10, manager)

algo = Algorithm(manager)
algo.shortest_route(3, 5)
algo.shortest_route(5, 9)
algo.shortest_route(5, 7)
# Down requests (accumulated on same lift when going down)
algo.shortest_route(9, 2)
algo.shortest_route(7, 1)
algo.shortest_route(1, 3)
algo.shortest_route(6, 3)