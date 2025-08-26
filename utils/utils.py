import os

def write_to_file(text, filename):
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as fh:
            fh.write(text)
        print(f"written to file: {filename}")
    except Exception as e:
        print(f'Failed to write to : {filename}: {e}')


