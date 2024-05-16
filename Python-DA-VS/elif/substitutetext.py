def substitute_text(text,old,new):
    return text.replace(old,new)
real_text = "welcome to my world guys"
old_text = "guys"
new_text = "friends"
substituted_text = substitute_text(real_text,old_text,new_text)
print(real_text)
print(substituted_text)