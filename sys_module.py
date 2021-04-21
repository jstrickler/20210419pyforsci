import sys
import datetime

print(sys.prefix)
print(sys.executable)
print(sys.version_info)
print(sys.version_info.major)
print(sys.version_info[0])

print(sys.modules['datetime'])
print(sys.modules['datetime'].datetime.now())

print(sys.platform)

print("Durham, we have a problem", file=sys.stderr)


