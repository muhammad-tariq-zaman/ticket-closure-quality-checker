"""Check closed tickets for closure quality.

Usage: python3 main.py tickets.csv
CSV columns: ticket,has_resolution_note (yes/no),reopened (yes/no).
PASS only when a resolution note exists and the ticket was not
reopened; otherwise FAIL with the reason. Prints the pass rate.
"""
import argparse, csv, sys

def check(rows):
    out = []
    for row in rows:
        note = row["has_resolution_note"].strip().lower() == "yes"
        reopened = row["reopened"].strip().lower() == "yes"
        if note and not reopened:
            out.append((row["ticket"], "PASS", ""))
        elif not note:
            out.append((row["ticket"], "FAIL", "no resolution note"))
        else:
            out.append((row["ticket"], "FAIL", "reopened after closure"))
    return out

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        result = check(list(csv.DictReader(f)))
    passed = sum(1 for _, v, _ in result if v == "PASS")
    for ticket, verdict, reason in result:
        print(f"{ticket}: {verdict}" + (f" ({reason})" if reason else ""))
    rate = passed / len(result) if result else 0
    print(f"Pass rate: {rate:.0%} ({passed}/{len(result)})")
    return 0

if __name__ == "__main__":
    sys.exit(main())
