*** Setting ***
Library    mylib
Library    Process  
Library    SeleniumLibrary   
Suite Setup    Run Keyword    Open the Browser    ${url}    Chrome
Suite Teardown    Close the Browser
*** Variable ***
${url}    http://4testautomation.com/VS2015Test/
@{userName}    Testerselenium1    Testerselenium2    Testerselenium3    Testerselenium4
...            Testerselenium5    Testerselenium6    Testerselenium7    Testerselenium8
...            Testerselenium9    Testerselenium10    Testerselenium11    Testerselenium12
...            Testerselenium13    Testerselenium14    Testerselenium15
...    

@{password}    selenium1    selenium2    selenium3    selenium4    selenium5    selenium6    selenium7
...            selenium8    selenium9    selenium10    selenium11    selenium12    selenium13    selenium14
...            selenium15
*** Test Cases ***
Test1
    Log To Console    Allo le monde
    log    test2
    #${result}=    Run Process    Calcule    10    5
    ${result}=    Calcule    ${10}    ${5}  
    Log To Console    ${result}
    
Test2
    Input Text    MainContent_LoginUser_UserName    Testerselenium4
    Input Text    MainContent_LoginUser_Password    selenium4
    Click Button    MainContent_LoginUser_LoginButton
    Capture Page Screenshot    ScreenShot.png
    Element Text Should Be    HeadLoginView_HeadLoginName    Testerselenium4  
    
Test 15 users
      :for    ${i}    ${j}    IN ZIP    ${userName}    ${password}  
      \    Login      ${i}    ${j}
      \    Check user    ${i}
      \    sleep  0.5s
      \    Logout
*** Keyword ***
Open the Browser
    [Arguments]    ${urlToOpen}    ${browser}
    Open Browser    ${urlToOpen}    ${browser}
    Maximize Browser Window
    
Close the Browser
    Sleep    5s    
    Close Browser
    
Login
    [Arguments]    ${user}    ${pass}
    Input Text    MainContent_LoginUser_UserName    ${user}
    Input Text    MainContent_LoginUser_Password    ${pass}
    Click Button    MainContent_LoginUser_LoginButton
    
Logout
    Click Link    HeadLoginView_HeadLoginStatus
    
Check user
    [Arguments]    ${user}
    Element Text Should Be    HeadLoginView_HeadLoginName    ${user}
    