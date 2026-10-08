from src.occupancy import max_occupancy


def test_overlapping_bookings():
    assert max_occupancy(
        [(9, 12), (10, 13), (11, 14)]
    ) == (3, 11, 12)


def test_non_overlapping_bookings():
    assert max_occupancy(
        [(9, 10), (10, 11), (11, 12)]
    ) == (1, 9, 10)


def test_empty_bookings():
    assert max_occupancy([]) == (0, None, None)


def test_multiple_peak_intervals_returns_first_peak():
    assert max_occupancy(
        [(9, 11), (10, 11), (14, 16), (15, 16)]
    ) == (2, 10, 11)


def test_simultaneous_end_and_start():
    assert max_occupancy(
        [(9, 12), (10, 12), (12, 15)]
    ) == (2, 10, 12)


def test_single_booking():
    assert max_occupancy(
        [(10, 15)]
    ) == (1, 10, 15)


def test_multiple_bookings_starting_at_same_time():
    assert max_occupancy(
        [(10, 15), (10, 14), (10, 13)]
    ) == (3, 10, 13)


def test_multiple_bookings_ending_at_same_time():
    assert max_occupancy(
        [(9, 12), (10, 12), (11, 12)]
    ) == (3, 11, 12)


def test_identical_bookings():
    assert max_occupancy(
        [(9, 12), (9, 12), (9, 12)]
    ) == (3, 9, 12)


def test_peak_starts_after_initial_booking():
    assert max_occupancy(
        [(9, 15), (10, 14), (11, 13)]
    ) == (3, 11, 13)


def test_multiple_endings_and_starting_at_same_time():
    assert max_occupancy(
        [
            (9, 12),
            (10, 12),
            (11, 12),
            (12, 15),
            (12, 16),
        ]
    ) == (3, 11, 12)