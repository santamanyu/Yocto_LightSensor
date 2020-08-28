#!/bin/bash
echo "Build static and dynamic library for C++"
echo "========================================"
gcc yapi/yapi.c -c
gcc yapi/yfifo.c -c
gcc yapi/yhash.c -c
gcc yapi/yjni.c -c
gcc yapi/yjson.c -c
gcc yapi/ykey.c -c
gcc yapi/ymemory.c -c
gcc yapi/ypkt_lin.c -c
gcc yapi/ypkt_osx.c -c
gcc yapi/ypkt_win.c -c
gcc yapi/yprog.c -c
gcc yapi/ystream.c -c
gcc yapi/ytcp.c -c
gcc yapi/ythread.c -c
g++ yocto_api.cpp -c
g++ yocto_lightsensor.cpp -c
