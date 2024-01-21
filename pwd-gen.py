import random
from time import sleep
import streamlit as st
import pandas as pd

chooseCase = 0
finalPassword = ''
progressStatus = 0

lowerCase   = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
upperCase   = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
numCase     = ('0','1','2','3','4','5','6','7','8','9')
specialCase = ('!','@','#','$','%','^','&','*','.',',')


def genPassword(digit):
    digit = int(digit)
    resultPassword = ""
    i=0
    while(i<digit):
        chooseCase = random.randint(1,4)
        if chooseCase == 1:
            resultPassword += lowerCase[random.randint(0,len(lowerCase)-1)]
        elif chooseCase == 2:
            resultPassword += upperCase[random.randint(0,len(upperCase)-1)]
        elif chooseCase == 3:
            resultPassword += numCase[random.randint(0,len(numCase)-1)]
        elif chooseCase == 4:
           resultPassword += specialCase[random.randint(0,len(specialCase)-1)]
        i += 1
    return resultPassword

sidebarChoice = st.sidebar.radio(
    "",["Generate","Your Passwords"]
)
    
if sidebarChoice=='Generate':
    try:
        st.title("Password Generator")
        digit = st.text_input("Enter the number of digits for Password: ")
        
        finalPassword = genPassword(digit)
        sleep(0.5)
        st.code(finalPassword,language='none')

        if st.button('Refresh'):
            sleep(0.5)
            pass

        

    except:
        pass

    

