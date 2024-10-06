
def read_file_in_chunks(file_path, chunk_size=1024):
    with open(file_path, 'r') as file:
        while chunk := file.read(chunk_size):
            yield chunk