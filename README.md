# repo-mirror

Project for setting-up local mirror with android sources.

Setting up:

1) Add:
export REPO_MIRROR_LOCATION="/shared/folder/android-mirror"

into your bashrc

2) Initialize repo
repo init -u https://android.googlesource.com/platform/manifest


3) Initialize mirror repositories

./repo-mirror.py


4) Syncrhonize mirrors

./repo-fetch.sh
