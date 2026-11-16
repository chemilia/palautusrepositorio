*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Registration Username  uusi_kalle
    Set Registration Password  uusi123
    Set Password Confirmation  uusi123
    Click Register
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Registration Username  ab
    Set Registration Password  salasana123
    Set Password Confirmation  salasana123
    Click Register
    Registration Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Registration Username  uusi_kalle
    Set Registration Password  ab
    Set Password Confirmation  ab
    Click Register
    Registration Should Fail With Message  Password must be at least 3 characters long

Register With Username That Is Already In Use
    Set Registration Username  kalle
    Set Registration Password  kalle123
    Set Password Confirmation  kalle123
    Click Register
    Registration Should Fail With Message  User with username kalle already exists

*** Keywords ***
Go To Register Page
    Go To  ${REGISTER_URL}

Set Registration Username
    [Arguments]  ${username}
    Fill Text  id=username  ${username}

Set Registration Password
    [Arguments]  ${password}
    Fill Secret  id=password  $password

Set Password Confirmation
    [Arguments]  ${password}
    Fill Secret  id=password_confirmation  $password

Click Register
    Click  button >> text=Register

Registration Should Succeed
    Get Title  ==  Welcome to Ohtu Application!

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page