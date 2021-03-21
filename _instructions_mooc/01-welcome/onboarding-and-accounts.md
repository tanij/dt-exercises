# Ready to get started?

Your first task is to set up your development environment.

Compared to other courses you might have taken, it might seem intimidating to set up so many things at the beginning.

However, it's going to be worth it, we promise!

This document summarizes the steps that you need to do. We will write here on edX _a  synthetic summary_ for the steps to take. Usually the details are in one of our Duckiebooks at the site [docs.duckietown.org/daffy/](https://docs.duckietown.org/daffy/).
 

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

    > docker login -u DOCKER_USERNAME
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

[stack-overflow-duckietown]: https://stackoverflow.com/c/duckietown/
