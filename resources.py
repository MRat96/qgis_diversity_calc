# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.15.2)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x01\x33\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x17\x00\x00\x00\x18\x08\x02\x00\x00\x00\x9e\x1e\xf1\x22\
\x00\x00\x00\x01\x73\x52\x47\x42\x00\xae\xce\x1c\xe9\x00\x00\x00\
\x04\x67\x41\x4d\x41\x00\x00\xb1\x8f\x0b\xfc\x61\x05\x00\x00\x00\
\x09\x70\x48\x59\x73\x00\x00\x0e\xc3\x00\x00\x0e\xc3\x01\xc7\x6f\
\xa8\x64\x00\x00\x00\xc8\x49\x44\x41\x54\x38\x4f\x63\xf8\x4f\x0d\
\x30\x38\x4d\x99\xb5\xdf\x47\x69\x23\x0e\xb4\x3f\xcf\xef\x4c\xef\
\xac\x67\x8f\xef\x41\xd5\xa2\x03\x34\xb7\x3c\x86\x98\xe5\x77\xe6\
\x04\x92\x86\xc7\xf7\x9e\xf5\xfa\x41\xed\xc8\x9b\xf5\x09\x2a\x8a\
\x0c\xd0\x7d\x74\xef\x66\x1e\xc8\x94\x9b\x8f\xa1\x7c\x04\x78\xbc\
\xf7\x0c\xd4\x69\xa5\xcf\xa0\x42\x70\x40\xbc\x29\x40\x00\x75\xa9\
\xd2\xc6\xde\xbd\x50\x11\x28\x20\xc9\x94\xff\xff\x3f\xad\xf6\x03\
\x3b\x07\x4d\x01\x89\xa6\xc0\x9d\xb3\x7f\x35\x72\x48\x93\x6a\xca\
\x7f\x58\xe8\xa0\x78\x8a\x64\x53\x20\x0a\xd0\x22\x6b\x80\x4c\xa1\
\x8a\x8f\xa8\x12\xba\xd4\x88\x69\xec\x0e\x01\x02\xe2\x4d\x81\xe7\
\x00\x2c\x59\x09\xcd\x14\xa4\xdc\x88\x50\x8a\x94\x1b\xf7\xf7\xee\
\xc5\x9f\x1b\x61\x79\x04\x1b\x02\x95\x0c\xab\xf7\x7e\xc2\x15\xe4\
\xff\x19\x76\x56\x85\x53\x8e\x46\x4d\xc1\x86\xaa\xc2\x01\x3f\x09\
\x25\xac\x92\x73\x46\xea\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\
\x60\x82\
"

qt_resource_name = b"\
\x00\x07\
\x07\x3b\xe0\xb3\
\x00\x70\
\x00\x6c\x00\x75\x00\x67\x00\x69\x00\x6e\x00\x73\
\x00\x0e\
\x0a\x6c\xba\xe3\
\x00\x64\
\x00\x69\x00\x76\x00\x65\x00\x72\x00\x73\x00\x69\x00\x74\x00\x79\x00\x5f\x00\x63\x00\x61\x00\x6c\x00\x63\
\x00\x08\
\x0a\x61\x5a\xa7\
\x00\x69\
\x00\x63\x00\x6f\x00\x6e\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x14\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x36\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x14\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x36\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x7a\xe7\x77\x45\xb1\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
