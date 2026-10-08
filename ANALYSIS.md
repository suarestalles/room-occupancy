# Analysis

1. Approach

The solution uses a sweep-line algorithm based on booking start and end events.

Each booking is represented by two events:

* `(start, +1)` when a booking starts.
* `(end, -1)` when a booking ends.

All events are then sorted by timestamp. The algorithm processes the sorted events from left to right while maintaining the current room occupancy.

When the current occupancy becomes greater than the maximum occupancy found so far, a new peak interval starts. When the occupancy drops below the current maximum, the peak interval ends at that timestamp.

This approach avoids comparing every booking against every other booking.

## 2. Algorithm

For example, given:

```text
(9, 12)
(10, 13)
(11, 14)
```

the bookings are converted into:

```text
9  -> +1
10 -> +1
11 -> +1
12 -> -1
13 -> -1
14 -> -1
```

After sorting, the algorithm performs a single sweep:

```text
Time    Change    Occupancy
9       +1        1
10      +1        2
11      +1        3
12      -1        2
13      -1        1
14      -1        0
```

The maximum occupancy is `3`, and it occurs from `11` to `12`.

The returned result is therefore:

```python
(3, 11, 12)
```

### Simultaneous start and end events

The implementation uses Python tuple ordering when sorting events.

For events occurring at the same timestamp:

```python
(12, -1)
(12, +1)
```

the end event is processed before the start event because `-1 < +1`.

This matches the interval semantics used by the examples: bookings are treated as half-open intervals `[start, end)`.

Therefore, a booking ending at time `T` is no longer active at `T`, while another booking starting at `T` becomes active at `T`.

For example:

```python
[(9, 10), (10, 11)]
```

has a maximum occupancy of `1`, not `2`.

## 3. Complexity

Let `n` be the number of bookings.

Each booking produces two events, resulting in `2n` events.

### Time complexity

* Creating the events: `O(n)`
* Sorting the events: `O(n log n)`
* Sweeping through the events: `O(n)`

Therefore, the overall time complexity is:

```text
O(n log n)
```

The sorting step dominates the total running time.

### Space complexity

The algorithm stores two events for every booking.

Therefore, the additional memory required is:

```text
O(n)
```

This is necessary because the events must be stored before sorting.

## 4. Why This Approach Scales

A naive pairwise approach could compare every booking with every other booking, resulting in `O(n²)` time complexity.

For hundreds of thousands of bookings, that approach would require an impractical number of comparisons.

The event-based approach reduces the problem to sorting the event timestamps and performing a linear sweep afterward.

Its `O(n log n)` time complexity makes it substantially more suitable for large input volumes.

## 5. Edge Cases

The test suite covers the following cases:

* Empty booking list.
* A single booking.
* Multiple overlapping bookings.
* Completely non-overlapping bookings.
* Multiple bookings starting at the same time.
* Multiple bookings ending at the same time.
* Bookings ending and starting at the same timestamp.
* Identical bookings.
* A peak that starts after an initial booking.
* Multiple separate peak intervals with the same maximum occupancy.
* Multiple endings and starts occurring at the same timestamp.

The implementation was validated with all official examples and the additional edge cases above.

## 6. Assumptions and Unspecified Behavior

### Interval semantics

Bookings are treated as half-open intervals:

```text
[start, end)
```

This means the start time is included and the end time is excluded.

This behavior is consistent with the provided example where:

```python
[(9, 10), (10, 11), (11, 12)]
```

returns:

```python
(1, 9, 10)
```

rather than considering the bookings overlapping at their boundaries.

### Multiple maximum occupancy periods

The problem statement does not specify what should happen if multiple separate time intervals have the same maximum occupancy.

The implementation deterministically returns the first maximum-occupancy interval in chronological order.

For example:

```python
[(9, 11), (10, 11), (14, 16), (15, 16)]
```

returns:

```python
(2, 10, 11)
```

### Invalid intervals

The implementation assumes that bookings are valid intervals where:

```text
start < end
```

The problem statement does not define behavior for invalid bookings, so invalid intervals are considered outside the function's input contract.

7. Testing

The implementation is tested with pytest.

The current test suite contains 11 tests covering the official examples, normal scenarios, boundary conditions, and edge cases.

At the time of writing, all 11 tests pass.

During development, testing also identified a case where separate peak intervals with the same occupancy could incorrectly be merged into a single interval. The implementation was adjusted so that once a peak interval has ended, a later interval with the same occupancy is treated as a separate peak.

## 8. AI Usage

AI tools were used as a development aid during the implementation.

They were used for:

* Discussing algorithmic approaches and their complexity.
* Reviewing variable naming and code readability.
* Identifying relevant edge cases.
* Suggesting additional tests.
* Reviewing the implementation against the requirements.
* Structuring and improving the project documentation.

The final implementation was reviewed and tested manually. I understand the algorithm, its complexity, its assumptions, and the test cases included in the project.
