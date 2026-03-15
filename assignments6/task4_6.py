def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    sorted_words = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    return sorted_words

text = input("Enter a text: ")
sorted_words, total_words = word_frequency(text)
top_5 = sorted_words[:5]

top_count = 0
for word, count in top_5:
    top_count += count

    proportion = (top_count / total_words) * 100
 
print("Top 5:", dict(top_5))
print("Proportion of top 5 words:", proportion, "%")
print("Total words:", total_words)