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
  'includes' : [
    '../common.gypi',
  ],

  'variables': {
    # Used by make_into_app.gypi. We can define this once per target, or
    # globally here.
    'target_app_location_param': '<(PRODUCT_DIR)/demos',
  },

  'targets': [
    {
      'target_name': 'iondemohud_assets',
      'type': 'static_library',
      'includes': [
        '../dev/zipasset_generator.gypi',
      ],
      'dependencies': [
        '<(ion_dir)/port/port.gyp:ionport',
      ],
      'sources': [
        'res/iondemohud.iad',
      ],
    },  # target: iondemohud_assets

    {
      'target_name': 'textdemo_assets',
      'type': 'static_library',
      'includes': [
        '../dev/zipasset_generator.gypi',
      ],
      'dependencies': [
        '<(ion_dir)/port/port.gyp:ionport',
      ],
      'sources': [
        'res/textdemo_assets.iad',
      ],
    },  # target: textdemo_assets

    {
      'target_name': 'threadingdemo_assets',
      'type': 'static_library',
      'includes': [
        '../dev/zipasset_generator.gypi',
      ],
      'dependencies': [
        '<(ion_dir)/port/port.gyp:ionport',
      ],
      'sources': [
        'threadingdemo_assets.iad',
      ],
    },  # target: threadingdemo_assets

    {
      'target_name': 'particles_assets',
      'type': 'static_library',
      'includes': [
        '../dev/zipasset_generator.gypi',
      ],
      'dependencies': [
        '<(ion_dir)/port/port.gyp:ionport',
      ],
      'sources': [
        'particles_assets.iad',
      ],
    },  # target: particles_assets

    {
      'target_name': 'gearsdemo_assets',
      'type': 'static_library',
      'includes': [
        '../dev/zipasset_generator.gypi',
      ],
      'dependencies': [
        '<(ion_dir)/port/port.gyp:ionport',
      ],
      'sources': [
        'gearsdemo_assets.iad',
      ],
    },  # target: gearsdemo_assets

    {
      'target_name': 'shapedemo_assets',
      'type': 'static_library',
      'includes': [
        '../dev/zipasset_generator.gypi',
      ],
      'dependencies': [
        '<(ion_dir)/port/port.gyp:ionport',
      ],
      'sources': [
        'shapedemo_assets.iad',
      ],
    },  # target: shapedemo_assets


    {
      'target_name': 'skindemo_assets',
      'type': 'static_library',
      'includes': [
        '../dev/zipasset_generator.gypi',
      ],
      'dependencies': [
        '<(ion_dir)/port/port.gyp:ionport',
      ],
      'sources': [
        'skindemo_assets.iad',
        'skindemo_data_assets.iad',
      ],
    },  # target: skindemo_assets

    {
      'target_name': 'iondraw',
      'includes': [ 'demobase.gypi', ],
      'variables': {
        'demo_class_name': 'IonDraw'
      },
      'sources': [
        'iondraw.cc',
        'hud.cc',
        'hud.h',
      ],
      'dependencies': [
        ':iondemohud_assets',
        '<(ion_dir)/external/freetype2.gyp:ionfreetype2',
      ],
    },
    {
      # This will do the right things to get a runnable "thing", depending on
      # platform.
      'variables': {
        # The exact package name defined above, as a shared lib:
        'make_this_target_into_an_app_param': 'iondraw',
        # The name of the .java class
        'apk_class_name_param': 'IonDraw',
      },
      'includes': [
        'demo_apk_variables.gypi',
      ],
    },

    {
      'target_name': 'ionsimpledraw',
      'includes': [ 'demobase.gypi', ],
      'variables': {
        'demo_class_name': 'IonSimpleDraw'
      },
      'sources': [
        'ionsimpledraw.cc',
      ],
    },
    {
      'variables': {
        'make_this_target_into_an_app_param': 'ionsimpledraw',
        'apk_class_name_param': 'IonSimpleDraw',
      },
      'includes': [
        'demo_apk_variables.gypi',
      ],
    },

    {
      'target_name': 'particles',
      'includes': [ 'demobase.gypi', ],
      'variables': {
        'demo_class_name': 'Particles'
      },
      'sources': [
        'particles.cc',
      ],
      'dependencies': [
        ':particles_assets',
        '<(ion_dir)/external/freetype2.gyp:ionfreetype2',
      ],
    },
    {
      'variables': {
        'make_this_target_into_an_app_param': 'particles',
        'apk_class_name_param': 'Particles',
      },
      'includes': [
        'demo_apk_variables.gypi',
      ],
    },

    {
      'target_name': 'gearsdemo',
      'includes': [ 'demobase.gypi', ],
      'variables': {
        'demo_class_name': 'GearsDemo'
      },
      'sources': [
        'gearsdemo.cc',
      ],
      'dependencies': [
        'gearsdemo_assets',
      ],
    },
    {
      'variables': {
        'make_this_target_into_an_app_param': 'gearsdemo',
        'apk_class_name_param': 'GearsDemo',
      },
      'includes': [
        'demo_apk_variables.gypi',
      ],
    },

    {
      'target_name': 'shapedemo',
      'includes': [ 'demobase.gypi', ],
      'variables': {
        'demo_class_name': 'ShapeDemo'
      },
      'sources': [
        'shapedemo.cc',
      ],
      'dependencies': [
        'shapedemo_assets',
      ],
    },
    {
      'variables': {
        'make_this_target_into_an_app_param': 'shapedemo',
        'apk_class_name_param': 'ShapeDemo',
      },
      'includes': [
        'demo_apk_variables.gypi',
      ],
    },


    {
      'target_name': 'skindemo',
      'includes': [ 'demobase.gypi', ],
      'variables': {
        'demo_class_name': 'SkinDemo'
      },
      'sources': [
        'hud.cc',
        'hud.h',
        'skindemo.cc',
      ],
      'dependencies': [
        ':iondemohud_assets',
        ':skindemo_assets',
        '<(ion_dir)/external/external.gyp:ionopenctm',
      ],
    },
    {
      'variables': {
        'make_this_target_into_an_app_param': 'skindemo',
        'apk_class_name_param': 'SkinDemo',
      },
      'includes': [
        'demo_apk_variables.gypi',
      ],
    },

    {
      'target_name': 'textdemo',
      'includes': [ 'demobase.gypi', ],
      'variables': {
        'demo_class_name': 'TextDemo'
      },
      'sources': [
        'textdemo.cc',
      ],
      'dependencies': [
        ':textdemo_assets',
        '<(ion_dir)/external/freetype2.gyp:ionfreetype2',
        '<(ion_dir)/external/icu.gyp:ionicu',
      ],
    },
    {
      'variables': {
        'make_this_target_into_an_app_param': 'textdemo',
        'apk_class_name_param': 'TextDemo',
      },
      'includes': [
        'demo_apk_variables.gypi',
      ],
    },

    {
      'target_name': 'threadingdemo',
      'includes': [ 'demobase.gypi', ],
      'variables': {
        'demo_class_name': 'ThreadingDemo'
      },
      'sources': [
        'threadingdemo.cc',
      ],
      'dependencies': [
        ':threadingdemo_assets',
      ],
    },
    {
      'variables': {
        'make_this_target_into_an_app_param': 'threadingdemo',
        'apk_class_name_param': 'ThreadingDemo',
      },
      'includes': [
        'demo_apk_variables.gypi',
      ],
    },

    {
      'target_name': 'volatilescene',
      'includes': [ 'demobase.gypi', ],
      'variables': {
        'demo_class_name': 'VolatileScene'
      },
      'sources': [
        'volatilescene.cc',
      ],
    },
    {
      'variables': {
        'make_this_target_into_an_app_param': 'volatilescene',
        'apk_class_name_param': 'VolatileScene',
      },
      'includes': [
        'demo_apk_variables.gypi',
      ],
    },

  ],
}
