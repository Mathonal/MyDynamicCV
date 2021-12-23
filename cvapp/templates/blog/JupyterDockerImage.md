## Summary

----
*   [Overview](#overview)
    *   [Docker philosophy](#philosophy)
    *   [Summary](#summary)

*   [1. Basic uses of docker](#1)
    *   [Install docker engine](#install)
    *   [Pull images](#pull)
    *   [Run container from images](#run)

*   [2. Finalize setup](#2)
    *   [Adding a volume](#volume)
    *   [First Checkpoint](#checkpoint1)

*   [3. Improve an image](#improve)
    *   [Commit a container](#commit)
    *   [Run your image](#rerun)
    *   [Second Checkpoint](#checkpoint2)

*   [4. Automate Jupyter RUN command (linux)](#alias)
----
## Overview

### Philosophy

In the developping "realm", installing framework and setting up environnement can be really painfull for beginners.

If only there was a **tool that could encapsulate a framework and you only had to run this blackbox** and get to the good stuff, meaning actually learning to code and uses data libraries, treat data and plot graphs...

In fact there is, it's called **container technology**. Here I use *docker* but there are several layers to this solution (*Kubernetes*), I'll try to keep it simple here (simple user, localhost user)

To be quick on terms, an **image** is a blueprint of a software setup that can be run and used as one (or several) already configured virtual machine. A **container** is this virtual machine that you use as a service.

The goal for developpers is to spend time to configure and test their services once, keep it as an image, and run and take down containers from that image as they need, not to worry about configurations or compatibilities.

I will show how I use this tool when I need a datascience/data-filtering/quick code testing and visualisation environnement.

### Summary

> 1.   Basic uses of docker (how to start)
>    *   install docker engine 
>    *   search and pull an existing image on docker hub
>    *   run image as container and use it

> 2.   Finalise your jupyter setup with few options
>    *   Building run command with a shared volume
>    *   First check point

> 3.   Improve a container (by installing new libraries)
>    *   install new python librairies on server
>    *   save current (improved) server as new image
>    *   run new image

> 4. Automate your docker RUN command with aliases for Linux users

following theses steps leads to have a fully controlled jupyter/python environnement with only this command to prompt :
>     jupyter

## 1. Basic uses of docker (how to start)

### Install docker engine

Go on [Docker website](https://www.docker.com/get-started) and follow instruction to install docker on windows / mac.

For linux users go [ubuntu/#installation-methods](https://docs.docker.com/engine/install/ubuntu/#installation-methods)

Also, I recommend to follow the [linux-postinstall/#manage-docker-as-a-non-root-user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user) because adding `SUDO` in front of every docker command become painful pretty quick.

if you can run : 
>     docker run hello-world

and get grettings from docker dev teams, your docker engine is ready.

### search and pull an existing image on docker hub

Now that the engine is ready to run containers, we need an image (the blueprint).

[Docker hub](https://hub.docker.com/search?q=&type=image) offers a big choice of published officials and users' images.

Meaning that, there is a lot of verified containers already on shelf for anyone to use : ```ubuntu, redis, postgres, mysql, alpine , python ... and a lot more...```

Here, I will **focus on the process for the Jupyter image** but it's mostly the same for each one of them :
*   search a image with your keywords : `jupyter`
*   open the version you are interested in : `jupyter/all-spark-notebook`. I use this one because of the Spark tool, but there is other images available.

In the image description, you have useful **informations on the command and options available** to run it, sometimes you even have the **dockerfile (image building instructions in details)** and you have :
>     docker pull jupyter/all-spark-notebook 

This instruction will download the image in your engine and you will be able to run it.

Here is a list of image in my own docker engine (with command ```docker images```)

>       :~$docker images
>       REPOSITORY                   TAG                 IMAGE ID       CREATED         SIZE
>       postgres                     latest              1f0815c1cb6e   2 weeks ago     314MB
>       python                       alpine              55d14c2b2fc1   4 months ago    44.9MB
>       ubuntu                       latest              9140108b62dc   5 months ago    72.9MB
>       jupyter/all-spark-notebook   latest              7fd9190e2985   5 months ago    3.87GB


### run image as container and use it

Now, to run the jupyter notebook image as a container, the minimalist command is (most of the time, this command is also gven in image description on Docker hub) :

>       docker run -it --rm -p 8888:8888 -p 4040:4040 jupyter/all-spark-notebook

+   **-it**: keeps the terminal open and interractive (it's needed because it will give and URLadress to which the notebook is available)
+   **--rm**: order the container destruction when it's stopped (optionnal, because not having this will not prevent you to run a container but it's useful for process cleaning purposes)
+   **-p 8888:8888 -p 4040:4040**: permit an access to this container with port 8888 and 4040 (these port change with the type of service and application you run, again, theses infos are normally given in the description page of the image)
+   **jupyter/all-spark-notebook** : image name (repository)

Your terminal should display the URL adress on which you can access the notebook app with your favorite internet browser:
>       [NotebookApp] Jupyter Notebook 6.1.3 is running at:
>       [NotebookApp] http://668d103c6e16:8888/?token=e61ca0d5ca16871aa836dc734e34c4e6f3f4a53d35c20883
>       [NotebookApp]  or http://127.0.0.1:8888/?token=e61ca0d5ca16871aa836dc734e34c4e6f3f4a53d35c20883
>       [NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).

Note : the URL is composed of :
*   your localhost (meaning your computer) : **127.0.0.1** , because that where the container is running
*   the port you linked on your run command : **8888**
*   a connexion token : **?token=e61ca0d5ca16871aa836dc734e34c4e6f3f4a53d35c20883**, this is generated for security purposes by the jupyter app at launch and will be different at every RUN.

From there, you can open a new notebook (in python for example) and start coding : a ```print('hello world')``` should do.

## 2.    Finalise your jupyter setup with few options

So, the container is running, but, for now, everything we create or code is inside the container and will be lost when container is killed. Meaning you can modify or create files inside a container, the next time you will run it, new container will be build from the original (unchanged) image you pulled earlier.
And this is great, it ensures the constant behaviour of containers. 

We need to tweak the run command to keep our work, thanks to the **volume argument** :

>       -v /home/username/myworkfolder:/home/jovyan/work

Adding this option to the RUN command will couple the **work folder inside the container** '''/home/jovyan/work''' to ***your local folder*** '''/home/user/myworkfolder''', so you keep the content of what you code when container is taken down.
*(replace /home/username/myworkfolder by your own work tree of course)*

So now, our RUN command should look like 
>       docker run -it --rm -p 8888:8888 -p 4040:4040 -v /home/username/myworkfolder:/home/jovyan/work jupyter/all-spark-notebook


### First checkpoint

From here we have :

*   Installed an engine that handles containers
*   A [images Hub](https://hub.docker.com/) on which we can find all kind of setups (professionnal and amateur) in a "ready to run" format with documentation.

*   Jupyter containers that we can run from pulled image, with a *relatively* simple command, and we get to keep our work with the shared volume option. (If you want to explore available options during a run command : [docker RUN reference](https://docs.docker.com/engine/reference/run/) or help command in terminal: '''docker run --help''')   

*   An access to the Jupyter Notebook environnement with our favorite browser to start coding and testing things.

And it is nice... but not over yet...

You could just use this container as it is, but you will need a few more things...

## 3.   Improve a container (by installing new libraries)

Now we need to adress a question : What if you want to use a specific python library for a project, a librairie that is not in the original package of this container/image ? 

This jupyter image contains a lot of useful librairies as it is (execute '''pip list''' in any page to see), but you will have to install another one some day, let's say : keras and tensorflow because you want to try out DeepLearning !

There is a few way to do it :

*   1 . **Rapid & non-permanent** : Install librairies within your jupyter file by executing a : '''pip install tensorflow'''. This will work but librairies installed will die with the container. You will have to re-install them everytime you run a new jupyter container... It might get to your nerves pretty quick but works for quick test.

*   2 . **Over-complicated** : Get your hand on the dockerfile (= image build instructions) and modify it to add theses needed libraries before rebuilding a new image. It seems a bit complex for *new docker users* and dockerfile of heavy tools like JupyterAnacondaSparkNoteBook are way to complex to meddle and we just want to add a python library...

*   3 . **Permanent and rather simple** *(Spoiler : it is the one)* : Install libraries with PIP, and save the state of your current container as a new personnal image with a few docker commands.

Let's see how to do that.

### Commit a container as image

Once you installed your package with PIP in jupyter interface, open a command terminal : there is a few docker command to use.

check your running containers states :

>       :~$ docker ps

you get this kind result :

>       CONTAINER ID   IMAGE                        COMMAND                  CREATED         STATUS         PORTS                                            NAMES
>       fa87b81c0ae5   jupyter/all-spark-notebook   "tini -g -- start-no…"   5 seconds ago   Up 4 seconds   0.0.0.0:4040->4040/tcp, 0.0.0.0:8888->8888/tcp   jovial_visvesvaraya

my currently running container as an ID **fa87b81c0ae5** and a NAME **jovial_visvesvaraya**. You can use either to commit your container :

>       docker commit fa87b81c0ae5 myimprovedjupyterimage

This command just copy your container as it is into your images list, adding the **myimprovedjupyterimage**:

>       :~$ docker images
>       REPOSITORY                   TAG                 IMAGE ID       CREATED          SIZE
>       myimprovedjupyterimage       latest              6739586a8e50   25 seconds ago   3.87GB
>       jupyter/all-spark-notebook   latest              7fd9190e2985   5 months ago    3.87GB

### Run your image

You can now RUN your improved image by modifying the RUN command and replacing image name:

 >       docker run -it --rm -p 8888:8888 -p 4040:4040 -v /home/username/myworkfolder:/home/jovyan/work myimprovedjupyterimage

That's it ! (you can try to import the newly installed librairy to check if it is there at launch)

### Second Checkpoint

at the [First check point], we had : 

*   Capabilities to download and use dockerhub ready to use images 

Now we also have : 

*   A simple way, via JupyterNotebook itself and PIP, to install new python librairies if needed

*   With Docker, a way to save our improved container into our own docker image

*   RUN at will a container from this fine tunned image


Normally, at this point, you have all you need to start coding in JupyterNotebook environnement.

As I am a linux user and I find my RUN command pretty boring to enter or copy/paste in my terminal, the next and final part will be about ways to create an Alias to launch my personnal configuration of Jupyter.

## 3.   Automate your docker RUN command with aliases (for Linux users)

So the RUN command for our Jupyter container is pretty big :
 >       docker run -it --rm -p 8888:8888 -p 4040:4040 -v /home/username/myworkfolder:/home/jovyan/work myimprovedjupyterimage


Linux offers a way to encapsulate this kind of command into simpler one, called ```ALIAS```

In your **HOME** directory, there is a file called ```.bashrc```, if you open it in a text editor and go near the end, there is a section called ```# Alias definitions``` which stipulate that :

>       # You may want to put all your additions into a separate file like
>       # ~/.bash_aliases, instead of adding them here directly.
>       # See /usr/share/doc/bash-doc/examples in the bash-doc package.

so let's keep modifications to this file minimal by adding links to our own aliases files and code new things there. Personnaly, I have  two additionnal alias files in my HOME, **.bash_aliases** and  **.docker_aliases** and I have added these lines in the .bashrc : 

>       if [ -f ~/.bash_aliases ]; then
>           . ~/.bash_aliases
>       fi

>       if [ -f ~/.docker_aliases ]; then
>           . ~/.docker_aliases
>       fi

Now, in the **.docker_aliases**, I only keep **docker command** encapsulations, like the one for this JupyterNotebook :

>       jupyter(){
>         docker run -it --rm \
>           --name jupyter \
>           -p 8888:8888 -p 4040:4040 \
>           -v $HOME/work:$HOME/work \
>           -w $HOME/work \
>           myimprovedjupyterimage
>       }

To describe this line by line :
1. **name of the alias**, that's what we will type in the command prompt. Brackets open and close the encapsulation.
2. Beginning of the **docker RUN command**
3. **Name argument** : define the **name of my container** instead of docker random picked name 
3. **Ports arguments** : needed by Jupyter
4. **Volume argument** : linking my work folder to the container work folder
5. **workdirectory argument** : repositionning the working directory to my folder
6. the **name** of my improved **image**

With this micro-script, I can now launch my own JupyterNotebook easily with this simple command :
>       jupyter 

Simple and error proof !

You can also write this script so that it take the current directory the terminal is in (pwd) as working directory, you just have to be careful to launch your jupyter at the right place :

>       jupyter(){
>         local curworkdir=$(pwd)
>         docker run -it --rm \
>           --name jupyter \
>           -p 8888:8888 -p 4040:4040 \
>           -v $curworkdir:$curworkdir \
>           -w $curworkdir \
>           myimprovedjupyterimage
>       }

