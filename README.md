
# Course End Project
## PGC AIML Foundations: Programming Refresher
### part of Caltech PG program for Artificial Intelligence and Machine Learning

### Shopping App using Python 

# Table of Contents
[Overview](#_toc193729900)

[Requirements](#_toc193729901)

[Shopping App - Core Requirements](#_toc193729902)

[Software version](#_toc193729903)

[Code repository](#_toc193729904)

[folder structure](#_toc193729905)

[Database schema](#_toc193729906)

[ER Diagram](#_toc193729907)

[Tables as in the database](#_toc193729908)

[User Interface](#_toc193729909)

[Key Features](#_toc193729910)

[SQlite3 database](#_toc193729911)

[Mock data](#_toc193729912)

[Text based User Interface (TUI)](#_toc193729913)

[Role based Access Control (RBAC)](#_toc193729914)

[Data persistence](#_toc193729915)

[Database initialization](#_toc193729916)

[Predefined Users](#_toc193729917)

[Execution](#_toc193729918)

[Conclusion](#_toc193729919)


##
<a name="_toc193729900"></a>
## Overview
    This is the project developed for Course end assessment of the below course under **Caltech Post Graduate Program in AI and Machine Learning.**

    PGC AIML Foundations: Programming Refresher

The requirement is to develop a shopping cart app (backend) using Python that provides few user (shopping user) level features and few administrator level features.

The full problem statement is available in [word document format here](https://lms.simplilearn.com/user/project/download-attachment?file=1688638807_problem_statement_creating_a_shopping_app_using_python.docx)

This app has been developed in python programming language and *sqlite3*  as database store.
## <a name="_toc193729901"></a>Requirements
After reviewing the problem statement, the following software requirements have been derived to ease out the development process, so all features are implemented.
### <a name="_toc193729902"></a>Shopping App - Core Requirements

|` `Req-Id|Requirement description|Status|
| :- | :- | :- |
|1|A welcome message should initially display|**Completed**|
|2|demo database to be created for user and admin login|**Completed**|
|3|construct sample product catalog|**Completed**|
|4|product id, category id, price should present in database|**Completed**|
|5|Both administrator and users can view the catalog|**Completed**|
|6|user could view cart items|**Completed**|
|7|user could add items to cart|**Completed**|
|8|user could remove items from cart|**Completed**|
|9|demo payment checkout options|**Completed**|
|10|gateway redirect message after checkout|**Completed**|
|11|admin has exclusive login|**Completed**|
|12|error to be displayed on all invalid actions|**Completed**|
|13|admin could add new products to catalog|**Completed**|
|14|admin could modify existing products in catalog|**Completed**|
|15|admin could remove product from catalog|**Completed**|
|16|admin could add new catalog/category|**Completed**|
|17|admin could remove existing catalog/category|**Completed**|
|18|user should be prevented from all admin actions|**Completed**|




## <a name="_toc193729903"></a>Software version
The following are the versions of different software used in this application.

|**Software**|**Version**|
| :- | :- |
|Python Interpreter|3\.12.0|
|Sqlite3 database|3\.49.1 (64 bit)|
|Dbeaver|25\.0.1 (Community edition)|


## <a name="_toc193729904"></a>Code repository
The code including the sql files, documents, etc., of this application is available in the following GitHub repository. 

<https://github.com/msolayap/shopping_app>
### <a name="_toc193729905"></a>folder structure
For simplicity, the project is not so modularized. Each *class* should be developed in separate files, but instead all the code with classes, configurations, methods are placed in one single file called “app.py.” The code is organized in the following manner.

|Folder|Purpose and contents|
| :- | :- |
|shopping\_app/src/|Main folder for application source.[ app.py](mailto:https://github.com/msolayap/shopping_app/blob/main/src/app.py) is the primary application file.|
|shopping\_app/src/db/|Folder holding all SQL initialization file and actual database file (.db). |
|shopping\_app/docs/|Folder containing all project documents like problem statement, ER diagram, Application screenshots, this writeup document, etc.,|

## <a name="_toc193729906"></a>Database schema
Based on the requirements, table schemas were created for various features like products, catalog, users, user roles, user permissions, cart management, etc.,

Following are the list of tables created in the database.


|Table Name|Purpose|
| :- | :- |
|categories|Table to hold list of product catalogs|
|products|Table to hold list of available products under each catalog.<br>Foreign Key reference categories for category type|
|roles|Table to hold list of roles in the application|
|permissions|Table to hold list of all permissions available in the application|
|role\_permissions|Table to hold map of permissions applicable for each role in the application<br>Foreign key reference roles and permissions tables|
|users|Table to hold list of users in the application|
|users\_roles|Table to hold map of users to permitted roles in the application<br>Foreign key reference users and roles tables.|
|cart|Table to hold all carts created by users|
|cart\_items|Table to hold all items within each cart created by users during application usage.<br>Foreign key reference cart table for cart id of each item|
|payment\_modes|Table to hold list of available payment methods in the application.|




### <a name="_toc193729907"></a>ER Diagram
The following image shows the entity relationships between the tables present in the database.

![](Aspose.Words.03b9893a-e3d6-476f-b951-c7e7a0545a66.004.png)

### <a name="_toc193729908"></a>Tables as in the database
![](Aspose.Words.03b9893a-e3d6-476f-b951-c7e7a0545a66.005.png)

<a name="_toc193729909"></a>
## User Interface
Though the problem statement does not mandate User Interface as requirement, anyway its developed to test and show case the features of the application. Text based menu interface and prompt-based user input have been implemented for simplicity. For e.g., see the images below.

Login screen

![A screenshot of a computer

AI-generated content may be incorrect.](Aspose.Words.03b9893a-e3d6-476f-b951-c7e7a0545a66.006.png)

Main Menu showing various user options.

![A screenshot of a computer

AI-generated content may be incorrect.](Aspose.Words.03b9893a-e3d6-476f-b951-c7e7a0545a66.007.png)

<a name="_toc193729910"></a>
## Key Features
Apart from completing all the core requirements mentioned in the problem statement, the app has some features to note, such as
### <a name="_toc193729911"></a>SQlite3 database
Sqlite3 based database implementation (instead of mock data in process instance).
### <a name="_toc193729912"></a>Mock data
Mock data can be filled to the relevant Database Tables, using SQL DDL statements.
### <a name="_toc193729913"></a>Text based User Interface (TUI)
User Interface Menus were designed close to a professional application with proper alignment of elements using Python format strings.
### <a name="_toc193729914"></a>Role based Access Control (RBAC)
Role Based Access Control has been implemented using a full normalization model. The following four tables play a vital role in that. 

- users
- roles
- users\_roles
- permissions
- roles\_permission

Users were mapped to their roles in *the users\_roles* table, correspondingly roles and applicable permissions were mapped in *roles\_permissions* table.

In this way, not just users or admin, but any number of roles can be created and assigned to users with specific permissions. For e.g., a category\_admin to manage product catalog or product\_admin to add, remove products alone can be created easily.

This provides fine-grained access control in the application.
### <a name="_toc193729915"></a>Data persistence
Any modification to the product catalog will be persisted as the actual data were written to database tables in real time.
## <a name="_toc193729916"></a>Database initialization
Before running the app, the database must be initialized with Tables and Mock data in the tables. The DDL SQL statements and mock data are available in the SQL file *src/db/init\_database.sql*

The file can be executed by the following steps.

Launch sqlite CLI interface. **Mickoo** is the application name, so the database is created in the file *mickoo.db*

![](Aspose.Words.03b9893a-e3d6-476f-b951-c7e7a0545a66.008.png)

Execute the init SQL file using the “.read” command in SQLITE cli interface.

![A black screen with white text

AI-generated content may be incorrect.](Aspose.Words.03b9893a-e3d6-476f-b951-c7e7a0545a66.009.png)
## <a name="_toc193729917"></a>Predefined Users

|user name|password |role|
| :- | :- | :- |
|user1|abc123|User (Normal shopping user)|
|user2|abc123|User (Normal shopping user)|
|admin1|abc123|Administrator|
|admin2|abc123|Administrator|
## <a name="_toc193729918"></a>Execution
The app can be started in command line interface. Use “bash” in Linux or “command” shell in Windows operating system.

![A black background with white text

AI-generated content may be incorrect.](Aspose.Words.03b9893a-e3d6-476f-b951-c7e7a0545a66.010.png)

![A screenshot of a computer

AI-generated content may be incorrect.](Aspose.Words.03b9893a-e3d6-476f-b951-c7e7a0545a66.011.png)

Please refer to the screenshot document for full usage of the application.
## <a name="_toc193729919"></a>Conclusion
` `This project is a simple implementation of the problem statements, still there is ample room for improvement. For example, the following features could be implemented.

- Security
- Modularization
- Scalability
- Asynchronization
- Cache implementation
- Data security
- REST API based backend
- Real Payment interface.

