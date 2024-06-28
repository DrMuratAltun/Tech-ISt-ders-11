import gradio as gr
import stylecloud
from PIL import Image
import os
#fonksiyon tanımla
def create_stylecloud(file,language,icon):
    #icon kodları için :https://fontawesome.com/icons
    text=file.decode("utf-8")
    output_file='stylecloud.png'
    
    #kelime bulutu oluştur
    stylecloud.gen_stylecloud(
        text=text,
        icon_name=icon,
        size=500,
        output_name=output_file,
    )
    #oluşturlan kelime bulutunun dosya adı
    return output_file
'''
Extra paretmetreler
 palette="cartocolors.qualitative.Bold_10",
        gradient="horizontal",
        background_color="white",
        collocations=False
'''
#Gradio arayüzünü oluştur
with gr.Blocks() as demo:
    gr.Markdown('Kelime Bulutu Oluşturucu')
    with gr.Row():
        file_input=gr.File(label='Metin dosyasını yükle', type='binary')
        language=gr.Radio(choices=['TR', 'En'],label='Dil Seçimi', value='TR')
        icon=gr.Dropdown(choices=["fas fa-car", "fas fa-star-and-crescent", "fas fa-trophy", "fas fa-heart"],
                        label='İkon seçimi',value="fas fa-car")
        output_file=gr.File(label='Kelime Bulutunu indir')
        create_button=gr.Button('Oluştur')
        #butona basıldığında
        create_button.click(
        create_stylecloud,
        inputs=[file_input,language,icon],
        outputs=output_file
        )
demo.launch(share=True) #share=True public lnk verir