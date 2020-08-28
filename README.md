For Yocto light sensor library
1.Upgrade c and c++ to latest version for the linux environment
2.Downoload source code for c++ from main website
	https://www.yoctopuce.com/FR/downloads/YoctoLib.cpp.41115.zip
3.Bring the example code(main.cpp) and all dependent libraries from sourse folder into same directory
4.Install usb library
	sudo apt-get install libusb-1.0-0-dev
5.Get the root access to compy the files as described in Readme file in main directory
	To get the Administrative access:- 
	sudo apt install nautilus-admin
	nautilus -q
	Referance:-https://www.explorelinux.com/open-directory-root-privilege-ubuntu-20-04-lts/
6.Run these commands on terminal to compile each library
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
	g++ main.cpp *.o -lpthread -lusb-1.0

7.Connect the sensor module to the virtual box and run below command
	./a.out any