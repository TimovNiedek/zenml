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

from pytorch_lightning.trainer import Trainer

from zenml.integrations.pytorch_lightning.materializers.pytorch_lightning_materializer import (
    PyTorchLightningMaterializer,
)
from zenml.steps import step


def test_pytorch_lightning_trainer_materializer():
    """Tests whether the steps work for the PyTorch Lightning materializer."""

    @step
    def some_step() -> Trainer:
        return Trainer()

    with does_not_raise():
        some_step().with_return_materializers(PyTorchLightningMaterializer)()
