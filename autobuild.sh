#!/bin/sh

while sleep 1
do
	find app content static templates | entr sh -c './VEnv/bin/python -m app build && echo Building'
done
