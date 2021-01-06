# SpeedChecker
Incremental internet speed checking script

## Background:
The idea behind this script is to obtain an understanding for what your regular internet speeds are. Internet Service Providers (ISPs) have a service-level agreement (SLA) for internet speeds YOU pay for. Obviously, you'll never (or maybe you will) achieve consistent internet speeds always matching what you pay for. At the same time, you shouldn’t have to pay for speeds you obviously aren’t getting either. This tool is simply a mechanism you can utilize to provide your ISP with reliable evidence of their SLA failure (if they are failing).

**EXAMPLE:** If you’re paying for gigabit internet speeds (Download) and you’re only obtaining 12MB (Download) on a consistent basis, why are you paying for gigabit internet speeds? 

SpeedChecker will provide that evidence you need to go back to your ISP with actionable evidence of how they’re not providing you with internet speeds you’re paying for.

There are two files in this repository **speedchecker.py** and **crontab**. The “crontab” file is merely an example for a cron job you can enter to conduct an hourly run of the “speedchecker.py” script. At the end of the execution, the cron job will save the results to a log file you specify.

**NOTE:**
Prior to setting the cron job and executing the SpeedChecker script, you’ll need to install the command line version of “Speedtest” (provided and maintained by Ookla).

**To install for MacOS:**

> brew tap teamookla/speedtest

> brew update

> brew install speedtest --force

**To install for Ubuntu/Debian:**

> sudo apt-get install gnupg1 apt-transport-https dirmngr

> export INSTALL_KEY=379CE192D401AB61

> sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys $INSTALL_KEY

> echo "deb https://ookla.bintray.com/debian generic main" | sudo tee  /etc/apt/sources.list.d/speedtest.list

> sudo apt-get update

// Other non-official binaries will conflict with Speedtest CLI. Example: how to remove using apt-get > sudo apt-get remove speedtest-cli

> sudo apt-get install speedtest

**To install for Fedora/Centos/Redhat:**

> sudo yum install wget

> wget https://bintray.com/ookla/rhel/rpm -O bintray-ookla-rhel.repo

> sudo mv bintray-ookla-rhel.repo /etc/yum.repos.d/

// Other non-official binaries will conflict with Speedtest CLI. Example how to remove using yum > rpm -qa | grep speedtest | xargs -I {} sudo yum -y remove {}

> sudo yum install speedtest

**Note:** Installation instructions were obtained from https://www.speedtest.net/apps/cli

## How-To:

* Install speedtest-cli functionality through terminal.
* Test the newly installed speedtest-cli functionality to make sure it works.
* Download this repo if you haven’t and place the “speedchecker.py” script wherever you want it to run from.
**Note:** You’ll need to modify the “os.system” (line 24) command in the script to call the location for your speedtest installation.
* Test the “speedchecker.py” file to make sure it runs and properly calls the speedtest-cli application you installed. If not, you may need to modify the appropriate path in the python script. 
* Create a cron job to call (and run) the script at whatever incremental value you want set. (I have the example option provided set to an hourly interval)

> crontab -e

**Note:** Make sure to review the provided example, you’ll need to provide the full path for where the “speedchecker.py” file is located. You’ll also need to provide the full path for where you would like the log file to be stored.

* Wait a couple hours and check your log file results to make sure the incremental test is being conducted and stored.
* Accumulate results over the next month and then contact your ISP if the majority of results do not meet the expected outcome. I would personally ask for a credit to my next billing cycle for not meeting defined SLAs for the internet speeds you’re paying for. 

## Recommended Implementation:

The best use of this script is on a Raspberry Pi directly connected via ethernet (hard-plugged) to your router. That being said, you can also install it on any (NIX) based implementation and run it. I would still make sure you’re doing it from a system that’s directly plugged into your router. 

Running this on a computer connected to your Wifi will provide tainted results… Meaning, there could be environmental things in your home causing a speed degradation rather than the speeds provided directly from your ISP. Being connected directly to the router will provide more realistic results, and can’t easily be argued away by your ISP.

### ChangeLog:

* This is the first publishing of this process… Obviously, it’s very basic in it’s implementation. That being said, I have additional goals and modifications in mind for this use case. At some point, I hope to have this more plug and play rather than the added manual aspect. Stay tuned for updates and thanks for the support!
