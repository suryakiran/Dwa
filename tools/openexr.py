from waflib.Configure import conf

def options(ctx):
    pass

def configure(ctx):
    ctx.start_msg('Checking openexr')
    ctx.check_cfg(
        package = 'OpenEXR',
        uselib_store = 'OPENEXR',
        args = ['--cflags', '--libs']
    )
    openexr_prefix = ctx.check_cfg(
        package = 'OpenEXR',
        args = ['--variable=prefix']
        )

    ctx.env.RPATH_OPENEXR = ctx.env.LIBPATH_OPENEXR
    ctx.end_msg(openexr_prefix.strip())
