#!/usr/bin/env python2

import os
import sys
import hashlib
import urlparse

# script my be executed only in initnialized repo
assert(os.path.exists('./.repo/repo'))
sys.path.insert(0, './.repo/repo')

from manifest_xml import XmlManifest
manifest = XmlManifest("./.repo/")
manifest._Load()

MIRRORDIR = os.path.expanduser(os.environ["REPO_MIRROR_LOCATION"])
for name,projects in manifest._projects.items():
    for project in projects:
        remoteUrl = project.remote.url

        moduleDir = MIRRORDIR + "/.repo/projects/" + project.relpath + ".git"

        if not os.path.exists(moduleDir + "/config"):
            if not os.path.exists(moduleDir):
                os.makedirs(moduleDir)
            # TODO: use subprocess
            cmd = "cd %s && git init --bare" % moduleDir
            ret = os.system(cmd)
            assert(ret==0)

        md5su = hashlib.new("md5")
        md5su.update(remoteUrl)
        remoteName = md5su.hexdigest()[:10]

        # TODO: use git remote -v
        if remoteName not in open(moduleDir + "/config").read():
            cmd = "cd %s && git remote add %s %s" % (moduleDir, remoteName, remoteUrl)
            ret = os.system(cmd)
            print(cmd)
            assert(ret==0)
