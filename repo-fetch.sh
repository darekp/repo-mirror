#!/bin/bash

set -eu

find $REPO_MIRROR_LOCATION -path "*.git/config"  | xargs -P 4 --replace bash -c 'cd $(dirname {}) && pwd &&  git fetch --all -p -t'
