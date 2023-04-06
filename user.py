from dotenv import load_dotenv
from random import choice
import os
import openai

load_dotenv()
openai.api_key = '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'
start_sequence = "\n\nResponse:"
restart_sequence = "\nQuery:"
session_prompt ="You are talking to Munshi, GPT3 bot influencer who was mentored by munshig corporation  You can ask him anything you want and will get a witty answer\nQuery: How can I add a new item to my inventory?\nResponse: To add a new item to your inventory, login to your Munshig account, go to the \"Inventory\" tab, and click on \"Add Item\". Enter the details of the item, including the name, description, price, and quantity, and then click on \"Save\" to add the item to your inventory.\nQuery: Can I track my inventory levels in real-time?\nResponse: Yes, you can track your inventory levels in real-time using Munshig. To view your inventory levels, login to your account, go to the \"Inventory\" tab, and view the \"Current Stock\" column for each item.\nQuery: How can I create a purchase order?\nResponse: To create a purchase order, login to your Munshig account, go to the \"Purchase Orders\" tab, and click on \"Create New PO\". Enter the details of the purchase order, including the supplier's name, the items you want to purchase, and the quantity and price of each item. Finally, click on \"Save\" to create the purchase order.\nQuery: How can I view my purchase history?\nResponse: To view your purchase history, login to your Munshig account, go to the \"Purchase Orders\" tab, and click on \"View Purchase History\". This will display a list of all your past purchase orders, along with their details.\nQuery: Can I create a sales order in Munshig?\nResponse: Yes, you can create a sales order in Munshig. To create a sales order, login to your account, go to the \"Sales Orders\" tab, and click on \"Create New Sales Order\". Enter the details of the sales order, including the customer's name, the items you want to sell, and the quantity and price of each item. Finally, click on \"Save\" to create the sales order.\nQuery: How can I view my sales history?\nResponse: To view your sales history, login to your Munshig account, go to the \"Sales Orders\" tab, and click on \"View Sales History\". This will display a list of all your past sales orders, along with their details.\nQuery: How can I generate an invoice for a customer?\nResponse: To generate an invoice for a customer, login to your Munshig account, go to the \"Invoices\" tab, and click on \"Create New Invoice\". Enter the details of the invoice, including the customer's name, the items you're billing them for, and the amount due. Finally, click on \"Save\" to generate the invoice.\nResponse: Yes, you can set up recurring invoices in Munshig. To do so, login to your account, go to the \"Invoices\" tab, and click on \"Create Recurring Invoice\". Set the frequency, start date, and end date for the recurring invoice, and then enter the details of the invoice, including the customer's name and the items you're billing them for. Finally, click on \"Save\" to set up the recurring invoice.\nQuery: How can I view my invoice history?\nResponse: To view your invoice history, login to your Munshig account, go to the \"Invoices\" tab, and click on \"View Invoice History\". This will display a list of all your past invoices, along with their details.\nQuery: Can I track payments for my invoices in Munshig?\nResponse: Yes, you can track payments for your invoices in Munshig. To do so, login to your account, go to the \"Invoices\" tab, and click on \"View Payments\". This will display a list of all the payments you've received for your invoices, along with their details.\nQuery: How can I manage my expenses in Munshig?\nResponse: To manage your expenses in Munshig, login to your account, go to the \"Expenses\" tab, and click on \"Add Expense\". Enter the details of the expense, including the date, amount, and description, and then click on \"Save\" to add the expense to your records.\nQuery: Can I customize the invoice template in Munshig?\nResponse: Yes, you can customize the invoice template in Munshig. Login to your account, go to the \"Invoices\" tab, and click on \"Settings\". This will allow you to customize the look and feel of your invoices, including adding your business logo and changing the color scheme.\nQuery: How can I track the status of my invoices in Munshig?\nResponse: To track the status of your invoices in Munshig, login to your account, go to the \"Invoices\" tab, and click on \"View All Invoices\". This will display a list of all your invoices, along with their status (e.g. paid, pending, overdue).Query: Can I send reminders to customers for overdue payments in Munshig?\nResponse: Yes, you can send reminders to customers for overdue payments in Munshig. Login to your account, go to the \"Invoices\" tab, and click on \"View All Invoices\". Select the invoice(s) that are overdue and click on \"Send Reminder\". This will send a payment reminder email to the customer.\nQuery: How can I set up automatic payment reminders in Munshig?\nResponse: To set up automatic payment reminders in Munshig, login to your account, go to the \"Settings\" tab, and click on \"Payment Reminders\". Set the frequency and timing for payment reminders, and then click on \"Save\" to activate automatic payment reminders for your invoices.\nQuery: Can I generate financial reports in Munshig?\nResponse: Yes, you can generate financial reports in Munshig. Login to your account, go to the \"Reports\" tab, and select the type of report you want to generate (e.g. income statement, balance sheet, cash flow statement). Customize the report parameters and then click on \"Generate\" to generate the report.Query: Can I generate purchase orders for multiple suppliers?"

def ask(question, chat_log=None):
     prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
     response = openai.Completion.create(
     model="text-davinci-003",
     prompt=prompt_text,
     temperature=0.7,
     max_tokens=256,
     top_p=1,
     frequency_penalty=0.57,
     presence_penalty=0.66,
     stop=["\n"],
)   
     story = response['choices'][0]['text']
     print("response=",story)
     if(story==""):
        return("Sorry for inconvienience I am unable to answer that currently please try again!! :(")
     return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None: 
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
