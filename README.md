# 🚆 Train Intercept Planner

Your friend is riding a train that loops endlessly around a fixed set of stations. You're driving around a city of one-way roads, where each road has a **cost** and a **travel time**. Where and when should you drive so you arrive at a station **at the exact moment** your friend's train is there, while spending as little as possible?

This project solves that with a **time-expanded graph** and a modified **Dijkstra's algorithm**, implemented from scratch in Python.

---

## 🧠 How it works

1. **Time-layered ("multiverse") graph.** Because the train's position repeats every loop, each node is a pair *(location, minute within the train's cycle)*. Driving a road moves you to a new location **and** forward in time.
2. **Train schedule.** The friend's position at every minute of the cycle is precomputed from the station list.
3. **Modified Dijkstra.** It explores states in order of **lowest cost**, breaking ties by **shortest total driving time**, using a hand-built **min-heap** priority queue with decrease-key.
4. **Interception.** The first state where you're at the same station at the same time as your friend is optimal, and the route is rebuilt by backtracking. If no such state is reachable, it returns `None`.

The optimal route can revisit the same location several times, for example circling to wait for the train to come round again.

---

## 🚀 Usage

```python
from intercept_planner import intercept

roads = [(0, 1, 10, 7), (0, 2, 10, 3), (2, 0, 1, 4), (1, 0, 1, 7)]  # (from, to, cost, minutes)
stations = [(2, 4), (1, 3)]                                        # (station, minutes to next station)

intercept(roads, stations, start=0, friendStart=1)
# -> (10, 3, [0, 2])   total cost, total driving time, route
```

```bash
python -m unittest test_intercept_planner    # 4 scenarios, all pass
```

The tests cover a simple interception, an **unsolvable** map, a route that **revisits** locations, and two equal-cost routes where the **faster** one must win.

## 🛠️ Tech
Python 3 · graph modelling · Dijkstra's algorithm · binary min-heap (no external libraries)
