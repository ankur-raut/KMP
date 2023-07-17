import streamlit as st
from termcolor import colored
import time

from timeit import default_timer as timer
from datetime import timedelta


start = time.time()
def KMPSearch(pat, txt):
    indices=[]
    M = len(pat)
    N = len(txt)

    lps = [0]*M
    j = 0

   
    computeLPSArray(pat, M, lps)

    i = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:

            indices.append((i-j,i))
            j = lps[j-1]
           

       
        elif i < N and pat[j] != txt[i]:
       
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return indices

def computeLPSArray(pat, M, lps):
    len = 0

    lps[0]
    i = 1

   
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:

            if len != 0:
                len = lps[len-1]


            else:
                lps[i] = 0
                i += 1
main_string = st.text_input('Enter the String:')
pattern = st.text_input('Enter the Pattern:')
if len(main_string) < len(pattern):
    st.write("Length of Text should be greater than Pattern")
else:
    counter=0
    if(st.button('Submit')):
        start = timer()
        indices=KMPSearch(pattern, main_string)
        if len(indices)>=1:
            end = timer()
            new_string=main_string[0:indices[0][0]]
            for i in range(len(indices)):
                start=indices[i][0]
                end=indices[i][1]
                sub = "<mark style = \"background-color: yellow;color: black;\">"+ main_string[start:end] + "</mark>"
                counter=counter+1
                new_string=new_string+sub
                if i+1 < len(indices):
                    sub=main_string[end: indices[i+1][0]]
                    new_string=new_string+sub
           
            new_string =new_string + main_string[indices[len(indices)-1][-1]:]
            st.markdown(new_string, unsafe_allow_html=True)
            st.write("Occurrence is,",counter)
        else:
            st.write("No occurence is found")
