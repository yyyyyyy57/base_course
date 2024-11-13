import sys, os

print(os.getcwd())


os.system('echo hi!')
#os.system('python3 /workspaces/base_course/lec_sys_os.py')

print(sys.version)
print(sys.path)
print(sys.platform)

print(dir(sys))
print(dir(os))