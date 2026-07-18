# Linux Filesystem Cleanup Challenge

**Scenario:** First week as a Junior System Administrator — team lead assigned a high-priority ticket. The directory `~/project/workspace` is a chaotic mess of mixed file types. Mission: restore order by organizing files, backing up critical data, and removing junk.

## Task List
1. Create a directory structure to categorize files
2. Secure critical data by creating a backup
3. Sort files into their respective folders
4. Clean up unnecessary temporary files

## Task 1 — Build the directory structure
```
cd ~/project/workspace
mkdir images
mkdir docs
mkdir backups
```
> Note to self: there's probably a quicker way to do this — turns out `mkdir` just accepts multiple names on one line: `mkdir images docs backups`. See [commands.md](../linux-admin/commands.md).

## Task 2 — Back up critical data
```
cp readme.txt readme.txt.bak
cp readme.txt backups/
```
Used `cp <source> <destination>` to make a safety copy before touching anything else.

## Task 3 — Sort image files
```
ls -a *.jpg
mv *.jpg images/
```
Used the `*` wildcard to find every `.jpg` file, then moved them all into `images/` in one shot.

## Task 4 — Sort document files
```
ls -a *.txt
mv *.txt docs/
```
Same pattern as Task 3, applied to `.txt` files and the `docs/` folder.

## Task 5 — Clean up temp files
```
ls *.tmp
rm *.tmp
```
Listed the temp files first to confirm what would be deleted, then removed them — `rm` doesn't have a trash can, so checking first matters.

## Skills demonstrated
- **Organization** — using `mkdir` to build a directory structure
- **Safety** — using `cp` to back up data before moving/deleting anything
- **Categorization** — using `mv` and wildcards to sort files
- **Hygiene** — using `rm` to clear out junk

Verified everything at each step with `ls`, occasionally adding a flag like `-a` or `-l`.

## Related Notes
- [linux-admin/commands.md](../linux-admin/commands.md) — reference for `mkdir`, `cp`, `mv`, `rm`, and wildcard syntax used in this challenge
- [linux-admin/filesystem-hierarchy.md](../linux-admin/filesystem-hierarchy.md) — absolute vs. relative paths, relevant to the `~/project/workspace` path used here
