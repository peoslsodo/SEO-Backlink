
import json,requests,re,sys

try:
  
  if (sys.version_info.major == 5):
    site = input(" => Backlink  Site\t: ")
  else:
    site = raw_input(" => Backlink Site\t: ")
except:
  print("\n\n => exit\n")
