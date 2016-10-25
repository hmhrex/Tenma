from __future__ import absolute_import
from celery.decorators import task
from .utils.comicimporter import ComicImporter

@task(name="import_comic_files_task")
def import_comic_files_task():
	importer = ComicImporter()
	importer.import_comic_files()