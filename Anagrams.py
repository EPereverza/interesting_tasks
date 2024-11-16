'''
Напишите функцию, которая найдет все наборы анаграмм в строке. 
Анаграммы - слова, составленные из одного и того же набора букв (рост-сорт-трос).
str = 'адрес карп кума куст мир мука парк рим среда стук рост сорт трос';
'''
def getAnagrams(s):
    words = s.split()
    anagram_groups = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_groups:
            anagram_groups[sorted_word] = []
        
        anagram_groups[sorted_word].append(word)

    result = [group for group in anagram_groups.values() if len(group) > 1]
    
    return result

# Пример использования
s = 'адрес карп кума куст мир мука парк рим среда стук рост сорт трос'
print(getAnagrams(s))
