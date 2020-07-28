*** Settings ***
Documentation     SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://127.0.0.1:8000/login/
${BROWSER}        Chrome


*** Test Cases ***
For-Loop-In-Range
    [Tags]    NoTest
    FOR    ${INDEX}    IN RANGE    1    5
            Open Browser To Login Page
            Input Username    dansot
            Input Password    jdrs.0012RS
            Submit Credentials
            sleep  2s
            Close Browser
 
    END



            
*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Iniciar sesión

Input Username
    [Arguments]    ${username}
    Input Text    username    ${username}
  
Input Password
    [Arguments]    ${password}
    Input Text    password    ${password}

Submit Credentials
    Click Button    btnLogin

Welcome Page Should Be Open
    Title Should Be    Welcome Page




