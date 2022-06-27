#!/bin/bash
fission spec init
fission env create --spec --name post-user-ticket-env --image nexus.sigame.com.br/python-env-3.8:0.0.5 --builder nexus.sigame.com.br/python-builder-3.8:0.0.2
fission fn create --spec --name post-user-ticket-fn --env post-user-ticket-env --src "./func/*" --entrypoint main.get_user_snapshot --executortype newdeploy --maxscale 1
fission route create --spec --method POST --url /get_user_snapshot --function get-user-snapshot-fn
