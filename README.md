# Room Occupancy

## Overview

This project implements an efficient solution to calculate the maximum room occupancy from a list of bookings.

For each booking, the function returns:

* The maximum number of simultaneous bookings.
* The start time of the peak occupancy.
* The end time of the peak occupancy.

The solution uses a sweep-line algorithm based on sorted booking start and end events.

## Requirements

* Python 3.11+
* pytest

## Setup

Clone the repository and navigate to the project directory.

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

## Running the Tests

Run the complete test suite with:

```powershell
pytest
```

The project includes tests for the official examples, overlapping and non-overlapping bookings, simultaneous start/end events, multiple peak intervals, and other edge cases.

## Usage

The main function is available in `src/occupancy.py`:

```python
from src.occupancy import max_occupancy

result = max_occupancy(
    [(9, 12), (10, 13), (11, 14)]
)

print(result)
```

Output:

```text
(3, 11, 12)
```

The function signature is:

```python
def max_occupancy(
    bookings: list[tuple[int, int]]
) -> tuple[int, int | None, int | None]:
    ...
```

Bookings are treated as half-open intervals `[start, end)`. Therefore, a booking ending at the same time another booking starts does not overlap with it.

For an empty list, the function returns:

```python
(0, None, None)
```

## Algorithm

The algorithm converts every booking into two events:

* `(start, +1)` when a booking starts.
* `(end, -1)` when a booking ends.

The events are sorted by timestamp and processed sequentially while tracking the current occupancy and the maximum occupancy found so far.

When multiple events have the same timestamp, end events are processed before start events. This is achieved by sorting `(timestamp, delta)` tuples, since `-1` is ordered before `+1`.

For more details about the algorithm, complexity, assumptions, edge cases, and design decisions, see [`ANALYSIS.md`](ANALYSIS.md).

## Complexity

* Time: `O(n log n)`
* Additional space: `O(n)`

The sorting of the `2n` generated events is the dominant operation.

## Video

Video link: *To be added before submission.*
