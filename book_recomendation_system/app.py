import streamlit as st
import pickle
import pandas as pd
import numpy as np

top50 = pickle.load(open('top50books.pkl', 'rb'))
top50 = pd.DataFrame(top50)


matrix = pickle.load(open('user_matrix.pkl', 'rb'))
matrix = pd.DataFrame(matrix)


similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(book_name):
    index = np.where(matrix.index==book_name)[0][0]
    distances = similarity[index]
    similar_items = sorted(list(enumerate(distances)),key=lambda x:x[1], reverse=True)

    recommended_book = []
    for i in similar_items[1:6]:
        recommended_book.append(matrix.index[i[0]])
    return recommended_book

def main():
    left, right = st.columns(2)
    left.button("Recommend", use_container_width=True, type="primary")
    if right.button("Top 50", use_container_width=True):
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
            
    else:
        selected_book_name = st.selectbox(
                            "Select the book you like",
                            matrix.index,
                        )
        if st.button("Recommend"):
            # st.text(selected_book_name)
            recommended = recommend(selected_book_name)
            for i in recommended:
                st.text(i)
    pass


if __name__=='__main__':
    main()