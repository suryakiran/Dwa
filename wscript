top = '.'
out = 'build'
from waflib.Configure import conf
from waflib.Tools import gcc, compiler_cxx, compiler_c

tools = {
    'builtin':
    ['compiler_cxx'],
    
    'custom':
    ['openexr', 'alembic', 'boost', 'python'],
}

def options(ctx):
    ctx.add_option('--prefix', action='store', default=out, help='prefix dir')
    [ctx.load(t) for t in tools['builtin']]
    [ctx.load(t, tooldir='tools') for t in tools['custom']]

def configure(ctx):
    print ('Configuring the project in ' + ctx.options.prefix)
    [ctx.load(t) for t in tools['builtin']]
    [ctx.load(t, tooldir='tools') for t in tools['custom']]
    ctx.recurse('Boost')

def test(ctx):
    print type(ctx)

def build(ctx):
    ctx.recurse('Boost')

def install(ctx):
    print type(ctx)
