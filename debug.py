from pathlib import Path

from _debug_external import PathFinder

root_path = (Path('cow')).absolute()
target_path = (Path('cow') / 'moo').absolute()

spec = PathFinder.find_spec('cow.moo',[str(root_path), str(target_path)])
print(spec)



