muzzler
=======

A harness for running [Project Euler][1] solutions in Python.

Using a Separate Repo for Problems
==================================

You can use git-submodule to stick it in the default namespace:

    > cd ~/projects
    > git clone git://github.com/bsandrow/muzzler.git
    > cd muzzler
    > git submodule add /url/to/repo muzzler/problem

You can also link it in from somewhere else:

    > cd ~/projects
    > git clone git://github.com/bsandrow/muzzler.git
    > git clone git://github.com/user/project-euler-problems.git
    > ln -s ../../project-euler-problems muzzler/muzzler/problem

Requirements
============

 * Python 2.7+

Credits
=======

Copyright 2012 Brandon Sandorowicz <brandon@sandrowicz.org>

License
=======

LICENSE

[1]: http://projecteuler.net
