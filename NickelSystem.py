#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mtTkinter import *
#Entry,Label,Toplevel,StringVar,EW
from os.path import getsize,normpath,isfile,isdir,islink
import ctypes
import thread
import threading
import time
from collections import OrderedDict
import subprocess
from lib.ScrollB import ScrollB

from lib.Rtfd import Rtfd

from lib.Binding import Binding as Binding

from os import path

#Script comes here , only import steps are a little abstract waiting the code.
import winshell
import send2trash
