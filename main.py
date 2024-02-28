from grobid_client.client import Client
from grobid_client.api.pdf.process_fulltext_document import sync_detailed


cl = Client("https://kermitt2-grobid.hf.space/api", timeout=30)

from pathlib import Path
from grobid_client.api.pdf import process_fulltext_document
from grobid_client.models import Article, ProcessForm
from grobid_client.types import TEI, File
pdf_file = "test.pdf"


with open("test.tei", "rb") as f:
    content = f.read()

article: Article = TEI.parse(content, figures=False)

print(article)
def download_file():
    with open(pdf_file, "rb") as fin:
        form = ProcessForm(
            segment_sentences="1",
            input_=File(file_name=pdf_file, payload=fin, mime_type="application/pdf"),
        )
        r = process_fulltext_document.sync_detailed(client=cl, multipart_data=form)
        print(r.status_code)
        if r.is_success:

            with open("test.tei", "wb") as f:
                f.write(r.content)
            article: Article = TEI.parse(r.content, figures=False)
            assert article.title