import streamlit as st
import pickle
import pandas as pd
import requests

top50 = pickle.load(open('top50books.pkl', 'rb'))
top50 = pd.DataFrame(top50)


matrix = pickle.load(open('user_matrix.pkl', 'rb'))
matrix = pd.DataFrame(matrix)

def main():
    left, right = st.columns(2)
    left.button("Top 50", use_container_width=True, type="primary")
    if right.button("Recommend", use_container_width=True):
        selected_book_name = st.selectbox(
                            "Select the book you like",
                            matrix.index,
                        )
        if st.button("Recommend"):
            st.text(selected_book_name)
            
    else:
        st.title('Top 50 Books')
        names = top50['Book-Title']
        authors = top50['Book-Author']
        images = top50['Image-URL-M']
        ratings = top50['avg_ratings']

        start = 0
        end = 6
        for _ in range(10):
            cols = st.columns(5)
            for col, book_name, author, image, rating in zip(cols, names[start:end], authors[start:end], images[start:end], ratings[start:end]):
                with col:
                    st.text(book_name)
                    st.text('Rating: ' + str(round(rating,2)))
                    st.text(author)
                    st.image(image)
                st.write("")
            start += 5
            end += 5
    pass


if __name__=='__main__':
    main()