# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# This is here so that we can mix storages as we need. We'll do this for pipeline
# and whitenoise with hashing and gzip when we get those both working.

from pipeline.storage import PipelineMixin
from whitenoise.django import GzipManifestStaticFilesStorage


class ManifestPipelineStorage(PipelineMixin, GzipManifestStaticFilesStorage):
    pass
