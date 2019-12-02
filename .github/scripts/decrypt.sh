#!/bin/bash

mkdir $HOME/secrets

gpg --quiet --batch --yes --decrypt --passphrase="$TOKEN" --output $HOME/secrets/token.txt.gpg