from io import BytesIO
from typing import Iterable, Dict


def extract(byte_io: BytesIO) -> Iterable[Dict]:
    """
    Implement corpus specific extract function
    """
    from itertools import chain
    from zipfile import ZipFile

    zip_obj = ZipFile(byte_io)
    archives = zip_obj.namelist()
    jsons = filter(lambda x: x.endswith(".json"), archives)
    file_ios = map(zip_obj.open, jsons)
    return chain(map(extract_each_json, file_ios))
    # return chain(*map(extract_each_json, file_ios))


def extract_each_json(byte_io: BytesIO) -> Iterable[Dict]:
    import json

    json_io = json.load(byte_io)
    category = json_io["metadata"]["category"]
    print("extract_each_json")

    def extract_doc(document: dict) -> dict:
        title = document["metadata"]["title"]
        url = document["metadata"]["url"]
        text = "\n".join(line["form"] for line in document["paragraph"])

        return {"category": category, "text": text, "title": title, "url": url}

    texts = map(extract_doc, json_io["document"])

    return texts

from io import BytesIO
from typing import Iterable, Dict


def extract(byte_io: BytesIO) -> Iterable[Dict]:
    """
    Implement corpus specific extract function
    """
    from itertools import chain
    from zipfile import ZipFile

    zip_obj = ZipFile(byte_io)
    archives = zip_obj.namelist()
    jsons = filter(lambda x: x.endswith(".json"), archives)
    file_ios = map(zip_obj.open, jsons)
    for file_io in file_ios:
        
    return chain(map(extract_each_json, file_ios))
    # return chain(*map(extract_each_json, file_ios))


def extract_each_json(byte_io: BytesIO) -> Iterable[Dict]:
    import json

    json_io = json.load(byte_io)
    category = json_io["metadata"]["category"]
    print("extract_each_json")

    def extract_doc(document: dict) -> dict:
        title = document["metadata"]["title"]
        url = document["metadata"]["url"]
        text = "\n".join(line["form"] for line in document["paragraph"])

        return {"category": category, "text": text, "title": title, "url": url}

    texts = map(extract_doc, json_io["document"])

    return texts

import boto3
import io

s3 = boto3.resource('s3')
obj = s3.Object('skt-lsl-raw-apne2','raw/everyone_corpus_web/NIKL_WEB_v1.0.zip')

class S3File(io.RawIOBase):
    def __init__(self, s3_object):
        self.s3_object = s3_object
        self.position = 0

    def __repr__(self):
        return "<%s s3_object=%r>" % (type(self).__name__, self.s3_object)

    @property
    def size(self):
        return self.s3_object.content_length

    def tell(self):
        return self.position

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.position = offset
        elif whence == io.SEEK_CUR:
            self.position += offset
        elif whence == io.SEEK_END:
            self.position = self.size + offset
        else:
            raise ValueError("invalid whence (%r, should be %d, %d, %d)" % (
                whence, io.SEEK_SET, io.SEEK_CUR, io.SEEK_END
            ))

        return self.position

    def seekable(self):
        return True

    def read(self, size=-1):
        if size == -1:
            # Read to the end of the file
            range_header = "bytes=%d-" % self.position
            self.seek(offset=0, whence=io.SEEK_END)
        else:
            new_position = self.position + size

            # If we're going to read beyond the end of the object, return
            # the entire object.
            if new_position >= self.size:
                return self.read()

            range_header = "bytes=%d-%d" % (self.position, new_position - 1)
            self.seek(offset=size, whence=io.SEEK_CUR)

        return self.s3_object.get(Range=range_header)["Body"].read()

    def readable(self):
        return True


import io

# bytes_io = io.BufferedReader(obj.get()['Body']._raw_stream)
bytes_io = S3File(obj)

from io import BytesIO
from typing import Iterable, Dict


def extract(byte_io: BytesIO) -> Iterable[Dict]:
    """
    Implement corpus specific extract function
    """
    from itertools import chain
    from zipfile import ZipFile

    zip_obj = ZipFile(byte_io)
    archives = zip_obj.namelist()
    jsons = filter(lambda x: x.endswith(".json"), archives)
    file_ios = map(zip_obj.open, jsons)
    return file_ios

def extract_each_json(byte_io: BytesIO) -> Iterable[Dict]:
    import json

    json_io = json.load(byte_io)
    category = json_io["metadata"]["category"]

    def extract_doc(document: dict) -> dict:
        title = document["metadata"]["title"]
        url = document["metadata"]["url"]
        text = "\n".join(line["form"] for line in document["paragraph"])

        return {"category": category, "text": text, "title": title, "url": url}

    texts = map(extract_doc, json_io["document"])

    return texts

a = extract(bytes_io)

for i in a:
    print(i)
    break

b = a.()

a = extract(bytes_io)

for i, x in enumerate(a):
    print(x)
    if i == 1:
        break

