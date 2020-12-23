def num_to_eng(num: int):
    ones = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
            9: "Nine"}
    afterones = {10: 'Ten', 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
                 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
    tens = {2: "Twenty", 3: "Thirty", 4: "Fourty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty",
            9: "Ninety"}
    eng_num = ""
    if num//100 > 0:
        eng_num += ones[num//100] + " Hundred "
        num %= 100
        if num == 0:
            return eng_num
    if num//10 > 1:
        eng_num += tens[num//10] + " "
        if num % 10 != 0:
            eng_num += ones[num % 10]
        return eng_num
    elif num//10 == 1:
        eng_num += afterones[num]
    else:
        eng_num += ones[num % 10]
    return eng_num


if __name__ == "__main__":
    print(num_to_eng(0))
    print(num_to_eng(18))
    print(num_to_eng(126))
    print(num_to_eng(909))
    print(num_to_eng(990))
    print(num_to_eng(915))
    print(num_to_eng(900))