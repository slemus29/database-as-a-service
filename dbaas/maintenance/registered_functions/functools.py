import sys, inspect

def is_mod_function(mod, func):
    return inspect.isfunction(func) and inspect.getmodule(func) == mod

def get_registered_functions():
    current_module = sys.modules[__name__]
    return ((func.__name__, func.__doc__) for func in current_module.__dict__.itervalues()
            if is_mod_function(current_module,
                func) and func.__name__ not in['is_mod_function','get_registered_functions'])


def return_host_id_str(host_id):
    """Get HostId String"""
    return str(host_id)

