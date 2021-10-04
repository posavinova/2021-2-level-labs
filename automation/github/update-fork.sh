#!/bin/bash

while (( "$#" )); do
  case "$1" in
    --URL)
      FORKED_URL=$2
      shift 2
      ;;
    --USER)
      USER=$2
      shift 2
      ;;
    --FORCE)
      FORCE=$2
      shift 2
      ;;
    *)
      echo Unsupport argument $1
      exit 1
      ;;
  esac
done

git config --global user.name "${USER}"
git config --global user.email "${USER}@users.noreply.github.com"

git pull --unshallow

git remote add upstream ${FORKED_URL}
git fetch upstream

git remote -v

git checkout upstream/main

if [[ $FORCE -eq 1 ]]; then
  git merge --strategy-option theirs --no-edit origin/main
else
  git merge --no-edit origin/main
fi

DIFF=$(git diff --name-only HEAD@{0} HEAD@{1})

echo ::set-output name=files_diff::"${DIFF}"

git push upstream HEAD:main
