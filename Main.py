import streamlit as st
import  pickle
import pandas as pd
import numpy as np
from PIL import Image
image = Image.open('img2.jpg')

## importing the model
pipe = pickle.load(open('ppipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Laptop Price Predictor")

st.image(image)

st.write('')
st.write('')
st.write('')


## brand

brand = st.selectbox('Select Brand:',df['brand'].unique())

## display_size

display_size = st.number_input('Display Size (inches)')

## ram_gb
ram_gb = st.selectbox('Ram (GB)', [2,4,8,12,16,24,32,64])

## ram_type
ram_type = st.selectbox('Ram Type',df['ram_type'].unique())

## ssd_gb
ssd_gb = st.selectbox('SSD (GB)',[0,64,128,256,512,1024,2048])

## hdd_gb 
hdd_gb = st.selectbox('HDD (GB)',[0,64,128,256,512,1024,2048])

## processor_name
processor_name= st.selectbox('Processor Brand',df['processor_name'].unique())

## processor_model
processor_model= st.selectbox('Processor model',df['processor_model'].unique())

## OS
OS = st.selectbox('OS',df['OS'].unique())

## touchscreen
touchscreen = st.selectbox('Touchscreen',['Yes','No'])
if touchscreen== 'Yes':
    touchscreen = 'yes'
else:
    touchscreen = 'no'

## gpu 
gpu =  st.selectbox('GPU',df['gpu'].unique())

## GPU_gb
GPU_gb = st.selectbox('GPU Memory(GB) (select 0 GB if only integrated graphics are present)',df['GPU_gb'].unique())

st.write('')
st.write('')
st.write('')
## pridiction
#st.button('Pridict')

## specs:
specs = pd.DataFrame({'display_size':float(display_size),'brand':brand,'ram_gb':int(ram_gb)
                      ,'ram_type':ram_type,'ssd_gb':int(ssd_gb),'hdd_gb':int(hdd_gb),'processor_name':processor_name
                      ,'processor_model':processor_model,'OS':OS,'touchscreen':touchscreen, 'gpu':gpu,'GPU_gb':int(GPU_gb) },index=[0])

if st.button('Predict'):
    prediction = pipe.predict(specs)
    st.title(f'Price: {round(np.exp(prediction[0]),0)} ₹')












