# Copyright 2014 Diamond Light Source Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. module:: Timeseries_field_corrections
   :platform: Unix
   :synopsis: A Plugin to apply a simple dark and flatfield correction to some
       raw timeseries data

.. moduleauthor:: Mark Basham <scientificsoftware@diamond.ac.uk>

"""
from savu.data.structures import RawTimeseriesData, ProjectionData
from savu.plugins.plugin import Plugin

import numpy as np


class TimeseriesFieldCorrections(Plugin):
    """
    A Plugin to apply a simple dark and flatfield correction to some
    raw timeseries data
    """

    def __init__(self):
        super(TimeseriesFieldCorrections, self).__init__()

    def process(self, data, processes, process):
        """
        """
        image_key = data.image_key[...]
        # pull out the average dark and flat data
        dark = np.mean(data.data[image_key == 2, :, :], 0)
        flat = np.mean(data.data[image_key == 1, :, :], 0)
        # shortcut to reduce processing
        flat = flat - dark

        # get a list of all the frames
        projection_frames = np.arange(len(image_key))[image_key == 0]
        output_frames = np.arange(len(projection_frames))

        frames = np.array_split(output_frames, processes)[process]

        for frame in frames:
            projection = data.data[projection_frames[frame], :, :]
            projection = (projection-dark)/flat  # (flat-dark)
            # write the frame to disk

    def required_resource(self):
        """
        This plugin needs to use the CPU to work
        :returns:  CPU
        """
        return "CPU"

    def required_data_type(self):
        """
        The input for this plugin is RawTimeseriesData
        :returns:  RawTimeseriesData
        """
        return RawTimeseriesData

    def output_data_type(self):
        """
        The output of this plugin is ProjectionData
        :returns:  ProjectionData
        """
        return ProjectionData