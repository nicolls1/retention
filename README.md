# Retention

Run with `python retention.py <data_file>`  
Make sure your python is version 2.7 (not 3). Worked on 2.7.6 and 2.7.8, think it sould would on anything above that.

Tested on OSX 10.10.5 and Ubuntu 14.04.

Computer specs:  
MacBook Air (13-inch, Mid 2013)  
1.4 GHz Intel Core i5  
8 GB 1600 MHz DDR3  

Ran in 2.65322685242 seconds on OSX with all 8GB of memory.  
Ran in 3.18237805367 seconds on Ubuntu VM with 2GB of memory.

##Setup

Tested on a clean Ubuntu 14.04 and the following installs were required: (Pandas needs 2 GB of RAM to install and takes a long time so be patient)
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

##Output I saw for the file you provided:

1,4283,1533,781,401,324,226,162,204,205,154,101,93,74,1290  
2,2830,503,219,89,60,37,26,23,30,13,15,11,72,0  
3,2971,554,206,101,65,55,36,32,20,14,10,94,0,0  
4,2918,519,198,117,112,91,56,29,19,14,134,0,0,0  
5,2798,550,245,154,185,78,23,30,22,173,0,0,0,0  
6,2762,470,243,108,77,47,22,24,115,0,0,0,0,0  
7,2753,486,221,105,59,35,24,113,0,0,0,0,0,0  
8,2687,523,221,124,57,31,182,0,0,0,0,0,0,0  
9,2829,539,228,98,49,224,0,0,0,0,0,0,0,0  
10,2945,594,207,104,302,0,0,0,0,0,0,0,0,0  
11,2937,449,184,544,0,0,0,0,0,0,0,0,0,0  
12,2773,524,910,0,0,0,0,0,0,0,0,0,0,0  
13,2717,1082,0,0,0,0,0,0,0,0,0,0,0,0  
14,3894,0,0,0,0,0,0,0,0,0,0,0,0,0  

