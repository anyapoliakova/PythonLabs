def nearest_chapter(book_dict: dict, page: int):
    delta = 0
    flag = True
    curr_chapt = ""
    for chapter, f_page in book_dict.items():
        if flag:
            delta = abs(f_page - page)
            curr_chapt = chapter
            flag = False
        else:
            if abs(f_page - page) <= delta:
                curr_chapt = chapter
            else:
                return curr_chapt
    return curr_chapt


if __name__ == "__main__":
    print(nearest_chapter({
        "Chapter 1": 1,
        "Chapter 2": 15,
        "Chapter 3": 37
    }, 10))

    print(nearest_chapter({
        "New Beginnings": 1,
        "Strange Developments": 62,
        "The End?": 194,
        "The True Ending": 460
    }, 200))

    print(nearest_chapter({
        "Chapter 1a": 1,
        "Chapter 1b": 5
    }, 3))
