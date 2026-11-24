# The Funniest Out-of-Office

Entry for make.fun's "The Funniest Out-of-Office" bounty
(`u-kreutzx-the-funniest-out-of-office-054815cf`).

The program writes one line of an out-of-office auto-reply — the
funniest one line we could write — to `/output/entry.txt`:

> I'm out of the office until next week. My inbox was left unsupervised and, last I checked, was quietly interviewing my replacement.

One line, 131 characters, deterministic: the same bytes on every run.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
