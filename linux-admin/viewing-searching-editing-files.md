# Viewing, Searching, & Editing Files in Linux

## Three fundamental ways to look inside a file
1. **`cat`** — reads the entire file at once. Best for small notes/files
2. **`head`** — reads just the beginning ("headline"). Best for checking what a file is about
3. **`tail`** — reads just the end. Best for checking the latest updates in a log file

## head
- Shows the first 10 lines by default
- `-n` (number flag) — tells `head` exactly how many lines you want, e.g. `head -n 20 file.log`

## tail
- Same `-n` flag works the same way as `head`, e.g. `tail -n 20 file.log`
- **In Linux, logs are written sequentially — the "newest" entry is always at the bottom.** This is exactly why `tail` (not `head`) is the tool for checking what just happened
- `-f` flag — stands for **follow**. If a program writes a new line to the file, `tail -f` catches it and prints it instantly. It's like watching a live news ticker — the standard way to watch a log file in real time as a system runs

## Related Notes
- [commands.md](commands.md) — the general command basics (`ls`, `cd`, etc.) these viewing tools build on
- [filesystem-hierarchy.md](filesystem-hierarchy.md) — where log files typically live (`/var/log`)
