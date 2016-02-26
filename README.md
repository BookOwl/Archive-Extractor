# Archive Extractor
A simple graphical archive extractor written in Python.
To use, just run archiveextractor.pyw

This tool support extracting
- gztar: gzip’ed tar-file
- bztar: bzip2’ed tar-file (if the bz2 module is available.)
- xztar: xz’ed tar-file (if the lzma module is available.)
- tar: uncompressed tar file
- zip: ZIP file

## Changelog:
2.0: Extractions are now performed on a separate thread, so multiple extractions can be run at once. The file and directory pickers remember the last directory picked. Added an about button.

1.0: First release.

## License
Released under the MIT license.

The homepage for this project is https://github.com/BookOwl/Archive-Extractor
