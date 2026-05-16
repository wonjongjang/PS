def solution(numbers):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i, word in enumerate(words):
        numbers = numbers.replace(word, str(i))
    
    return int(numbers)