# pgp key review protocol

**All modifications to the `keys.txt` file should follow this protocol as a base.**

Both the comment message and the github pull-request message should in the following form:

```
{Add/Update} {User_ID} {(Github_Username)} pgp key {into/in} the keys.txt file.

Before merging, Please:

1. Import the key into your local gpg database:
$ gpg --keyserver hkps://keys.openpgp.org --recv-keys {Full_Key_ID}

2. Print the full-key info:
$ gpg --with-subkey-fingerprint --list-key {Full_Key_ID}

3. Print the commit author info, commit signature details, and diff:
$ git show --show-signature [git commit]

and then Verify:

* The commit `keys.txt' diff fingerprint is identical to:
    the `pub` fingerprint in the gpg key info.

* The commit `keys.txt' diff has the same name as the:
    the commit author name.
    the gpg key info.

* The commit `keys.txt' diff has the same username (in brackets) as:
    the github username for the pull-request.

* The commit signing key fingerprint is listed in:
    the gpg key info.

* The commit author email address is listed in:
    the gpg key info.
```
**Edit this message where indicated by the {curly brackets}.**

### * *The creator of the pull request should be different to the merging user.*

### * *There should be extra review when updating an existing key.*
