from waflib.Configure import conf
import os, sys, re

def options(ctx):
    pass

def configure(ctx):
    ctx.check_cfg(
        package = 'python-2.7',
        uselib_store = 'PYTHON',
        args = ['--cflags', '--libs']
    )

    ctx.env.RPATH_PYTHON = ctx.env.LIBPATH_PYTHON
