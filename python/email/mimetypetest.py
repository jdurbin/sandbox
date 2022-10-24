#!/usr/bin/env python3 

import mimetypes
mime_type,mime_subtype = mimetypes.guess_type('invoice.pdf')[0].split("/")
print(mime_type,mime_subtype)
