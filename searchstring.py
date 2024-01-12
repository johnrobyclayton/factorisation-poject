import re

def regex_string_list(searchstringlist, excludestringlist, targetstringlist):
    search_pattern = ''.join(f'({pattern})|' for pattern in searchstringlist)[:-1]
    exclude_pattern = ''.join(f'(?:(?!{pattern}).)*' for pattern in excludestringlist)

    pattern = re.compile(f'{exclude_pattern}{search_pattern}')

    matches = [match.group(0) for string in targetstringlist if (match := pattern.search(string))]

    return matches

# Example usage
stringlist1 = ['.', 'she', 'is']
stringlist2 = ['she', 'is', 'everywhere', 'she', 'is', 'there', 'she', 'is', 'here', '.', 'is', 'she', 'here', '.', 'is', 'she', 'there', '.', 'is', 'she', 'everywhere', '.']
stringlist3 = ['she', 'is', '.']

result = regex_string_list(stringlist1, stringlist2, stringlist3)
print(result)
