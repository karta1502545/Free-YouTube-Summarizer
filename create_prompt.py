# Read the content of subtitle.txt
with open('subtitle.txt', 'r', encoding='utf-8') as subtitle_file:
    subtitle_content = subtitle_file.read()

# Read the content of the template
with open('template.txt', 'r', encoding='utf-8') as template_file:
    template_content = template_file.read()

# Replace the placeholder with the content of subtitle.txt
result_content = template_content.replace('---subtitle.txt---', subtitle_content)

# Write the result to prompt.txt
with open('prompt.txt', 'w', encoding='utf-8') as prompt_file:
    prompt_file.write(result_content)

print("Replacement complete. The output is saved in prompt.txt")