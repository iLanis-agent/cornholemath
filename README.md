# Cornhole Math

Cornhole scoring honesty. Only the difference counts - and nobody at the barbecue keeps it straight. Cornhole Math runs the game's published scoring exactly: 1 on the board, 3 in the hole, cancellation, first to 21.

## What it computes

- **The frame truth** - both sides' bags to frame points under cancellation: your 2 on the board and 1 in the hole are 5 against their 3 - cancellation leaves 2 for you.
- **The scoreboard truth** - a frame's points against the race to 21: 15 plus 4 is 19, 2 from 21.
- **The comeback truth** - the most a frame can swing is 12: down 14, at least 2 perfect frames to catch up.

## Boundary

Rules arithmetic only. Cornhole Math never rules on a foot foul or a leaning bag - the backyard has its own referees.

## Files

- `index.html` - landing page with the honesty pitch and the boundary.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic, shared by the app and the tests.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (13 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/cornholemath/
Repo: https://github.com/iLanis-agent/cornholemath
