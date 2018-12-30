*** Setting ***
Library    mylib.py
Library    Process    
*** Test Cases ***
Test1
    Log To Console    Allo le monde
    log    test2
    #${result}=    Run Process    Calcule    10    5  
    ${result}=    Calcule    ${10}    ${5}  
    Log To Console    ${result}