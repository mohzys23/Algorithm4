some = {'Name': ['Moses Ubah', 'Chukwuemeka'], 'Dob': ['January-09-1997', 'Thursday']}
def invert_dict(some):
    inverse = dict()
    for key in some:
        for list_value in some[key]:
            if list_value not in inverse:
                inverse[list_value] = [key]
            else:
                inverse[list_value].append(key)
    return inverse
print(some)
