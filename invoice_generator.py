#https://invoicehome.com/invoices/129749268/edit?goal=form_start
#https://html-online.com/
import jinja2
import pdfkit
import questionary
from datetime import datetime

name = input("Enter your name:")
today_date = datetime.today().strftime("%d %b, %Y")
date = input("Enter the Booking date: ")
set_type = input("Enter the set type: ")
nail_color = input("Enter colour: ")
nail_style = input("Enter nail style: ")
gems = input("Would you like some Accesories? [y/n]") #charge extra R50 for accesories/nail deco

context = {'name': name, "today_date": today_date, "date":date, "set_type":set_type, "nail_color":nail_color, "nail_style":nail_style,"gems":gems}
#create a jinja  envitonment
#path
html_loader = jinja2.FileSystemLoader('./')  #finds the directory of the html file
html_env = jinja2.Environment(loader=html_loader)   #Create an environment

file_templete = html_env.get_template("my_demo.html")
result_text = file_templete.render(context)
#to find the file path : which {filename}  /usr/bin/wkhtmltopdf

config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")

pdfkit.from_string(result_text, "automated_invoice.pdf", configuration=config)

#Separate into functions for easier readability
#Make use of pep-8 to complete
#Doc string every function




