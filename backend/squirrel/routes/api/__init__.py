import os
import glob

# injecting all *.py file other than __init__.py in this file
modules = glob.glob(os.path.dirname(__file__) + "/*.py")
__all__ = [os.path.basename(f)[:-3] for f in modules]
