import requests
import shutil

def test_stream():
    url = 'http://127.0.0.1:5002/dropcam/stream'
    local_filename = 'client/foo_stream.jpeg'
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            f.write(r.content)
                
def test_file():
    url = 'http://127.0.0.1:5002/dropcam/file'
    local_filename = 'client/foo_file.jpeg'
    r = requests.get(url)
    with open(local_filename, 'wb') as fp:
        fp.write(r.content)
        
if __name__ == '__main__':
    test_stream()

