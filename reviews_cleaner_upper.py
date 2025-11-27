import csv
import sys

#
#This file was written by copilot
#
#


#!/usr/bin/env python3

IN_FILE = "reviews.csv"
OUT_FILE = "different.csv"

REQUIRED_COLS = [
    "recommendationid",
    "appid",
    "voted_up",  # take the first occurrence of this column name
]

def find_first_index(header_lower, name):
    for i, h in enumerate(header_lower):
        if h == name:
            return i
    return None

def to_int_or_none(s):
    try:
        return int(float(s))
    except Exception:
        return None

def main(in_file=IN_FILE, out_file=OUT_FILE):
    with open(in_file, newline='', encoding='utf-8') as inf, \
         open(out_file, 'w', newline='', encoding='utf-8') as outf:
        reader = csv.reader(inf)
        writer = csv.writer(outf)

        try:
            header = next(reader)
        except StopIteration:
            return

        header_lower = [h.strip().lower() for h in header]

        # find indices for required columns (use first occurrence)
        idx_map = {}
        for name in REQUIRED_COLS:
            idx = find_first_index(header_lower, name)
            if idx is None:
                # missing required column -> stop
                raise SystemExit(f"Missing required column in input CSV: {name}")
            idx_map[name] = idx

        # write output header (use canonical names)
        writer.writerow(REQUIRED_COLS)

        for row in reader:
            # guard against short rows
            if len(row) < max(idx_map.values()) + 1:
                continue

            # extract values
            rec_id = row[idx_map["recommendationid"]].strip()
            appid = row[idx_map["appid"]].strip()
            voted_up = row[idx_map["voted_up"]].strip()


            writer.writerow([rec_id, appid, voted_up])

if __name__ == "__main__":
    # optional: allow passing filenames as args
    if len(sys.argv) >= 3:
        main(sys.argv[1], sys.argv[2])
    else:
        main()