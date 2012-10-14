import os, sys, inspect

############
### Add subfolder public to system path so that any class can import it.
############
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"public")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)