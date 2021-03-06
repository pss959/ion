#
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
{
  'includes': [
    '../../common.gypi',
  ],

  'targets': [
    {
      'target_name': 'ionportgfx_test',
      'includes': [ '../../dev/test_target.gypi' ],
      'sources' : [
        'getglprocaddress_test.cc',
        'isextensionsupported_test.cc',
        'setswapinterval_test.cc',
        'visual_test.cc',
      ],
      'dependencies' : [
        '<(ion_dir)/portgfx/portgfx.gyp:ionportgfx_for_tests',
        '<(ion_dir)/base/base.gyp:ionbase_for_tests',
        '<(ion_dir)/external/gtest.gyp:iongtest_safeallocs',
        '<(ion_dir)/port/port.gyp:ionport',
      ],
      'conditions': [
        ['OS == "asmjs"', {
          'sources!': [
            # TODO(user): Re-enable these tests by creating a stubbed out
            # canvas.
            'getglprocaddress_test.cc',
            'isextensionsupported_test.cc',
            'setswapinterval_test.cc',
            'visual_test.cc',
          ],
        }],
      ],
    },
  ],
}
