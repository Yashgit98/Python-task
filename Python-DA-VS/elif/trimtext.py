def trim_text(text, side='both'):
    if side == 'left':
        return text.lstrip()
    elif side == 'right':
        return text.rstrip()
    elif side == 'both':
        return text.strip()

text = "    world     "
trimmed_text_both = trim_text(text)
print('trimmed(both side):', trimmed_text_both)

trimmed_text_left = trim_text(text, 'left')
print('trimmed(left side):', trimmed_text_left)

trimmed_text_right = trim_text(text, 'right')
print('trimmed(right side):', trimmed_text_right)
