#!/bin/bash
fission spec init
fission env create --spec --name get-user-snapshot-env --image nexus.sigame.com.br/fission-async:0.1.6 --builder nexus.sigame.com.br/fission-builder-3.8:0.0.1
fission fn create --spec --name get-user-snapshot-fn --env get-user-snapshot-env --src "./func/*" --entrypoint main.get_user_snapshot --executortype newdeploy --maxscale 1
fission route create --spec --name get-user-snapshot-rt --method GET --url /support/get-user-snapshot --function get-user-snapshot-fn
