#  Copyright (c) ZenML GmbH 2022. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.
from contextlib import ExitStack as does_not_raise
from datetime import datetime

from whylogs.core import DatasetProfileView

from zenml.integrations.whylogs.materializers.whylogs_materializer import (
    WhylogsMaterializer,
)
from zenml.pipelines import pipeline
from zenml.steps import step


def test_whylogs_materializer(clean_repo):
    """Tests whether the steps work for the Whylogs materializer."""

    @step
    def read_view() -> DatasetProfileView:
        """Reads and materializes a Whylogs dataset profile view."""
        return DatasetProfileView(
            columns={},
            dataset_timestamp=datetime.now(),
            creation_timestamp=datetime.now(),
        )

    @pipeline
    def test_pipeline(read_view) -> None:
        """Tests the Whylogs materializer."""
        read_view()

    with does_not_raise():
        test_pipeline(
            read_view=read_view().with_return_materializers(WhylogsMaterializer)
        ).run()

    last_run = clean_repo.get_pipeline("test_pipeline").runs[-1]
    dataset_profile_view = last_run.steps[-1].output.read()
    assert isinstance(dataset_profile_view, DatasetProfileView)
