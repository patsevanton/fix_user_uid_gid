#!/usr/bin/env python
from __future__ import print_function

import pwd
import grp
import os

def get_username_from_uid(uid):
  username = None
  try:
    username = pwd.getpwuid(uid).pw_name
    return username
  except KeyError:
    return username

def get_groupname_from_gid(gid):
  groupname = None
  try:
    groupname = grp.getgrgid(gid).gr_name
    return groupname
  except KeyError:
    return groupname

def get_uid_from_username(username):
  uid = None
  try:
    uid = pwd.getpwnam(username).pw_uid
    return int(uid)
  except KeyError:
    return uid

def get_gid_from_groupname(groupname):
  gid = None
  try:
    gid = grp.getgrnam(groupname).gr_gid
    return int(gid)
  except KeyError:
    return gid

if get_username_from_uid(503) != None:
  if get_username_from_uid(503) != 'teamcity':
    username_uid_503 = get_username_from_uid(503)
    for new_uid in range(600,610):
      if get_username_from_uid(new_uid) == None:
        os.system("sudo usermod -u {0} {1}".format(new_uid, username_uid_503))
        break

if get_groupname_from_gid(503) != None:
  if get_groupname_from_gid(503) != 'teamcity':
    groupname_gid_503 = get_groupname_from_gid(503)
    for new_gid in range(600,610):
      if get_groupname_from_gid(new_gid) == None:
        os.system("sudo groupmod -g {0} {1}".format(new_gid, groupname_gid_503))
        break

# add user teamcity
try:
  os.system('useradd -u 503 -g 503 teamcity')
except KeyError:
  print('user teamcity exist')

for home_dir in os.listdir('/home'):
  print(os.path.join('/home', home_dir))
  print(get_uid_from_username(home_dir), get_gid_from_groupname(home_dir))
  if get_uid_from_username(home_dir) != None or get_gid_from_groupname(home_dir) != None:
    os.chown(os.path.join('/home', home_dir), get_uid_from_username(home_dir), get_gid_from_groupname(home_dir))
  for dirpath, dirnames, filenames in os.walk(os.path.join('/home', home_dir), followlinks=False):
    for dirname in dirnames:
      # print(dirname)
      # print(get_uid_from_username(home_dir), get_gid_from_groupname(home_dir))
      if get_uid_from_username(home_dir) != None or get_gid_from_groupname(home_dir) != None:
        os.chown(os.path.join(dirpath, dirname), get_uid_from_username(home_dir), get_gid_from_groupname(home_dir))
    for filename in filenames:
      # print(filename)
      # print(get_uid_from_username(home_dir), get_gid_from_groupname(home_dir))
      if get_uid_from_username(home_dir) != None or get_gid_from_groupname(home_dir) != None:
        os.chown(os.path.join(dirpath, filename), get_uid_from_username(home_dir), get_gid_from_groupname(home_dir))

