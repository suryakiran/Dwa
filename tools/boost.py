import os, sys, re
from waflib.Configure import conf

def options(ctx):
    ctx.add_option('--boost', action='store', default='', help='boost libs')

def is_not_empty(s):
    return (len(s.strip()) > 0)

def configure(ctx):
    boost=os.environ.get('BOOST_ROOT')
    boost_libs = []
    boost_lib_paths = set()
    for lib in filter(is_not_empty, re.split('[, ]', ctx.options.boost)):
        f = ctx.find_file('libboost_%s_mt.so' % lib, [os.path.join (boost, 'lib')])
        real = os.path.realpath(f)
        print real
        boost_lib_paths.add(os.path.dirname(real))
        prefix,ext = os.path.splitext(os.path.basename(f))
        boost_libs.append(prefix.split('lib')[1])

    if boost is not None:
        ctx.env.INCLUDES_boost = [os.path.join(boost, 'include')]
        ctx.env.LIBPATH_boost = [os.path.join(boost, 'lib')]
        ctx.env.LIB_boost = boost_libs
        ctx.env.RPATH_boost = boost_lib_paths
