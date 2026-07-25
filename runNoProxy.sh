#!/bin/bash

echo "开始运行"

    export  http_proxy=
    export https_proxy=
    export  HTTP_PROXY=$http_proxy
    export HTTPS_PROXY=$https_proxy

    #u3d proxy ?
    export  HTTP_proxy=$http_proxy
    export HTTPS_proxy=$https_proxy

    # export NO_PROXY="localhost,127.0.0.*,10.192.*,192.168.*,kubernetes.docker.internal,wpad,172.16.0.0/12,172.17.0.0/16"
    export NO_PROXY="localhost,127.0.0.0/24,10.192.0.0/16,192.168.0.0/16,kubernetes.docker.internal,wpad,172.16.0.0/12,172.17.0.0/16"
    export no_proxy=$NO_PROXY

echo 'https_proxy=', $https_proxy

DYLD_LIBRARY_PATH=/opt/homebrew/opt/zbar/lib python SourcePackages/pandalearning.py
