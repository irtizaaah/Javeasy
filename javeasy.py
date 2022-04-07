# @irtizaaah
# This program helps create Java classes for you

# INPUT CLASS NAME
print("JAVEASY >>")
className = input('\n Class ')
className = className[0].capitalize() + className[1:];
myCode = ''
properties = []
quit = False

# INPUT MEMBER VARIABLES
while(quit is False):
  myCode = input('\n\tprivate ')
  if myCode != ';':
    access = 'private'
    dataType, name = myCode.split()
    properties.append([access, dataType, name])
  else:
    quit = True;
    
propertiesCode = ''
constructorParameters = ''
constructorCode = ''
gettersCode = ''
settersCode = ''

# TEMPLATE GETTER, SETTER, CONSTRUCTOR PARAMETERS
for prop in properties:
  propertiesCode += '\t' + prop[0] + ' ' + prop[1] + ' ' + prop[2] + ';\n' 
  
  constructorParameters += prop[1] + ' ' + prop[2] + ', '
  
  tempName = prop[2][0].capitalize() + prop[2][1:].lower(); 
  
  gettersCode += f'''
  \tpublic {prop[1]} get{tempName}(){{
  \t\treturn this.{prop[2]};
  \t}}
  '''
  settersCode += f'''
  \tpublic void set{tempName}({prop[1]} {prop[2]}){{
  \t\tthis.{prop[2]} = {prop[2]};
  \t}}
  '''

# TEMPLATE CONSTRUCTOR
constructorCode = f'\tpublic {className}({constructorParameters}){{\n' # start constructor
constructorCode = constructorCode.replace(', )', ')') # remove last comma from parameters
for prop in properties: # set constructor values
  constructorCode += f'\t\tthis.{prop[2]} = {prop[2]};\n'
constructorCode += '\t}' # end constructor

# COMPILE ALL TEMPLATE CODE
code = f'''
public class {className}{{
\n\t//MEMBER VARIABLES\n
{propertiesCode}
\n\t//CONSTRUCTOR\n
{constructorCode}
\n\t//SETTERS
{settersCode}
\n\t//GETTERS
{gettersCode}
}}
''' 
print("\n\nTRANSPILED JAVA CODE >>\n")
print(code)