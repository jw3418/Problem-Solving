count = 0
def solution(word):
    global count
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(word_string):
        global count
        count += 1
        
        if word_string == word: return True #찾음
        elif len(word_string) == 5: return False
        
        for v in vowels:
            if dfs(word_string + v): return True # if문 반환값이 True면 바로 count 반환

    for v in vowels:
        if dfs(v): return count