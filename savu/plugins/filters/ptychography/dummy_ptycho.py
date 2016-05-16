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
.. module:: ica
   :platform: Unix
   :synopsis: A plugin to fit peaks

.. moduleauthor:: Aaron Parsons <scientificsoftware@diamond.ac.uk>

"""
import logging
from savu.plugins.utils import register_plugin
from savu.plugins.filters.base_ptycho import BasePtycho
import numpy as np


@register_plugin
class DummyPtycho(BasePtycho):
    """
    This plugin performs ptychography using the ptypy package
    """

    def __init__(self):
        super(DummyPtycho, self).__init__("DummyPtycho")

    def filter_frames(self, data):
        data = data[0]
        probe = data[0]
        object_transmission = np.random.rand(self.obj_shape)
        positions = self.get_positions()
        return [probe, object_transmission, positions]