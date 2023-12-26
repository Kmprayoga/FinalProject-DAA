class Dictionary:
    def __init__(self, word, meaning):
        self.left = None
        self.right = None
        self.word = word.lower()
        self.meaning = meaning

def insert(root, temp):
    if root is None:
        return temp
    else:
        if temp.word < root.word:
            root.left = insert(root.left, temp)
        elif temp.word > root.word:
            root.right = insert(root.right, temp)

    print(f"masukkan {temp.word}, kata saat ini: {root.word}")  # Tambahkan ini
    return root

def search_by_prefix(root, prefix):
    results = []
    prefix = prefix.lower()  # Menormalisasi prefiks menjadi huruf kecil
    search_by_prefix_helper(root, prefix, results)
    if not results:
        print("\nKata Tidak Ditemukan")
    else:
        print("\nKata Ditemukan:")
        for word, meaning in results:
            print(f"{word}: {meaning}")

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

        print(f"Membaca file, kata saat ini: {root.word}")  # Tambahkan ini
        return root
    except FileNotFoundError:
        print("File tidak ditemukan")
    return root
