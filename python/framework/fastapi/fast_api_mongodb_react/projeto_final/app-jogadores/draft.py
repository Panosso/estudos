def sort_code(code):
    
    code = [''.join(x) for x in sorted(code)]

    print(code)

    return code

sort_code('bgrfd')