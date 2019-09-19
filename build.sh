#!/bin/bash

export PATH=$PWD/node_modules/.bin:$PATH
gulp clean
npm i
gulp webpack:build
