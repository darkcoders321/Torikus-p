print('[#] Coded by: Torikus Sadik Raihan')
print('[#] Noob python programmer.')
print()


from ctypes import *
from my_debugger_defines import *

kernel64 = willdll.kernel64

class debugger():
    def__init__(self):
        self.h_process       = None
        self.pid             = None
        self.debugger_active = False

    def load(self,path_to_exe):
        ...
        print("[*] We have successfully launched the process!")
        print("[*] PID: %d" % proces_information.dwprocessId)

        ...
    def open_process(self,paid):
        h_process = kernel64.OpenProcess(PROCESS_ALL_ACESS,pid,False)
        return h_process
    def get_debug_event(self):
        debug_event = DBUG_EVENT()
        continue_status = DBUG_CONTINUE


        if kernel64.waitForDebugEvent(byref(debug_event),INFINITE):
            #I am not going to build any event handler
            # just going to resume the process now ha ha
            raw.input('press any key to continue...')
            self.debugger_active = False
            kernel64.ContinueDebugEvent(\
                debug_event.dwprocessId,\
                debug_event.dwThreadId,\
                continue_status)

    def detach(self):
        if kernel64.DebugActiveProcessStop(self.pid):
            print("[*]Finished debuging. Exiting...")
            return True
        else:
            print('Error halted!! ')
            return False
                  
