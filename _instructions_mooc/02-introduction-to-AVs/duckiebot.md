_If you don't have a Duckiebot kit, skip this step_. You are missing a lot of the fun, but you can enjoy the course regardless.

# 🚙  Duckiebot assembly and handling  

It is time to prepare a clean, well lit, flat surface and open your Duckiebox.

## Step 1: Initialize your Duckiebot memory card

The Duckiebot is a scaled differential drive vehicle powered by a small but powerful computer, the NVIDA Jetson Nano. Before assembling the robot, we can start setting up the hard drive memory disk of the Duckiebot's onboard computer.

As you lay the Duckiebox components on your working surface, take the micro sd card from the Duckiebox (along with the sd card adapter if needed) and follow [these instructions][duckiebook-init-sd-card] to initialize the Duckiebot's memory from the computer you have previously set up.

[duckiebook-init-sd-card]: https://docs.duckietown.org/daffy/opmanual_duckiebot/out/setup_duckiebot.html

At the end of this step you will have an initialized and verified sd card.

## Step 2: Assemble your Duckiebot

⚠️ The Duckiebot is equipped with a Lithium-Ion battery, like typical power banks for phones. These batteries can be dangerous if mishandled. [Read Sec. 1.1 here ][duckiebook-duckiebattery] to learn what to do and not do with a lithium-ion battery, and more about the Duckiebattery.

Once you are ready to proceed, you can follow [these instructions][duckiebook-robot-assembly] to fully assemble the Duckiebot. All the tools necessary for the job are included in the box.  

At then end of this step you should have a correctly initialized, fully charged, ready to go Duckiebot.  

[duckiebook-duckiebattery]: https://docs.duckietown.org/daffy/opmanual_duckiebot/out/db_opmanual_preliminaries_electronics.html

[duckiebook-robot-assembly]: https://docs.duckietown.org/daffy/opmanual_duckiebot/out/assembling_duckiebot_db21m.html

## Step 3: Duckiebot handling 101

Before delving in the middle of things, let's learn how to perform fundamental operations for Duckiebot handling, such as powering it on and off, recharging it, and keeping the hardware up to date.  

Follow [these instructions][duckiebook-robot-handling] to learn about Duckiebot handling.

[duckiebook-robot-handling]: https://docs.duckietown.org/daffy/opmanual_duckiebot/out/handling_duckiebot_db21m.html

## Step 4: Checkpoint!

At this point you should be able to turn your Duckiebot on for the first time and see the screen on the top turn on and show basic diagnostics, and the LEDs turn white.

🤔 If you have problems with this step, please ask [a question on our Stack Overflow with tag `#DB21M`](https://stackoverflow.com/c/duckietown/questions/tagged/DB21M).

<!--

## DB21M Init SD card

Today we are going to see how to initialize an SD card for our Duckiebot.

In this video we will use the word "flash" to indicate the transfer of data from our computer to the  microSD card that we will then put in the robot. Take your microSD card and connect it to your PC now. A USB adapter for microSD cards is included in the Duckiebot kit.

Let's start with the base command "dts init_sd_card".

This command takes,
- the "hostname", which in this case is going to be "myrobot", this will be the name of the robot and it has to be unique within your local network;
- a robot type, so "duckiebot";
- a robot configuration, which is the model of the robot you are flashing your SD card for, for example a "DB21M";
- and finally, a wifi configuration in the format "wifi name, colon, wifi password";
and we press ENTER.

In order to use the Duckietown software we have to agree to the terms and conditions, software license and privacy policy of Duckietown. We can do so by typing in "y" and ENTER,
Given that our duckiebot model is based on nvidia hardware, we will be asked to accept the nvidia software license terms as well. This might not appear depending on the robot configuration we are using.
Ok, now the most important part, we choose the SD card device to flash.
First of all, we are going to type in the size in GB of the SD card we are using, in this case, 32.
We will see that one or more devices will appear listed.
Make sure you select the right device, double check that the time you plugged in your SD card roughly matches the one listed.
So we are going to copy the device name and paste it in the prompt, then we press ENTER.
The data is now being transferred from the computer to the SD card, we will wait for it to finish.
When the transfer is complete, the program will go back to the SD card and verify that the data transfer was successfull, again, we wait for it to finish.
The verification step completed, that is great news.
Note that throughout this process, you might be asked for a password, this is necessary to flash the SD card, so when prompted, insert your password.
Let the program perform the last configuration steps on your SD card...
The process has finished, we can now unplug the SD card and insert it into the robot.




## DB21M Battery update script

In this video we are going to see how to update the software on the battery of your DB21M Duckiebot.

It is safe to do what is shown in this video even just to check if there is a new software update available for your battery. The program will only perform an update when an older version of the software is detected on your battery.

Let's open a terminal, and type in the command "dts duckiebot battery upgrade" and then we pass the name of our duckiebot as the sole argument, in this case "myrobot", and we press ENTER.

The program is now talking to the battery to figure out whether an update is necessary.

As we can see, in this case the battery is running the software version 1.0 while the version 2.0 is available. We will be asked if we want to update now, and we confirm by typing "y" and pressing ENTER.

The program is now ready to transfer the new software to the battery, but we have to tell the battery to get ready for an incoming update.

 We can do so by putting the battery into the so-called "Boot Mode" by pressing the button on the battery twice in a row.

When we are done, we press ENTER on the terminal.

 Do not worry if you are not sure the double press was done properly, the program will tell us if we need to try again.


The message "Updating battery" is telling us that the battery is now receiving the new code, let's wait.

Well done, the battery is now updated and ready to go back to work.


# Dashboard tutorial

In this video we are going to see how to setup the Duckiebot browser interface, or  dashboard,  on our newly flashed Duckiebot.

Once your computer is setup and the Duckiebot is initialized, powered on and connected to the network, we can open a browser tab, and type in the address bar the name of our robot, for example "myrobot" followed by ".local" and a final "slash (/)", and press ENTER.

A setup page will show up. The first two steps of the procedure will appear as already completed as they are not needed on a Duckiebot's dashboard.

On Step 3, you can change things like the name of the Website (which is the name that will appear as the title of your dashboard on the browser tab. Although you can accept the default values provided,  we suggest you make sure that at least the timezone is set to your current one. You can leave the email address as default, as the robot is not going to use this email address for anything.

When you are done, click NEXT.

Step 4 will show you an image of the robot you have, if the image is depicting a different robot, it means that you picked the wrong configuration during the SD card initialization and you should not proceed further.

Duckietown collects usage statistics and bug reports from robots in order to help the developers fix bugs and improve the software.

You can read the Privacy Policy on the Duckietown website before deciding what data to share with Duckietown.
Make your choices and then click NEXT.

Step 5 is only there to  tell you that you are now ready to use the Dashboard, you can click on FINISH.

By default, the Dashboard shows you the ROBOT page, we will talk about this and other features in the "How to use the Dashboard" video. Right now, we want to go to the LOGIN page, by clicking on the LOGIN on the sidebar.

Right now, your Duckiebot is not linked to your Duckietown account on `duckietown.org`, so we are going to do so by logging in using your personal Duckietown Token. We go ahead and click on "Sign in with Duckietown", a prompt will ask for the Duckietown Token, click on the link "Get your token" to go to duckietown.org and get your token.

You should see your token, if you don't see it, make sure you are logged in on duckietown.org.

Copy your token and go back to the Dashboard tab in your browser then paste your token into the prope r field. When ready, click on LOGIN.

The message in blue "Administrator account created" indicates that your Duckiebot is now linked to your Duckietown account.
As you can see, now that we are logged in as ADMINISTRATORS, we have access to many more pages. We will cover them in the next video "How to use the Dashboard", make sure to check it



## How to use the dashboard

In this video we are going to see how to use the Dashboard on our Duckiebot.

If you have not setup your dashboard yet, check out the video on "how to setup the dashboard".

Let's start by opening our browser to the address "ROBOT NAME . local" followed by a slash "/" and login using our personal Duckietown Token. We should end up on the ROBOT page as shown.

The default page of your Dashboard is the ROBOT page.

On this page, you can see:
- Basic information about the robot;
- Core temperature;
- CPU Usage and clock Frequency;
- RAM and Disk Usage;
- Battery level and estimated time until empty;

At the bottom of the page, the Status indicators will turn yellow to indicate a warning state and red to indicate a critical state of the health of your Duckiebot. Make sure you check them regularly.


From the ROBOT page, we go to the MISSION CONTROL tab. Mission Control is a very powerful tool. It lets you build custom visualization pages, called "missions".

Today we are only going to check out the default mission.
The first thing to check on Mission Control is that the Bridge is connected. A bridge is a direct connection between your browser and the robot. If the bridge is not connected, then the browser and the robot cannot talk to each other.

Other useful information you will find on this page are the current mission, default in this case and the name of your duckiebot.

The default mission only shows the camera feed and the motor speeds. A more in-depth video will cover the topic of how to create new custom missions in Mission Control.


The second Tab is the HEALTH tab. Here we can monitor some signals of our Duckiebot useful for diagnostics, such as Core Temperature, CPU, RAM and SWAP usages.

The third Tab is called ARCHITECTURE. This tool let's us see how the various software modules currently running on our Duckebot are talking to each other. Blue rectangles indicate processes, also called nodes, and grey ovals indicate stream of messages, also known as topics. If you are familiar with ROS, this is what we call the ROS network.

The final tab is the robot SETTINGS tab, which lets you change data permissions and other robot settings like its type and configuration. For most users, this tab will never be touched.


The next page we are going to look at is PORTAINER. PORTAINER is a third-party tool that seamlessly integrates into the dashboard and lets us monitor and control the software modules that are running on your Duckiebot.
The Duckiebot software is Dockerized, and portainer lets us monitor and control the execution of Docker containers.
We can click on PRIMARY and then on CONTAINERS. This page shows a list of containers and their health. Everything looks healthy, which is great.

The most important role of PORTAINER is that of monitoring our software modules. For any module, say for example, "duckiebot interface", we can see the container LOGS, INSPECT its configuration, look at the STATISTICS of the processes running in that container and for advanced users it is also possible to attach a terminal to that container.

Let's look at the container logs, for example. In this case, the LOGS for the duckiebot interface container show us some debugging messages from the process responsible for talking to the camera on our Duckiebot. From this log you can see for example the list of MODES supported by the camera and the one that the process is using right now.


The next page is going to be the FILE MANAGER. The file manager lets us see the files inside our Duckiebot.
Under "data", we can open for example the "config" directory, then "calibrations". This is the place where sensor calibration files will be stored.


The last thing we are going to see today is how we can shutdown or reboot our Duckiebot from the Dashboard. To do so, we go back to the ROBOT page, on the top-right corner of the page we see the POWER button. Click on it to show the options SHUTDOWN and REBOOT.




-->
