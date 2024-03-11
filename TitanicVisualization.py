import streamlit as st
import pandas as pd
import utils as utl
import os




def main():

    script_directory = os.path.dirname(os.path.realpath(__file__))
    os.chdir(script_directory)

    st.set_page_config(layout="wide", page_title='Titanic Visualizaiton')

    # utl.local_css("images/style.css")
    # utl.remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

    # Create a sample dataframe
    data = pd.DataFrame({
    'Fruits': ['Apples', 'Oranges', 'Bananas', 'Grapes'],
    'Quantity': [15, 25, 35, 45]
    })
    
    # Title
    st.title('Sinking of the RMS Titanic')
    st.markdown('Group Members: Proud CHAREESRI, Ru YI, Wenjing ZHAO, Hongyang YE')
    
    # Text
    multi = '''
        The dataset of this project is obtained from a classic machine learning disaster prediction problem - The sinking of the RMS Titanic in 1912.
        
        This tragic event resulted in the loss of 1,502 passengers and crew out of the total 2,224 onboard, 
        marking it as the deadliest peacetime maritime disaster in history.
    '''
    st.markdown(multi)

    # Sidebar
    with st.sidebar:
        st.title('The story of Titanic')
        st.markdown('- Story 1\n- Story 2\n- Story 3')

    # Create a bar chart
    st.bar_chart(data)


if __name__ == '__main__':
    main()