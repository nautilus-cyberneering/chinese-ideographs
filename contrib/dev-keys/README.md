## PGP keys of Developers

↳ For Review Process of Adding Keys see: [pgp Key Review Protocol](pgp_key_review_protocol.md)

The file `keys.txt` contains fingerprints of the public keys of active developers.

The most recent version of each pgp key can be found on most pgp key servers.

Fetch the latest version from the key server to see if any key was revoked in the meantime.
To fetch the latest version of all pgp keys in your gpg homedir,

```sh
gpg --refresh-keys
```

To fetch keys of active developers, feed the list of fingerprints of the primary keys into gpg:

```sh
while read fingerprint keyholder_name; do gpg --keyserver hkps://keys.openpgp.org --recv-keys ${fingerprint}; done < ./keys.txt
```

Add your key to the list if you an active developer.

