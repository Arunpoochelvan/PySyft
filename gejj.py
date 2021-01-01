text = "hi Arun https://google.com and my new search is https://google.com"

urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
print(urls)

word2 = []
for word in text.split():
  if word in urls:
    word = "["+word+"]"+"("+word+")"
  word2.append(word)
  
' '.join(map(str, word2))
