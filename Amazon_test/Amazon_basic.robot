*** Settings ***
Suite Setup    Open Browser    https://www.amazon.ca/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=caflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.ca%2F%3Fref_%3Dnav_custrec_signin&switch_account=    Chrome
Suite Teardown    Close Browser
Library    SeleniumLibrary

*** Variables ***
${undefined}    https://www.katalon.com/

*** Test Cases ***
Test Case
    #Open Browser    https://www.amazon.ca/    Chrome
    Wait Until Page Contains Element    id=ap_email
    #Click Element    id=ap_email
    Input Text    id=ap_email    maccam6@gmail.com
    Input Password    id=ap_password    18,Mac&Amo
    Click Button    id=signInSubmit
    #Click Element    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Bonjour, Martin'])[1]/following::span[1]
    #Click Element    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Votre compte'])[3]/span[1]
    Element Text Should Be    //span[contains(text(),'Bonjour, Martin')]    Bonjour, Martin
    check compte page    Votre compte    Votre compte
    check compte page    Vos commandes    Vos commandes
    check compte page    Votre liste de souhaits       Amazon.ca
    check compte page    Vos recommandations    Votre Amazon.ca
    Mouse Over     xpath=//a[@id='nav-link-yourAccount']//span[@class='nav-icon nav-arrow']
    sleep    1s
    Click Element    xpath=//span[contains(text(),'Fermer la session')]
    
    
*** Keyword ***
check compte page
    [Arguments]    ${element}    ${title_text}
    Mouse Over     xpath=//a[@id='nav-link-yourAccount']//span[@class='nav-icon nav-arrow']
    sleep    1s
    Click Element    xpath=//span[@class='nav-text'][contains(text(),'${element}')]
    Title Should Be    ${title_text}