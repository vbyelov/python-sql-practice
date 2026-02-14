from platform import platform, machine, processor, system, version
from platform import python_implementation, python_version_tuple

print(platform(aliased = False, terse = False))
print(platform())
print(platform(1))
print(platform(0, 1))

print(machine())

print(processor())
print(system() + ' System')
print(version() + ' Version')

print(python_implementation() + ' Python Implementation')
print(str(python_version_tuple()) + ' Python Version Tuple')

for atr in python_version_tuple():
    print(atr)

import platform

print(dir(platform))
