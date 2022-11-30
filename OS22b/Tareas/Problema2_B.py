cases = int(input())
for i in range(cases):
    f_word = input().lower()
    s_word = input().lower()
    f_word_a= list(f_word)
    s_word_a= list(s_word)
    f_word_a.sort()
    s_word_a.sort()
    f_word_n = "".join(f_word_a)
    s_word_n = "".join(s_word_a)
    if f_word_n == s_word_n:
        print("SI")
    elif f_word_n != s_word_n:
        print("NO")