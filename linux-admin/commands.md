# Linux Command Basics

## Terminal vs Shell
- **Terminal**: the text window you interact with
- **Shell**: the program inside the terminal that reads your commands and asks Linux to run them (e.g. zsh, bash)

## Check who/where you are
- `whoami` — confirms who you are. Good habit: before doing anything else on a system, confirm your user and environment
- `pwd` — Print Working Directory, shows your exact location in the file system
- `hostname` — the human-usable name of a machine on a network. Knowing it matters when managing multiple servers, so you're sure you're on the right one

## Reading the prompt
Standard prompt example: `labex:project/ $`
- `labex` = current username
- `project/` = current directory (short for `/home/labex/project`)
- `$` = standard user

Root/admin prompt looks different: `root@hostname:~#`

## sudo and exit
- `sudo` = "SuperUser Do" — runs a single command with admin privileges
- `exit` — returns a root session to the standard user and closes the session

## Basic output/utility commands
- `echo` — prints text back to the screen, often used for status updates or instructions; wrap text in quotes `" "`
- `date` — asks the system for the current time
- `clear` (or the shortcut Ctrl+L) — doesn't erase your work or command history, just redraws the screen for readability. Professionals rarely type `clear` — they use the shortcut
- `$USER` — variable that displays the current user

## Core cycle of using Linux
Input → Execution → Output

## Decoding common errors
- `zsh` showing up in an error = that's just the shell (your assistant) speaking, not the actual problem
- `command not found` = the real issue — the shell searched for the program and couldn't find it
- A placeholder-looking name (e.g. `foobar`) = whatever command you tried to run; this can be any command that doesn't exist

> When working on remote servers, it's good practice to log out properly when finished.

## Navigation
- `cd` — Change Directory, changes the shell's current context/location. Usually prints nothing if it works — in Linux, no news is good news
- `cd ..` — moves up one level (parent directory); can be chained, e.g. `cd ../..` moves up two levels at once
- `~` (tilde) — teleports you home instantly from anywhere in the system
- Use `pwd` after `cd` to verify you actually moved — see [filesystem-hierarchy.md](filesystem-hierarchy.md) for absolute vs. relative paths and what the major directories are for

## Listing files
- `ls` — "list," lets you look around
  - `ls -a` — show hidden files (dotfiles) — see [filesystem-hierarchy.md](filesystem-hierarchy.md)
  - `ls -l` — long format, shows details for every file, including permissions — see [file-permissions.md](file-permissions.md)
  - `ls -la` — flags can be combined: long details of all files
  - `ls -R` (capital R) — recursive, shows everything inside every sub-folder
  - **Careful:** `ls -r` (lowercase) does something completely different — it reverses sort order. Linux commands are case sensitive.

## Getting help
- `man <command>` — short for "manual," opens reference docs (man pages) for a command
- `--help` flag — prints a quick summary directly to the screen

## Creating and copying files/directories
- `touch <file>` — creates an empty file, a blank page waiting for content
- `mkdir <name>` — creates a directory (folder)
  - `-p` (parents) flag — tells `mkdir` to create any missing parent directories along the way
  - `-v` flag — verbose output
- `cp <source> <destination>` — copy
- `mv <source> <destination>` — move (also used to rename)

## Removing files & directories safely
- When you delete a file in the Linux terminal, it's gone — instantly, permanently, no trash can to pull it back out of
- `rm <file>` — shreds an individual file; think of it as a paper shredder, not a recycle bin
- `rmdir <directory>` — deletes a directory, but refuses if there's anything inside it — a built-in safety lock
- To delete a folder and everything inside it, use `rm` with two flags together:
  - `-r` (recursive) — go inside every subfolder
  - `-f` (force) — don't ask for confirmation
  - `rm -rf` is sometimes called "the bulldozer" — it's the most dangerous command in Linux, since there's no undo
- **Always double-check the file/path name before hitting enter.** Look before you act — one of the healthiest habits in Linux

## Wildcards (globbing)
Wildcards act like a joker card in a deck — they stand in for other characters when matching filenames.
- `*` — the most common wildcard, matches any number of characters (including zero)
  - `ls *.txt` — lists all files ending in `.txt`
  - `data_*` matches anything starting with `data_`
- `?` — matches exactly one character
  - `temp_?` matches only if there's exactly one character after the underscore
  - `rm temp_?` would remove all files named `temp_` followed by exactly one character

## Related Notes
- [filesystem-hierarchy.md](filesystem-hierarchy.md) — the directory structure these commands move around and operate in
- [file-permissions.md](file-permissions.md) — what the permission info from `ls -l` actually means
- [../challenges/linux-filesystem-cleanup-challenge.md](../challenges/linux-filesystem-cleanup-challenge.md) — hands-on practice applying `mkdir`, `cp`, `mv`, wildcards, and `rm` together
