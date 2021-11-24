# github-merge

A small script to automate merging pull-requests securely and sign them with GPG.

For example, if the "to" repo is identical to the "from" repo:

```bash
./github-merge.py 1234
```

(in any git repository) will help you merge pull request #1234 for the configured repository.

Otherwise, for a differing "from" repo:

```bash
./github-merge.py --repo-from=bitcoin-core/gui 1234
```

will fetch the pull request from another monotree repository. Be sure to also set `githubmerge.pushmirrors` (see below).

What it does:

* Fetch master and the pull request.
* Locally construct a merge commit.
* Show the diff that merge results in.
* Ask you to verify the resulting source tree (so you can do a make check or whatever).
* Ask you whether to GPG sign the merge commit.
* Ask you whether to push the result upstream.

This means that there are no potential race conditions (where a
pull request gets updated while you're reviewing it, but before you click
merge), and when using GPG signatures, that even a compromised GitHub
couldn't mess with the sources.

## Setup

Configuring the github-merge tool for the bitcoin repository is done in the following way:

```bash
git config githubmerge.repository bitcoin/bitcoin
git config githubmerge.pushmirrors "git@github.com:bitcoin-core/gui.git,
git@github.com:YourPrivateMirror/bitcoin-core.git"
git config githubmerge.testcmd "make -j4 check" (adapt to whatever you want to use for testing)
git config --global user.signingkey mykeyid
```

If you want to use HTTPS instead of SSH for accessing GitHub, you need set the host additionally:

```bash
git config githubmerge.host "https://github.com"  (default is "git@github.com", which implies SSH)
```

## Authentication (optional)

The API request limit for unauthenticated requests is quite low, but the
limit for authenticated requests is much higher. If you start running
into rate limiting errors it can be useful to set an authentication token
so that the script can authenticate requests.

* First, go to [Personal access tokens](https://github.com/settings/tokens).
* Click 'Generate new token'.
* Fill in an arbitrary token description. No further privileges are needed.
* Click the `Generate token` button at the bottom of the form.
* Copy the generated token (should be a hexadecimal string)

Then do:

git config --global user.ghtoken "pasted token"

## Create and verify timestamps of merge commits

To create or verify timestamps on the merge commits, install the OpenTimestamps
client via `pip3 install opentimestamps-client`. Then, download the gpg wrapper
`ots-git-gpg-wrapper.sh` and set it as git's `gpg.program`. See
[the ots git integration documentation](https://github.com/opentimestamps/opentimestamps-client/blob/master/doc/git-integration.md#usage)
for further details.
