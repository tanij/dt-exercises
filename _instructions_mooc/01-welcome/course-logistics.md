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

Throughout the course you will meet instructors from all the organizing institutions. In order of appearance:

* Emilio Frazzoli, Prof., ETHZ
* Andrea Censi, Ph. D., ETHZ
* Jacopo Tani, Ph. D., ETHZ
* Matthew Walther, Prof., TTIC
* Liam Paull, Prof., UdM
* Andrea Daniele, TTIC

Before the corse starts, we wanted to take a few minutes to introduce ourselves. You can watch this informal video on Vimeo: [Informal staff introductions][video-staff-intro].

Each of us will lead one or more learning modules. The lead instructor will always be the go-to person for addressing questions.

Additionally, Andrea Daniele will be responsible of supporting software challenges, and Jacopo hardware related ones. You can learn how to get help [here][sec:how-to-help]

[video-staff-intro]: # **TODO**

## Intended Learning Outcomes

This course is designed to be hands-on. This means that you will actually have to _do_ things in the real world with the information we will provide you. In the context of robotics, "real" world could mean a simulated environment as well as the physical world.   

By the end of this course, we will learn about the fundamental of robotics. What qualifies as a robot? What do they have in common? What are the differences and implications of logical and physical autonomy architectures? How painful is the difference between what _should_ happen in theory and what _actually_ happens, and how do we go from understanding to implementation?

Self-driving Cars with Duckietown is a "grand tour" of robotics. The focus is on the breadth rather than the depth. We  highlight how robotics is a system level discipline where many components interact with each other to produce real world autonomous behaviors. Any of these "components" could absorb an entire professional career.

Finally, we want to provide an understanding of the difference in approaches to solving the challenges of autonomy. The buzz of AI is high, but what's it place in robotics? How does using reinforcement or imitation learning relate to the "traditional" robotics approaches to given tasks?

Robotics and AI are a fast-paced field of research and this course is the beginning of a learning adventure.

## Course content

This course includes 9 learning modules in addition to this introduction.

* Module 1: Introduction to self-driving cars
  ○ The potentials and challenges
  ○ Levels of autonomy
  ○ The vision for autonomous vehicles (AVs)
  ○ Activities: learning environment setup

* Module 2: Towards autonomy
  ○ Making a robot
  ○ Sensorimotor architectures
  ○ Stateful architectures
  ○ Logical and physical architectures
  ○ Application: Braitenberg vehicles

* Module 3: Modeling and Control
  ○ Introduction to control systems
  ○ Representations and models
  ○ PID control
  ○ Application: Duckiebot angular velocity tracking

* Module 4: Robot Vision
  ○ Introduction to projective geometry
  ○ Camera modeling and calibration
  ○ Image processing
  ○ Application: visual servoing

* Module 5: Object Detection
  ○ Convolutional neural networks
  ○ One and two stage object detection
  ○ Application: duckie detection

* Module 6: State Estimation and Localization
  ○ Bayes filtering framework
  ○ Parameterized methods (Kalman filter)
  ○ Sampling-based methods (Particle and histogram filter)
  ○ Application: lane following (LF)

* Module 7: Planning
  ○ Planning formalization
  ○ Searching Graphs
  ○ Sampling-based planning
  ○ Application: duckie avoidance

* Module 8: Learning by Reinforcement
  ○ Markov decision processes
  ○ Value functions
  ○ Policy gradients
  ○ Domain randomization
  ○ Application: Lane following with RL

* Module 9: Learning by Imitation
  ○ Behaviour cloning
  ○ Online imitation learning
  ○ Safety and uncertainty
  ○ Application: Lane following with IL

## Prerequisites

We will assume that if you are taking this course, you are familiar with some basics of math, physics and programming.

* Basic Linux, Python, Git. We are going to:
	○  use terminal interface, so basic knowledge of Bash is required
	○  write "autonomy" code in Python 
	○  pull repositories, fork, push, branch, etc.  

* Elements of linear algebra, probability, calculus. We are going to:
	○  use matrices to represent coordinate systems 
	○  use notions of probability (marginalization, Bayes theorem) to derive perception algorithms for the Duckiebot
	○  write down equations of motion, which involve time ODEs (recognizing the acronym is a good start!)  

* Elements of kinematics
  ○ We are going to derive a kinematic model of the Duckiebot 

* Computer with native Ubuntu installation and admin network access 
  ○ we are going to use Ubuntu 20.04 with a native (e.g., dual boot) installation

* 🚙 Access to your router
  ○ If you are using a physical Duckiebot, you will require admin access to your router to iron out potential networking issues.

## The Duckiebot and Duckietown

The physical Duckiebot and Duckietown are not required to follow and complete this course. However, following along with a real robot will make you learn much more. You can get a Duckietown MOOC Founder Edition Kit (robot + city track) [here][dt-shop-mooc-kit].  


[dt-shop-mooc-kit]: https://get.duckietown.com/collections/starter-kits/products/db-mooc-kit

## Format, timeline

The course starts on Monday, March 22, 2021 with the release of the first learning module (in addition to this welcome). This course is instructor paced. To accommodate for the "real world" nuisances we expect from using real robots, and leave no-one behind, we will release a new module every 10 days. The final learning module will be released on Monday, June 14, 2021.

Learning modules will be released on Mondays and Thursdays alternatively, with exceptions for modules 7 and 8, which will happen on Tuesdays and Fridays, to avoid national holidays in some countries.

Each learning module will include video lectures, activities, a homework exercise, and optional additional materials like supplementary readings, surveys, quizzes, etc.

* Video Lectures will cover the theory behind the topics at hand.
  ○ You should watch all videos

* Activities
  ○ require you to follow along and reproduce some behaviors
  ○ can be software and hardware based
  ○ are **not** graded

* Homework exercises
  ○ are based upon the theory and activities
  ○ **are** graded

## Grading and the AI Driving Olympics (AI-DO)

The Duckietown platform is used for benchmarking the state of the art of embodied AI through international competitions that take place biannually at premiere robotics and ML conferences such as [ICRA][icra21] and [NeurIPS][neurips21]. You can learn more about the AI-DO [here][aido-info] if you want.

AI-DO is different from this course, but we will use the same technical infrastructure to grade your exercises. By construction, some exercises we will ask you to do will overlap with existing AI-DO challenges. What you will be doing is highly scientific!

At any time, with an additional line of code, you can decide to submit your "homework" to the actual scientific competition, too. If your agent reaches the finals, you could be featured in this year's AI-DO 6 finals at ICRA 2021!

 


- You get the certificate if >60/100
- There are 9 exercises, all with equal weights
-

## How to get help {#sec:how-to-help

  - EdX Forum for questions related to learning materials
- Instructor for each module will take the lead in answering
- Stack Overflow for technical questions
 
- Hardware: Jacopo
- Software: Andrea Daniele
-

## The certificates

- You can audit the course: welcome!  
- You can be verified and get a shiny certificate from edx
- special instructions will be sent by email 
- Robot not necessary for certificate
- if you have a robot, special instruction will follow via email
- dedicated hardware activities during throughout the course modules

## The Hero Quest

- Enjoy now
- Suffer in the middle
- Reach catharsis on the other side

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
