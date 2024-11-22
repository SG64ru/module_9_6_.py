def all_variants(text):
    l_str = len(text)
    for i in range(l_str):
        for j in range(l_str - i):
            # print(j, j+i+1)
            yield  text[j:j+i+1]




a = all_variants("abc")
for i in a:
    print(i)




