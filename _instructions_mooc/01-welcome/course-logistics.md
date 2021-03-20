# Course Logistics

Here is some organizational information about the course. You can some of this information in the course Syllabus in the "Handouts" section of the "Course" page.

<!--
🤔 🚗 ❓💡
-->

## Welcome

Welcome, again, to Self-Driving Cars with Duckietown!

This course is the result of the collaboration of ETH Zurich (ETHZ), the University of Montreal (UdM), the Toyota Technological Institute at Chicago (TTIC) and Duckietown.

The Duckietown platform was created in 2016 to teach the science and technology of autonomous vehicles to the master students of MIT. You can learn more about the history of the Duckietown project [here](duckietown-history).

[duckietown-history]: https://www.duckietown.org/about/history

## The Staff

Throughout the course you will meet instructors and staff from all the organizing institutions. In order of appearance:

* Prof. [Emilio Frazzoli][emilio-web], Prof., ETHZ
* Dr. [Andrea Censi][andrea-web], Ph. D., ETHZ 
* Dr. [Jacopo Tani][jacopo-web], ETHZ
* Prof. [Matthew Walter][matt-web], TTIC
* Prof. [Liam Paull][liam-web], UdM
* [Andrea Daniele][daniele-web], TTIC

[jacopo-web]: https://www.linkedin.com/in/jacopo-tani/?originalSubdomain=ch
[emilio-web]: https://idsc.ethz.ch/research-frazzoli.html
[andrea-web]: https://censi.science/
[andrea-linkedin]: https://www.linkedin.com/in/censi/

[liam-web]: https://liampaull.ca/
[matt-web]: https://ttic.uchicago.edu/~mwalter/
[daniele-web]: https://afdaniele.com/

Before the corse starts, we wanted to take a few minutes to introduce ourselves. You can watch this informal video on Vimeo: [Informal staff introductions][video-staff-intro].

[video-staff-intro]: # **TODO**

## Intended Learning Outcomes

This course is designed to be hands-on. This means that you will actually have to _do_ things in the real world with the information we will provide you. In the context of robotics, "real" world could mean a simulated environment as well as the physical world.   

By the end of this course, we will learn about the fundamental of robotics. What qualifies as a robot? What do they have in common? What are the differences and implications of logical and physical autonomy architectures? How painful is the difference between what _should_ happen in theory and what _actually_ happens, and how do we go from understanding to implementation?

Self-driving Cars with Duckietown is a "grand tour" of robotics. The focus is on the breadth rather than the depth. We  highlight how robotics is a system level discipline where many components interact with each other to produce real world autonomous behaviors. Any of these "components" could absorb an entire professional career.

Finally, we want to provide an understanding of the difference in approaches to solving the challenges of autonomy. The buzz of AI is high, but what is its place in robotics? How does using reinforcement or imitation learning relate to the "traditional" robotics approaches to given tasks?

Robotics and AI are a fast-paced field of research and this course is the beginning of a learning adventure.

## Course content

This course includes 9 learning modules in addition to this introduction.

* Module 1: Introduction to self-driving cars
  
  - The potentials and challenges
  - Levels of autonomy
  - The vision for autonomous vehicles (AVs)
  - Activities: learning environment setup

* Module 2: Towards autonomy
  
  - Making a robot
  - Sensorimotor architectures
  - Stateful architectures
  - Logical and physical architectures
  - Application: Braitenberg vehicles
  
* Module 3: Modeling and Control
  
  - Introduction to control systems
  - Representations and models
  - PID control
  - Application: Duckiebot angular velocity tracking

* Module 4: Robot Vision
  
  - Introduction to projective geometry
  - Camera modeling and calibration
  - Image processing
  - Application: visual servoing

* Module 5: Object Detection
  
  - Convolutional neural networks
  - One and two stage object detection
  - Application: duckie detection

* Module 6: State Estimation and Localization
  
  - Bayes filtering framework
  - Parameterized methods (Kalman filter)
  - Sampling-based methods (Particle and histogram filter)
  - Application: lane following (LF)

* Module 7: Planning
  
  - Planning formalization
  - Searching Graphs
  - Sampling-based planning
  - Application: duckie avoidance

* Module 8: Learning by Reinforcement
  
  - Markov decision processes
  - Value functions
  - Policy gradients
  - Domain randomization
  - Application: Lane following with RL

* Module 9: Learning by Imitation
  
  - Behaviour cloning
  - Online imitation learning
  - Safety and uncertainty
  - Application: Lane following with IL

## Prerequisites

We will assume that if you are taking this course, you are familiar with some basics of math, physics and programming.

* Basic Linux, Python, Git. We are going to:
	-  use terminal interface, so basic knowledge of Bash is required
	-  write "autonomy" code in Python 
	-  pull repositories, fork, push, branch, etc.  

* Elements of linear algebra, probability, calculus. We are going to:
	-  use matrices to represent coordinate systems 
	-  use notions of probability (marginalization, Bayes theorem) to derive perception algorithms for the Duckiebot
	-  write down equations of motion, which involve time ODEs (recognizing the acronym is a good start!)  

* Elements of kinematics
  - We are going to derive a kinematic model of the Duckiebot 

* Computer with native Ubuntu installation and admin network access 
  - we are going to use Ubuntu 20.04 with a native (e.g., dual boot) installation

* 🚙 Access to your router
  - If you are using a physical Duckiebot, you will require admin access to your router to iron out potential networking issues.

## The Duckiebot and Duckietown

The physical Duckiebot and Duckietown are not required to follow and complete this course. However, following along with a real robot will make you learn much more. You can get a Duckietown MOOC Founder Edition Kit (robot + city track) [here][dt-shop-mooc-kit].  


[dt-shop-mooc-kit]: https://get.duckietown.com/collections/starter-kits/products/db-mooc-kit

## Format, timeline

The course starts on Monday, March 22, 2021 with the release of the first learning module (in addition to this welcome). This course is instructor paced. To accommodate for the "real world" nuisances we expect from using real robots, and leave no-one behind, we will release a new module every 10 days. The final learning module will be released on Monday, June 14, 2021. The final homework assignment will be due on June 25, 2021, the end date of this course.

Learning modules will be released on Mondays and Thursdays alternatively, with exceptions for modules 7 and 8, which will happen on Tuesdays and Fridays, to avoid national holidays in some countries. Modules will always be released at 7AM PT | 10AM ET | 4PM CET | 7.30PM IST unless otherwise specified.

Each learning module will include video lectures, activities, a homework exercise, and optional additional materials like supplementary readings, surveys, quizzes, etc.

* Video Lectures will cover the theory behind the topics at hand.
  - You should watch all videos

* Activities
  - require you to follow along and reproduce some behaviors
  - can be software and hardware based
  - are **not** graded

* Homework exercises
  - are based upon the theory and activities
  - **are** graded
  - are due before the release of the next learning module (exception for the last exercise, which is due on June 25, 2021, AM PT | 10AM ET | 4PM CET | 7.30PM IST)

## Grading and the AI Driving Olympics (AI-DO)

The Duckietown platform is used for benchmarking the state of the art of embodied AI through international competitions that take place biannually at premiere robotics and ML conferences such as [ICRA (external link)][icra21] and [NeurIPS (external link)][neurips21]. You can learn more about the AI-DO [here][aido-info] if you want.

AI-DO is different from this course, but we will use the same [technical infrastructure][challenges-server] to grade your exercises. By construction, some exercises we will ask you to do will overlap with existing AI-DO challenges. What you will be doing is highly scientific!

At any time, with an additional line of code, you can decide to submit your "homework" to the actual scientific competition, too. If your agent reaches the finals, you could be featured in this year's AI-DO 6 finals at ICRA 2021!

[icra21]: http://www.icra2021.org/
[neurips21]: https://nips.cc/
[aido-info]: https://www.duckietown.org/research/AI-Driving-olympics
[challenges-server]: https://challenges.duckietown.org/v4/

## How to get help {#sec:how-to-help}

We will be answering questions related to:

* _learning materials_ on the [EdX Discussions forum][edx-disc-forum] and

* _technical questions_ on the [Duckietown Stack Overflow][dt-stack-overflow] space. This is a private space and will require an invitation to join. We will send an invitations out throughout the first week of the course. To receive an invitation you will have to have completed the "Create your Accounts" activity in the very first learning module.  

Each instructor will lead one or more learning modules. The lead instructor will always be the go-to person for addressing questions related to that module.

Additionally, Andrea Daniele will be responsible of supporting software challenges, and Jacopo hardware related ones.

To provide effective support, we will focus on answering questions posted in the above avenues, and ignore other requests for support. Additionally, when using any forum we expect all learners to maintain a constructive, positive and professional attitude (but clearly duckie puns are always welcome!). We will ban / report / take all appropriate actions to maintain a high-quality learning environment.

[dt-stack-overflow]: https://stackoverflow.com/c/duckietown/questions

[EdX Discussions forum]: https://courses.edx.org/courses/course-v1:ETHx+DT-01x+1T2021/discussion/forum/

## The verified track

If you are in the verified track, to obtain a certificate you will need to pass the course. You pass the course with a grade bigger or equal to 60/100. All homework exercises will be graded with the same weight. Late deliveries will not be accepted.  

If you are enrolled in the verified track, and/or own a Duckiebot, special instructions will follow via email.

## "There and back again": a Duckietown learning experience

A final word before proceeding.

Like any hero of your favorite historical or mythological saga, you are, right now, walking the first steps in a transformative quest, which might lead you to become a roboticist, a hacker, a software magician, or something else you will discover on the way.

You are now like Frodo preparing for the banquet in Hobbiton, unaware of the storm coming from east.

In this quest you will step from the comfort zone of what is known to you, in a journey through the unknown.

Like Frodo, you will be able to rely on "supernatural" aid provided by the beauty and perfection of mathematics.

Like Frodo, you will meet mentors. Your Gandalf will be able to point you in the right direction and provide you with essential tools, but, like for Frodo, Gandalf not walk the journey with you.

But if you look around, you will see that you are not alone in this journey. Many peers are setting their first steps, too. Associate, work together, help each other - because the eye of Sauron spotted us all. Build your fellowship of the duckie before marching towards Mount Fate.

During the first part of this quest, your path will lead you downwards. You will face _trials_ and _failures_ which will test your resolve. It is through perseveration and patience that new skills are acquired and cultivated. Remember that "the master has failed more times than the novice has tried."

Although your will be gathering new technical knowledge in this first part of your quest, you will come to feel overwhelmed. As you learn new things, the immensity of what you _do not_ know becomes more evident. And it weighs.

Half-way through this quest you will hit rock bottom. It's the "abyss of death and rebirth". Here you will metaphorically go through a process of death (nothing works, everything is broken, the course is terrible, everybody complains) and rebirth.

Rebirth is the second part of the quest, and it happens slowly, in a continuous process of revelations and transformation. As your coding skills start improving, and the "nuisances" of the real-world start to become clearer, "things will start working" slowly, but they will.

The final step of your quest to become a hero will be one of atonement. Your hard work will have produced imperishable fruits for you to banquet from and share at large. You will transition from the uncomfortable world of unknown back to the comforts of known territory.

There, and back again. Welcome to the Duckietown learning experience and see you on the other side!

<!--
Your first task is to set up your development environment.

Compared to other courses you might have taken, it might seem intimidating to set up so many things at the beginning.
However, it's going to be worth it, we promise!

This document summarizes the steps that you need to do. We will write here on EdX _a  synthetic summary_ for the steps to take. Usually the details are in one of our Duckiebooks at the site [docs.duckietown.org/daffy/](https://docs.duckietown.org/daffy/).

## Step 0: Watch a short introduction to the development workflow

If you want to know more about the big picture and why we ask you to do all these setup steps, please watch this video on Vimeo:

* [Development workflow (Andrea)][video-devel] **TODO**

## Step 1: Make all the accounts first!

At some point, in the next steps, you will need the following accounts:

* **Github account**. Needed for checking out the code. Sign up [here][signup-github].

* **Dockerhub account**. Needed for submitting exercises. Sign up [here][signup-dockerhub].

* **Duckietown account**. Needed to gain access to the autograder and many other features. Sign up [here][signup-duckietown].

* **Stack Overflow account**. Needed to gain access to [our private Stack Overflow][stack-overflow-duckietown].  **You will receive an invite after you sign up for a Duckietown account**.


## Step 2: Laptop setup

Follow the instructions [here][duckiebook-laptop-setup].

At the end of the instructions, you will have installed some essential software, such as

* Docker

* The Duckietown Shell

🤔 If you have problems with this step, please ask [a question on our Stack Overflow with tag #laptop-setup](https://stackoverflow.com/c/duckietown/questions/tagged/laptop-setup).

[duckiebook-laptop-setup]: https://docs.duckietown.org/daffy/opmanual_duckiebot/out/laptop_setup.html

## Step 3: Duckietown account link

Make sure you finish the previous step before continuing!

Follow the instructions [here][duckiebook-account-setup] to set up your local environment with the Duckietown token.

[duckiebook-account-setup]: https://docs.duckietown.org/daffy/opmanual_duckiebot/out/dt_account.html


## Step 5: Checkpoint!

Before we go on, this is a checkpoint to make sure you have installed everything.

If some of these commands don't work, please go back and fix it, before continuing.

If Docker installation went well, then you can run the following command:

    > docker run hello-world
    Hello from Docker!
    This message shows that your installation appears to be working correctly.

If you set up Github account and private key, you should be able to run this command successfully:

	> ssh -T git@github.com
    Hi GITHUB_USERNAME! You've successfully authenticated, but GitHub does not provide shell access.

If you have a valid DockerHub account then you can run

	❯ docker login -u DOCKER_USERNAME
    Password:

The second time it will just tell you:

    Authenticating with existing credentials...
    Login Succeeded

If the Duckietown Shell was installed, then you can run a command like this:

    > dts version

If you correctly configured the token, then this command should work:

	> dts challenges info
    ~        You are succesfully authenticated:
    ~
    ~                     ID: 3
    ~                   name: YOUR NAME
    ~                  login: YOUR DUCKIETOWN ACCOUNT


If there is something not working, please stop here. Ask for help on Stack Overflow.


[signup-github]: https://github.com/join
[signup-dockerhub]: https://hub.docker.com/signup
[signup-duckietown]: https://www.duckietown.org/site/register
[signup-stack-overflow]: https://stackoverflow.com/users/signup

[video-devel]: #
[stack-overflow-duckietown]: https://stackoverflow.com/c/duckietown/
-->
