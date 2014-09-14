Continuous Testing with Docker and Buildbot
===========================================

The goal of this tutorial is to help developers be more confident their
software is doing what it is designed to do, automating key parts of its QA
process.

Docker is a process oriented running engine geared toward building, shipping
and running distributed applications with a vibrant community and python
bindings.
The core idea is that your application is build and distributed with the full
stack of software dependencies (except the kernel) as a unit (a container),
so it can be easily deployed and run in an heterogeneous network. For systems
other than linux, these containers can be run on top of boot2docker for example.


Buildbot is an open-source python continuous integration framework based on
twisted. At its core, it is a scheduler with a web frontend and a database
backend for build metadata. One neat thing about this system, is its
configuration simplicity, it is just a python dictionary.



Assumptions,
  * linux based bare-metal or virtualized system
  * Intermediate programming and system level. Beginners are encouraged to
    participate as we will be talking about relevant mainstream tools and
    concepts that are widely used in our industry today and in the foreseeable
    future.


References:
    https://www.docker.com
    http://boot2docker.io
    http://buildbot.net
