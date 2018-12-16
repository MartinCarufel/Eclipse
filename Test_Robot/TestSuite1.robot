*** Setting ***
Library    ../pythonLib/Function_Lib.py
*** Test Cases ***
testcase1
    #Print Screen    Bonjour
    #Greet Person    Robert
    Test 1
    #${result} =    Additionne    ${3}  ${5}  ${10}  ${100}
    #Log To Console    ${result}    
    #${fileName} =    Create Log File
    #Print Screen    ${fileName}