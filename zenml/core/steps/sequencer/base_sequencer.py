#  Copyright (c) maiot GmbH 2021. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.

from abc import abstractmethod

from tensorflow_metadata.proto.v0.schema_pb2 import Schema
from tensorflow_metadata.proto.v0.statistics_pb2 import \
    DatasetFeatureStatisticsList

from zenml.core.steps.base_step import BaseStep
from zenml.utils.enums import StepTypes


class BaseSequencerStep(BaseStep):
    """
    Base class for all sequencing steps. These steps are used to
    specify transformation and filling operations on timeseries datasets
    that occur before the data preprocessing takes place.
    """

    STEP_TYPE = StepTypes.sequencer.name

    def __init__(self,
                 statistics: DatasetFeatureStatisticsList = None,
                 schema: Schema = None,
                 **kwargs):
        super().__init__(**kwargs)

        self.statistics = statistics
        self.schema = schema

    @abstractmethod
    def get_category_do_fn(self):
        """

        :return:
        """
        pass

    @abstractmethod
    def get_timestamp_do_fn(self):
        """

        :return:
        """
        pass

    @abstractmethod
    def get_combine_fn(self):
        """

        :return:
        """
        pass

    @abstractmethod
    def get_window(self):
        """

        :return:
        """
        pass
