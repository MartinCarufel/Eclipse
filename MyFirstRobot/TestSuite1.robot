*** Setting ***
Library    mylib.py
Library    ../pythonLib/Function_Lib.py
Library    Process    
*** Test Cases ***
01-Testa
    Log To Console    Allo le monde
    log    test2
    Test 1
    #${result}=    Run Process    Calcule    10    5  
    ${result}=    Calcule    ${10}    ${5}  
    Log To Console    ${result}