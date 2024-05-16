def cut_text(text,start,end):
    return text[start:end]

original_text = "Hello World"

start_position = 2
end_position = 5

cut_portion = cut_text(original_text,start_position,end_position)

print(original_text)

print(cut_portion)