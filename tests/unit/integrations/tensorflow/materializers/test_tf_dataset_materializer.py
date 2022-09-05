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

import tensorflow as tf

from zenml.integrations.tensorflow.materializers.tf_dataset_materializer import (
    TensorflowDatasetMaterializer,
)
from zenml.pipelines import pipeline
from zenml.steps import step


def test_tensorflow_tf_dataset_materializer(clean_repo):
    """Tests whether the steps work for the TensorFlow TF Dataset materializer."""

    @step
    def read_dataset() -> tf.data.Dataset:
        """Reads and materializes a Keras model."""
        return tf.data.Dataset.from_tensor_slices([1, 2, 3])

    @pipeline
    def test_pipeline(read_dataset) -> None:
        """Tests the PillowImageMaterializer."""
        read_dataset()

    with does_not_raise():
        test_pipeline(
            read_dataset=read_dataset().with_return_materializers(
                TensorflowDatasetMaterializer
            )
        ).run()

    last_run = clean_repo.get_pipeline("test_pipeline").runs[-1]
    dataset = last_run.steps[-1].output.read()
    assert isinstance(dataset, tf.data.Dataset)
