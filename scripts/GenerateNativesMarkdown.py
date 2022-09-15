from ast import arg
import json
import os
from re import S

if os.getcwd().endswith("scripts"):
    print("Please run this script from the main folder!")
    print("Example: python3 scripts/GenerateNativesMarkdown.py")
    exit()

jsonContent = open("natives.json").read()
jsonContent = json.loads(jsonContent)

def getReturnName(idx):
    return jsonContent["returnNames"][idx]

def generateMarkdownFile(nativeFunc):
    returnName = getReturnName(nativeFunc["return"])
    methodName = nativeFunc["methodName"]

    if "className" in nativeFunc:
        methodName = nativeFunc["className"] + "::" + methodName

    argFmt = ""

    for argIdx in range(0, nativeFunc["minArguments"]):
        argFmt += f"unk p{argIdx}, "
    
    if not nativeFunc["minArguments"] == nativeFunc["maxArguments"]:
        argFmt += "..."
    else:
        argFmt = argFmt[:-2]

    addressFmt = f"// {nativeFunc['address']}"
    paramFmt = f"{addressFmt}\n{ returnName } { methodName }({argFmt})"
    descriptionFmt =   f"Minimum Arguments: {nativeFunc['minArguments']}\nMaximum Arguments: {nativeFunc['maxArguments']}"
    markdownFmt = f"""# {methodName}
```c
{paramFmt}
```
## Description
```
{descriptionFmt}
```
"""
    return markdownFmt

def generateClassMarkdown(className, classContent):
    markdownFmt = f"# {className}\n"
    markdownFmt += "## Functions\n"
    markdownFmt +=f"| Function | Note |\n"
    markdownFmt +=f"|----------|------|\n"

    classFuncCount = 0
    
    for currentFunc in classContent:
        linkFmt = f"[{currentFunc}]({currentFunc}.md)"
        markdownFmt += f"|{linkFmt}| |\n"
        classFuncCount += 1

    markdownFmt +=  "## Description\n"
    markdownFmt += f"```\nFunctions: {classFuncCount}\n```"

    return markdownFmt

print("generating md for global functions")

globalFunctions = jsonContent["globalFunctions"]
classFunctions = jsonContent["classFunctions"]

for currentFunc in globalFunctions:
    currentName = f"docs/globals/{currentFunc}.md"
    if not os.path.exists(currentName):
        open(currentName, "w+").write(generateMarkdownFile(globalFunctions[currentFunc]))

for currentClassName in classFunctions:
    currentClassFolderPath = f"docs/classes/{currentClassName}"
    if not os.path.exists(currentClassFolderPath):
        os.mkdir(currentClassFolderPath)
    
    open(f"{currentClassFolderPath}/README.md", "w+").write(generateClassMarkdown(currentClassName, classFunctions[currentClassName]))

    for currentFunc in classFunctions[currentClassName]:
        currentClassFuncPath = f"docs/classes/{currentClassName}/{currentFunc}.md"
        if not os.path.exists(currentClassFuncPath):
            open(currentClassFuncPath, "w+").write(generateMarkdownFile(classFunctions[currentClassName][currentFunc]))