# Importing the modules
import tkinter as tk
import tkinter.font as font
from functools import partial
from tkinter import StringVar, messagebox
from tkinter import ttk


# Creating the root window
root = tk.Tk()
root.geometry('500x460')
root.title('Unit Converter')
root.configure(bg='paleturquoise') 

# Creating the fonts
font1 = font.Font(family='times', size='30')
font2 = font.Font(family='times', size='18')
font3 = font.Font(family='arial', size='16')

# The textvariables
number_from = StringVar()


# All the functions
# Fromfunc function
def fromfunc(event):
    global result_from
    result_from = event.widget.get()


# Tofunc function
def tofunc(event):
    global result_to
    result_to = event.widget.get()


# The answer function
def answer(n1):
    num1 = n1.get()
    try:
        number1 = int(num1)
    except:
        messagebox.showerror('Error', 'Term not recognised')

    # Volume

    if result_from == 'Cubic meters' and result_to == 'Cubic meters':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic meters' and result_to == 'Cubic foot':
        calculate = number1 * 35.3147
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic meters' and result_to == 'Liters':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic meters' and result_to == 'Gallons':
        calculate = number1 * 264.172
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic meters' and result_to == 'Cubic centimeters':
        calculate = number1 * 1000000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic foot' and result_to == 'Cubic meters':
        calculate = number1 * 0.02831
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic foot' and result_to == 'Cubic foot':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic foot' and result_to == 'Liters':
        calculate = number1 * 28.31679
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic foot' and result_to == 'Gallons':
        calculate = number1 * 7.4805
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic foot' and result_to == 'Cubic centimeters':
        calculate = number1 * 28316.8
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Liters' and result_to == 'Cubic meters':
        calculate = number1 * 0.000999
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Liters' and result_to == 'Cubic foot':
        calculate = number1 * 0.0353146
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Liters' and result_to == 'Liters':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Liters' and result_to == 'Gallons':
        calculate = number1 * 0.26417
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Liters' and result_to == 'Cubic centimeters':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Gallons' and result_to == 'Cubic meters':
        calculate = number1 * 0.003785
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Gallons' and result_to == 'Cubic foot':
        calculate = number1 * 0.13368
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Gallons' and result_to == 'Liters':
        calculate = number1 * 3.7854
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Gallons' and result_to == 'Gallons':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Gallons' and result_to == 'Cubic centimeters':
        calculate = number1 * 3786.41
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Cubic meters':
        calculate = number1 * 9.99999
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Cubic foot':
        calculate = number1 * 3.53146
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Liters':
        calculate = number1 * 0.000999
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Cubic meters':
        calculate = number1 * 9.9999
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Liters':
        calculate = number1 * 0.00099999
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Gallons':
        calculate = number1 * 0.00026417
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Cubic centimeters':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))


    elif result_from == 'Cubic meters' and result_to == 'Cubic meters':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic meters' and result_to == 'Cubic foot':
        calculate = number1 * 35.3147
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic meters' and result_to == 'Liters':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic meters' and result_to == 'Gallons':
        calculate = number1 * 264.172
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic meters' and result_to == 'Cubic centimeters':
        calculate = number1 * 1000000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic foot' and result_to == 'Cubic meters':
        calculate = number1 * 0.02831
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic foot' and result_to == 'Cubic foot':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic foot' and result_to == 'Liters':
        calculate = number1 * 28.31679
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic foot' and result_to == 'Gallons':
        calculate = number1 * 7.4805
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic foot' and result_to == 'Cubic centimeters':
        calculate = number1 * 28316.8
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Liters' and result_to == 'Cubic meters':
        calculate = number1 * 0.000999
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Liters' and result_to == 'Cubic foot':
        calculate = number1 * 0.0353146
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Liters' and result_to == 'Liters':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Liters' and result_to == 'Gallons':
        calculate = number1 * 0.26417
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Liters' and result_to == 'Cubic centimeters':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Gallons' and result_to == 'Cubic meters':
        calculate = number1 * 0.003785
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Gallons' and result_to == 'Cubic foot':
        calculate = number1 * 0.13368
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Gallons' and result_to == 'Liters':
        calculate = number1 * 3.7854
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Gallons' and result_to == 'Gallons':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Gallons' and result_to == 'Cubic centimeters':
        calculate = number1 * 3786.41
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Cubic meters':
        calculate = number1 * 9.99999
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Cubic foot':
        calculate = number1 * 3.53146
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Liters':
        calculate = number1 * 0.000999
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Cubic meters':
        calculate = number1 * 9.9999
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Liters':
        calculate = number1 * 0.00099999
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Gallons':
        calculate = number1 * 0.00026417
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Cubic centimeters':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))


    # Length

    elif result_from == 'Millimeters' and result_to == 'Millimeters':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Millimeters' and result_to == 'Centimeters':
        calculate = number1 * 0.1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Centimeters' and result_to == 'Millimeters':
        calculate = number1 * 10
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Millimeters' and result_to == 'Meters' :
        calculate = number1 * 0.001
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Meters' and result_to == ' Millimeters' :
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Centimeters' and result_to == 'Meters':
        calculate = number1 * 0.01
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Meters' and result_to == 'Centimeters':
        calculate = number1 * 100
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Meters' and result_to == 'Kilometers':
        calculate = number1 * 0.001
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kilometers' and result_to == 'Meters':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Centimeters' and result_to == 'Centimeters':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kilometers' and result_to == 'Kilometers':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Millimeters' and result_to == 'Kilometers':
        calculate = number1 * 0.000001
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kilometers' and result_to == 'Millimeters':
        calculate = number1 * 1000000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Centimeters' and result_to == 'Kilometers':
        calculate = number1 * 0.00001
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kilometers' and result_to == 'Centimeters':
        calculate = number1 * 100000
        result.cget('text')
        result.configure(text=(calculate, result_to))


    # Mass

    elif result_from == 'Milligrams' and result_to == 'Grams':
        calculate = number1 * 0.001
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Centigrams' and result_to == 'Centigrams':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Centigrams' and result_to == 'Grams':
        calculate = number1 / 100
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Centigrams' and result_to == 'Milligrams':
        calculate = number1 * 10
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Centigrams' and result_to == 'Kilograms':
        calculate = number1 / 100000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Grams' and result_to == 'Centigrams':
        calculate = number1 * 100
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kilograms' and result_to == 'Centigrams':
        calculate = number1 * 100000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Milligrams' and result_to == 'Centigrams':
        calculate = number1 / 10
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Grams' and result_to == 'Milligrams':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Grams' and result_to == 'Kilograms':
        calculate = number1 * 0.001
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kilograms' and result_to == 'Grams':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

   
    elif result_from == 'Milligrams' and result_to == 'Kilograms':
        calculate = number1 * 0.000001
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kilograms' and result_to == 'Milligrams':
        calculate = number1 * 1000000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Milligrams' and result_to == 'Milligrams':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate, result_to))

   
    elif result_from == 'Grams' and result_to == 'Grams':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))
        
    elif result_from == 'Kilograms' and result_to == 'Kilograms':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))


    #Temperature

    elif result_from == 'Celsius' and result_to == 'Celsius':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Celsius' and result_to == 'Fahrenheit':
        calculate = (number1 * 9/5)+32
        result.cget('text') 
        result.configure(text=(calculate, result_to))

    elif result_from == 'Celsius' and result_to == 'Kelvin':
        calculate = number1 + 273.15
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kelvin' and result_to == 'Kelvin':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kelvin' and result_to == 'Celsius':
        calculate = number1 - 273.15
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kelvin' and result_to == 'Fahrenheit':
        calculate = (number1 - 273.15) * ((9/5) + 32)
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Fahrenheit' and result_to == 'Fahrenheit':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Fahrenheit' and result_to == 'Kelvin':
        calculate = (number1 - 32) * 5/9 + 273.15
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Fahrenheit' and result_to == 'Celsius':
        calculate = (number1 - 32) * 5/9 
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Fahrenheit' and result_to == 'Rankine':
        calculate = (number1 + 459.67)
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Rankine' and result_to == 'Rankine':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate, result_to))


    elif result_from == 'Kelvin' and result_to == 'Rankine':
        calculate = number1 * 1.8 
        result.cget('text')
        result.configure(text=(calculate, result_to))
               
    elif result_from == 'Rankine' and result_to == 'Celsius':
        calculate = (number1 - 491.67) * 5/9 
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Celsius' and result_to == 'Rankine':
        calculate = (number1 * (9/5)) + 491.67 
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Rankine' and result_to == 'Fahrenheit':
        calculate = (number1 - 459.67)
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Rankine' and result_to == 'Kelvin':
        calculate = (number1 * 5/9) 
        result.cget('text')
        result.configure(text=(calculate, result_to))

        
    #Force

    elif result_from == 'Kilonewton' and result_to == 'Kilonewton':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kilonewton' and result_to == 'Newton':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Newton' and result_to == 'Kilonewton':
        calculate = number1 * 0.001
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Newton' and result_to == 'Newton':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Newton' and result_to == 'Dyne':
        calculate = number1 * 100000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Dyne' and result_to == 'Newton':
        calculate = number1 / 100000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Dyne' and result_to == 'Dyne':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Kilonewton' and result_to == 'Dyne':
        calculate = number1 * 100000000
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Dyne' and result_to == 'Kilonewton':
        calculate = number1 / 100000000
        result.cget('text')
        result.configure(text=(calculate, result_to))


    #Energy

    elif result_from == 'Calorie' and result_to == 'Calorie':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Calorie' and result_to == 'Joule':
        calculate = number1 * 4.184
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Calorie' and result_to == 'Kilowatt hour':
        calculate = number1 / 860420.65
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Joule' and result_to == 'Calorie':
        calculate = number1 / 4.184 
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Joule' and result_to == 'Kilojoule':
        calculate = number1  / 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kilojoule' and result_to == 'Joule':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kilojoule' and result_to == 'Calorie':
        calculate = number1 * 239.005736
        result.cget('text')
        result.configure(text=(calculate, result_to))


    elif result_from == 'Joule' and result_to == 'Watt hour':
        calculate = number1 / 3600
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Watt hour' and result_to == 'Joule':
        calculate = number1 * 3600
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Watt hour' and result_to == 'Kilojoule':
        calculate = number1 * 3.6
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Watt hour' and result_to == 'Calorie':
        calculate = number1 * 860.4
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Watt hour' and result_to == 'Kilowatt hour':
        calculate = number1 / 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Calorie' and result_to == 'Kilojoule':
        calculate = number1 / 239.005736
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Calorie' and result_to == 'Watt hour':
        calculate = number1 / 860.4
        result.cget('text')
        result.configure(text=(calculate, result_to))



    elif result_from == 'Joule' and result_to == 'Kilowatt hour':
        calculate = number1 / 3600000
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Kilojoule' and result_to == 'Kilowatt hour':
        calculate = number1 / 3600
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Kilojoule' and result_to == 'Watt hour':
        calculate = number1 / 3.6
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kilowatt hour' and result_to == 'Joule':
        calculate = number1 * 3600000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kilowatt hour' and result_to == 'Kilojoule':
        calculate = number1 * 3600
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Kilowatt hour' and result_to == 'Calorie':
        calculate = number1 * 860420.65
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Kilowatt hour' and result_to == 'Watt hour':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Joule' and result_to == 'Joule':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Watt hour' and result_to == 'Watt hour':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Kilojoule' and result_to == 'Kilojoule':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Kilowatt hour' and result_to == 'Kilowatt hour':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate, result_to))

    
    #Power

    elif result_from == 'Watt' and result_to == 'Watt':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kilowatt' and result_to == 'Kilowatt':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Megawatt' and result_to == 'Megawatt':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Gigawatt' and result_to == 'Gigawatt':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Horsepower' and result_to == 'Horsepower':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Watt' and result_to == 'Kilowatt':
        calculate = number1 / 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Watt' and result_to == 'Megawatt':
        calculate = number1 / 1000000
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Watt' and result_to == 'Gigawatt':
        calculate = number1 / 1000000000
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Watt' and result_to == 'Horsepower':
        calculate = number1 / 745.699872
        result.cget('text')
        result.configure(text=(calculate, result_to))


    elif result_from == 'Kilowatt' and result_to == 'Watt':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kilowatt' and result_to == 'Megawatt':
        calculate = number1 / 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Kilowatt' and result_to == 'Gigawatt':
        calculate = number1 / 1000000
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Kilowatt' and result_to == 'Horsepower':
        calculate = number1 * 1.34102209
        result.cget('text')
        result.configure(text=(calculate, result_to))


    elif result_from == 'Megawatt' and result_to == 'Kilowatt':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Megawatt' and result_to == 'Watt':
        calculate = number1 * 1000000
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Megawatt' and result_to == 'Gigawatt':
        calculate = number1 / 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Megawatt' and result_to == 'Horsepower':
        calculate = number1 * 1341.02209
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Gigawatt' and result_to == 'Kilowatt':
        calculate = number1 * 1000000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Gigawatt' and result_to == 'Watt':
        calculate = number1 * 1000000000
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Gigawatt' and result_to == 'Megawatt':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Gigawatt' and result_to == 'Horsepower':
        calculate = number1 * 1341000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Horsepower' and result_to == 'Kilowatt':
        calculate = number1 / 1.34102209
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Horsepower' and result_to == 'Watt':
        calculate = number1 * 745.699872
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Horsepower' and result_to == 'Gigawatt':
        calculate = number1 / 1341000
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Horsepower' and result_to == 'Megawatt':
        calculate = number1 / 1341.02209
        result.cget('text')
        result.configure(text=(calculate, result_to))


    #Angle

    elif result_from == 'Radian' and result_to == 'Radian':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Degree' and result_to == 'Degree':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Gradian' and result_to == 'Gradian':
        calculate = number1 * 0.001
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Revolution' and result_to == 'Revolution':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Radian' and result_to == 'Degree':
        calculate = number1 * 57.2957795
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Radian' and result_to == 'Gradian':
        calculate = number1 * 63.6619772
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Radian' and result_to == 'Revolution':
        calculate = number1 / 6.28318531
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Degree' and result_to == 'Radian':
        calculate = number1 /  57.2957795
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Degree' and result_to == 'Gradian':
        calculate = number1 * 1.11111111
        result.cget('text')
        result.configure(text=(calculate, result_to))


    elif result_from == 'Degree' and result_to == 'Revolution':
        calculate = number1 / 360
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Revolution' and result_to == 'Radian':
        calculate = number1 * 6.28318531
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Revolution' and result_to == 'Degree':
        calculate = number1 * 360
        result.cget('text')
        result.configure(text=(calculate, result_to))
    
    elif result_from == 'Revolution' and result_to == 'Gradian':
        calculate = number1 * 400
        result.cget('text')
        result.configure(text=(calculate, result_to))


    # Pressure

    elif result_from == 'Pascal' and result_to == 'Pascal':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Pascal' and result_to == 'Psi':
        calculate = number1 / 6894.75729
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Pascal' and result_to == 'Bar':
        calculate = number1 / 100000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Bar' and result_to == 'Bar':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Psi' and result_to == 'Psi':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Psi' and result_to == 'Bar':
        calculate = number1 / 14.5038
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Bar' and result_to == 'Psi':
        calculate = number1 * 14.5038
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Bar' and result_to == 'Pascal':
        calculate = number1 * 100000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Torr' and result_to == 'Torr':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Standard atmosphere' and result_to == 'Standard atmosphere':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Bar' and result_to == 'Torr':
        calculate = number1 * 750.061685
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Torr' and result_to == 'Bar':
        calculate = number1 / 750.061685
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Torr' and result_to == 'Pascal':
        calculate = number1 * 133.322368
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Torr' and result_to == 'Psi':
        calculate = number1 / 51.7149327
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Torr' and result_to == 'Standard atmosphere':
        calculate = number1 / 760.000002
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Standard atmosphere' and result_to == 'Psi':
        calculate = number1 * 14.6959488
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Standard atmosphere' and result_to == 'Torr':
        calculate = number1 * 760.000002
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Standard atmosphere' and result_to == 'Pascal':
        calculate = number1 * 101325
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Standard atmosphere' and result_to == 'Bar':
        calculate = number1 * 1.01325
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Pascal' and result_to == 'Torr':
        calculate = number1 / 133.322368
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Pascal' and result_to == 'Standard atmosphere':
        calculate = number1 / 101325
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Psi' and result_to == 'Standard atmosphere':
        calculate = number1 / 14.6959488
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Psi' and result_to == 'Torr':
        calculate = number1 * 51.7149327
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Psi' and result_to == 'Pascal':
        calculate = number1 * 6894.75729
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Bar' and result_to == 'Standard atmosphere':
        calculate = number1 / 1.01325
        result.cget('text')
        result.configure(text=(calculate, result_to))


    # Velocity

    elif result_from == 'Mile/hour' and result_to == 'Mile/hour':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Mile/hour' and result_to == 'Kilometer/hour':
        calculate = number1 * 1.60934
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Mile/hour' and result_to == 'Meter/second':
        calculate = number1 / 2.237
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kilometer/hour' and result_to == 'Kilometer/hour':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Kilometer/hour' and result_to == 'Meter/second':
        calculate = number1 / 3.6
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Meter/second' and result_to == 'Kilometer/hour':
        calculate = number1 * 3.6
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Meter/second' and result_to == 'Meter/second':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Meter/second' and result_to == 'Mile/hour':
        calculate = number1 * 2.237
        result.cget('text')
        result.configure(text=(calculate, result_to))


# Selected function
def selected(event):
    unit = event.widget.get()
    if unit == 'Volume':
        fromdd['values'] = ('Cubic meters',
                            'Cubic foot',
                            'Liters',
                            'Gallons',
                            'Cubic centimeters')

        todd['values'] = ('Cubic meters',
                          'Cubic foot',
                          'Liters',
                          'Gallons',
                          'Cubic centimeters')


    elif unit == 'Length':
        fromdd['values'] = ('Millimeters',
                            'Centimeters',
                            'Meters',
                            'Kilometers')

        todd['values'] = ('Millimeters',
                          'Centimeters',
                          'Meters',
                          'Kilometers')


    elif unit == 'Mass':
        fromdd['values'] = ('Milligrams',
                            'Centigrams',
                            'Grams',
                            'Kilograms')

        todd['values'] = ('Milligrams',
                          'Centigrams',
                          'Grams',
                          'Kilograms')


    elif unit == 'Angle':
        fromdd['values'] = ('Radian',
                            'Degree',
                            'Gradian',
                            'Revolution')

        todd['values'] = ('Radian',
                            'Degree',
                            'Gradian',
                            'Revolution')



    elif unit == 'Temperature':
        fromdd['values'] = ('Celsius',
                            'Fahrenheit',
                            'Kelvin',
                            'Rankine')

        todd['values'] = ('Celsius',
                            'Fahrenheit',
                            'Kelvin',
                            'Rankine')


    elif unit == 'Pressure':
        fromdd['values'] = ('Pascal',
                            'Psi',
                            'Bar',
                            'Torr',
                            'Standard atmosphere')
                            

        todd['values'] = ('Pascal',
                            'Psi',
                            'Bar',
                            'Torr',
                            'Standard atmosphere')


    elif unit == 'Force':
        fromdd['values'] = ('Newton',
                            'Dyne',
                            'Kilonewton')
                            
        todd['values'] = ('Newton',
                          'Dyne', 
                          'Kilonewton')


    elif unit == 'Energy':
        fromdd['values'] = ('Joule',
                            'Kilojoule',
                            'Calorie',
                            'Watt hour',
                            'Kilowatt hour')

        todd['values'] = ('Joule',
                          'Kilojoule',
                          'Calorie',
                          'Watt hour',
                          'Kilowatt hour')


    elif unit == 'Power':
        fromdd['values'] = ('Watt', 
                            'Kilowatt',
                            'Megawatt',
                            'Gigawatt',
                            'Horsepower')
                            

        todd['values'] = ('Watt', 
                            'Kilowatt',
                            'Megawatt',
                            'Gigawatt',
                            'Horsepower')
                            
                      
    elif unit == 'Velocity':
        fromdd['values'] = ('Meter/second',
                            'Kilometer/hour',
                            'Mile/hour')

        todd['values'] = ('Meter/second',
                           'Kilometer/hour',
                           'Mile/hour')
                    
     

# Creating the unit converter label
main = tk.Label(root, text='Unit Converter', fg='blue' , bg= 'paleturquoise')
main['font'] = font1
main.place(x=250 , y= 30, anchor='center')

# Creating the unit label
unit = tk.Label(root, text='Unit :', bg= 'paleturquoise')
unit['font'] = font2
unit.place(x= 52, y= 66)

# Creating the main combobox
n = StringVar()
unitdd = ttk.Combobox( width='36', textvariable=n)


# Values
unitdd['values'] = ('Angle',
                    'Volume',
                    'Length',
                    'Mass',
                    'Energy',
                    'Temperature',
                    'Pressure',
                    'Force',
                    'Power',
                    'Velocity')


unitdd.place(x=260, y=85, anchor='center' , height = 30)
unitdd.current()
unitdd.bind('<<ComboboxSelected>>', selected)

# Value label
label= tk.Label(root, text="Enter the value to convert :" , bg= 'paleturquoise')
label['font'] = font2
label.place(x=50, y=122)

# Creating the num_from entry
num_from = tk.Entry(root, width=20 , textvariable= number_from)
num_from.place(x=340, y=125, height=30)
answer = partial(answer, num_from)


# Creating the from label
label_from = tk.Label(root, text='From :' , bg= 'paleturquoise')
label_from['font'] = font2
label_from.place(x=50, y=180 )

# Creating the fromdd
f = StringVar()
fromdd = ttk.Combobox(root, width='36', textvariable=f)

fromdd.place(x=260, y=200, anchor='center' , height = 30)
fromdd.current()
fromdd.bind('<<ComboboxSelected>>', fromfunc)


# Creating the to label
to = tk.Label(root, text='To :' , bg= 'paleturquoise')
to['font'] = font2
to.place(x=50, y=242, height=30 )

# Creating the to drop down
t = StringVar()
todd = ttk.Combobox(root, width=36, textvariable=t)

todd.place(x= 260, y=260, anchor='center' , height = 30)
todd.current()
todd.bind('<<ComboboxSelected>>', tofunc)


# Creting the result label
result = tk.Label(root, text='', bg='paleturquoise', width=36) 
result['font'] = font3
result.place(x=30, y=300 , height =40)

# Creating the get answer button
get_answer = tk.Button(root, text='Get Answer', bg='lightgrey', command=answer)
get_answer['font'] = font2
get_answer.place(x=180, y= 350 )


# Creating the art label
art = tk.Label(root, text='Python Program', fg='crimson' , bg= 'paleturquoise')
art['font'] = font2
art.place(x=170, y=420)

# Creating the tkinter gui mainloop
root.mainloop()
