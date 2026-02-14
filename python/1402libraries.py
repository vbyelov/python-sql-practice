from platform import platform, machine, processor

print(platform(aliased = False, terse = False))
print(platform())
print(platform(1))
print(platform(0, 1))

print(machine())

print(processor())