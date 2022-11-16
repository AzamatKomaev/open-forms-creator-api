import sys
import pathlib


# Append path to current dir to sys.path.
current_dir = pathlib.Path(__file__).parent.resolve()
sys.path.append(str(current_dir))
