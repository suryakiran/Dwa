from waflib.Configure import conf

def options(ctx):
    pass

def configure(ctx):
    ctx.start_msg('Checking for alembic')
    lib_names = ['Abc', 'AbcCollection', 'AbcCoreAbstract', 'AbcCoreFactory',
                 'AbcCoreHDF5', 'AbcCoreOgawa', 'AbcGeom', 'AbcMaterial',
                 'AbcOpenGL', 'Ogawa', 'Util', 'WFObjConvert']
