import streamlit as st

# Define the path to the model file
model_path = 'logistics_model.plk','rb'

def main():
    st.title('Book Recommendation')
        
    # Input variables
    year = st.text_input('Year-Of-Publication')
    book_title = st.text_input('Book-Title')
    book_author = st.text_input('Book-Author')
    book_rating = st.text_input('Book-Rating')
    image_url = st.text_input('image_url')
        
    # Recommendation code
    if st.button('Recommend'):
      recommendations = model.predict([[year, book_title, book_author, book_rating, image_url]])
    output = round(recommendations[0], 2)
    st.success('Books recommendation will be {recommendations}'.format(output))
    st.error(f"Error in generating recommendation: {recommendations}")

    if__name__=='__main__'
    main()