# Linux Filesystem Hierarchy

There's no "C:" or "D:" drive like Windows — everything in Linux is organized into a single, massive tree structure.

## The tree (upside down)
- **Root (`/`)** is at the top
- **Directories** (branches) spread downward
- **Files** (leaves) hang at the ends

## Absolute vs. relative paths
- A **path** is the written address of a location in the file system. Linux uses `/` to separate each level.
- **Absolute path** — starts with `/` (like `/tmp`), telling the system "start looking from the very top (root)." Think of it as a fixed address.
- **Relative path** — relative to wherever you already are. Linux gets a lot more comfortable once you understand moving relative to your current location.
- `.` — represents the current directory
- `..` — represents the parent directory (one level up)

## Home directory
- `/home` is where your files live
- `ls /` shows the system (root)
- `ls ~` shows your stuff (home)

> **Root directory ≠ root user.** Root directory is the top of the file system. Root user is the administrator account. Not the same thing.

## Key directories (Filesystem Hierarchy Standard / FHS)
FHS describes the expected purpose of the major directories:

- `/boot` — startup files
- `/dev` — hardware devices
- `/tmp` — temporary scratch pad; short-lived working files, caches, or intermediate data. Treat it as a temporary workspace, not a permanent home for important files
- `/usr` — user programs and data
- `/bin` — binaries; the system's toolbox. When you run a command like `ls` or `cp`, the system looks in `/bin` to find the "tool"
- `/etc` — where configuration lives ("Editable Text Configuration"). Basically the settings app for the system. Files ending in `.conf` are commonly named after the software they configure

> Commands aren't magic — they're just programs stored in a directory (like `/bin`), waiting for you to run them.

## Hidden files
Any file starting with a dot (`.`) is hidden from a standard `ls`. These are usually configuration files, often called "dotfiles" — many Linux tools and shells use them to store settings in a user's home directory. Use `ls -a` to see them.

## Related Notes
- [commands.md](commands.md) — the commands (`cd`, `ls`, `pwd`, etc.) used to move around and inspect this structure
- [file-permissions.md](file-permissions.md) — how to read permissions once you're looking at a directory listing
