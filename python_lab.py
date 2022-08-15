#!/usr/bin/env python3

## Libraries we will need
import sys
from Crypto.Hash import MD5

## Our secret password stored as an MD5 Hash
secret_hash="4034a346ccee15292d823416f7510a2f"

## Primary function
def checkPass(inputPass):
  inputPass = inputPass
  while True:
    print("You entered, {name}".format(name=inputPass))
    
    # create MD5 hash of the entry
    entryHash = MD5.new()
    entryHash.update(inputPass.encode('utf-8'))
    hexHash = entryHash.hexdigest()

    # show the user the hash of the entry they sent
    print("This is the MD5 hash of your entry: {hash}".format(hash=hexHash))

    # lastly let's compare it to our stored secret
    if (hexHash == secret_hash):
      print("The hashes match! The password is: {password}".format(password=inputPass))
      break
    else:
      print("The input password is not correct")
      inputPass = enterPass()
      
  sys.exit()

## funtion to get new password attempt
def enterPass():
  newPass = input("Please enter new password attempt:")
  while (len(newPass) == 0):
    newPass = input("Password must be at least 1 character, please re-enter:")
  return newPass


## This is the entry point to the program
## Read arguments and call the primary function
if __name__=="__main__":

#  Check args
  if len(sys.argv) != 2:
    print("You must enter exactly one argument.\nExiting.")
    sys.exit(-1)
  else:
    testPass = sys.argv[1]
    checkPass(testPass)
