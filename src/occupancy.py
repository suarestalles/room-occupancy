def max_occupancy(
    bookings: list[tuple[int, int]]
) -> tuple[int, int | None, int | None]:
    """Return the maximum occupancy and the time interval where it occurs."""

    if not bookings:
        return 0, None, None

    events: list[tuple[int, int]] = []

    for start, end in bookings:
        events.append((start, 1))
        events.append((end, -1))

    events.sort()

    current_occupancy = 0
    maximum_occupancy = 0
    peak_start: int | None = None
    peak_end: int | None = None

    for time, delta in events:
        previous_occupancy = current_occupancy
        current_occupancy += delta

        if current_occupancy > maximum_occupancy:
            maximum_occupancy = current_occupancy
            peak_start = time
            peak_end = None

        elif (
            previous_occupancy == maximum_occupancy
            and current_occupancy < maximum_occupancy
            and peak_start is not None
            and peak_end is None
        ):
            peak_end = time

    return maximum_occupancy, peak_start, peak_end