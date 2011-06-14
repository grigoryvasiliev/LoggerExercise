Exercise: Figure out the issue in the Python code with logger. 

Platform: Windows 
Python 2.6

Run the example and confirm the following problem:

C:\LoggerTest>..\Python26\python.exe logger_test.py
Traceback (most recent call last):
  File "C:\Python26\lib\logging\handlers.py", line 72, in emit
    self.doRollover()
  File "C:\Python26\lib\logging\handlers.py", line 129, in doRollover
    os.rename(self.baseFilename, dfn)
WindowsError: [Error 32] The process cannot access the file because it is being used by another process
Error in atexit._run_exitfuncs:
Traceback (most recent call last):
  File "C:\Python26\lib\atexit.py", line 24, in _run_exitfuncs
    func(*targs, **kargs)
  File "C:\Python26\lib\logging\__init__.py", line 1486, in shutdown
    h.flush()
  File "C:\Python26\lib\logging\__init__.py", line 746, in flush
    self.stream.flush()
ValueError: I/O operation on closed file
Error in sys.exitfunc:
Traceback (most recent call last):
  File "C:\Python26\lib\atexit.py", line 24, in _run_exitfuncs
    func(*targs, **kargs)
  File "C:\Python26\lib\logging\__init__.py", line 1486, in shutdown
    h.flush()
  File "C:\Python26\lib\logging\__init__.py", line 746, in flush
    self.stream.flush()
ValueError: I/O operation on closed file

As we can see that logger does not work as expected. 
Please explain the behavior and fix the problem in the code.
