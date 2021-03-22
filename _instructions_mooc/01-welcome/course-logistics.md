# Course Logistics

Here is some organizational information about the course. Some of this information can be found in the course Syllabus in the "Handouts" section of the "Course" page.

## Welcome

Welcome, again, to Self-Driving Cars with Duckietown!

This course is the result of the collaboration of ETH Zurich (ETHZ), the University of Montreal (UdM), the Toyota Technological Institute at Chicago (TTIC) and Duckietown.

The Duckietown platform was created in 2016 to teach the science and technology of autonomous vehicles to the master students of MIT. You can learn more about the history of the Duckietown project [here][duckietown-history].

[duckietown-history]: https://www.duckietown.org/about/history

## The Staff

Throughout the course you will meet instructors and staff from all the organizing institutions. Before starting, we wanted to very briefly introduce ourselves. Check out our informal introductions on Vimeo! In order of appearance:

* Prof. [Emilio Frazzoli][emilio-web],  ETHZ
* Dr. [Andrea Censi][andrea-web],  ETHZ ([introduction][ac-intro], [LinkedIn][andrea-linkedin])
* Dr. [Jacopo Tani][jacopo-web], ETHZ ([introduction][jt-intro], [LinkedIn][jacopo-linkedin])
* Prof. [Matthew Walter][matt-web], TTIC  ([LinkedIn][matt-linkedin])
* Prof. [Liam Paull][liam-web], UdM ([introduction][lp-intro], [LinkedIn][liam-linkedin])
* [Andrea Daniele][daniele-web], TTIC ([introduction][afd-intro], [LinkedIn][daniele-linkedin])

[jacopo-web]: https://www.linkedin.com/in/jacopo-tani/
[jacopo-linkedin]: https://www.linkedin.com/in/jacopo-tani/
[emilio-web]: https://idsc.ethz.ch/research-frazzoli.html
[andrea-web]: https://censi.science/
[andrea-linkedin]: https://www.linkedin.com/in/censi/
[liam-web]: https://liampaull.ca/
[liam-linkedin]: https://www.linkedin.com/in/liam-paull-83a5442b/
[matt-web]: https://ttic.uchicago.edu/~mwalter/
[matt-linkedin]: https://www.linkedin.com/in/matthew-walter-70320b2/
[daniele-web]: https://afdaniele.com/
[daniele-linkedin]: https://www.linkedin.com/in/andreafdaniele/

[ac-intro]: https://vimeo.com/527052737
[jt-intro]: https://vimeo.com/526949215
[lp-intro]: https://vimeo.com/527052564
[afd-intro]: https://vimeo.com/527124388

<!--
TODO:  mw intro videos.
-->


## Intended Learning Outcomes

This course is designed to be hands-on. This means that you will actually have to _do_ things in the real world with the information we will provide you. In the context of robotics, "real" world could mean a simulated environment as well as the physical world.   

By the end of this course, we will learn about the fundamental of robotics. What qualifies as a robot? What do they have in common? What are the differences and implications of logical and physical autonomy architectures? How painful is the difference between what _should_ happen in theory and what _actually_ happens, and how do we go from understanding to implementation?

Self-driving Cars with Duckietown is a "grand tour" of robotics. The focus is on breadth rather than depth. We highlight how robotics is a system level discipline where many components interact with each other to produce real-world autonomous behaviors. Any of these "components" could absorb an entire professional career.

Finally, we want to provide an understanding of the difference in approaches to solving the challenges of autonomy. The buzz of AI is high. What is its place in robotics? How does using reinforcement or imitation learning relate to the "traditional" robotics approaches to given tasks?

Robotics and AI are a fast-paced field of research and this course is just the beginning of a learning adventure.

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

	- use terminal interface, so basic knowledge of Bash is required;
	- write "autonomy" code in Python;
	- pull repositories, fork, push, branch, etc.

* Elements of linear algebra, probability, calculus. We are going to:

	- use matrices to represent coordinate systems;
	- use notions of probability (marginalization, Bayes theorem) to derive perception algorithms for the Duckiebot;
	- write down equations of motion, which involve continuous time ODEs (recognizing the acronym is a good start!).

* Elements of kinematics

  - We are going to derive a kinematic model of the Duckiebot.

* Computer with native Ubuntu installation and admin network access

  - we are going to use Ubuntu 20.04 with a native (e.g., dual boot) installation

* 🚙 Access to your router

  - If you are using a physical Duckiebot, you will require admin access to your router to iron out potential networking issues.

## The Duckiebot and Duckietown

The physical Duckiebot and Duckietown are not required to follow and complete this course. However, following along with a real robot will make you learn much more. You can get a Duckietown MOOC Founder Edition Kit (robot + city track) [here][dt-shop-mooc-kit].  


[dt-shop-mooc-kit]: https://get.duckietown.com/collections/starter-kits/products/db-mooc-kit

## Format, timeline

The course starts on Monday, March 22, 2021, with the release of this welcome module. This course is instructor-paced. To accommodate for the "real world" nuisances we expect from using real robots, and leave no-one behind, we will release a new module every 10 days. The first module will be released on March 24. The final learning module will be released on Monday, June 14, 2021. The final homework assignment will be due on June 25, 2021, the end date of this course.

Learning modules will be released on Mondays and Thursdays alternatively, with exceptions for modules 1 (March 24), 7 and 8, which will happen on Tuesdays and Fridays, to avoid national holidays in some countries. Modules will always be released at 15:00 UTC unless otherwise specified.

Each learning module will include video lectures, activities, a homework exercise, and optional additional materials like supplementary readings, surveys, quizzes, etc.

* Video Lectures will cover the theory behind the topics at hand.

  - You should watch all videos

* Activities

  - require you to follow along and reproduce some behaviors
  - can be software or hardware based
  - are **not** graded

* Homework exercises

  - are based upon the theory and activities
  - **are** graded
  - are due before the release of the next learning module (except for the last exercise, which is due on June 25, 2021, 15:00 UTC)

## Grading and the AI Driving Olympics (AI-DO)

The Duckietown platform is used for benchmarking the state of the art of embodied AI through international competitions that take place biannually at premiere robotics and ML conferences such as [ICRA (external link)][icra21] and [NeurIPS (external link)][neurips21]. You can learn more about the AI-DO [here][aido-info] if you want.

AI-DO is different from this course, but we will use the same [technical infrastructure][challenges-server] to grade your exercises. By construction, in some exercises we will ask you to do will overlap with existing AI-DO challenges. What you will be doing is highly scientific!

At any time, with an additional line of code, you can decide to submit your "homework" to the actual competition, too. If your agent reaches the finals, you could be featured in this year's AI-DO 6 finals at ICRA 2021!

[icra21]: http://www.icra2021.org/
[neurips21]: https://nips.cc/
[aido-info]: https://www.duckietown.org/research/AI-Driving-olympics
[challenges-server]: https://challenges.duckietown.org/v4/

## How to get help {#sec:how-to-help}

We will be answering questions related to:

* _learning materials_ on the [EdX Discussions forum][edx-disc-forum] and

* _technical questions_ on the [Duckietown Stack Overflow][dt-stack-overflow] space. This is a private space and will require an invitation to join. We will send invitations out throughout the first week of the course. To receive an invitation, you will have to have completed the "Create your Accounts" activity in the very first learning module.  

Each instructor will lead one or more learning modules. The lead instructor will always be the go-to person for addressing questions related to that module.

Additionally, Andrea Daniele will be responsible for supporting software challenges, and Jacopo hardware-related ones.

To provide effective support, we will focus on answering questions posted in the above avenues, and ignore other requests for support. Additionally, when using any forum we expect all learners to maintain a constructive, positive and professional attitude (but clearly duckie puns are always welcome!). We will ban / report / take all appropriate actions to maintain a high-quality learning environment.

[dt-stack-overflow]: https://stackoverflow.com/c/duckietown/questions

[edx-disc-forum]: https://courses.edx.org/courses/course-v1:ETHx+DT-01x+1T2021/discussion/forum/

## The verified track

If you are in the verified track, to obtain a certificate you will need to pass the course. You pass the course with a grade bigger or equal to 60/100. All homework exercises will be graded with the same weight. Late deliveries will not be accepted.  

If you are enrolled in the verified track, and/or own a Duckiebot, special instructions will follow via email.
