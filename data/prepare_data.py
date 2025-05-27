'''
Prepare the data for the model
- Combine all the books into one file
- Split into train, val and test (0.8, 0.1, 0.1)
- Save the data in the data folder
'''

import os

def combine_books(folder_path):
    '''
    Combine all the books into one file
    '''
    # Combine all the books into one file
    for file in os.listdir(folder_path):
        if file.endswith('.txt'):
            with open(os.path.join(folder_path, file), 'r') as f:
                content = f.read()
            with open('combined.txt', 'a') as f:
                f.write(content)

    # Split into train, val and test (0.8, 0.1, 0.1)
    with open('combined.txt', 'r') as f:
        text = f.read()
    train_text = text[:int(len(text) * 0.8)]
    val_text = text[int(len(text) * 0.8):int(len(text) * 0.9)]
    test_text = text[int(len(text) * 0.9):]

    with open('train.txt', 'w') as f:
        f.write(train_text)
    with open('val.txt', 'w') as f:
        f.write(val_text)
    with open('test.txt', 'w') as f:
        f.write(test_text)

if __name__ == '__main__':
    combine_books('./')