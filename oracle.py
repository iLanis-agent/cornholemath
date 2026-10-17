#!/usr/bin/env python3
# Cornhole Math oracle - mirrors engine.js float-for-float.
import json, math

def _side(on, in_hole, who):
    if not math.isfinite(on) or on < 0 or not math.isfinite(in_hole) or in_hole < 0:
        raise ValueError("bag counts must be zero or more")
    if on + in_hole > 4:
        raise ValueError(who + " only throws 4 bags")
    return on + 3 * in_hole

def frame_truth(my_on, my_in, their_on, their_in):
    mine = _side(my_on, my_in, "a side")
    theirs = _side(their_on, their_in, "a side")
    if mine == theirs:
        return f"{mine} against {theirs} - cancellation washes the frame, nobody moves."
    if mine > theirs:
        return (f"Your {my_on} on the board and {my_in} in the hole are {mine} against their "
                f"{theirs} - cancellation leaves {mine - theirs} for you.")
    return (f"Their {their_on} on the board and {their_in} in the hole are {theirs} against your "
            f"{mine} - cancellation leaves {theirs - mine} for them.")

def score_truth(current, frame_points):
    if not math.isfinite(current) or current < 0 or current >= 21:
        raise ValueError("the game is already over")
    if not math.isfinite(frame_points) or frame_points < 0 or frame_points > 12:
        raise ValueError("a frame scores at most 12")
    nxt = current + frame_points
    if nxt >= 21:
        return f"{current} plus {frame_points} is {nxt} - game, you reach 21."
    return f"{current} plus {frame_points} is {nxt} - {21 - nxt} from 21."

def comeback_truth(mine, theirs):
    for s in (mine, theirs):
        if not math.isfinite(s) or s < 0 or s >= 21:
            raise ValueError("scores must be under 21")
    if mine >= theirs:
        return f"You are not behind - {mine} to {theirs}."
    deficit = theirs - mine
    frames = math.ceil(deficit / 12)
    f_word = "frame" if frames == 1 else "frames"
    return (f"Down {deficit}, and a frame can swing at most 12 - at least {frames} "
            f"perfect {f_word} to catch up.")

CASES = [
    ("frameTruth", (2, 1, 3, 0)),
    ("frameTruth", (0, 1, 0, 0)),
    ("frameTruth", (4, 0, 0, 1)),
    ("frameTruth", (1, 1, 1, 1)),
    ("frameTruth", (0, 0, 0, 2)),
    ("frameTruth", (3, 2, 0, 0)),
    ("scoreTruth", (15, 4)),
    ("scoreTruth", (19, 4)),
    ("scoreTruth", (21, 2)),
    ("scoreTruth", (15, 13)),
    ("comebackTruth", (15, 20)),
    ("comebackTruth", (6, 20)),
    ("comebackTruth", (20, 15)),
]

FNS = {"frameTruth": frame_truth, "scoreTruth": score_truth, "comebackTruth": comeback_truth}

out = []
for name, args in CASES:
    try:
        expected = FNS[name](*args)
    except ValueError as e:
        expected = "ERR:" + str(e)
    out.append({"fn": name, "args": list(args), "expected": expected})

with open("expected.json", "w") as f:
    f.write(json.dumps(out, indent=2) + "\n")
print(f"{len(out)} cases written")
