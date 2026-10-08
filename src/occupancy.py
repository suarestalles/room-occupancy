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
    max_occupancy_value = 0
    peak_start = None
    peak_end = None

    for time, change in events:
        previous_occupancy = current_occupancy
        current_occupancy += change

        if current_occupancy > max_occupancy_value:
            max_occupancy_value = current_occupancy
            peak_start = time
            peak_end = None

        elif (
            previous_occupancy == max_occupancy_value
            and current_occupancy < max_occupancy_value
            and peak_start is not None
            and peak_end is None
        ):
            peak_end = time

    return max_occupancy_value, peak_start, peak_end