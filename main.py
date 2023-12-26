import streamlit as st
from PIL import Image

from kamus import (Dictionary, insert, view_helper, search_by_prefix, search_by_prefix_helper, save_dictionary, read_dictionary_from_file)


def main():
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        img = Image.open("logoDAA.png")
    st.image(
        img,
        caption="",
        width=400,
        channels="RGB"
    )
    st.title('Y Dictionary App')
    filename = 'kamus.txt'
    root = None
    root = read_dictionary_from_file(filename, root)

    action = st.sidebar.selectbox("Choose an action", ["View Dictionary", "Search by Prefix", "Insert Word", "Save to File"])

    if action == "View Dictionary":
        words = []
        view_helper(root, words)
        if words:
            for word in words:
                st.text(word)
        else:
            st.write("Dictionary is empty")

    elif action == "Search by Prefix":
        prefix = st.text_input("Enter prefix")
        if st.button("Search"):
            results = []
            search_by_prefix_helper(root, prefix, results)
            if results:
                for word, meaning in results:
                    st.text(f"{word}: {meaning}")
            else:
                st.write("No words found with the given prefix")

    elif action == "Insert Word":
        word = st.text_input("Word")
        meaning = st.text_input("Meaning")
        if st.button("Insert"):
            if word and meaning:
                temp = Dictionary(word, meaning)
                root = insert(root, temp)  # **Assign the updated root**
                st.success("Word inserted successfully")
                save_dictionary(root, filename)  # **Save immediately (optional)**

    elif action == "Save to File":
        if st.button("Save"):
            save_dictionary(root, filename)
            st.success("Dictionary saved to file")

if __name__ == "__main__":
    main()