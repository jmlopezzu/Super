import streamlit as st
import time
import random
import pandas as pd
from PIL import Image
import string

# Para instalar streamlit ---> pip install streamlit
# Primero: correr el script app.py
# Segundo: en la terminal correr streamlit run app.py

# Gestionar path directorio de trabajo
#path = "/Users/jmlz_rp/Documents/SistemasIA/Taller4"

st.title("Primeros Pasos con Git y GitHub")
st.markdown("## TD ")
st.markdown("<h1 style='text-align: center;'> Super </h>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>BI & DEV Team </h4>", unsafe_allow_html=True)
st.markdown("")
image = Image.open('git.png')#'/Users/jmlz_rp/Documents/SistemasIA/Taller4/chatbot.png'
image1 = Image.open('super.png')#'/Users/jmlz_rp/Documents/SistemasIA/Taller4/student.png'
resized_image = image.resize((200, 200))
resized_image1 = image1.resize((200, 200))

col1, col2 = st.columns([2, 1])
with col1:
    st.image(resized_image, caption='Transformación Digital Super', use_column_width=False)  
with col2:
    st.image(resized_image1, caption='Super', use_column_width=False)    
    
st.sidebar.markdown("# Indice")
st.sidebar.markdown("#### 1. ¿Que es Git? ")
st.sidebar.markdown("#### 2. ¿Que es GitHub? ")
st.sidebar.markdown("#### 3. ¿Que es un repositorio? ")
st.sidebar.markdown("#### 4. ¿Que es un commit? ")
st.sidebar.markdown("#### 5. ¿Que es un push? ")
st.sidebar.markdown("#### 6. ¿Que es un pull? ")
st.sidebar.markdown("#### 7. ¿Que es un branch? ")
st.sidebar.markdown("#### 8. ¿Que es un merge? ")
st.sidebar.markdown("#### 9. ¿Que es un fork? ")
st.sidebar.markdown("#### 10. ¿Que es un pull request? ")
st.sidebar.markdown("#### 11. ¿Que es un issue? ")
st.sidebar.markdown("#### 12. ¿Que es un clone? ")
st.sidebar.markdown("#### 13. ¿Que es un tag? ")
st.sidebar.markdown("#### 14. ¿Que es un stash? ")
st.sidebar.markdown("#### 15. ¿Que es un rebase? ")
st.sidebar.markdown("#### 16. ¿Que es un cherry-pick? ")
st.sidebar.markdown("#### 17. ¿Que es un revert? ")
st.sidebar.markdown("#### 18. ¿Que es un gitignore? ")
st.sidebar.markdown("#### 19. ¿Que es un gitlab? ")
st.sidebar.markdown("#### 20. ¿Que es un bitbucket? ")
st.sidebar.markdown("#### 21. ¿Que es un gitflow? ")
st.sidebar.markdown("#### 22. ¿Que es un webhook? ")
st.sidebar.markdown("#### 23. ¿Que es un hook? ")
st.sidebar.markdown("#### 24. ¿Que es un merge conflict? ")
st.sidebar.markdown("#### 25. ¿Que es un rebase conflict? ")
st.sidebar.markdown("#### 26. ¿Que es un squash? ")
st.sidebar.markdown("#### 27. ¿Que es un rebase interactivo? ")


st.markdown("<h1 style='text-align: center;'> Links Importantes </h>", unsafe_allow_html=True)
st.markdown("")

st.markdown("<h1 style='text-align: center;'> Git </h>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'> https://git-scm.com/ </h4>", unsafe_allow_html=True)
st.markdown("")

st.markdown("<h1 style='text-align: center;'> GitHub </h>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'> https://github/ </h4>", unsafe_allow_html=True)
st.markdown("")

st.markdown("<h1 style='text-align: center;'> VSCode </h>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>https://vscode.dev/ </h4>", unsafe_allow_html=True)
st.markdown("")

st.markdown("<h1 style='text-align: center;'> Repositorio Super </h>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'> https://github.com/SuperDeAlimentos </h4>", unsafe_allow_html=True)
st.markdown("")


# Save the DataFrame to a CSV file
#df.to_csv(path + '/chat_history.csv', index=False)

# Nueva pregunta
#if st.button("Añadir nueva pregunta"):
#   user_message = st.text_input("Escribe tu nueva pregunta",key=random.choice(string.ascii_uppercase)+str(random.randint(0,999999)))

# Load the CSV file
#df = pd.read_csv(path + '/chat_history.csv')

# Display the DataFrame

#import base64
#def add_bg_from_local(image_file):
 #   with open(image_file, "rb") as image_file:
  #      encoded_string = base64.b64encode(image_file.read())
   # st.markdown(
    #f"""
    #<style>
    #.stApp {{
    #    background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
     #   background-size: cover
    #}}
    #</style>
   # """,
    #unsafe_allow_html=True
    #)
#add_bg_from_local('drawing.PNG')  #/Users/jmlz_rp/Documents/SistemasIA/Taller4/drawing.png
