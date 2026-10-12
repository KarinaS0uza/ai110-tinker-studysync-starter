"""
Tinker 1B, Part 1: write an assert-based pytest test for session_rating()
BEFORE you touch anything else. One test is started for you -- add at least
one more.
"""

from scoring import session_rating


def test_session_rating_boundary_90_is_great():
    assert session_rating(90) == "Great"


def test_session_rating_boundary_80_is_good():
    assert session_rating(80) == "Good"


# Part 3: breaker inputs tried in a Python shell; preserve existing behavior.
# -1 returned "Skip"; flag out of scope because negative scores are outside 0-100.
# 101 returned "Great"; flag out of scope because it exceeds the score range.
# 87.5 returned "Good"; flag out of scope because this activity uses integer scores.
