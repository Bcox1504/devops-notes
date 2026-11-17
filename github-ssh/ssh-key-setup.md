# GitHub SSH Key Setup (Mac)

How I switched this repo from HTTPS to SSH so I stop getting locked out when a token expires. SSH keys don't expire, so `git push` just works even if I haven't touched the repo in months.

## Why I did this
Pushed my Terraform notes and got:

```
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/Bcox1504/devops-notes.git/'
```

The remote was HTTPS, and GitHub only takes a personal access token (PAT) for that, not my account password. The token my Mac had saved had expired. The commit itself was fine locally; only the push failed. Committing never touches GitHub, pushing does.

## The setup steps

### 1. Check for an existing key
```bash
ls ~/.ssh
```
If `id_ed25519` and `id_ed25519.pub` show up, skip to step 3. (Mine only had an `agent` folder, which is just macOS stuff, so I didn't have a key yet.)

### 2. Make a key
```bash
ssh-keygen -t ed25519 -C "cox.brandonm@gmail.com"
```
- Press Enter for the default location
- Set a passphrase (the keychain remembers it, so it's not annoying)

This makes two files:
- `id_ed25519` = **private key**. Never share it, never paste it anywhere.
- `id_ed25519.pub` = **public key**. This is the one that goes on GitHub.

### 3. Make the Mac remember the key (`~/.ssh/config`)
```bash
cat > ~/.ssh/config <<'EOF'
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
EOF
```
Then load it into the agent and the keychain:
```bash
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```
Check it worked:
```bash
cat ~/.ssh/config    # should show the 4 lines above
ssh-add -l           # should show a line ending in (ED25519)
```

### 4. Add the public key to GitHub
```bash
pbcopy < ~/.ssh/id_ed25519.pub
```
Run that **in Terminal**. It prints nothing, it just copies the key to the clipboard. Then:
- github.com/settings/keys → **New SSH key**
- Title: "MacBook"
- Type: **Authentication Key** (NOT Signing Key)
- Paste into the Key box with Cmd+V → **Add SSH key** (finish any password/2FA prompt or it won't save)

### 5. Test it
```bash
ssh -T git@github.com
```
First time it asks whether to trust GitHub's fingerprint, so type `yes`. Success looks like:
```
Hi Bcox1504! You've successfully authenticated, but GitHub does not provide shell access.
```
The "no shell access" part is normal. GitHub only lets you use git over SSH, not log in.

### 6. Switch the repo's remote from HTTPS to SSH
```bash
cd ~/Library/CloudStorage/OneDrive-Personal/DevOps-Notes
git remote set-url origin git@github.com:Bcox1504/devops-notes.git
git remote -v        # should show git@github.com:... for fetch and push
git push
git status           # "Your branch is up to date with 'origin/master'"
```

## Stuff that went wrong (and the fixes)

### Running git commands from the wrong folder
```
fatal: not a git repository (or any of the parent directories): .git
```
I was in my home folder (prompt said `brandoncox@Mac ~ %`). Git only works inside a folder with a `.git` in it. Fix: `cd` into the repo first. The prompt should say `DevOps-Notes %`.

### Stuck at a `heredoc>` prompt
The `cat > ~/.ssh/config <<'EOF'` command keeps reading lines until it sees a line that's only `EOF`. I pasted just the first line, so it started eating my next commands as file text.
- Fix: **Ctrl+C** to cancel (nothing gets written), then paste the **whole block at once**, including the final `EOF` line.

### TextEdit didn't save the config file
`cat ~/.ssh/config` said `No such file or directory`. Making the file with the `cat > ... <<'EOF'` command in Terminal is easier than TextEdit (TextEdit can also save as rich text, which breaks it).

### "Key is invalid. You must supply a key in OpenSSH public key format"
GitHub's error when the Key box has something that isn't the key. My clipboard had the `pbcopy` *command* in it instead of the key, since I copied the command from my notes. Fix: run `pbcopy` in Terminal first, OR run `cat ~/.ssh/id_ed25519.pub` and copy the output. A valid key is one line that starts with `ssh-ed25519 AAAA` and ends with my email.

### `Permission denied (publickey)`
Means GitHub doesn't recognize the key. To debug:
```bash
ssh-add -l              # is the key loaded on my Mac?
ls ~/.ssh               # does the key file exist?
ssh -vT git@github.com  # verbose: shows exactly what happens
```
In the `-vT` output, the important part is:
- `Offering public key: ... id_ed25519 ... SHA256:...` means my Mac is sending the key (good)
- followed right after by `Authentications that can continue: publickey` means **GitHub rejected it**

So the Mac side was fine and the problem was on GitHub: the key wasn't actually saved on my account (bad paste, see above). Other things that cause this: key added under Signing keys instead of Authentication keys, added to the wrong GitHub account, or added as a repo deploy key.

**Quick check:** the `SHA256:...` fingerprint on github.com/settings/keys should match what `ssh-add -l` shows.

## Takeaways
- HTTPS remote = needs a token that expires. SSH remote = key that doesn't. For a repo I don't update often, SSH is way less hassle.
- Public key (`.pub`) goes on GitHub. Private key stays on my Mac, period.
- `ssh -T git@github.com` is the go-to test before blaming git.
- New Mac or reinstall? Redo steps 2–5 and add the new key on GitHub. Old keys can be deleted from github.com/settings/keys.

## Related Notes
- [aws-app-monitoring-pipeline/troubleshooting/git-push-troubleshooting.md](../aws-app-monitoring-pipeline/troubleshooting/git-push-troubleshooting.md): the earlier push walkthrough (ahead-of-origin, `git status` before pushing)
