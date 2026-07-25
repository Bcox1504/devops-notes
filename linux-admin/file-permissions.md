# File Permissions

## Reading `ls -l` output
`ls -l` shows the long format for a directory listing — think of it as asking to see the "ID card" for every file.

Example permission string: `drwxrwxr-x`

- **First character is the key:**
  - `d` = directory (folder)
  - `-` = regular file
- The remaining 9 characters break into three groups of `rwx` (read/write/execute): owner, group, and others.

## Related Notes
- [commands.md](commands.md) — the `ls -l` / `ls -a` flags this note is describing
- [filesystem-hierarchy.md](filesystem-hierarchy.md) — directory structure these permissions apply to
