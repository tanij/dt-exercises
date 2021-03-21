_If you don't have a Duckiebot kit, skip this step_. You are missing a lot of the fun, but you can enjoy the course regardless.
 

## 🚙  Duckiebot assembly and setup  

If you have a Duckiebot, [please follow the instructions here until "make it see" included][duckiebook-robot-assembly].

At the end of that step, you should have been able to have a Duckiebot that you can drive.

🤔 If you have problems with this step, please ask [a question on our Stack Overflow with tag `#DB21`](https://stackoverflow.com/c/duckietown/questions/tagged/DB21).

[duckiebook-robot-assembly]: https://docs.duckietown.org/daffy/opmanual_duckiebot/out/assembling_duckiebot_db21.html


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









-->
