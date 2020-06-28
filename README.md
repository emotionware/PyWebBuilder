# PyWebBuilder

### Introduction

PyWebBuilder is an open source project for developing enterprise-data web projects of any kind.

It uses MySQL as database or MariaDB.
Automatically creates source code integrated on one Python Project, as a Flask project.

Runs on Linux and Windows, i suppose on Mac too, i have nost tested (i dont have a Mac).

It works better with Google Chrome.

What kind of projects you can develop?
Database driven apps like...
CRM, ERP of any kind, administrative solucionts, account solutions, data control projects of any kind; customers, products, etc. 

I developed with and abstraction idea of data model applications.

Everything here data related has two main web forms; 

- the datagrid view
- the form view

With the datagrid view you can admin multiple records, delete, open, block, find data over the records etc..
With the form view you can edit one record and do any actions related to that record.

## Speed is the point
I developed this solution for making developer life easier. As a developer when i need to create a solution usually the process it's very similar. Providers, customers, productos, sells, discounts... records... tables... querys... reports... Usually all lands at same technical solutions.... So, can we automate all this?... this is the point with PyWelBuilder.

## How?

### First - The database
All projects starts from a mysql database skeleton called vacio.sql (you can find this skeleton inside the folder database _4TPyModel/database)

#### Step 1 - Create an empty database on MySQL or MariaDB
#### Step 2 - Load vacio.sql inside your database
#### Step 3 - Update dbstring.py (_4TPyModel/code/dbstring.py) with database info like username, database name, server ip or name and port (usually 3306)
#### Step 4 - You can now run the flask project. I recommend using PyCharm Community Edition (runserver.py)

### Second - The data pages 






