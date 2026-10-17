// Cornhole Math engine - cancellation scoring, run exactly.
// Mirrored float-for-float by oracle.py; keep the op order identical.

function _side(on, inHole, who) {
  if (!isFinite(on) || on < 0 || !isFinite(inHole) || inHole < 0) {
    throw new Error("bag counts must be zero or more");
  }
  if (on + inHole > 4) throw new Error(who + " only throws 4 bags");
  return on + 3 * inHole;
}

// The frame truth: board 1, hole 3, and only the difference counts.
function frameTruth(myOn, myIn, theirOn, theirIn) {
  var mine = _side(myOn, myIn, "a side");
  var theirs = _side(theirOn, theirIn, "a side");
  if (mine === theirs) {
    return mine + " against " + theirs + " - cancellation washes the frame, nobody moves.";
  }
  if (mine > theirs) {
    return "Your " + myOn + " on the board and " + myIn + " in the hole are " + mine +
      " against their " + theirs + " - cancellation leaves " + (mine - theirs) + " for you.";
  }
  return "Their " + theirOn + " on the board and " + theirIn + " in the hole are " + theirs +
    " against your " + mine + " - cancellation leaves " + (theirs - mine) + " for them.";
}

// The scoreboard truth: what a frame does to the race to 21.
function scoreTruth(current, framePoints) {
  if (!isFinite(current) || current < 0 || current >= 21) throw new Error("the game is already over");
  if (!isFinite(framePoints) || framePoints < 0 || framePoints > 12) {
    throw new Error("a frame scores at most 12");
  }
  var next = current + framePoints;
  if (next >= 21) {
    return current + " plus " + framePoints + " is " + next + " - game, you reach 21.";
  }
  return current + " plus " + framePoints + " is " + next + " - " + (21 - next) + " from 21.";
}

// The comeback truth: how much a frame can actually swing.
function comebackTruth(mine, theirs) {
  if (!isFinite(mine) || mine < 0 || mine >= 21 || !isFinite(theirs) || theirs < 0 || theirs >= 21) {
    throw new Error("scores must be under 21");
  }
  if (mine >= theirs) {
    return "You are not behind - " + mine + " to " + theirs + ".";
  }
  var deficit = theirs - mine;
  var frames = Math.ceil(deficit / 12);
  var fWord = frames === 1 ? "frame" : "frames";
  return "Down " + deficit + ", and a frame can swing at most 12 - at least " + frames +
    " perfect " + fWord + " to catch up.";
}
