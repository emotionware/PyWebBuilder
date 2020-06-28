# PyWebBuilder

### Introduction

PyWebBuilder is an open source project for developing enterprise-data web projects of any kind.

It uses MySQL as database or MariaDB.
Automatically creates source code integrated on one Python Project, as a Flask project.

Runs on Linux and Windows, i suppose on Mac too, i have nost tested (i dont have a Mac).

It works better with Google Chrome.

What kind of projects you can develop?
Database driven apps like...
CRM, ERP of any kind, administrative solutions, account solutions, data control projects of any kind; customers, products, etc. 

I developed PyWebBuilder with and abstraction idea of data model applications.

Everything here (data related pages) has two main web pages; 

- the datagrid view
- the form view

With the datagrid view you can admin multiple records, delete, open, block, find data over the records etc..
With the form view you can edit one record and do any actions related to that record.

## Speed is the point
I developed this solution for making developer life easier. As a developer when i need to create a solution usually the process it's very similar... providers, customers, products, sells, discounts... records... tables... querys... reports... Usually all lands at same technical solutions.... So, can we automate all this?... this is the point with PyWelBuilder.

## How can i create a solution?

### First - The database
All projects starts from a mysql database skeleton called vacio.sql (you can find this skeleton inside the folder database _4TPyModel/database)

#### Step 1 - Create an empty database on MySQL or MariaDB
#### Step 2 - Load vacio.sql inside your database. 
You can do this from terminal on linux/windows with mysql.exe or mysql -u root -p databasebame < path/to/vacio.sql
#### Step 3 - Update dbstring.py (_4TPyModel/code/dbstring.py) with database info like username, database name, server ip or name and port (usually 3306)
#### Step 4 - You can now run the flask project. I recommend using PyCharm Community Edition (runserver.py)

### Second - Creating the data pages

Well this the most important point here. PyWebBuilder can understand some logic about tables creation. We must follow some rules;

#### First Rule. All tables names are lower case
#### Second Rule. All tables name begins with tbl
Example;
tblcustomer, tblprovider, tblsell,e tc...
#### Thrid Rule. First field on every table must;
1. All fields must be UPPERCASED
2. First field must start with ID plus the tablename without tbl. Example. A table called tblcustomer bust have the first field called IDCUSTOMER
3. The first field is the keyfield is INT (11) auto increment and not null. IT's a keyfield.
#### All fields must be UPPERCASED

### Field Types
PyWebBulder understand some field types. PyWebBulder checks the comment made on every field on mysql comments field area. This is the key concept for PyWebBuilder understand what kind of control must create.

The field types are; short text, big text, date, time, sublinked table, numeric field, money field, url field, email field, whatsapp field, password field, rating field, checkbox field, and calendar field.

Please see this video for understand this better. 
LINK TO VIDEO ABOUT CREATING FIELDS


# Building

# Sysbuild

# Systable

# Master/detail

# Attachments and notes

# Calendar

# Blocking Records

# Deleting Records

# Clone Records

# Hide fields on form

# Hide fields on grid

# Not editable fields

# Store Procedures AFTER INSERT, AFTER UPDATE, REFRESCADOR

# Grid Buttons

# Form Buttons

# Grid Inclusions

# Form Inclusions

# Status item

# On Value Change Trigger

# Blocky Development Integration

# Help text

# User Types (levels)

# Permissions

# Login and users creation

# Main menu config

# Graphical menu config

# Making diagrams

# Voice integration

# SMTP

# Form Config (captions, field order, etc..)

# Adding custom controls

# Mobile version

# Google Form Integration

# Templates

# Admin Template

# Home Template Redirection

# External Perspetives

# Mobile Menu


