# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_DiffEngine', [dirname(__file__)])
        except ImportError:
            import _DiffEngine
            return _DiffEngine
        if fp is not None:
            try:
                _mod = imp.load_module('_DiffEngine', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _DiffEngine = swig_import_helper()
    del swig_import_helper
else:
    import _DiffEngine
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def GetDWORD(*args):
  return _DiffEngine.GetDWORD(*args)
GetDWORD = _DiffEngine.GetDWORD
class DBWrapper(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DBWrapper, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DBWrapper, name)
    __repr__ = _swig_repr
    def __init__(self, DatabaseName = None): 
        this = _DiffEngine.new_DBWrapper(DatabaseName)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _DiffEngine.delete_DBWrapper
    __del__ = lambda self : None;
DBWrapper_swigregister = _DiffEngine.DBWrapper_swigregister
DBWrapper_swigregister(DBWrapper)

class OneIDAClientManager(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OneIDAClientManager, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OneIDAClientManager, name)
    __repr__ = _swig_repr
    def __init__(self, StorageDB = None): 
        this = _DiffEngine.new_OneIDAClientManager(StorageDB)
        try: self.this.append(this)
        except: self.this = this
    def GetClientAnalysisInfo(self): return _DiffEngine.OneIDAClientManager_GetClientAnalysisInfo(self)
    def GetClientFileInfo(self): return _DiffEngine.OneIDAClientManager_GetClientFileInfo(self)
    def DumpAnalysisInfo(self): return _DiffEngine.OneIDAClientManager_DumpAnalysisInfo(self)
    def DumpBlockInfo(self, *args): return _DiffEngine.OneIDAClientManager_DumpBlockInfo(self, *args)
    def RemoveFromFingerprintHash(self, *args): return _DiffEngine.OneIDAClientManager_RemoveFromFingerprintHash(self, *args)
    def GetBlockAddress(self, *args): return _DiffEngine.OneIDAClientManager_GetBlockAddress(self, *args)
    def GetMappedAddresses(self, *args): return _DiffEngine.OneIDAClientManager_GetMappedAddresses(self, *args)
    def GetDisasmLines(self, *args): return _DiffEngine.OneIDAClientManager_GetDisasmLines(self, *args)
    def FreeDisasmLines(self): return _DiffEngine.OneIDAClientManager_FreeDisasmLines(self)
    def ShowAddress(self, *args): return _DiffEngine.OneIDAClientManager_ShowAddress(self, *args)
    __swig_destroy__ = _DiffEngine.delete_OneIDAClientManager
    __del__ = lambda self : None;
OneIDAClientManager_swigregister = _DiffEngine.OneIDAClientManager_swigregister
OneIDAClientManager_swigregister(OneIDAClientManager)

class IDAClientManager(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IDAClientManager, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IDAClientManager, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _DiffEngine.new_IDAClientManager()
        try: self.this.append(this)
        except: self.this = this
    def SetDatabase(self, *args): return _DiffEngine.IDAClientManager_SetDatabase(self, *args)
    def StartIDAListener(self, *args): return _DiffEngine.IDAClientManager_StartIDAListener(self, *args)
    def SetIDAPath(self, *args): return _DiffEngine.IDAClientManager_SetIDAPath(self, *args)
    def SetOutputFilename(self, *args): return _DiffEngine.IDAClientManager_SetOutputFilename(self, *args)
    def SetLogFilename(self, *args): return _DiffEngine.IDAClientManager_SetLogFilename(self, *args)
    def RunIDAToGenerateDB(self, *args): return _DiffEngine.IDAClientManager_RunIDAToGenerateDB(self, *args)
    __swig_destroy__ = _DiffEngine.delete_IDAClientManager
    __del__ = lambda self : None;
IDAClientManager_swigregister = _DiffEngine.IDAClientManager_swigregister
IDAClientManager_swigregister(IDAClientManager)

class DiffMachine(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DiffMachine, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DiffMachine, name)
    __repr__ = _swig_repr
    def __init__(self, the_source = None, the_target = None): 
        this = _DiffEngine.new_DiffMachine(the_source, the_target)
        try: self.this.append(this)
        except: self.this = this
    def ShowDiffMap(self, *args): return _DiffEngine.DiffMachine_ShowDiffMap(self, *args)
    def PrintMatchMapInfo(self): return _DiffEngine.DiffMachine_PrintMatchMapInfo(self)
    def Analyze(self): return _DiffEngine.DiffMachine_Analyze(self)
    def AnalyzeFunctionSanity(self): return _DiffEngine.DiffMachine_AnalyzeFunctionSanity(self)
    def GetMatchAddr(self, *args): return _DiffEngine.DiffMachine_GetMatchAddr(self, *args)
    def GetUnidentifiedBlockCount(self, *args): return _DiffEngine.DiffMachine_GetUnidentifiedBlockCount(self, *args)
    def GetUnidentifiedBlock(self, *args): return _DiffEngine.DiffMachine_GetUnidentifiedBlock(self, *args)
    def Retrieve(self, *args): return _DiffEngine.DiffMachine_Retrieve(self, *args)
    def Save(self, *args): return _DiffEngine.DiffMachine_Save(self, *args)
    __swig_destroy__ = _DiffEngine.delete_DiffMachine
    __del__ = lambda self : None;
DiffMachine_swigregister = _DiffEngine.DiffMachine_swigregister
DiffMachine_swigregister(DiffMachine)

class DarunGrim(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DarunGrim, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DarunGrim, name)
    __repr__ = _swig_repr
    def SetLogParameters(self, *args): return _DiffEngine.DarunGrim_SetLogParameters(self, *args)
    def SetIDAPath(self, *args): return _DiffEngine.DarunGrim_SetIDAPath(self, *args)
    def GenerateDB(self, *args): return _DiffEngine.DarunGrim_GenerateDB(self, *args)
    def ConnectToIDA(self): return _DiffEngine.DarunGrim_ConnectToIDA(self)
    def Analyze(self): return _DiffEngine.DarunGrim_Analyze(self)
    def __init__(self): 
        this = _DiffEngine.new_DarunGrim()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _DiffEngine.delete_DarunGrim
    __del__ = lambda self : None;
DarunGrim_swigregister = _DiffEngine.DarunGrim_swigregister
DarunGrim_swigregister(DarunGrim)



