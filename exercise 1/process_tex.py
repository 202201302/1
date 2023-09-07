# Function to process and replace words in the text
def process_text(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        content = file.read()

    # Initialize a count for the word "terrible"
    terrible_count = 0

    # Split the content into words while preserving punctuation
    words_and_punctuation = content.split()
    modified_text = ""

    for word in words_and_punctuation:
        # Check if the word ends with punctuation
        punctuation = ''
        if word[-1] in '.,!?;':
            punctuation = word[-1]
            word = word[:-1]

        # Process "terrible"  and keep punctuation
        if word.lower() == "terrible":
            terrible_count += 1
            if terrible_count % 2 == 0:
                modified_word = "pathetic" + punctuation
            else:
                modified_word = "marvellous" + punctuation
        else:
            modified_word = word + punctuation

        modified_text += modified_word + ' '

    # Write the modified text to the result file
    with open(output_filename, 'w') as result_file:
        result_file.write(modified_text)

    # Display the total count of "terrible"
    print(f'Total occurrences of "terrible": {terrible_count}')

if __name__ == '__main__':
    # Call the function to process the text
    process_text('file_to_read.txt', 'result.txt')