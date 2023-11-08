#!/bin/bash


for file in $(find ~/python-project-49/brain_games/games -name '*.py')
do
  autopep8 --in-place --aggressive --aggressive $file
done
