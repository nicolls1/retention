# Retention

Run with `python retention.py <data_file>`

Tested on OSX 10.10.5 and Ubuntu 14.04 

Computer specs:  
MacBook Air (13-inch, Mid 2013)  
1.4 GHz Intel Core i5  
8 GB 1600 MHz DDR3  

Ran in 2.79395508766 seconds on OSX with all 8GB of memory.  
Ran in 3.47766804695 seconds on Ubuntu VM with 2GB memory.

Tested on a clean 14.04 and the following installs were required: (Pandas needs 2 GB of RAM to install and takes a long time so be patient)
```
sudo apt-get -y update
sudo apt-get -y install python-dev python-pip python-numpy
sudo pip install pandas
```

Also tested on a mac but not on a clean install. I don't know what exactly I did in the past for things to be working now also but this is my best guess:  
Make sure you have xCode command line installed: `xcode-select --install`  
Install homebrew: `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`  
Python: `brew install python`  
Pip: `brew install pip`  
Might need numpy before pandas: `sudo pip install numpy`  
Pandas: `sudo pip install pandas`  

###Output I saw for the file you provided:

1,9831,0,0,0,0,0,0,0,0,0,0,0,0,0  
2,3928,5548,0,0,0,0,0,0,0,0,0,0,0,0  
3,4158,1098,4015,0,0,0,0,0,0,0,0,0,0,0  
4,4207,1187,595,3234,0,0,0,0,0,0,0,0,0,0  
5,4258,1289,633,376,2833,0,0,0,0,0,0,0,0,0  
6,3868,1460,770,427,287,2509,0,0,0,0,0,0,0,0  
7,3796,1106,910,572,326,227,2283,0,0,0,0,0,0,0  
8,3825,1043,636,665,455,261,190,2121,0,0,0,0,0,0  
9,3967,1138,557,393,511,343,206,164,1917,0,0,0,0,0  
10,4152,1138,615,336,285,326,252,170,141,1712,0,0,0,0  
11,4114,1207,599,394,231,208,248,196,138,111,1558,0,0,0  
12,4207,1177,613,371,270,172,161,225,167,118,98,1457,0,0  
13,3799,1434,728,406,273,213,137,139,195,148,104,83,1364,0  
14,3894,1082,910,544,302,224,182,113,115,173,134,94,72,1290  
