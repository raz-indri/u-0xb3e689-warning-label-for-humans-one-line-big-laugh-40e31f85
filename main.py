#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the winning single-line safety warning label to /output/entry.txt
(and prints it to stdout). The entry is one line, 145 characters, UTF-8.

The line below is the duel winner: 7 drafts were written, then every pair
was judged both ways against the brief (label for humans first, laugh in
one read with the turn in the last few words, true about people, real-label
wording, inside 160 characters). This draft went 6-0: the concrete scene
(214 unread-but-read messages, zero replies) escalates into the punch
"personally attacked by all of them" in the final words, which is exactly
how humans actually behave in group chats.
"""

import os

ENTRY = (
    "WARNING: Do not leave unattended near a group chat. "
    "This unit will read 214 messages, reply to none, "
    "and feel personally attacked by all of them."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
