"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter to /output/entry.txt: "A" for coffee.
The gate requires UTF-8 text of exactly 1 character, so no newline.
"""

import os

ENTRY = "A"  # A = coffee: the bolder, more vivid answer — the standing
# answer in the coffee-against-tea argument. One letter, nothing else.


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
