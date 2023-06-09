# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from __future__ import division

import builtins
import os
import sys

from . import backends
from .backends import CORE_BACKENDS, BACKEND_NAMES, BACKENDMAP, TRIED_BACKENDS
from .. import config
from .base import BaseApplicationBackend as ApplicationBackend  # noqa
from ._detect_eventloop import _get_running_interactive_framework
from ..util import logger

class Application(object):
    def __init__(self, backend_name: str | None = None): ...
    def __repr__(self): ...
    @property
    def backend_name(self): ...
    @property
    def backend_module(self): ...
    def process_events(self): ...
    def sleep(self, duration_sec: float): ...
    def create(self): ...
    def is_interactive(self): ...
    def is_notebook(self): ...
    def run(self, allow_interactive: bool = True): ...
    def reuse(self): ...
    def quit(self): ...
    @property
    def native(self): ...
    def _use(self, backend_name=None): ...
