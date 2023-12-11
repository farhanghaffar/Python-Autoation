## **Python Behave BDD Framework**

This is a BDD automation framework developed on Selenium and Python Behave.

Page Object Model is followed in this framework

**pages** folder contains the web elements and corresponding actions of the pages

**features** folder contains **steps** folder which has all the test files and also the feature files.

**configuration** directory contains the configuration files

**requirements.txt** file contains the library versions used

**reports** folder contains **HTMLReports** and **Screenshots**. HTMLreports folder contains reports of the test scrips and its currently not yet decided. Screenshots folder will contains the screenshots of the failed test cases or the failed condition.



### **Commands to run the tests**

**To run the test without allure report**  TDB
`behave NavigoPlatform/features/login.feature`

**To run the test tagname**  TDB
`behave NavigoPlatform/features/login.feature --tags=<tagname>`

**To run the test with allure report**  TDB
`behave -f allure_behave.formatter:AllureFormatter -o reports/ NavigoPlatform/features/login.feature`

[comment]: <> (updated by Farhan)
**To run the test without allure report** `behave NavigoPlatform/features/login.feature`

**To generate the html allure report from the json files inside reports folder**
`allure serve reports/`   TDB


### **Use of PascalCase and snake_case**
Snake case is used for creating variable and method names.
eg: method names can be used like this - "upload_seat_schematics"
    variable names can be used liek this - "tail_number"
    for locators, we can use like this to easily identify - "LOC_MainDeck_Toggle"

PascalCase can be used for creating ClassNames:
Eg: ClassNames can be used like this - "CreateAirCraftPage"

camelCase will not be used anywhere !
