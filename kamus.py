import streamlit as st

class Dictionary:
    def _init_(self, word, meaning):
        self.left = None
        self.right = None
        self.word = word.lower()
        self.meaning = meaning

def check(a, b):
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            return 1
        elif b[j] > a[i]:
            return -1
        i += 1
        j += 1
    if len(a) > len(b):
        return 1
    elif len(b) > len(a):
        return -1
    return 0


def insert(root, temp):
    if root is None:
        root = temp
    else:
        ptr = root
        par = None
        while ptr is not None:
            par = ptr
            if check(temp.word, ptr.word) < 0:
                ptr = ptr.left
            elif check(temp.word, ptr.word) > 0:
                ptr = ptr.right
            else:
                return root

        if check(par.word, temp.word) < 0:
            par.right = temp
        else:
            par.left = temp

    return root


def search_by_prefix_helper(node, prefix, results):
    if node is None:
        return
    if prefix in node.word:
        results.append((node.word, node.meaning))
    search_by_prefix_helper(node.left, prefix, results)
    search_by_prefix_helper(node.right, prefix, results)


def view_helper(ptr, words):
    if ptr is not None:
        view_helper(ptr.left, words)
        words.append(f"{ptr.word}: {ptr.meaning}")
        view_helper(ptr.right, words)


def save_dictionary_to_file(node, file):
    if node is not None:
        save_dictionary_to_file(node.left, file)
        file.write(f"{node.word}:{node.meaning}\n")
        save_dictionary_to_file(node.right, file)


def save_dictionary(root, filename):
    with open(filename, 'w') as file:
        save_dictionary_to_file(root, file)


def read_dictionary_from_file(filename, root):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(':')
                if len(data) == 2:
                    word = data[0].strip()
                    meaning = data[1].strip()
                    new_word = Dictionary(word, meaning)
                    root = insert(root, new_word)
    except FileNotFoundError:
        print("File not found")
    return root


# Streamlit App
def main():
    st.title('Y Dictionary App')
    logo_path = r'/Users/dwiprayoga/Downloads'  # Ganti dengan jalur file logo yang benar
    st.image(logo_path, width=100)

    filename = 'kamus.txt'
    root = None
    root = read_dictionary_from_file(filename, root)

    action = st.sidebar.selectbox("Choose an action",
                                  ["View Dictionary", "Search by Prefix", "Insert Word", "Save to File"])

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
                root = insert(root, temp)
                st.success("Word inserted successfully")

    elif action == "Save to File":
        if st.button("Save"):
            save_dictionary(root, filename)
            st.success("Dictionary saved to file")


if __name__ == "_main_":
    main()
