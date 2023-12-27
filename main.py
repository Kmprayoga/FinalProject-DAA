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
    st.title('A-Z Dictionary App')
    filename = 'kamus.txt'
    root = None
    root = read_dictionary_from_file(filename, root)

    action = st.sidebar.selectbox("Pilih menu ", ["Lihat Dictionary", "Cari Kata", "Tambah Kata", "Simpan ke File"])

    if action == "Lihat Dictionary":
        words = []
        view_helper(root, words)
        if words:
            for word in words:
                st.text(word)
        else:
            st.write("Dictionary Kosong")

    elif action == "Cari kata":
        prefix = st.text_input("Masukkan Huruf")
        if st.button("Cari"):
            results = []
            prefix = prefix.lower()
            search_by_prefix_helper(root, prefix, results)
            if results:
                for word, meaning in results:
                    st.text(f"{word}: {meaning}")
            else:
                st.write("Tidak kata yang ditemukan")

    elif action == "Tambah kata":
        word = st.text_input("kata")
        meaning = st.text_input("arti")
        if st.button("Tambah Kata"):
            if word and meaning:
                temp = Dictionary(word, meaning)
                root = insert(root, temp)  
                st.success("Kata berhasil ditambahkan")
                save_dictionary(root, filename)  

    elif action == "Simpan ke File":
        if st.button("Simpan"):
            save_dictionary(root, filename)
            st.success("Dictionary berhasil disimpan ke file")

if __name__ == "__main__":
    main()
