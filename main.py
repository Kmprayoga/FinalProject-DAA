import streamlit as st

from kamus import Dictionary, insert, search_by_prefix_helper, save_dictionary, read_dictionary_from_file, view_helper
from PIL import Image

gambar = Image.open("logoDAA.PNG")

# Load kamus dari file
root = None
filename = 'kamus.txt'
root: None = read_dictionary_from_file(filename, root)

# Fungsi untuk mendapatkan semua kata dalam bentuk string
def get_all_words(node):
    words = []
    view_helper(node, words)
    return '\n'.join(words)

# Judul aplikasi
st.title('Kamus Streamlit')

# Form untuk menambahkan kata baru
with st.form("add_word_form"):
    st.write("Tambahkan Kata Baru")
    new_word = st.text_input("Kata").lower()
    new_meaning = st.text_area("Arti")
    submitted = st.form_submit_button("Tambahkan")
    if submitted and new_word and new_meaning:
        root = insert(root, Dictionary(new_word, new_meaning))
        st.success(f'Kata "{new_word}" telah ditambahkan!')

# Pencarian berdasarkan prefiks
prefix = st.text_input("Cari Kata dengan Prefiks")
if prefix:
    results = []
    search_by_prefix_helper(root, prefix.lower(), results)
    if results:
        for word, meaning in results:
            st.text(f"{word}: {meaning}")
    else:
        st.write("Tidak ada kata yang ditemukan dengan prefiks tersebut.")

# Menampilkan seluruh kamus
if st.button("Tampilkan Seluruh Kamus"):
    all_words = get_all_words(root)
    st.text_area("Kamus", all_words, height=300)

# Menyimpan perubahan ke file
if st.button("Simpan Perubahan ke File"):
    save_dictionary(root, filename)
    st.success("Perubahan telah disimpan ke file.")

# Footer
st.caption("Aplikasi Kamus dengan Streamlit")