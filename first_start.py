# Import module namespace
import extModule
# Import exact attribute from module namespace
from extModule import anotherExternalVar

# Use attribute as a variable
print(extModule.externalVarName + ' added from main file')
print(anotherExternalVar)

# Use dir() function in order to import all variable from module namespace
dirFromModule = dir(extModule)
