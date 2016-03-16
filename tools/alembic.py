from waflib.Configure import conf

def configure(ctx):
    ctx.start_msg('Checking for alembic')
    ctx.end_msg('Done')
