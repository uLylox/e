meme_dict = {
            "CRINGE": "Called to something weird or uncomfortable.",
            "LOL": "Means 'Laughing Out Loud'.",
            
            }
            
            
word = input("Search what a word means. (in caps):")

if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(word,"means",meme_dict[word])
else:
    print(word,"couldn't be found.")
