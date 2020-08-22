#Function to calculate Fahrenheit
def fahrenheit(c):
    f = c * (9/5) + 32
    return f   #returns the Fahrenheit value the parameter 'c'
    #end of fahrenheit function

#Function to calculate Fahrenheit and print result
def calc_print(c):
    try:
        cel_float = float(c) #converts input-string to float
        print() #prints empty line for readability
        cel_decimals = len(c) - c.find('.') - 1   #calculate decimal places
        if (cel_float % 1 > 0) and (cel_decimals > 1):
            #when the user input is a floating point number
            #and when the floating point number is more than 1 decimal place
            print(f'Fahrenheit value of {cel_float} deg C is \
{round(fahrenheit(cel_float),cel_decimals)} F')
            print() #prints empty line for readability

        #following code block prints fahrenheit value of all 10
        #values of the given number's first decimal place
        cel_int = int(cel_float)
        for index in range(0, 10, 1):
            temp = (cel_int - index * 1 / 10) if cel_float < 0 \
             else  (cel_int + index * 1 / 10)
            print(f'Fahrenheit value of {temp} deg C is \
{round(fahrenheit(temp),2)} F')
    except: #exception block
        #prints when any unknown error occurs
        print('Error: Cannot convert to Fahrenheit')
    finally: #this block executes no-matter-what-happens
        print('------------------------------------------------------')
        print() #prints empty line for readability
        return  #this function has no return value
    #end of calc_print function


#Main block
try:
    cont_flag = True
    while cont_flag == True: #Loop until user wants to continue
        print() #prints empty line for readability
        print('Conversion of Celsius to Fahrenheit') #prints title
        print('-----------------------------------')

        #input validation
        input_flag = True
        while input_flag == True: #Loop until user enters a numeric value
            celsius = input('Enter Celsius value: ' )  #user input of celsius
            if  celsius.replace('-','',1).replace('.','',1).isdigit():
                input_flag = False
            else:
                #Warn the user and prompt to input again
                print('Input is not a number, please enter a numeric value')
                print() #prints empty line for readability

        #Call calc_print function if user input-string has numeric value
        calc_print(celsius)

        cont_input = input('Continue...? (y/n): ')  #user input to continue
        if cont_input.lower().replace(' ','') != 'y' \
           and \
           cont_input.lower().replace(' ','') != 'yes':
            cont_flag = False
            break
        else:
            cont_flag = True

except: #exception block in case of any unknown error
    print('Error Occurred - Cannot continue')

finally: #this block executes no-matter-what-happens
    print('------------------------------------------------------')
    print() #prints empty line for readability
    exit()  #gracefully exit
