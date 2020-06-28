from flask import Flask, jsonify, request, render_template, session

def navbartemplate():
     return render_template('navbar.html',
                            projectame='Projecto Nombre',projectnameurl='project',
                            analysis='Análisis',analysisurl='analysis',
                            catalogs='Entidades',catalogsurl='entities',
                            operations='Operaciones',operationsurl='operations',
                            homelink='Home', homelinkurl='home',
                            logout='Logout', logouturl='logout',
                            adminzone='Admin', adminzoneurl='adminzone',
                            help='Ayuda', helpurl='help',
                            reports='Reportes',reportsurl='reports')
