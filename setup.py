#!/usr/bim/env python

from distutils.core import setup

setup( name = "pyxdg",
       version = "0.5",
	   description = "PyXDG contains implementations of freedesktop.org standards in python.",
	   maintainer = "Heinrich Wendel",
	   maintainer_email = "h_wendel@cojobo.net",
	   url = "http://cvs.cojobo.net/cgi-bin/viewcvs.cgi/pyxdg/",
	   packages = ['xdg'],
	   license = "GPL-2")