import os

# Xác định đường dẫn tệp dữ liệu
file_path = "./data/text.txt"

# Kiểm tra tệp có tồn tại không
if not os.path.exists(file_path):
    print("Lỗi: Tệp không tồn tại!")
else:
    word_counts = {}

    # Mở tệp và đếm số lần xuất hiện của từ
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                word_counts[word] = word_counts.get(word, 0) + 1

    # In 10 từ đầu tiên và số lần xuất hiện
    print('{:15}{:10}'.format('Từ', 'Tần số'))
    print('-------------------------')

    for w in list(word_counts)[:10]:
        print('{:15}{:10}'.format(w, word_counts[w]))
