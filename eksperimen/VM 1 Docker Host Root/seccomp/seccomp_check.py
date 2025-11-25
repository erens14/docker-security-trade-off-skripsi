# seccomp_check.py
import ctypes, errno, sys

libc = ctypes.CDLL("libc.so.6", use_errno=True)

def try_ptrace():
    PTRACE_TRACEME = 0
    r = libc.ptrace(PTRACE_TRACEME, 0, None, None)
    e = ctypes.get_errno()
    return r, e

def try_open_by_handle_at():  
    return None

r,e = try_ptrace()
print("ptrace:", r, "errno:", e, errno.errorcode.get(e))
