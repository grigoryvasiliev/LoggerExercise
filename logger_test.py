import logging
import logging.handlers

log = logging.getLogger( "MyLog" )
log.setLevel(logging.INFO)
handler = logging.handlers.RotatingFileHandler(r'test.log', maxBytes=100,backupCount=500)
log.addHandler(handler)

log.info('log in root process before starting external process')

import subprocess
subprocess.Popen('python.exe external.py')

log.info('log in root process after starting external process')
