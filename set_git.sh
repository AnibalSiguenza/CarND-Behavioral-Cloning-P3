#!/bin/bash

git config --global user.name Anibal
git config --global user.email anibal.siguenza1@gmail.com
git remote set-url origin https://github.com/AnibalSiguenza/behavioral_cloning
echo

echo Please verify remote:
git remote -v
echo

echo Please verify your credentials:
echo username: `git config user.name`
echo email: `git config user.email`