# ticket-closure-quality-checker

Audit closed tickets: a closure passes only with a resolution note and no reopen — everything else is listed with its reason, plus the overall pass rate.

## How to run

```sh
python3 main.py tickets.csv
```

## Example output

```
T-101: PASS
T-102: FAIL (no resolution note)
Pass rate: 50% (1/2)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
