import copy

# -------------------------------------------
# ------------ Default Settings -------------
# -------------------------------------------

DEFAULT_TEXTURE_ALIAS = {
    "floor": "floorplane",
    "wall": "walls_mat",
    "table_legs": "table_legs_metal",
    "table": "table_ceramic",
    "door": "Door_MatDarkWood",
    "door_handle": "Door_MatMetal",
    "lift_object": "cube_redwood_mat",
    "na_metal1": "smetal",
    "na_metal2": "bmetal",
    "pp_table1": "light-wood",
    "pp_table2": "dark-wood",
    "stack_object1": "greenwood_mat",
    "stack_object2": "redwood_mat",
    "handoff_hammer_head": "metal_mat",
    "handoff_hammer_body": "wood_mat",
    "ta_lift_pot": "pot_mat",
    "ta_lift_handle1": "handle1_mat",
    "ta_lift_handle2": "handle2_mat",
    "ta_pih_plate": "plate_mat",
    "ta_pih_stick": "greenwood_mat",
}

DEFAULT_TEXTURE_TYPE = {
    "floor": "2d",
    "wall": "2d",
    "table_legs": "cube",
    "table": "2d",
    "door": "cube",
    "door_handle": "cube",
    "lift_object": "cube",
    "na_metal1": "cube",
    "na_metal2": "cube",
    "pp_table1": "2d",
    "pp_table2": "2d",
    "stack_object1": "cube",
    "stack_object2": "cube",
    "handoff_hammer_head": "cube",
    "handoff_hammer_body": "cube",
    "ta_lift_pot": "cube",
    "ta_lift_handle1": "cube",
    "ta_lift_handle2": "cube",
    "ta_pih_plate": "cube",
    "ta_pih_stick": "cube",
}

DEFAULT_TASK_TEXTURE_LIST = {
    "Door": ["floor", "wall", "table_legs", "table", "door", "door_handle"],
    "Lift": ["floor", "wall", "table_legs", "table", "lift_object"],
    "NutAssembly": ["floor", "wall", "table_legs", "table", "na_metal1", "na_metal2"],
    "NutAssemblyRound": [
        "floor",
        "wall",
        "table_legs",
        "table",
        "na_metal1",
        "na_metal2",
    ],
    "NutAssemblySingle": [
        "floor",
        "wall",
        "table_legs",
        "table",
        "na_metal1",
        "na_metal2",
    ],
    "NutAssemblySquare": [
        "floor",
        "wall",
        "table_legs",
        "table",
        "na_metal1",
        "na_metal2",
    ],
    "PickPlace": ["floor", "wall", "table_legs", "pp_table1", "pp_table2"],
    "PickPlaceBread": ["floor", "wall", "table_legs", "pp_table1", "pp_table2"],
    "PickPlaceCan": ["floor", "wall", "table_legs", "pp_table1", "pp_table2"],
    "PickPlaceCereal": ["floor", "wall", "table_legs", "pp_table1", "pp_table2"],
    "PickPlaceMilk": ["floor", "wall", "table_legs", "pp_table1", "pp_table2"],
    "PickPlaceSingle": ["floor", "wall", "table_legs", "pp_table1", "pp_table2"],
    "Stack": ["floor", "wall", "table_legs", "table", "stack_object1", "stack_object2"],
    "TwoArmHandover": [
        "floor",
        "wall",
        "table_legs",
        "table",
        "handoff_hammer_head",
        "handoff_hammer_body",
    ],
    "TwoArmLift": [
        "floor",
        "wall",
        "table_legs",
        "table",
        "ta_lift_pot",
        "ta_lift_handle1",
        "ta_lift_handle2",
    ],
    "TwoArmPegInHole": ["floor", "wall", "ta_pih_plate", "ta_pih_stick"],
    "Wipe": ["floor", "wall", "table_legs", "table"],
}


# -------------------------------------------
# ---- SECANT's Preset Configurations ----
# -------------------------------------------

PRESET_TEXTURE_CONFIG = {
    # random seed
    "seed": 100,
    # a dictionary that maps alias names of target objects (see DEFAULT_TEXTURE_ALIAS)
    # to some texture candidates. Keys should be subsets of keys from
    # DEFAULT_TEXTURE_ALIAS'. Values should be a texture candidate or a list of texture
    # candidates. If a list of texture candidates is provided, a random candidate will
    # be selected and applied to the corresponding target object.
    # A texture candidate is either a string representing the path to a image texture
    # file, or a tuple of RGB values normalized to [0, 1]. Note that you can use the
    # names of robosuite's builtin texture files as texture candidate.
    # Check `secant.envs.robosuite.ALL_TEXTURES` for all the builtin texture names,
    # or `secant.envs.robosuite.TEXTURES` to get a dictionary that maps these names
    # to their source files.
    "tex_candidate": {
        "floor": [
            "WoodTiles",
            "WoodPanels",
            "WoodDark",
            "WoodLight",
            "WoodgrainGray",
            "FeltGray",
            "Dirt",
        ],
        "wall": [
            "PlasterCream",
            "PlasterPink",
            "PlasterYellow",
            "PlasterGray",
            "PlasterWhite",
            "BricksWhite",
            "Clay",
        ],
        "table_legs": ["Metal", "SteelBrushed", "SteelScratched"],
        "table": [
            "Ceramic",
            "PlasterCream",
            "PlasterYellow",
            "PlasterGray",
            "WoodDark",
            "WoodLight",
        ],
        "door": ["WoodDark", "WoodLight", "WoodGreen", "WoodRed", "WoodBlue"],
        "door_handle": ["Brass", "Metal", "SteelBrushed", "SteelScratched"],
        "lift_object": ["WoodGreen", "WoodRed", "WoodBlue"],
        "na_metal1": [
            "Brass",
            "SteelBrushed",
            "Metal",
            "WoodGreen",
            "WoodRed",
            "WoodBlue",
        ],
        "na_metal2": [
            "Brass",
            "SteelBrushed",
            "Metal",
            "WoodGreen",
            "WoodRed",
            "WoodBlue",
        ],
        "pp_table1": [
            "WoodDark",
            "Ceramic",
            "PlasterCream",
            "PlasterYellow",
            "PlasterGray",
            "WoodLight",
            "WoodGreen",
            "WoodRed",
            "WoodBlue",
        ],
        "pp_table2": [
            "WoodDark",
            "Ceramic",
            "PlasterCream",
            "PlasterYellow",
            "PlasterGray",
            "WoodLight",
            "WoodGreen",
            "WoodRed",
            "WoodBlue",
        ],
        "stack_object1": ["WoodGreen", "WoodRed", "WoodBlue"],
        "stack_object2": ["WoodGreen", "WoodRed", "WoodBlue"],
        "handoff_hammer_head": ["Brass", "Metal", "SteelBrushed", "SteelScratched"],
        "handoff_hammer_body": [
            "WoodDark",
            "WoodLight",
            "WoodGreen",
            "WoodRed",
            "WoodBlue",
        ],
        "ta_lift_pot": ["WoodGreen", "WoodRed", "WoodBlue"],
        "ta_lift_handle1": ["WoodGreen", "WoodRed", "WoodBlue"],
        "ta_lift_handle2": ["WoodGreen", "WoodRed", "WoodBlue"],
        "ta_pih_plate": ["WoodGreen", "WoodRed", "WoodBlue"],
        "ta_pih_stick": ["WoodGreen", "WoodRed", "WoodBlue"],
    },
    # List of sets, where each set contains some texture keys. Each texture key from a
    # set will be assigned a different texture from the other keys in the same set.
    # This arg is used to enforce texture difference on important objects so that they
    # are more easily identified by vision algorithms. If None, no constraint is used.
    "tex_diff_constraint": [
        ["na_metal1", "na_metal2"],
        ["pp_table1", "pp_table2"],
        ["stack_object1", "stack_object2"],
        ["ta_lift_pot", "ta_lift_handle1", "ta_lift_handle2"],
        ["ta_pih_plate", "ta_pih_stick"],
    ],
    # List of object alias names whose texture need to be modified. If None, use
    # SECANT's default texture list in DEFAULT_TASK_TEXTURE_LIST[task]
    "tex_to_change": None,
    # A dictionary that maps object alias names to their texture types. Check
    # http://www.mujoco.org/book/XMLreference.html#texture on how texture types affect
    # rendering effect
    "tex_type": DEFAULT_TEXTURE_TYPE,
}

# Arguments to pass to the TextureModder of Robosuite
# https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/utils/mjmod.py#L779
PRESET_COLOR_CONFIG = {
    "seed": 100,  # random seed
    "geom_names": None,  # all geoms are randomized
    "randomize_local": True,  # sample nearby colors
    "randomize_material": True,  # randomize material reflectance / shininess / specular
    "local_rgb_interpolation": 0.2,
    "local_material_interpolation": 0.3,
    "texture_variations": [
        "rgb",
        "checker",
        "noise",
        # "gradient",
    ],  # all texture variation types
    "randomize_skybox": True,  # by default, randomize skybox too
}

# Arguments to pass to the CameraModder of Robosuite
# https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/utils/mjmod.py#L516
PRESET_CAMERA_CONFIG = {
    "seed": 100,  # random seed
    "camera_names": None,  # all cameras are randomized
    "randomize_position": True,
    "randomize_rotation": True,
    "randomize_fovy": True,
    "position_perturbation_size": 0.01,
    "rotation_perturbation_size": 0.087,
    "fovy_perturbation_size": 5.0,
}

# Arguments to pass to the LightingModder of Robosuite
# https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/utils/mjmod.py#L60
PRESET_LIGHTING_CONFIG = {
    "seed": 100,  # random seed
    "light_names": None,  # all lights are randomized
    "randomize_position": True,
    "randomize_direction": True,
    "randomize_specular": True,
    "randomize_ambient": True,
    "randomize_diffuse": True,
    "randomize_active": True,
    "position_perturbation_size": 0.1,
    "direction_perturbation_size": 0.35,
    "specular_perturbation_size": 0.1,
    "ambient_perturbation_size": 0.1,
    "diffuse_perturbation_size": 0.1,
}

# -------------------------------------------
# ----------- Preset Collection  ------------
# -------------------------------------------

# All available preset names mapped to their corresponding arguments for env.reset().
# Used for the custom_reset_config argument of RobosuiteAdapter.
ALL_PRESET_ARGUMENTS = {
    "SECANT": dict(
        custom_texture="SECANT",
        custom_color="SECANT",
        custom_camera="SECANT",
        custom_light="SECANT",
    ),
}

# All available preset names for texture/color/camera/lighting mapped to their configs.
ALL_TEXTURE_PRESETS = {
    "SECANT": PRESET_TEXTURE_CONFIG,
}
ALL_COLOR_PRESETS = {"SECANT": PRESET_COLOR_CONFIG}
ALL_CAMERA_PRESETS = {"SECANT": PRESET_CAMERA_CONFIG}
ALL_LIGHTING_PRESETS = {"SECANT": PRESET_LIGHTING_CONFIG}


def get_custom_reset_config(task, gen_type, scene_id):
  custom_seed = TASK_RANDOM_SEED[task][gen_type][scene_id]
  custom_texture = custom_color = custom_camera = custom_light = custom_seed
  custom_reset_config = {}
  if custom_texture:
    custom_texture_config = copy.deepcopy(PRESET_TEXTURE_CONFIG)
    custom_texture_config["tex_candidate"] = TASK_TEX_CANDIDATE[task][gen_type][scene_id]
    custom_texture_config["seed"] = custom_texture
    custom_reset_config["custom_texture"] = custom_texture_config
  if custom_color:
    custom_color_config = copy.deepcopy(PRESET_COLOR_CONFIG)
    custom_color_config["seed"] = custom_color
    custom_reset_config["custom_color"] = custom_color_config
  if custom_camera:
    custom_camera_config = copy.deepcopy(PRESET_CAMERA_CONFIG)
    custom_camera_config["seed"] = custom_camera
    custom_reset_config["custom_camera"] = custom_camera_config
  if custom_light:
    custom_light_config = copy.deepcopy(PRESET_LIGHTING_CONFIG)
    custom_light_config["randomize_active"] = False
    custom_light_config["seed"] = custom_light
    custom_reset_config["custom_light"] = custom_light_config
  if not custom_reset_config:
    custom_reset_config = None
  return custom_reset_config


"""
Default texture config by robosuite:
    wall: PlasterCream
    floor: WoodTiles
    table: Ceramic
    door: WoodDark
    pp_table1: WoodLight
    pp_table2: WoodDark

Texture candidate for domain randomization
"""

DR_TEX_CANDIDATE = {
    "wall": ["PlasterPink", "PlasterYellow", "PlasterGray", "PlasterWhite", "Clay"],
    "floor": [
        "PlasterPink",
        "PlasterYellow",
        "PlasterGray",
        "PlasterWhite",
        "PlasterCream",
        "WoodDark",
        "WoodLight",
        "SteelBrushed",
        "SteelScratched",
        "Brass",
    ],
    "table": [
        "PlasterPink",
        "PlasterYellow",
        "PlasterGray",
        "PlasterWhite",
        "PlasterCream",
        "WoodDark",
        "WoodLight",
        "SteelBrushed",
        "SteelScratched",
        "Brass",
        "Metal",
    ],
    "door": [
        "PlasterPink",
        "PlasterYellow",
        "PlasterGray",
        "PlasterWhite",
        "PlasterCream",
        "SteelBrushed",
        "SteelScratched",
        "Brass",
        "Metal",
    ],
    "pp_table": [
        "PlasterPink",
        "PlasterYellow",
        "PlasterGray",
        "PlasterWhite",
        "PlasterCream",
        "SteelBrushed",
        "SteelScratched",
        "Brass",
        "Metal",
    ],
}

EVAL_TEX_CANDIDATE = {
    "eval-easy": [
        "WoodGreen",
        "WoodRed",
        "WoodBlue",
        "WoodgrainGray",
        "FeltGray",
        "Dirt",
    ]
    + [f"Custom{i:02d}" for i in range(1, 6)],
    "eval-hard": ["WoodPanels", "BricksWhite"]
    + [f"Custom{i:02d}" for i in range(6, 26)],
    "eval-extreme": [f"Custom{i:02d}" for i in range(26, 41)],
}

TASK_RANDOM_SEED = {
    "Door": {
        "train": [6, 8, 11, 12, 13, 20, 21, 24, 28, 29],
        "eval-easy": [40, 251, 262, 358, 364, 406, 442, 457, 459, 580],
        "eval-hard": [14, 20, 69, 239, 332, 442, 450, 476, 551, 572],
        "eval-extreme": [62, 104, 251, 304, 344, 354, 455, 505, 581, 589]
    },
    "Lift": {
        "train": [0, 2, 6, 8, 12, 13, 15, 16, 19, 23, 25],
        "eval-easy": [105, 106, 113, 114, 120, 130, 132, 163, 224, 281],
        "eval-hard": [16, 22, 102, 171, 190, 235, 309, 338, 343, 369],
        "eval-extreme": [26, 29, 31, 100, 112, 148, 229, 275, 291, 369],
    },
    "NutAssembly": {
        "train": [0, 2, 6, 8, 12, 13, 15, 16, 19, 23, 25],
        "eval-easy": [105, 106, 113, 114, 120, 130, 132, 163, 224, 281],
        "eval-hard": [16, 22, 102, 171, 190, 235, 309, 338, 343, 369],
        "eval-extreme": [26, 29, 31, 100, 112, 148, 229, 275, 291, 369],
    },
    "TwoArmPegInHole": {
        "train": [0, 1, 3, 6, 7, 22, 14, 16, 17, 19, 11],
        "eval-easy": [26, 35, 57, 95, 101, 108, 130, 271, 324, 359],
        "eval-hard": [110, 113, 116, 127, 131, 174, 219, 267, 283, 421],
        "eval-extreme": [11, 101, 108, 122, 132, 145, 166, 327, 349, 429],
    },
    "NutAssemblyRound": {
        "train": [0, 1, 4, 6, 8, 9, 15, 16, 20, 22, 23],
        "eval-easy": [36, 57, 66, 82, 107, 110, 113, 252, 310, 369],
        "eval-hard": [58, 66, 105, 119, 128, 183, 255, 287, 303, 374],
        "eval-extreme": [12, 22, 42, 67, 77, 91, 192, 195, 255, 279],
    },
    "TwoArmLift": {
        "train": [0, 3, 10, 12, 14, 18, 20, 22, 23, 24, 25],
        "eval-easy": [77, 119, 149, 207, 237, 214, 221, 245, 479, 540],
        "eval-hard": [17, 52, 56, 66, 84, 94, 99, 123, 200, 380],
        "eval-extreme": [26, 41, 49, 59, 68, 163, 244, 246, 257, 550],
    },
    "NutAssemblySingle": {
        "train": [6, 14, 17, 18, 19, 21, 22, 24, 25, 29],
        "eval-easy": [41, 69, 86, 120, 183, 243, 288, 358, 387, 574],
        "eval-hard": [194, 226, 242, 275, 279, 320, 359, 417, 545, 582],
        "eval-extreme": [45, 219, 293, 330, 371, 395, 440, 451, 463, 562]
    },
    "NutAssemblySquare": {
        "train": [3, 6, 7, 8, 11, 14, 16, 20, 21, 27],
        "eval-easy": [18, 56, 97, 302, 308, 343, 361, 401, 554, 572],
        "eval-hard": [17, 85, 97, 149, 272, 377, 382, 405, 504, 584],
        "eval-extreme": [27, 55, 330, 343, 345, 415, 422, 508, 510, 584]
    },
    "PickPlace": {
        "train": [0, 9, 11, 12, 17, 21, 24, 26, 27, 28],
        "eval-easy": [15, 68, 126, 137, 161, 264, 282, 423, 442, 447],
        "eval-hard": [0, 33, 65, 194, 247, 266, 318, 328, 578, 586],
        "eval-extreme": [139, 238, 239, 273, 296, 311, 315, 408, 447, 469]
    },
    "PickPlaceBread": {
        "train": [3, 5, 12, 13, 15, 16, 17, 18, 21, 28],
        "eval-easy": [5, 223, 278, 343, 369, 446, 467, 482, 551, 580],
        "eval-hard": [116, 291, 310, 341, 372, 458, 495, 513, 583, 586],
        "eval-extreme": [78, 96, 160, 383, 481, 489, 497, 549, 561, 569]
    },
    "PickPlaceCan": {
        "train": [0, 6, 7, 9, 11, 19, 22, 24, 25, 28],
        "eval-easy": [12, 46, 60, 63, 88, 95, 203, 213, 349, 531],
        "eval-hard": [99, 165, 181, 269, 313, 343, 457, 551, 561, 594],
        "eval-extreme": [41, 50, 64, 101, 190, 314, 327, 534, 565, 578]
    },
    "PickPlaceCereal": {
        "train": [0, 1, 2, 5, 14, 15, 21, 22, 25, 26],
        "eval-easy": [65, 119, 228, 273, 292, 367, 405, 455, 585, 589],
        "eval-hard": [45, 148, 276, 287, 301, 374, 423, 425, 492, 590],
        "eval-extreme": [16, 124, 137, 158, 241, 261, 386, 391, 513, 516]
    },
    "PickPlaceMilk": {
        "train": [1, 4, 6, 7, 8, 15, 16, 20, 23, 26],
        "eval-easy": [51, 103, 135, 140, 153, 160, 352, 393, 549, 551],
        "eval-hard": [16, 20, 42, 132, 146, 228, 275, 311, 419, 490],
        "eval-extreme": [92, 356, 362, 423, 424, 485, 500, 505, 564, 567]
    },
    "PickPlaceSingle": {
        "train": [0, 2, 10, 11, 18, 19, 23, 25, 26, 29],
        "eval-easy": [35, 54, 57, 62, 126, 147, 310, 388, 402, 449],
        "eval-hard": [68, 77, 98, 112, 115, 116, 406, 423, 430, 507],
        "eval-extreme": [53, 113, 177, 216, 310, 384, 447, 495, 541, 580]
    },
    "Stack": {
        "train": [1, 6, 8, 12, 13, 14, 15, 17, 18, 20],
        "eval-easy": [29, 50, 249, 308, 338, 353, 377, 398, 409, 420],
        "eval-hard": [158, 268, 292, 312, 319, 324, 427, 437, 447, 504],
        "eval-extreme": [12, 96, 155, 196, 211, 246, 317, 432, 440, 573]
    },
    "Wipe": {
        "train": [1, 4, 5, 6, 7, 8, 10, 17, 25, 29],
        "eval-easy": [12, 54, 132, 246, 301, 356, 364, 455, 488, 520],
        "eval-hard": [40, 50, 127, 142, 244, 301, 314, 367, 373, 560],
        "eval-extreme": [20, 130, 198, 228, 234, 327, 386, 465, 477, 478]
    },
    "TwoArmHandover": {
        "train": [2, 4, 5, 8, 10, 16, 17, 21, 26, 27],
        "eval-easy": [25, 167, 192, 196, 220, 372, 436, 453, 481, 527],
        "eval-hard": [52, 107, 233, 267, 272, 337, 391, 393, 409, 562],
        "eval-extreme": [88, 97, 150, 242, 250, 255, 486, 507, 569, 597]
    },
}

TASK_TEX_CANDIDATE = {
    "Lift": {
        "train": [
            {
                # "floor": "WoodTiles",
                # "wall": "PlasterCream",
                # "table_legs": "SteelBrushed",
                # "table": "Ceramic",
                # "lift_object": "Brass",
            },
            {
                # "floor": "WoodDark",
                # "wall": "PlasterGray",
                # "table_legs": "Metal",
                # "table": "PlasterGray",
                # "lift_object": "SteelScratched",
            },
            {
                # "floor": "Brass",
                # "wall": "PlasterYellow",
                # "table_legs": "SteelScratched",
                # "table": "WoodLight",
                # "lift_object": "Metal",
            },
            {
                # "floor": "PlasterYellow",
                # "wall": "PlasterWhite",
                # "table_legs": "Metal",
                # "table": "SteelScratched",
                # "lift_object": "Metal",
            },
            {
                # "floor": "WoodDark",
                # "wall": "PlasterGray",
                # "table_legs": "SteelScratched",
                # "table": "PlasterYellow",
                # "lift_object": "Metal",
            },
            {
                # "floor": "WoodLight",
                # "wall": "PlasterWhite",
                # "table_legs": "SteelScratched",
                # "table": "PlasterGray",
                # "lift_object": "Brass",
            },
            {
                # "floor": "SteelScratched",
                # "wall": "PlasterPink",
                # "table_legs": "Metal",
                # "table": "PlasterCream",
                # "lift_object": "Metal",
            },
            {
                # "floor": "Brass",
                # "wall": "PlasterYellow",
                # "table_legs": "SteelBrushed",
                # "table": "WoodDark",
                # "lift_object": "SteelBrushed",
            },
            {
                # "floor": "PlasterGray",
                # "wall": "Clay",
                # "table_legs": "SteelBrushed",
                # "table": "SteelScratched",
                # "lift_object": "SteelBrushed",
            },
            {
                # "floor": "WoodLight",
                # "wall": "PlasterWhite",
                # "table_legs": "SteelScratched",
                # "table": "PlasterYellow",
                # "lift_object": "Brass",
            },
            {
                # "floor": "PlasterWhite",
                # "wall": "PlasterPink",
                # "table_legs": "SteelBrushed",
                # "table": "Metal",
                # "lift_object": "Metal",
            },
        ],
        "eval-easy": [
            {
                "floor": "Custom03",
                "wall": "Custom05",
                "table_legs": "Metal",
                "table": "Custom02",
                "lift_object": "Custom04",
            },
            {
                "floor": "WoodRed",
                "wall": "WoodgrainGray",
                "table_legs": "SteelScratched",
                "table": "Custom04",
                "lift_object": "Dirt",
            },
            {
                "floor": "Custom02",
                "wall": "WoodGreen",
                "table_legs": "SteelBrushed",
                "table": "FeltGray",
                "lift_object": "WoodRed",
            },
            {
                "floor": "WoodGreen",
                "wall": "FeltGray",
                "table_legs": "SteelScratched",
                "table": "Dirt",
                "lift_object": "Custom02",
            },
            {
                "floor": "WoodgrainGray",
                "wall": "Custom05",
                "table_legs": "Metal",
                "table": "WoodBlue",
                "lift_object": "Custom01",
            },
            {
                "floor": "Custom05",
                "wall": "WoodRed",
                "table_legs": "SteelBrushed",
                "table": "Custom03",
                "lift_object": "WoodGreen",
            },
            {
                "floor": "FeltGray",
                "wall": "Dirt",
                "table_legs": "SteelBrushed",
                "table": "Custom04",
                "lift_object": "Custom02",
            },
            {
                "floor": "Custom03",
                "wall": "WoodgrainGray",
                "table_legs": "SteelBrushed",
                "table": "Dirt",
                "lift_object": "WoodGreen",
            },
            {
                "floor": "Custom01",
                "wall": "WoodBlue",
                "table_legs": "Metal",
                "table": "Custom03",
                "lift_object": "WoodGreen",
            },
            {
                "floor": "Custom04",
                "wall": "Custom03",
                "table_legs": "Metal",
                "table": "WoodBlue",
                "lift_object": "Dirt",
            },
        ],
        "eval-hard": [
            {
                "floor": "Custom23",
                "wall": "Custom10",
                "table_legs": "SteelBrushed",
                "table": "Custom16",
                "lift_object": "Custom19",
            },
            {
                "floor": "Custom19",
                "wall": "Custom22",
                "table_legs": "SteelBrushed",
                "table": "Custom07",
                "lift_object": "Custom09",
            },
            {
                "floor": "Custom16",
                "wall": "Custom20",
                "table_legs": "Metal",
                "table": "BricksWhite",
                "lift_object": "Custom07",
            },
            {
                "floor": "Custom07",
                "wall": "Custom09",
                "table_legs": "SteelBrushed",
                "table": "Custom10",
                "lift_object": "Custom19",
            },
            {
                "floor": "BricksWhite",
                "wall": "Custom20",
                "table_legs": "SteelScratched",
                "table": "Custom06",
                "lift_object": "Custom24",
            },
            {
                "floor": "WoodPanels",
                "wall": "Custom14",
                "table_legs": "Metal",
                "table": "Custom08",
                "lift_object": "Custom11",
            },
            {
                "floor": "Custom17",
                "wall": "Custom19",
                "table_legs": "SteelBrushed",
                "table": "Custom10",
                "lift_object": "Custom18",
            },
            {
                "floor": "Custom10",
                "wall": "Custom15",
                "table_legs": "Metal",
                "table": "Custom22",
                "lift_object": "Custom12",
            },
            {
                "floor": "Custom12",
                "wall": "Custom25",
                "table_legs": "SteelBrushed",
                "table": "Custom14",
                "lift_object": "Custom19",
            },
            {
                "floor": "Custom08",
                "wall": "Custom15",
                "table_legs": "SteelScratched",
                "table": "Custom09",
                "lift_object": "Custom13",
            },
        ],
        "eval-extreme": [
            {
                "floor": "Custom35",
                "wall": "Custom40",
                "table_legs": "SteelBrushed",
                "table": "Custom34",
                "lift_object": "Custom37",
            },
            {
                "floor": "Custom37",
                "wall": "Custom39",
                "table_legs": "SteelBrushed",
                "table": "Custom30",
                "lift_object": "Custom36",
            },
            {
                "floor": "Custom29",
                "wall": "Custom27",
                "table_legs": "SteelScratched",
                "table": "Custom34",
                "lift_object": "Custom31",
            },
            {
                "floor": "Custom39",
                "wall": "Custom36",
                "table_legs": "Metal",
                "table": "Custom35",
                "lift_object": "Custom32",
            },
            {
                "floor": "Custom28",
                "wall": "Custom33",
                "table_legs": "Metal",
                "table": "Custom29",
                "lift_object": "Custom39",
            },
            {
                "floor": "Custom34",
                "wall": "Custom35",
                "table_legs": "SteelScratched",
                "table": "Custom37",
                "lift_object": "Custom32",
            },
            {
                "floor": "Custom36",
                "wall": "Custom28",
                "table_legs": "SteelBrushed",
                "table": "Custom30",
                "lift_object": "Custom37",
            },
            {
                "floor": "Custom32",
                "wall": "Custom40",
                "table_legs": "SteelScratched",
                "table": "Custom31",
                "lift_object": "Custom34",
            },
            {
                "floor": "Custom30",
                "wall": "Custom33",
                "table_legs": "SteelBrushed",
                "table": "Custom34",
                "lift_object": "Custom32",
            },
            {
                "floor": "Custom26",
                "wall": "Custom33",
                "table_legs": "SteelScratched",
                "table": "Custom27",
                "lift_object": "Custom29",
            },
        ],
    },
    "Door": {
        "train": [
            {
                "floor": "WoodTiles",
                "wall": "BricksWhite",
                "table_legs": "SteelScratched",
                "table": "PlasterYellow",
                "door": "WoodBlue",
                "door_handle": "SteelScratched"
            },
            {
                "floor": "WoodTiles",
                "wall": "PlasterPink",
                "table_legs": "SteelScratched",
                "table": "WoodDark",
                "door": "WoodRed",
                "door_handle": "Brass"
            },
            {
                "floor": "Dirt",
                "wall": "Clay",
                "table_legs": "SteelScratched",
                "table": "WoodLight",
                "door": "WoodDark",
                "door_handle": "SteelScratched"
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterCream",
                "table_legs": "SteelBrushed",
                "table": "WoodLight",
                "door": "WoodGreen",
                "door_handle": "SteelBrushed"
            },
            {
                "floor": "Dirt",
                "wall": "PlasterYellow",
                "table_legs": "Metal",
                "table": "Ceramic",
                "door": "WoodRed",
                "door_handle": "SteelBrushed"
            },
            {
                "floor": "Dirt",
                "wall": "PlasterGray",
                "table_legs": "SteelBrushed",
                "table": "Ceramic",
                "door": "WoodGreen",
                "door_handle": "SteelBrushed"
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterCream",
                "table_legs": "SteelScratched",
                "table": "Ceramic",
                "door": "WoodGreen",
                "door_handle": "Metal"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "BricksWhite",
                "table_legs": "Metal",
                "table": "Ceramic",
                "door": "WoodGreen",
                "door_handle": "SteelBrushed"
            },
            {
                "floor": "Dirt",
                "wall": "PlasterPink",
                "table_legs": "SteelBrushed",
                "table": "WoodDark",
                "door": "WoodDark",
                "door_handle": "SteelBrushed"
            },
            {
                "floor": "WoodDark",
                "wall": "BricksWhite",
                "table_legs": "SteelScratched",
                "table": "PlasterYellow",
                "door": "WoodBlue",
                "door_handle": "Brass"
            }
        ],
        "eval-easy": [
            {
                "floor": "Custom02",
                "wall": "Dirt",
                "table_legs": "WoodGreen",
                "table": "Custom03",
                "door": "Custom02",
                "door_handle": "WoodRed"
            },
            {
                "floor": "FeltGray",
                "wall": "FeltGray",
                "table_legs": "Dirt",
                "table": "WoodRed",
                "door": "Custom05",
                "door_handle": "Custom01"
            },
            {
                "floor": "WoodBlue",
                "wall": "Custom01",
                "table_legs": "Dirt",
                "table": "Custom03",
                "door": "WoodGreen",
                "door_handle": "Custom05"
            },
            {
                "floor": "WoodRed",
                "wall": "Custom05",
                "table_legs": "WoodBlue",
                "table": "WoodgrainGray",
                "door": "WoodGreen",
                "door_handle": "Custom03"
            },
            {
                "floor": "Dirt",
                "wall": "Custom04",
                "table_legs": "Dirt",
                "table": "WoodBlue",
                "door": "WoodBlue",
                "door_handle": "WoodgrainGray"
            },
            {
                "floor": "Custom01",
                "wall": "Custom03",
                "table_legs": "Custom03",
                "table": "Custom03",
                "door": "Custom01",
                "door_handle": "Custom03"
            },
            {
                "floor": "Custom05",
                "wall": "WoodGreen",
                "table_legs": "Custom02",
                "table": "Custom01",
                "door": "WoodBlue",
                "door_handle": "Custom01"
            },
            {
                "floor": "WoodBlue",
                "wall": "WoodGreen",
                "table_legs": "Custom05",
                "table": "WoodGreen",
                "door": "WoodBlue",
                "door_handle": "FeltGray"
            },
            {
                "floor": "Custom01",
                "wall": "FeltGray",
                "table_legs": "Custom04",
                "table": "WoodBlue",
                "door": "Custom02",
                "door_handle": "Custom02"
            },
            {
                "floor": "Dirt",
                "wall": "Dirt",
                "table_legs": "Custom01",
                "table": "Custom01",
                "door": "Dirt",
                "door_handle": "Custom02"
            }
        ],
        "eval-hard": [
            {
                "floor": "Custom20",
                "wall": "Custom24",
                "table_legs": "Custom08",
                "table": "Custom24",
                "door": "Custom25",
                "door_handle": "Custom09"
            },
            {
                "floor": "BricksWhite",
                "wall": "BricksWhite",
                "table_legs": "Custom18",
                "table": "Custom10",
                "door": "Custom19",
                "door_handle": "Custom19"
            },
            {
                "floor": "Custom25",
                "wall": "Custom07",
                "table_legs": "Custom11",
                "table": "Custom16",
                "door": "Custom13",
                "door_handle": "Custom12"
            },
            {
                "floor": "Custom14",
                "wall": "Custom20",
                "table_legs": "Custom23",
                "table": "Custom11",
                "door": "WoodPanels",
                "door_handle": "Custom17"
            },
            {
                "floor": "Custom18",
                "wall": "Custom15",
                "table_legs": "Custom16",
                "table": "Custom13",
                "door": "Custom25",
                "door_handle": "Custom06"
            },
            {
                "floor": "Custom17",
                "wall": "Custom18",
                "table_legs": "Custom20",
                "table": "Custom17",
                "door": "Custom07",
                "door_handle": "Custom07"
            },
            {
                "floor": "Custom06",
                "wall": "Custom11",
                "table_legs": "Custom20",
                "table": "Custom11",
                "door": "Custom09",
                "door_handle": "Custom18"
            },
            {
                "floor": "Custom16",
                "wall": "Custom13",
                "table_legs": "Custom25",
                "table": "Custom23",
                "door": "Custom14",
                "door_handle": "Custom14"
            },
            {
                "floor": "Custom18",
                "wall": "Custom14",
                "table_legs": "Custom18",
                "table": "Custom06",
                "door": "Custom17",
                "door_handle": "Custom12"
            },
            {
                "floor": "Custom16",
                "wall": "Custom23",
                "table_legs": "Custom24",
                "table": "Custom16",
                "door": "BricksWhite",
                "door_handle": "Custom23"
            }
        ],
        "eval-extreme": [
            {
                "floor": "Custom26",
                "wall": "Custom40",
                "table_legs": "Custom34",
                "table": "Custom33",
                "door": "Custom32",
                "door_handle": "Custom36"
            },
            {
                "floor": "Custom28",
                "wall": "Custom35",
                "table_legs": "Custom29",
                "table": "Custom36",
                "door": "Custom38",
                "door_handle": "Custom39"
            },
            {
                "floor": "Custom31",
                "wall": "Custom29",
                "table_legs": "Custom26",
                "table": "Custom39",
                "door": "Custom33",
                "door_handle": "Custom31"
            },
            {
                "floor": "Custom29",
                "wall": "Custom40",
                "table_legs": "Custom34",
                "table": "Custom40",
                "door": "Custom30",
                "door_handle": "Custom31"
            },
            {
                "floor": "Custom40",
                "wall": "Custom27",
                "table_legs": "Custom34",
                "table": "Custom32",
                "door": "Custom34",
                "door_handle": "Custom34"
            },
            {
                "floor": "Custom28",
                "wall": "Custom28",
                "table_legs": "Custom28",
                "table": "Custom30",
                "door": "Custom29",
                "door_handle": "Custom30"
            },
            {
                "floor": "Custom39",
                "wall": "Custom27",
                "table_legs": "Custom38",
                "table": "Custom40",
                "door": "Custom34",
                "door_handle": "Custom38"
            },
            {
                "floor": "Custom30",
                "wall": "Custom34",
                "table_legs": "Custom30",
                "table": "Custom37",
                "door": "Custom34",
                "door_handle": "Custom31"
            },
            {
                "floor": "Custom39",
                "wall": "Custom39",
                "table_legs": "Custom39",
                "table": "Custom29",
                "door": "Custom36",
                "door_handle": "Custom30"
            },
            {
                "floor": "Custom30",
                "wall": "Custom37",
                "table_legs": "Custom33",
                "table": "Custom36",
                "door": "Custom33",
                "door_handle": "Custom29"
            }
        ]
    },
    "NutAssembly": {
        "train": [
            {
                "floor": "WoodgrainGray",
                "wall": "PlasterGray",
                "table_legs": "Metal",
                "table": "WoodDark",
                "na_metal1": "WoodRed",
                "na_metal2": "WoodRed"
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterWhite",
                "table_legs": "SteelScratched",
                "table": "Ceramic",
                "na_metal1": "WoodGreen",
                "na_metal2": "WoodGreen"
            },
            {
                "floor": "WoodPanels",
                "wall": "Clay",
                "table_legs": "Metal",
                "table": "PlasterGray",
                "na_metal1": "WoodRed",
                "na_metal2": "WoodRed"
            },
            {
                "floor": "WoodLight",
                "wall": "PlasterCream",
                "table_legs": "SteelBrushed",
                "table": "PlasterCream",
                "na_metal1": "SteelBrushed",
                "na_metal2": "SteelBrushed"
            },
            {
                "floor": "WoodLight",
                "wall": "PlasterYellow",
                "table_legs": "SteelBrushed",
                "table": "PlasterCream",
                "na_metal1": "WoodGreen",
                "na_metal2": "WoodGreen"
            },
            {
                "floor": "WoodLight",
                "wall": "BricksWhite",
                "table_legs": "Metal",
                "table": "Ceramic",
                "na_metal1": "WoodBlue",
                "na_metal2": "WoodGreen"
            },
            {
                "floor": "WoodPanels",
                "wall": "PlasterCream",
                "table_legs": "SteelBrushed",
                "table": "PlasterYellow",
                "na_metal1": "Metal",
                "na_metal2": "Brass"
            },
            {
                "floor": "Dirt",
                "wall": "PlasterCream",
                "table_legs": "SteelBrushed",
                "table": "PlasterGray",
                "na_metal1": "WoodGreen",
                "na_metal2": "WoodRed"
            },
            {
                "floor": "WoodLight",
                "wall": "BricksWhite",
                "table_legs": "Metal",
                "table": "WoodLight",
                "na_metal1": "Brass",
                "na_metal2": "WoodBlue"
            },
            {
                "floor": "Dirt",
                "wall": "PlasterYellow",
                "table_legs": "SteelBrushed",
                "table": "WoodDark",
                "na_metal1": "WoodGreen",
                "na_metal2": "Metal"
            }
        ],
        "eval-easy": [
            {
                "floor": "Custom02",
                "wall": "WoodgrainGray",
                "table_legs": "Custom01",
                "table": "WoodRed",
                "na_metal1": "Custom01",
                "na_metal2": "FeltGray"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "Custom02",
                "table_legs": "WoodgrainGray",
                "table": "Custom04",
                "na_metal1": "WoodRed",
                "na_metal2": "Custom02"
            },
            {
                "floor": "Dirt",
                "wall": "WoodBlue",
                "table_legs": "Dirt",
                "table": "Custom02",
                "na_metal1": "Custom01",
                "na_metal2": "WoodBlue"
            },
            {
                "floor": "Custom03",
                "wall": "Custom05",
                "table_legs": "WoodgrainGray",
                "table": "Dirt",
                "na_metal1": "Dirt",
                "na_metal2": "WoodRed"
            },
            {
                "floor": "FeltGray",
                "wall": "WoodRed",
                "table_legs": "Custom03",
                "table": "FeltGray",
                "na_metal1": "Custom05",
                "na_metal2": "Custom02"
            },
            {
                "floor": "Custom03",
                "wall": "Custom04",
                "table_legs": "Custom01",
                "table": "Custom05",
                "na_metal1": "Dirt",
                "na_metal2": "Dirt"
            },
            {
                "floor": "WoodBlue",
                "wall": "WoodgrainGray",
                "table_legs": "Custom01",
                "table": "WoodBlue",
                "na_metal1": "Custom01",
                "na_metal2": "WoodgrainGray"
            },
            {
                "floor": "Custom03",
                "wall": "WoodGreen",
                "table_legs": "FeltGray",
                "table": "WoodRed",
                "na_metal1": "FeltGray",
                "na_metal2": "Custom02"
            },
            {
                "floor": "Dirt",
                "wall": "Dirt",
                "table_legs": "WoodRed",
                "table": "WoodBlue",
                "na_metal1": "Dirt",
                "na_metal2": "Custom03"
            },
            {
                "floor": "FeltGray",
                "wall": "WoodRed",
                "table_legs": "WoodGreen",
                "table": "Custom01",
                "na_metal1": "WoodgrainGray",
                "na_metal2": "Custom04"
            }
        ],
        "eval-hard": [
            {
                "floor": "Custom25",
                "wall": "Custom12",
                "table_legs": "Custom25",
                "table": "Custom10",
                "na_metal1": "Custom11",
                "na_metal2": "Custom07"
            },
            {
                "floor": "Custom06",
                "wall": "WoodPanels",
                "table_legs": "Custom13",
                "table": "BricksWhite",
                "na_metal1": "Custom18",
                "na_metal2": "Custom11"
            },
            {
                "floor": "Custom13",
                "wall": "Custom16",
                "table_legs": "WoodPanels",
                "table": "Custom16",
                "na_metal1": "Custom25",
                "na_metal2": "Custom22"
            },
            {
                "floor": "Custom15",
                "wall": "Custom21",
                "table_legs": "BricksWhite",
                "table": "Custom15",
                "na_metal1": "Custom22",
                "na_metal2": "Custom13"
            },
            {
                "floor": "Custom24",
                "wall": "Custom17",
                "table_legs": "Custom13",
                "table": "Custom24",
                "na_metal1": "WoodPanels",
                "na_metal2": "Custom13"
            },
            {
                "floor": "Custom09",
                "wall": "Custom16",
                "table_legs": "Custom22",
                "table": "Custom25",
                "na_metal1": "Custom22",
                "na_metal2": "Custom08"
            },
            {
                "floor": "Custom24",
                "wall": "Custom23",
                "table_legs": "WoodPanels",
                "table": "Custom16",
                "na_metal1": "Custom06",
                "na_metal2": "WoodPanels"
            },
            {
                "floor": "Custom16",
                "wall": "Custom14",
                "table_legs": "Custom21",
                "table": "Custom14",
                "na_metal1": "Custom15",
                "na_metal2": "Custom15"
            },
            {
                "floor": "Custom17",
                "wall": "Custom15",
                "table_legs": "Custom18",
                "table": "Custom22",
                "na_metal1": "Custom14",
                "na_metal2": "Custom12"
            },
            {
                "floor": "Custom15",
                "wall": "Custom17",
                "table_legs": "Custom13",
                "table": "Custom12",
                "na_metal1": "Custom10",
                "na_metal2": "Custom07"
            }
        ],
        "eval-extreme": [
            {
                "floor": "Custom33",
                "wall": "Custom29",
                "table_legs": "Custom33",
                "table": "Custom26",
                "na_metal1": "Custom27",
                "na_metal2": "Custom27"
            },
            {
                "floor": "Custom38",
                "wall": "Custom34",
                "table_legs": "Custom37",
                "table": "Custom32",
                "na_metal1": "Custom28",
                "na_metal2": "Custom32"
            },
            {
                "floor": "Custom26",
                "wall": "Custom37",
                "table_legs": "Custom27",
                "table": "Custom28",
                "na_metal1": "Custom38",
                "na_metal2": "Custom36"
            },
            {
                "floor": "Custom32",
                "wall": "Custom40",
                "table_legs": "Custom35",
                "table": "Custom33",
                "na_metal1": "Custom39",
                "na_metal2": "Custom32"
            },
            {
                "floor": "Custom31",
                "wall": "Custom27",
                "table_legs": "Custom39",
                "table": "Custom30",
                "na_metal1": "Custom27",
                "na_metal2": "Custom31"
            },
            {
                "floor": "Custom39",
                "wall": "Custom40",
                "table_legs": "Custom34",
                "table": "Custom29",
                "na_metal1": "Custom26",
                "na_metal2": "Custom34"
            },
            {
                "floor": "Custom28",
                "wall": "Custom34",
                "table_legs": "Custom39",
                "table": "Custom38",
                "na_metal1": "Custom32",
                "na_metal2": "Custom33"
            },
            {
                "floor": "Custom27",
                "wall": "Custom33",
                "table_legs": "Custom28",
                "table": "Custom28",
                "na_metal1": "Custom38",
                "na_metal2": "Custom37"
            },
            {
                "floor": "Custom35",
                "wall": "Custom32",
                "table_legs": "Custom32",
                "table": "Custom27",
                "na_metal1": "Custom38",
                "na_metal2": "Custom36"
            },
            {
                "floor": "Custom32",
                "wall": "Custom30",
                "table_legs": "Custom40",
                "table": "Custom34",
                "na_metal1": "Custom38",
                "na_metal2": "Custom40"
            }
        ]
    },
    "TwoArmPegInHole": {
        "train": [
            {
                "floor": "WoodTiles",
                "wall": "PlasterCream",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodGreen",
            },
            {
                "floor": "PlasterCream",
                "wall": "PlasterYellow",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodBlue",
            },
            {
                "floor": "WoodLight",
                "wall": "PlasterWhite",
                "ta_pih_plate": "WoodBlue",
                "ta_pih_stick": "WoodGreen",
            },
            {
                "floor": "Brass",
                "wall": "PlasterYellow",
                "ta_pih_plate": "WoodBlue",
                "ta_pih_stick": "WoodRed",
            },
            {
                "floor": "PlasterPink",
                "wall": "PlasterGray",
                "ta_pih_plate": "WoodGreen",
                "ta_pih_stick": "WoodBlue",
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterGray",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodGreen",
            },
            {
                "floor": "SteelBrushed",
                "wall": "Clay",
                "ta_pih_plate": "WoodGreen",
                "ta_pih_stick": "WoodRed",
            },
            {
                "floor": "Brass",
                "wall": "PlasterYellow",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodGreen",
            },
            {
                "floor": "PlasterPink",
                "wall": "PlasterGray",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodBlue",
            },
            {
                "floor": "PlasterGray",
                "wall": "Clay",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodGreen",
            },
            {
                "floor": "PlasterWhite",
                "wall": "PlasterPink",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodBlue",
            },
        ],
        "eval-easy": [
            {
                "floor": "Custom03",
                "wall": "WoodgrainGray",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodGreen",
            },
            {
                "floor": "WoodgrainGray",
                "wall": "Custom03",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodBlue",
            },
            {
                "floor": "FeltGray",
                "wall": "WoodBlue",
                "ta_pih_plate": "WoodBlue",
                "ta_pih_stick": "WoodRed",
            },
            {
                "floor": "WoodGreen",
                "wall": "Dirt",
                "ta_pih_plate": "WoodBlue",
                "ta_pih_stick": "WoodRed",
            },
            {
                "floor": "FeltGray",
                "wall": "Custom05",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodGreen",
            },
            {
                "floor": "Dirt",
                "wall": "WoodBlue",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodBlue",
            },
            {
                "floor": "Custom05",
                "wall": "WoodRed",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodBlue",
            },
            {
                "floor": "Custom01",
                "wall": "Custom03",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodBlue",
            },
            {
                "floor": "WoodgrainGray",
                "wall": "Custom01",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodGreen",
            },
            {
                "floor": "WoodBlue",
                "wall": "WoodgrainGray",
                "ta_pih_plate": "WoodGreen",
                "ta_pih_stick": "WoodRed",
            },
        ],
        "eval-hard": [
            {
                "floor": "Custom08",
                "wall": "Custom11",
                "ta_pih_plate": "WoodGreen",
                "ta_pih_stick": "WoodBlue",
            },
            {
                "floor": "Custom15",
                "wall": "BricksWhite",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodGreen",
            },
            {
                "floor": "Custom19",
                "wall": "Custom10",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodBlue",
            },
            {
                "floor": "Custom20",
                "wall": "Custom17",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodGreen",
            },
            {
                "floor": "Custom21",
                "wall": "Custom10",
                "ta_pih_plate": "WoodBlue",
                "ta_pih_stick": "WoodGreen",
            },
            {
                "floor": "WoodPanels",
                "wall": "Custom07",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodBlue",
            },
            {
                "floor": "Custom14",
                "wall": "Custom12",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodGreen",
            },
            {
                "floor": "Custom22",
                "wall": "Custom12",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodGreen",
            },
            {
                "floor": "Custom16",
                "wall": "Custom10",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodGreen",
            },
            {
                "floor": "Custom17",
                "wall": "Custom07",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodBlue",
            },
        ],
        "eval-extreme": [
            {
                "floor": "Custom32",
                "wall": "Custom31",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodBlue",
            },
            {
                "floor": "Custom38",
                "wall": "Custom31",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodGreen",
            },
            {
                "floor": "Custom26",
                "wall": "Custom31",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodBlue",
            },
            {
                "floor": "Custom34",
                "wall": "Custom29",
                "ta_pih_plate": "WoodBlue",
                "ta_pih_stick": "WoodGreen",
            },
            {
                "floor": "Custom30",
                "wall": "Custom37",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodGreen",
            },
            {
                "floor": "Custom35",
                "wall": "Custom26",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodBlue",
            },
            {
                "floor": "Custom33",
                "wall": "Custom38",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodBlue",
            },
            {
                "floor": "Custom37",
                "wall": "Custom28",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodGreen",
            },
            {
                "floor": "Custom31",
                "wall": "Custom26",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodBlue",
            },
            {
                "floor": "Custom29",
                "wall": "Custom35",
                "ta_pih_plate": "WoodRed",
                "ta_pih_stick": "WoodGreen",
            },
        ],
    },
    "NutAssemblyRound": {
        "train": [
            {
                "floor": "WoodTiles",
                "wall": "PlasterCream",
                "table_legs": "SteelBrushed",
                "table": "Ceramic",
                "na_metal1": "SteelScratched",
                "na_metal2": "Brass",
            },
            {
                "floor": "PlasterCream",
                "wall": "PlasterYellow",
                "table_legs": "Metal",
                "table": "PlasterYellow",
                "na_metal1": "WoodBlue",
                "na_metal2": "WoodGreen",
            },
            {
                "floor": "SteelBrushed",
                "wall": "Clay",
                "table_legs": "Metal",
                "table": "PlasterCream",
                "na_metal1": "Metal",
                "na_metal2": "SteelBrushed",
            },
            {
                "floor": "Brass",
                "wall": "PlasterYellow",
                "table_legs": "Metal",
                "table": "WoodLight",
                "na_metal1": "Metal",
                "na_metal2": "SteelBrushed",
            },
            {
                "floor": "PlasterYellow",
                "wall": "PlasterWhite",
                "table_legs": "SteelBrushed",
                "table": "SteelScratched",
                "na_metal1": "WoodGreen",
                "na_metal2": "WoodBlue",
            },
            {
                "floor": "PlasterGray",
                "wall": "Clay",
                "table_legs": "SteelScratched",
                "table": "Brass",
                "na_metal1": "WoodRed",
                "na_metal2": "Brass",
            },
            {
                "floor": "SteelScratched",
                "wall": "PlasterPink",
                "table_legs": "SteelBrushed",
                "table": "PlasterCream",
                "na_metal1": "Brass",
                "na_metal2": "WoodBlue",
            },
            {
                "floor": "Brass",
                "wall": "PlasterYellow",
                "table_legs": "SteelBrushed",
                "table": "WoodDark",
                "na_metal1": "SteelBrushed",
                "na_metal2": "Metal",
            },
            {
                "floor": "PlasterWhite",
                "wall": "PlasterPink",
                "table_legs": "Metal",
                "table": "Brass",
                "na_metal1": "WoodGreen",
                "na_metal2": "Metal",
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterGray",
                "table_legs": "Metal",
                "table": "PlasterPink",
                "na_metal1": "WoodBlue",
                "na_metal2": "WoodRed",
            },
            {
                "floor": "PlasterWhite",
                "wall": "PlasterPink",
                "table_legs": "Metal",
                "table": "Metal",
                "na_metal1": "SteelBrushed",
                "na_metal2": "WoodBlue",
            },
        ],
        "eval-easy": [
            {
                "floor": "Custom02",
                "wall": "Custom01",
                "table_legs": "SteelScratched",
                "table": "WoodGreen",
                "na_metal1": "WoodBlue",
                "na_metal2": "Metal",
            },
            {
                "floor": "FeltGray",
                "wall": "WoodBlue",
                "table_legs": "SteelScratched",
                "table": "WoodgrainGray",
                "na_metal1": "WoodBlue",
                "na_metal2": "Brass",
            },
            {
                "floor": "Custom01",
                "wall": "Custom04",
                "table_legs": "SteelScratched",
                "table": "Custom05",
                "na_metal1": "WoodRed",
                "na_metal2": "WoodBlue",
            },
            {
                "floor": "FeltGray",
                "wall": "Custom01",
                "table_legs": "SteelBrushed",
                "table": "WoodRed",
                "na_metal1": "WoodGreen",
                "na_metal2": "Metal",
            },
            {
                "floor": "Dirt",
                "wall": "WoodBlue",
                "table_legs": "SteelScratched",
                "table": "Custom05",
                "na_metal1": "Brass",
                "na_metal2": "Metal",
            },
            {
                "floor": "Custom01",
                "wall": "WoodBlue",
                "table_legs": "SteelBrushed",
                "table": "FeltGray",
                "na_metal1": "Brass",
                "na_metal2": "WoodRed",
            },
            {
                "floor": "Custom02",
                "wall": "WoodGreen",
                "table_legs": "SteelScratched",
                "table": "FeltGray",
                "na_metal1": "WoodBlue",
                "na_metal2": "WoodRed",
            },
            {
                "floor": "Custom03",
                "wall": "FeltGray",
                "table_legs": "SteelScratched",
                "table": "WoodBlue",
                "na_metal1": "WoodGreen",
                "na_metal2": "SteelBrushed",
            },
            {
                "floor": "FeltGray",
                "wall": "Dirt",
                "table_legs": "SteelBrushed",
                "table": "Custom02",
                "na_metal1": "WoodRed",
                "na_metal2": "WoodBlue",
            },
            {
                "floor": "WoodgrainGray",
                "wall": "Custom02",
                "table_legs": "SteelScratched",
                "table": "WoodRed",
                "na_metal1": "WoodBlue",
                "na_metal2": "Metal",
            },
        ],
        "eval-hard": [
            {
                "floor": "Custom13",
                "wall": "Custom16",
                "table_legs": "SteelBrushed",
                "table": "Custom11",
                "na_metal1": "WoodGreen",
                "na_metal2": "Brass",
            },
            {
                "floor": "Custom09",
                "wall": "Custom13",
                "table_legs": "SteelScratched",
                "table": "BricksWhite",
                "na_metal1": "WoodRed",
                "na_metal2": "WoodBlue",
            },
            {
                "floor": "Custom09",
                "wall": "Custom16",
                "table_legs": "Metal",
                "table": "Custom06",
                "na_metal1": "Brass",
                "na_metal2": "Metal",
            },
            {
                "floor": "WoodPanels",
                "wall": "Custom22",
                "table_legs": "SteelScratched",
                "table": "Custom09",
                "na_metal1": "Metal",
                "na_metal2": "WoodGreen",
            },
            {
                "floor": "Custom10",
                "wall": "Custom20",
                "table_legs": "SteelBrushed",
                "table": "Custom07",
                "na_metal1": "Metal",
                "na_metal2": "WoodRed",
            },
            {
                "floor": "Custom10",
                "wall": "Custom24",
                "table_legs": "SteelBrushed",
                "table": "Custom14",
                "na_metal1": "WoodBlue",
                "na_metal2": "WoodRed",
            },
            {
                "floor": "Custom22",
                "wall": "Custom21",
                "table_legs": "SteelBrushed",
                "table": "Custom15",
                "na_metal1": "WoodGreen",
                "na_metal2": "SteelBrushed",
            },
            {
                "floor": "Custom07",
                "wall": "BricksWhite",
                "table_legs": "SteelScratched",
                "table": "Custom10",
                "na_metal1": "WoodGreen",
                "na_metal2": "WoodRed",
            },
            {
                "floor": "Custom17",
                "wall": "Custom18",
                "table_legs": "SteelScratched",
                "table": "Custom21",
                "na_metal1": "WoodGreen",
                "na_metal2": "WoodBlue",
            },
            {
                "floor": "Custom13",
                "wall": "Custom23",
                "table_legs": "SteelScratched",
                "table": "BricksWhite",
                "na_metal1": "WoodRed",
                "na_metal2": "Brass",
            },
        ],
        "eval-extreme": [
            {
                "floor": "Custom31",
                "wall": "Custom39",
                "table_legs": "SteelScratched",
                "table": "Custom38",
                "na_metal1": "WoodGreen",
                "na_metal2": "WoodRed",
            },
            {
                "floor": "Custom27",
                "wall": "Custom37",
                "table_legs": "Metal",
                "table": "Custom33",
                "na_metal1": "WoodBlue",
                "na_metal2": "WoodRed",
            },
            {
                "floor": "Custom39",
                "wall": "Custom34",
                "table_legs": "SteelScratched",
                "table": "Custom35",
                "na_metal1": "WoodGreen",
                "na_metal2": "WoodBlue",
            },
            {
                "floor": "Custom30",
                "wall": "Custom37",
                "table_legs": "SteelBrushed",
                "table": "Custom28",
                "na_metal1": "WoodGreen",
                "na_metal2": "Metal",
            },
            {
                "floor": "Custom35",
                "wall": "Custom38",
                "table_legs": "SteelBrushed",
                "table": "Custom40",
                "na_metal1": "WoodRed",
                "na_metal2": "WoodBlue",
            },
            {
                "floor": "Custom27",
                "wall": "Custom35",
                "table_legs": "SteelScratched",
                "table": "Custom32",
                "na_metal1": "Metal",
                "na_metal2": "WoodGreen",
            },
            {
                "floor": "Custom26",
                "wall": "Custom30",
                "table_legs": "SteelScratched",
                "table": "Custom29",
                "na_metal1": "Metal",
                "na_metal2": "SteelBrushed",
            },
            {
                "floor": "Custom32",
                "wall": "Custom27",
                "table_legs": "SteelBrushed",
                "table": "Custom36",
                "na_metal1": "SteelBrushed",
                "na_metal2": "WoodRed",
            },
            {
                "floor": "Custom26",
                "wall": "Custom30",
                "table_legs": "SteelBrushed",
                "table": "Custom37",
                "na_metal1": "WoodGreen",
                "na_metal2": "SteelBrushed",
            },
            {
                "floor": "Custom36",
                "wall": "Custom26",
                "table_legs": "Metal",
                "table": "Custom39",
                "na_metal1": "SteelBrushed",
                "na_metal2": "WoodGreen",
            },
        ],
    },
    "TwoArmLift": {
        "train": [
            {
                "floor": "WoodTiles",
                "wall": "PlasterCream",
                "table_legs": "SteelBrushed",
                "table": "Ceramic",
                "ta_lift_pot": "WoodRed",
                "ta_lift_handle1": "WoodGreen",
                "ta_lift_handle2": "WoodBlue",
            },
            {
                "floor": "WoodLight",
                "wall": "PlasterWhite",
                "table_legs": "SteelBrushed",
                "table": "PlasterWhite",
                "ta_lift_pot": "WoodBlue",
                "ta_lift_handle1": "WoodGreen",
                "ta_lift_handle2": "WoodRed",
            },
            {
                "floor": "PlasterWhite",
                "wall": "PlasterPink",
                "table_legs": "Metal",
                "table": "Metal",
                "ta_lift_pot": "WoodRed",
                "ta_lift_handle1": "WoodBlue",
                "ta_lift_handle2": "WoodGreen",
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterGray",
                "table_legs": "SteelScratched",
                "table": "PlasterYellow",
                "ta_lift_pot": "WoodBlue",
                "ta_lift_handle1": "WoodRed",
                "ta_lift_handle2": "WoodBlue",
            },
            {
                "floor": "SteelBrushed",
                "wall": "Clay",
                "table_legs": "SteelBrushed",
                "table": "PlasterWhite",
                "ta_lift_pot": "WoodGreen",
                "ta_lift_handle1": "WoodRed",
                "ta_lift_handle2": "WoodRed",
            },
            {
                "floor": "PlasterYellow",
                "wall": "PlasterWhite",
                "table_legs": "SteelBrushed",
                "table": "SteelBrushed",
                "ta_lift_pot": "WoodBlue",
                "ta_lift_handle1": "WoodRed",
                "ta_lift_handle2": "WoodGreen",
            },
            {
                "floor": "PlasterWhite",
                "wall": "PlasterPink",
                "table_legs": "Metal",
                "table": "Brass",
                "ta_lift_pot": "WoodBlue",
                "ta_lift_handle1": "WoodRed",
                "ta_lift_handle2": "WoodBlue",
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterGray",
                "table_legs": "Metal",
                "table": "PlasterPink",
                "ta_lift_pot": "WoodRed",
                "ta_lift_handle1": "WoodGreen",
                "ta_lift_handle2": "WoodRed",
            },
            {
                "floor": "WoodLight",
                "wall": "PlasterWhite",
                "table_legs": "SteelBrushed",
                "table": "PlasterYellow",
                "ta_lift_pot": "WoodBlue",
                "ta_lift_handle1": "WoodGreen",
                "ta_lift_handle2": "WoodRed",
            },
            {
                "floor": "SteelBrushed",
                "wall": "Clay",
                "table_legs": "SteelBrushed",
                "table": "PlasterGray",
                "ta_lift_pot": "WoodBlue",
                "ta_lift_handle1": "WoodRed",
                "ta_lift_handle2": "WoodGreen",
            },
            {
                "floor": "PlasterWhite",
                "wall": "PlasterPink",
                "table_legs": "Metal",
                "table": "Metal",
                "ta_lift_pot": "WoodRed",
                "ta_lift_handle1": "WoodBlue",
                "ta_lift_handle2": "WoodGreen",
            },
        ],
        "eval-easy": [
            {
                "floor": "WoodRed",
                "wall": "WoodGreen",
                "table_legs": "SteelBrushed",
                "table": "WoodBlue",
                "ta_lift_pot": "WoodGreen",
                "ta_lift_handle1": "WoodRed",
                "ta_lift_handle2": "WoodBlue",
            },
            {
                "floor": "WoodGreen",
                "wall": "WoodRed",
                "table_legs": "SteelScratched",
                "table": "Dirt",
                "ta_lift_pot": "WoodBlue",
                "ta_lift_handle1": "WoodGreen",
                "ta_lift_handle2": "WoodRed",
            },
            {
                "floor": "Custom03",
                "wall": "WoodBlue",
                "table_legs": "SteelBrushed",
                "table": "WoodgrainGray",
                "ta_lift_pot": "WoodRed",
                "ta_lift_handle1": "WoodGreen",
                "ta_lift_handle2": "WoodBlue",
            },
            {
                "floor": "FeltGray",
                "wall": "WoodRed",
                "table_legs": "SteelBrushed",
                "table": "Custom03",
                "ta_lift_pot": "WoodBlue",
                "ta_lift_handle1": "WoodGreen",
                "ta_lift_handle2": "WoodRed",
            },
            {
                "floor": "Dirt",
                "wall": "Custom03",
                "table_legs": "Metal",
                "table": "FeltGray",
                "ta_lift_pot": "WoodGreen",
                "ta_lift_handle1": "WoodRed",
                "ta_lift_handle2": "WoodBlue",
            },
            {
                "floor": "WoodBlue",
                "wall": "WoodGreen",
                "table_legs": "SteelScratched",
                "table": "Custom05",
                "ta_lift_pot": "WoodRed",
                "ta_lift_handle1": "WoodBlue",
                "ta_lift_handle2": "WoodBlue",
            },
            {
                "floor": "Custom05",
                "wall": "WoodgrainGray",
                "table_legs": "SteelScratched",
                "table": "Custom02",
                "ta_lift_pot": "WoodGreen",
                "ta_lift_handle1": "WoodRed",
                "ta_lift_handle2": "WoodRed",
            },
            {
                "floor": "Custom04",
                "wall": "Custom01",
                "table_legs": "SteelScratched",
                "table": "Custom03",
                "ta_lift_pot": "WoodRed",
                "ta_lift_handle1": "WoodBlue",
                "ta_lift_handle2": "WoodGreen",
            },
            {
                "floor": "Custom04",
                "wall": "Custom03",
                "table_legs": "Metal",
                "table": "WoodGreen",
                "ta_lift_pot": "WoodGreen",
                "ta_lift_handle1": "WoodRed",
                "ta_lift_handle2": "WoodRed",
            },
            {
                "floor": "Custom03",
                "wall": "Custom05",
                "table_legs": "SteelScratched",
                "table": "WoodRed",
                "ta_lift_pot": "WoodBlue",
                "ta_lift_handle1": "WoodRed",
                "ta_lift_handle2": "WoodBlue",
            },
        ],
        "eval-hard": [
            {
                "floor": "Custom23",
                "wall": "Custom07",
                "table_legs": "SteelScratched",
                "table": "WoodPanels",
                "ta_lift_pot": "WoodRed",
                "ta_lift_handle1": "WoodBlue",
                "ta_lift_handle2": "WoodGreen",
            },
            {
                "floor": "Custom11",
                "wall": "Custom22",
                "table_legs": "SteelBrushed",
                "table": "Custom10",
                "ta_lift_pot": "WoodRed",
                "ta_lift_handle1": "WoodGreen",
                "ta_lift_handle2": "WoodBlue",
            },
            {
                "floor": "Custom21",
                "wall": "Custom22",
                "table_legs": "Metal",
                "table": "Custom09",
                "ta_lift_pot": "WoodRed",
                "ta_lift_handle1": "WoodGreen",
                "ta_lift_handle2": "WoodBlue",
            },
            {
                "floor": "Custom09",
                "wall": "Custom13",
                "table_legs": "SteelScratched",
                "table": "BricksWhite",
                "ta_lift_pot": "WoodGreen",
                "ta_lift_handle1": "WoodRed",
                "ta_lift_handle2": "WoodBlue",
            },
            {
                "floor": "Custom15",
                "wall": "Custom22",
                "table_legs": "Metal",
                "table": "Custom07",
                "ta_lift_pot": "WoodBlue",
                "ta_lift_handle1": "WoodRed",
                "ta_lift_handle2": "WoodBlue",
            },
            {
                "floor": "Custom08",
                "wall": "Custom25",
                "table_legs": "SteelBrushed",
                "table": "Custom15",
                "ta_lift_pot": "WoodBlue",
                "ta_lift_handle1": "WoodGreen",
                "ta_lift_handle2": "WoodRed",
            },
            {
                "floor": "Custom14",
                "wall": "Custom15",
                "table_legs": "Metal",
                "table": "Custom21",
                "ta_lift_pot": "WoodRed",
                "ta_lift_handle1": "WoodBlue",
                "ta_lift_handle2": "WoodBlue",
            },
            {
                "floor": "Custom23",
                "wall": "Custom20",
                "table_legs": "SteelScratched",
                "table": "Custom08",
                "ta_lift_pot": "WoodBlue",
                "ta_lift_handle1": "WoodRed",
                "ta_lift_handle2": "WoodGreen",
            },
            {
                "floor": "Custom09",
                "wall": "Custom22",
                "table_legs": "Metal",
                "table": "Custom06",
                "ta_lift_pot": "WoodBlue",
                "ta_lift_handle1": "WoodRed",
                "ta_lift_handle2": "WoodGreen",
            },
            {
                "floor": "Custom17",
                "wall": "Custom11",
                "table_legs": "SteelScratched",
                "table": "Custom13",
                "ta_lift_pot": "WoodBlue",
                "ta_lift_handle1": "WoodGreen",
                "ta_lift_handle2": "WoodRed",
            },
        ],
        "eval-extreme": [
            {
                "floor": "Custom35",
                "wall": "Custom40",
                "table_legs": "Metal",
                "table": "Custom34",
                "ta_lift_pot": "WoodRed",
                "ta_lift_handle1": "WoodGreen",
                "ta_lift_handle2": "WoodRed",
            },
            {
                "floor": "Custom36",
                "wall": "Custom37",
                "table_legs": "Metal",
                "table": "Custom33",
                "ta_lift_pot": "WoodGreen",
                "ta_lift_handle1": "WoodBlue",
                "ta_lift_handle2": "WoodRed",
            },
            {
                "floor": "Custom27",
                "wall": "Custom40",
                "table_legs": "SteelBrushed",
                "table": "Custom29",
                "ta_lift_pot": "WoodBlue",
                "ta_lift_handle1": "WoodRed",
                "ta_lift_handle2": "WoodGreen",
            },
            {
                "floor": "Custom30",
                "wall": "Custom34",
                "table_legs": "SteelBrushed",
                "table": "Custom28",
                "ta_lift_pot": "WoodRed",
                "ta_lift_handle1": "WoodGreen",
                "ta_lift_handle2": "WoodBlue",
            },
            {
                "floor": "Custom29",
                "wall": "Custom35",
                "table_legs": "SteelScratched",
                "table": "Custom40",
                "ta_lift_pot": "WoodBlue",
                "ta_lift_handle1": "WoodRed",
                "ta_lift_handle2": "WoodGreen",
            },
            {
                "floor": "Custom36",
                "wall": "Custom31",
                "table_legs": "SteelScratched",
                "table": "Custom38",
                "ta_lift_pot": "WoodRed",
                "ta_lift_handle1": "WoodGreen",
                "ta_lift_handle2": "WoodBlue",
            },
            {
                "floor": "Custom35",
                "wall": "Custom32",
                "table_legs": "Metal",
                "table": "Custom39",
                "ta_lift_pot": "WoodBlue",
                "ta_lift_handle1": "WoodGreen",
                "ta_lift_handle2": "WoodRed",
            },
            {
                "floor": "Custom37",
                "wall": "Custom27",
                "table_legs": "SteelScratched",
                "table": "Custom32",
                "ta_lift_pot": "WoodGreen",
                "ta_lift_handle1": "WoodRed",
                "ta_lift_handle2": "WoodRed",
            },
            {
                "floor": "Custom27",
                "wall": "Custom30",
                "table_legs": "SteelBrushed",
                "table": "Custom36",
                "ta_lift_pot": "WoodBlue",
                "ta_lift_handle1": "WoodRed",
                "ta_lift_handle2": "WoodGreen",
            },
            {
                "floor": "Custom33",
                "wall": "Custom35",
                "table_legs": "Metal",
                "table": "Custom30",
                "ta_lift_pot": "WoodRed",
                "ta_lift_handle1": "WoodGreen",
                "ta_lift_handle2": "WoodBlue",
            },
        ],
    },
    "NutAssemblySingle": {
        "train": [
            {
                "floor": "WoodgrainGray",
                "wall": "PlasterGray",
                "table_legs": "Metal",
                "table": "WoodDark",
                "na_metal1": "WoodRed",
                "na_metal2": "WoodRed"
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterWhite",
                "table_legs": "SteelScratched",
                "table": "Ceramic",
                "na_metal1": "WoodGreen",
                "na_metal2": "WoodGreen"
            },
            {
                "floor": "WoodPanels",
                "wall": "Clay",
                "table_legs": "Metal",
                "table": "PlasterGray",
                "na_metal1": "WoodRed",
                "na_metal2": "WoodRed"
            },
            {
                "floor": "WoodLight",
                "wall": "PlasterCream",
                "table_legs": "SteelBrushed",
                "table": "PlasterCream",
                "na_metal1": "SteelBrushed",
                "na_metal2": "SteelBrushed"
            },
            {
                "floor": "WoodLight",
                "wall": "PlasterYellow",
                "table_legs": "SteelBrushed",
                "table": "PlasterCream",
                "na_metal1": "WoodGreen",
                "na_metal2": "WoodGreen"
            },
            {
                "floor": "WoodLight",
                "wall": "BricksWhite",
                "table_legs": "Metal",
                "table": "Ceramic",
                "na_metal1": "WoodBlue",
                "na_metal2": "WoodGreen"
            },
            {
                "floor": "WoodPanels",
                "wall": "PlasterCream",
                "table_legs": "SteelBrushed",
                "table": "PlasterYellow",
                "na_metal1": "Metal",
                "na_metal2": "Brass"
            },
            {
                "floor": "Dirt",
                "wall": "PlasterCream",
                "table_legs": "SteelBrushed",
                "table": "PlasterGray",
                "na_metal1": "WoodGreen",
                "na_metal2": "WoodRed"
            },
            {
                "floor": "WoodLight",
                "wall": "BricksWhite",
                "table_legs": "Metal",
                "table": "WoodLight",
                "na_metal1": "Brass",
                "na_metal2": "WoodBlue"
            },
            {
                "floor": "Dirt",
                "wall": "PlasterYellow",
                "table_legs": "SteelBrushed",
                "table": "WoodDark",
                "na_metal1": "WoodGreen",
                "na_metal2": "Metal"
            }
        ],
        "eval-easy": [
            {
                "floor": "Custom02",
                "wall": "WoodgrainGray",
                "table_legs": "Custom01",
                "table": "WoodRed",
                "na_metal1": "Custom01",
                "na_metal2": "FeltGray"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "Custom02",
                "table_legs": "WoodgrainGray",
                "table": "Custom04",
                "na_metal1": "WoodRed",
                "na_metal2": "Custom02"
            },
            {
                "floor": "Dirt",
                "wall": "WoodBlue",
                "table_legs": "Dirt",
                "table": "Custom02",
                "na_metal1": "Custom01",
                "na_metal2": "WoodBlue"
            },
            {
                "floor": "Custom03",
                "wall": "Custom05",
                "table_legs": "WoodgrainGray",
                "table": "Dirt",
                "na_metal1": "Dirt",
                "na_metal2": "WoodRed"
            },
            {
                "floor": "FeltGray",
                "wall": "WoodRed",
                "table_legs": "Custom03",
                "table": "FeltGray",
                "na_metal1": "Custom05",
                "na_metal2": "Custom02"
            },
            {
                "floor": "Custom03",
                "wall": "Custom04",
                "table_legs": "Custom01",
                "table": "Custom05",
                "na_metal1": "Dirt",
                "na_metal2": "Dirt"
            },
            {
                "floor": "WoodBlue",
                "wall": "WoodgrainGray",
                "table_legs": "Custom01",
                "table": "WoodBlue",
                "na_metal1": "Custom01",
                "na_metal2": "WoodgrainGray"
            },
            {
                "floor": "Custom03",
                "wall": "WoodGreen",
                "table_legs": "FeltGray",
                "table": "WoodRed",
                "na_metal1": "FeltGray",
                "na_metal2": "Custom02"
            },
            {
                "floor": "Dirt",
                "wall": "Dirt",
                "table_legs": "WoodRed",
                "table": "WoodBlue",
                "na_metal1": "Dirt",
                "na_metal2": "Custom03"
            },
            {
                "floor": "FeltGray",
                "wall": "WoodRed",
                "table_legs": "WoodGreen",
                "table": "Custom01",
                "na_metal1": "WoodgrainGray",
                "na_metal2": "Custom04"
            }
        ],
        "eval-hard": [
            {
                "floor": "Custom25",
                "wall": "Custom12",
                "table_legs": "Custom25",
                "table": "Custom10",
                "na_metal1": "Custom11",
                "na_metal2": "Custom07"
            },
            {
                "floor": "Custom06",
                "wall": "WoodPanels",
                "table_legs": "Custom13",
                "table": "BricksWhite",
                "na_metal1": "Custom18",
                "na_metal2": "Custom11"
            },
            {
                "floor": "Custom13",
                "wall": "Custom16",
                "table_legs": "WoodPanels",
                "table": "Custom16",
                "na_metal1": "Custom25",
                "na_metal2": "Custom22"
            },
            {
                "floor": "Custom15",
                "wall": "Custom21",
                "table_legs": "BricksWhite",
                "table": "Custom15",
                "na_metal1": "Custom22",
                "na_metal2": "Custom13"
            },
            {
                "floor": "Custom24",
                "wall": "Custom17",
                "table_legs": "Custom13",
                "table": "Custom24",
                "na_metal1": "WoodPanels",
                "na_metal2": "Custom13"
            },
            {
                "floor": "Custom09",
                "wall": "Custom16",
                "table_legs": "Custom22",
                "table": "Custom25",
                "na_metal1": "Custom22",
                "na_metal2": "Custom08"
            },
            {
                "floor": "Custom24",
                "wall": "Custom23",
                "table_legs": "WoodPanels",
                "table": "Custom16",
                "na_metal1": "Custom06",
                "na_metal2": "WoodPanels"
            },
            {
                "floor": "Custom16",
                "wall": "Custom14",
                "table_legs": "Custom21",
                "table": "Custom14",
                "na_metal1": "Custom15",
                "na_metal2": "Custom15"
            },
            {
                "floor": "Custom17",
                "wall": "Custom15",
                "table_legs": "Custom18",
                "table": "Custom22",
                "na_metal1": "Custom14",
                "na_metal2": "Custom12"
            },
            {
                "floor": "Custom15",
                "wall": "Custom17",
                "table_legs": "Custom13",
                "table": "Custom12",
                "na_metal1": "Custom10",
                "na_metal2": "Custom07"
            }
        ],
        "eval-extreme": [
            {
                "floor": "Custom33",
                "wall": "Custom29",
                "table_legs": "Custom33",
                "table": "Custom26",
                "na_metal1": "Custom27",
                "na_metal2": "Custom27"
            },
            {
                "floor": "Custom38",
                "wall": "Custom34",
                "table_legs": "Custom37",
                "table": "Custom32",
                "na_metal1": "Custom28",
                "na_metal2": "Custom32"
            },
            {
                "floor": "Custom26",
                "wall": "Custom37",
                "table_legs": "Custom27",
                "table": "Custom28",
                "na_metal1": "Custom38",
                "na_metal2": "Custom36"
            },
            {
                "floor": "Custom32",
                "wall": "Custom40",
                "table_legs": "Custom35",
                "table": "Custom33",
                "na_metal1": "Custom39",
                "na_metal2": "Custom32"
            },
            {
                "floor": "Custom31",
                "wall": "Custom27",
                "table_legs": "Custom39",
                "table": "Custom30",
                "na_metal1": "Custom27",
                "na_metal2": "Custom31"
            },
            {
                "floor": "Custom39",
                "wall": "Custom40",
                "table_legs": "Custom34",
                "table": "Custom29",
                "na_metal1": "Custom26",
                "na_metal2": "Custom34"
            },
            {
                "floor": "Custom28",
                "wall": "Custom34",
                "table_legs": "Custom39",
                "table": "Custom38",
                "na_metal1": "Custom32",
                "na_metal2": "Custom33"
            },
            {
                "floor": "Custom27",
                "wall": "Custom33",
                "table_legs": "Custom28",
                "table": "Custom28",
                "na_metal1": "Custom38",
                "na_metal2": "Custom37"
            },
            {
                "floor": "Custom35",
                "wall": "Custom32",
                "table_legs": "Custom32",
                "table": "Custom27",
                "na_metal1": "Custom38",
                "na_metal2": "Custom36"
            },
            {
                "floor": "Custom32",
                "wall": "Custom30",
                "table_legs": "Custom40",
                "table": "Custom34",
                "na_metal1": "Custom38",
                "na_metal2": "Custom40"
            }
        ]
    },
    "NutAssemblySquare": {
        "train": [
            {
                "floor": "Dirt",
                "wall": "Clay",
                "table_legs": "SteelBrushed",
                "table": "PlasterYellow",
                "na_metal1": "WoodRed",
                "na_metal2": "Brass"
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterWhite",
                "table_legs": "SteelBrushed",
                "table": "Ceramic",
                "na_metal1": "Metal",
                "na_metal2": "Metal"
            },
            {
                "floor": "WoodPanels",
                "wall": "BricksWhite",
                "table_legs": "Metal",
                "table": "PlasterGray",
                "na_metal1": "Brass",
                "na_metal2": "Metal"
            },
            {
                "floor": "Dirt",
                "wall": "PlasterYellow",
                "table_legs": "SteelScratched",
                "table": "WoodLight",
                "na_metal1": "WoodBlue",
                "na_metal2": "WoodGreen"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "PlasterYellow",
                "table_legs": "Metal",
                "table": "Ceramic",
                "na_metal1": "SteelBrushed",
                "na_metal2": "WoodRed"
            },
            {
                "floor": "WoodTiles",
                "wall": "PlasterPink",
                "table_legs": "SteelScratched",
                "table": "Ceramic",
                "na_metal1": "Brass",
                "na_metal2": "Metal"
            },
            {
                "floor": "FeltGray",
                "wall": "BricksWhite",
                "table_legs": "SteelBrushed",
                "table": "PlasterYellow",
                "na_metal1": "WoodBlue",
                "na_metal2": "WoodRed"
            },
            {
                "floor": "WoodLight",
                "wall": "BricksWhite",
                "table_legs": "Metal",
                "table": "PlasterGray",
                "na_metal1": "WoodGreen",
                "na_metal2": "WoodRed"
            },
            {
                "floor": "Dirt",
                "wall": "PlasterCream",
                "table_legs": "SteelScratched",
                "table": "WoodLight",
                "na_metal1": "WoodGreen",
                "na_metal2": "Metal"
            },
            {
                "floor": "WoodPanels",
                "wall": "PlasterGray",
                "table_legs": "SteelScratched",
                "table": "WoodDark",
                "na_metal1": "Brass",
                "na_metal2": "WoodGreen"
            }
        ],
        "eval-easy": [
            {
                "floor": "WoodgrainGray",
                "wall": "WoodBlue",
                "table_legs": "WoodRed",
                "table": "WoodBlue",
                "na_metal1": "Dirt",
                "na_metal2": "Custom03"
            },
            {
                "floor": "Dirt",
                "wall": "Custom02",
                "table_legs": "Custom03",
                "table": "WoodGreen",
                "na_metal1": "Custom03",
                "na_metal2": "Custom03"
            },
            {
                "floor": "WoodBlue",
                "wall": "Custom02",
                "table_legs": "WoodGreen",
                "table": "Custom05",
                "na_metal1": "Custom04",
                "na_metal2": "WoodRed"
            },
            {
                "floor": "Custom01",
                "wall": "WoodGreen",
                "table_legs": "FeltGray",
                "table": "WoodBlue",
                "na_metal1": "Dirt",
                "na_metal2": "Custom03"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "Custom02",
                "table_legs": "Dirt",
                "table": "Custom03",
                "na_metal1": "WoodRed",
                "na_metal2": "FeltGray"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "WoodBlue",
                "table_legs": "Custom05",
                "table": "Custom03",
                "na_metal1": "WoodBlue",
                "na_metal2": "WoodGreen"
            },
            {
                "floor": "Custom05",
                "wall": "Custom03",
                "table_legs": "Custom05",
                "table": "Custom01",
                "na_metal1": "WoodgrainGray",
                "na_metal2": "Custom05"
            },
            {
                "floor": "WoodRed",
                "wall": "WoodGreen",
                "table_legs": "WoodRed",
                "table": "WoodgrainGray",
                "na_metal1": "Custom04",
                "na_metal2": "WoodRed"
            },
            {
                "floor": "WoodRed",
                "wall": "WoodGreen",
                "table_legs": "Custom02",
                "table": "Dirt",
                "na_metal1": "WoodBlue",
                "na_metal2": "FeltGray"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "Custom05",
                "table_legs": "FeltGray",
                "table": "Custom04",
                "na_metal1": "WoodRed",
                "na_metal2": "FeltGray"
            }
        ],
        "eval-hard": [
            {
                "floor": "Custom21",
                "wall": "Custom23",
                "table_legs": "Custom23",
                "table": "WoodPanels",
                "na_metal1": "Custom17",
                "na_metal2": "BricksWhite"
            },
            {
                "floor": "Custom18",
                "wall": "Custom13",
                "table_legs": "Custom22",
                "table": "Custom08",
                "na_metal1": "Custom20",
                "na_metal2": "Custom08"
            },
            {
                "floor": "Custom20",
                "wall": "Custom16",
                "table_legs": "BricksWhite",
                "table": "BricksWhite",
                "na_metal1": "Custom07",
                "na_metal2": "Custom20"
            },
            {
                "floor": "Custom22",
                "wall": "Custom21",
                "table_legs": "Custom12",
                "table": "Custom17",
                "na_metal1": "WoodPanels",
                "na_metal2": "Custom14"
            },
            {
                "floor": "Custom19",
                "wall": "Custom21",
                "table_legs": "Custom19",
                "table": "Custom08",
                "na_metal1": "Custom18",
                "na_metal2": "Custom07"
            },
            {
                "floor": "Custom13",
                "wall": "Custom09",
                "table_legs": "Custom22",
                "table": "Custom22",
                "na_metal1": "Custom18",
                "na_metal2": "Custom25"
            },
            {
                "floor": "Custom13",
                "wall": "Custom06",
                "table_legs": "Custom20",
                "table": "Custom23",
                "na_metal1": "Custom10",
                "na_metal2": "Custom08"
            },
            {
                "floor": "Custom21",
                "wall": "Custom12",
                "table_legs": "Custom09",
                "table": "Custom18",
                "na_metal1": "Custom13",
                "na_metal2": "Custom22"
            },
            {
                "floor": "Custom14",
                "wall": "Custom18",
                "table_legs": "Custom15",
                "table": "Custom09",
                "na_metal1": "Custom23",
                "na_metal2": "Custom15"
            },
            {
                "floor": "Custom12",
                "wall": "Custom06",
                "table_legs": "Custom09",
                "table": "Custom16",
                "na_metal1": "Custom22",
                "na_metal2": "Custom14"
            }
        ],
        "eval-extreme": [
            {
                "floor": "Custom33",
                "wall": "Custom29",
                "table_legs": "Custom36",
                "table": "Custom31",
                "na_metal1": "Custom35",
                "na_metal2": "Custom30"
            },
            {
                "floor": "Custom27",
                "wall": "Custom36",
                "table_legs": "Custom32",
                "table": "Custom39",
                "na_metal1": "Custom29",
                "na_metal2": "Custom29"
            },
            {
                "floor": "Custom26",
                "wall": "Custom34",
                "table_legs": "Custom35",
                "table": "Custom30",
                "na_metal1": "Custom28",
                "na_metal2": "Custom29"
            },
            {
                "floor": "Custom38",
                "wall": "Custom29",
                "table_legs": "Custom30",
                "table": "Custom26",
                "na_metal1": "Custom31",
                "na_metal2": "Custom40"
            },
            {
                "floor": "Custom38",
                "wall": "Custom39",
                "table_legs": "Custom35",
                "table": "Custom26",
                "na_metal1": "Custom29",
                "na_metal2": "Custom36"
            },
            {
                "floor": "Custom26",
                "wall": "Custom26",
                "table_legs": "Custom31",
                "table": "Custom27",
                "na_metal1": "Custom26",
                "na_metal2": "Custom37"
            },
            {
                "floor": "Custom36",
                "wall": "Custom38",
                "table_legs": "Custom26",
                "table": "Custom27",
                "na_metal1": "Custom28",
                "na_metal2": "Custom26"
            },
            {
                "floor": "Custom32",
                "wall": "Custom26",
                "table_legs": "Custom32",
                "table": "Custom35",
                "na_metal1": "Custom33",
                "na_metal2": "Custom33"
            },
            {
                "floor": "Custom39",
                "wall": "Custom39",
                "table_legs": "Custom37",
                "table": "Custom39",
                "na_metal1": "Custom38",
                "na_metal2": "Custom33"
            },
            {
                "floor": "Custom36",
                "wall": "Custom39",
                "table_legs": "Custom40",
                "table": "Custom28",
                "na_metal1": "Custom28",
                "na_metal2": "Custom37"
            }
        ]
    },
    "PickPlace": {
        "train": [
            {
                "floor": "WoodPanels",
                "wall": "PlasterGray",
                "table_legs": "SteelBrushed",
                "pp_table1": "PlasterCream",
                "pp_table2": "WoodLight"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "Clay",
                "table_legs": "SteelScratched",
                "pp_table1": "WoodDark",
                "pp_table2": "WoodRed"
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterCream",
                "table_legs": "SteelBrushed",
                "pp_table1": "PlasterGray",
                "pp_table2": "Ceramic"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "PlasterWhite",
                "table_legs": "Metal",
                "pp_table1": "Ceramic",
                "pp_table2": "PlasterGray"
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterWhite",
                "table_legs": "SteelScratched",
                "pp_table1": "WoodDark",
                "pp_table2": "PlasterCream"
            },
            {
                "floor": "FeltGray",
                "wall": "PlasterYellow",
                "table_legs": "SteelScratched",
                "pp_table1": "WoodDark",
                "pp_table2": "WoodLight"
            },
            {
                "floor": "WoodDark",
                "wall": "BricksWhite",
                "table_legs": "SteelBrushed",
                "pp_table1": "PlasterGray",
                "pp_table2": "PlasterCream"
            },
            {
                "floor": "WoodLight",
                "wall": "PlasterWhite",
                "table_legs": "SteelScratched",
                "pp_table1": "PlasterYellow",
                "pp_table2": "WoodGreen"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "BricksWhite",
                "table_legs": "SteelScratched",
                "pp_table1": "PlasterCream",
                "pp_table2": "WoodGreen"
            },
            {
                "floor": "Dirt",
                "wall": "BricksWhite",
                "table_legs": "SteelBrushed",
                "pp_table1": "PlasterCream",
                "pp_table2": "WoodRed"
            }
        ],
        "eval-easy": [
            {
                "floor": "WoodRed",
                "wall": "Custom01",
                "table_legs": "WoodBlue",
                "pp_table1": "Custom05",
                "pp_table2": "WoodBlue"
            },
            {
                "floor": "FeltGray",
                "wall": "Dirt",
                "table_legs": "Custom05",
                "pp_table1": "Custom04",
                "pp_table2": "WoodBlue"
            },
            {
                "floor": "Custom02",
                "wall": "WoodGreen",
                "table_legs": "Custom02",
                "pp_table1": "Custom04",
                "pp_table2": "FeltGray"
            },
            {
                "floor": "Custom05",
                "wall": "FeltGray",
                "table_legs": "WoodBlue",
                "pp_table1": "Custom01",
                "pp_table2": "Custom05"
            },
            {
                "floor": "Dirt",
                "wall": "Custom03",
                "table_legs": "Custom04",
                "pp_table1": "Custom05",
                "pp_table2": "WoodgrainGray"
            },
            {
                "floor": "Custom02",
                "wall": "Custom03",
                "table_legs": "WoodBlue",
                "pp_table1": "WoodRed",
                "pp_table2": "WoodRed"
            },
            {
                "floor": "Dirt",
                "wall": "WoodGreen",
                "table_legs": "Custom01",
                "pp_table1": "Custom02",
                "pp_table2": "Custom01"
            },
            {
                "floor": "Custom01",
                "wall": "Dirt",
                "table_legs": "FeltGray",
                "pp_table1": "Dirt",
                "pp_table2": "WoodGreen"
            },
            {
                "floor": "WoodGreen",
                "wall": "Custom03",
                "table_legs": "Custom03",
                "pp_table1": "Custom02",
                "pp_table2": "WoodgrainGray"
            },
            {
                "floor": "Custom02",
                "wall": "WoodRed",
                "table_legs": "Custom04",
                "pp_table1": "Custom01",
                "pp_table2": "Dirt"
            }
        ],
        "eval-hard": [
            {
                "floor": "Custom20",
                "wall": "BricksWhite",
                "table_legs": "Custom16",
                "pp_table1": "Custom14",
                "pp_table2": "Custom19"
            },
            {
                "floor": "Custom06",
                "wall": "Custom11",
                "table_legs": "Custom25",
                "pp_table1": "Custom14",
                "pp_table2": "Custom06"
            },
            {
                "floor": "Custom16",
                "wall": "Custom15",
                "table_legs": "Custom07",
                "pp_table1": "Custom07",
                "pp_table2": "Custom21"
            },
            {
                "floor": "Custom09",
                "wall": "Custom20",
                "table_legs": "Custom11",
                "pp_table1": "Custom09",
                "pp_table2": "Custom25"
            },
            {
                "floor": "Custom12",
                "wall": "Custom11",
                "table_legs": "Custom23",
                "pp_table1": "WoodPanels",
                "pp_table2": "Custom09"
            },
            {
                "floor": "Custom20",
                "wall": "Custom11",
                "table_legs": "Custom14",
                "pp_table1": "Custom09",
                "pp_table2": "Custom22"
            },
            {
                "floor": "Custom25",
                "wall": "Custom19",
                "table_legs": "Custom13",
                "pp_table1": "Custom18",
                "pp_table2": "Custom11"
            },
            {
                "floor": "Custom24",
                "wall": "Custom13",
                "table_legs": "Custom20",
                "pp_table1": "Custom23",
                "pp_table2": "BricksWhite"
            },
            {
                "floor": "Custom09",
                "wall": "Custom16",
                "table_legs": "Custom06",
                "pp_table1": "Custom24",
                "pp_table2": "Custom11"
            },
            {
                "floor": "BricksWhite",
                "wall": "Custom10",
                "table_legs": "Custom12",
                "pp_table1": "Custom14",
                "pp_table2": "Custom23"
            }
        ],
        "eval-extreme": [
            {
                "floor": "Custom36",
                "wall": "Custom39",
                "table_legs": "Custom34",
                "pp_table1": "Custom31",
                "pp_table2": "Custom35"
            },
            {
                "floor": "Custom38",
                "wall": "Custom27",
                "table_legs": "Custom32",
                "pp_table1": "Custom28",
                "pp_table2": "Custom39"
            },
            {
                "floor": "Custom37",
                "wall": "Custom34",
                "table_legs": "Custom28",
                "pp_table1": "Custom30",
                "pp_table2": "Custom36"
            },
            {
                "floor": "Custom28",
                "wall": "Custom39",
                "table_legs": "Custom33",
                "pp_table1": "Custom40",
                "pp_table2": "Custom35"
            },
            {
                "floor": "Custom34",
                "wall": "Custom36",
                "table_legs": "Custom40",
                "pp_table1": "Custom28",
                "pp_table2": "Custom38"
            },
            {
                "floor": "Custom28",
                "wall": "Custom40",
                "table_legs": "Custom28",
                "pp_table1": "Custom26",
                "pp_table2": "Custom40"
            },
            {
                "floor": "Custom33",
                "wall": "Custom36",
                "table_legs": "Custom30",
                "pp_table1": "Custom31",
                "pp_table2": "Custom40"
            },
            {
                "floor": "Custom30",
                "wall": "Custom31",
                "table_legs": "Custom31",
                "pp_table1": "Custom35",
                "pp_table2": "Custom40"
            },
            {
                "floor": "Custom27",
                "wall": "Custom28",
                "table_legs": "Custom26",
                "pp_table1": "Custom35",
                "pp_table2": "Custom34"
            },
            {
                "floor": "Custom31",
                "wall": "Custom34",
                "table_legs": "Custom28",
                "pp_table1": "Custom30",
                "pp_table2": "Custom30"
            }
        ]
    },
    "PickPlaceBread": {
        "train": [
            {
                "floor": "WoodDark",
                "wall": "PlasterWhite",
                "table_legs": "SteelBrushed",
                "pp_table1": "WoodRed",
                "pp_table2": "WoodGreen"
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterGray",
                "table_legs": "Metal",
                "pp_table1": "WoodGreen",
                "pp_table2": "PlasterCream"
            },
            {
                "floor": "WoodLight",
                "wall": "PlasterYellow",
                "table_legs": "SteelBrushed",
                "pp_table1": "WoodBlue",
                "pp_table2": "PlasterCream"
            },
            {
                "floor": "FeltGray",
                "wall": "PlasterPink",
                "table_legs": "Metal",
                "pp_table1": "WoodLight",
                "pp_table2": "WoodGreen"
            },
            {
                "floor": "Dirt",
                "wall": "Clay",
                "table_legs": "SteelScratched",
                "pp_table1": "WoodDark",
                "pp_table2": "PlasterYellow"
            },
            {
                "floor": "WoodPanels",
                "wall": "Clay",
                "table_legs": "SteelBrushed",
                "pp_table1": "WoodRed",
                "pp_table2": "WoodBlue"
            },
            {
                "floor": "FeltGray",
                "wall": "PlasterCream",
                "table_legs": "Metal",
                "pp_table1": "WoodRed",
                "pp_table2": "WoodRed"
            },
            {
                "floor": "FeltGray",
                "wall": "BricksWhite",
                "table_legs": "Metal",
                "pp_table1": "WoodRed",
                "pp_table2": "WoodBlue"
            },
            {
                "floor": "FeltGray",
                "wall": "PlasterCream",
                "table_legs": "SteelBrushed",
                "pp_table1": "Ceramic",
                "pp_table2": "WoodLight"
            },
            {
                "floor": "WoodDark",
                "wall": "BricksWhite",
                "table_legs": "Metal",
                "pp_table1": "PlasterGray",
                "pp_table2": "WoodGreen"
            }
        ],
        "eval-easy": [
            {
                "floor": "Custom03",
                "wall": "FeltGray",
                "table_legs": "Custom05",
                "pp_table1": "WoodgrainGray",
                "pp_table2": "WoodgrainGray"
            },
            {
                "floor": "Custom04",
                "wall": "Custom04",
                "table_legs": "WoodRed",
                "pp_table1": "Dirt",
                "pp_table2": "FeltGray"
            },
            {
                "floor": "FeltGray",
                "wall": "FeltGray",
                "table_legs": "Custom01",
                "pp_table1": "Custom01",
                "pp_table2": "Custom04"
            },
            {
                "floor": "Custom03",
                "wall": "WoodGreen",
                "table_legs": "Custom01",
                "pp_table1": "Custom01",
                "pp_table2": "WoodRed"
            },
            {
                "floor": "WoodBlue",
                "wall": "Custom04",
                "table_legs": "Custom01",
                "pp_table1": "Custom05",
                "pp_table2": "FeltGray"
            },
            {
                "floor": "Dirt",
                "wall": "Custom04",
                "table_legs": "Custom05",
                "pp_table1": "WoodgrainGray",
                "pp_table2": "WoodGreen"
            },
            {
                "floor": "Custom01",
                "wall": "Custom03",
                "table_legs": "WoodGreen",
                "pp_table1": "Dirt",
                "pp_table2": "Custom05"
            },
            {
                "floor": "Custom03",
                "wall": "WoodBlue",
                "table_legs": "Custom05",
                "pp_table1": "Custom01",
                "pp_table2": "Custom04"
            },
            {
                "floor": "Custom04",
                "wall": "WoodBlue",
                "table_legs": "Custom04",
                "pp_table1": "WoodgrainGray",
                "pp_table2": "WoodRed"
            },
            {
                "floor": "WoodGreen",
                "wall": "WoodBlue",
                "table_legs": "WoodgrainGray",
                "pp_table1": "Custom02",
                "pp_table2": "Custom05"
            }
        ],
        "eval-hard": [
            {
                "floor": "Custom08",
                "wall": "Custom10",
                "table_legs": "Custom07",
                "pp_table1": "Custom07",
                "pp_table2": "Custom25"
            },
            {
                "floor": "Custom19",
                "wall": "Custom11",
                "table_legs": "Custom10",
                "pp_table1": "Custom10",
                "pp_table2": "Custom06"
            },
            {
                "floor": "Custom06",
                "wall": "Custom06",
                "table_legs": "Custom22",
                "pp_table1": "Custom15",
                "pp_table2": "Custom14"
            },
            {
                "floor": "Custom18",
                "wall": "Custom23",
                "table_legs": "Custom17",
                "pp_table1": "Custom13",
                "pp_table2": "Custom22"
            },
            {
                "floor": "Custom11",
                "wall": "Custom11",
                "table_legs": "Custom14",
                "pp_table1": "Custom06",
                "pp_table2": "Custom18"
            },
            {
                "floor": "Custom09",
                "wall": "Custom15",
                "table_legs": "Custom22",
                "pp_table1": "Custom07",
                "pp_table2": "Custom22"
            },
            {
                "floor": "Custom17",
                "wall": "Custom24",
                "table_legs": "WoodPanels",
                "pp_table1": "Custom25",
                "pp_table2": "Custom20"
            },
            {
                "floor": "Custom16",
                "wall": "Custom15",
                "table_legs": "Custom25",
                "pp_table1": "Custom07",
                "pp_table2": "Custom08"
            },
            {
                "floor": "Custom11",
                "wall": "Custom16",
                "table_legs": "Custom12",
                "pp_table1": "Custom09",
                "pp_table2": "Custom17"
            },
            {
                "floor": "Custom23",
                "wall": "Custom22",
                "table_legs": "Custom06",
                "pp_table1": "Custom07",
                "pp_table2": "Custom13"
            }
        ],
        "eval-extreme": [
            {
                "floor": "Custom34",
                "wall": "Custom32",
                "table_legs": "Custom36",
                "pp_table1": "Custom27",
                "pp_table2": "Custom26"
            },
            {
                "floor": "Custom31",
                "wall": "Custom37",
                "table_legs": "Custom26",
                "pp_table1": "Custom27",
                "pp_table2": "Custom33"
            },
            {
                "floor": "Custom26",
                "wall": "Custom32",
                "table_legs": "Custom40",
                "pp_table1": "Custom32",
                "pp_table2": "Custom27"
            },
            {
                "floor": "Custom37",
                "wall": "Custom35",
                "table_legs": "Custom32",
                "pp_table1": "Custom35",
                "pp_table2": "Custom34"
            },
            {
                "floor": "Custom33",
                "wall": "Custom33",
                "table_legs": "Custom29",
                "pp_table1": "Custom29",
                "pp_table2": "Custom38"
            },
            {
                "floor": "Custom39",
                "wall": "Custom38",
                "table_legs": "Custom36",
                "pp_table1": "Custom27",
                "pp_table2": "Custom33"
            },
            {
                "floor": "Custom28",
                "wall": "Custom40",
                "table_legs": "Custom39",
                "pp_table1": "Custom29",
                "pp_table2": "Custom40"
            },
            {
                "floor": "Custom34",
                "wall": "Custom26",
                "table_legs": "Custom40",
                "pp_table1": "Custom26",
                "pp_table2": "Custom37"
            },
            {
                "floor": "Custom27",
                "wall": "Custom26",
                "table_legs": "Custom35",
                "pp_table1": "Custom32",
                "pp_table2": "Custom28"
            },
            {
                "floor": "Custom29",
                "wall": "Custom35",
                "table_legs": "Custom30",
                "pp_table1": "Custom26",
                "pp_table2": "Custom27"
            }
        ]
    },
    "PickPlaceCan": {
        "train": [
            {
                "floor": "FeltGray",
                "wall": "PlasterPink",
                "table_legs": "SteelBrushed",
                "pp_table1": "WoodGreen",
                "pp_table2": "Ceramic"
            },
            {
                "floor": "FeltGray",
                "wall": "PlasterWhite",
                "table_legs": "SteelScratched",
                "pp_table1": "PlasterCream",
                "pp_table2": "PlasterCream"
            },
            {
                "floor": "WoodTiles",
                "wall": "Clay",
                "table_legs": "Metal",
                "pp_table1": "WoodRed",
                "pp_table2": "PlasterYellow"
            },
            {
                "floor": "WoodTiles",
                "wall": "PlasterYellow",
                "table_legs": "Metal",
                "pp_table1": "WoodDark",
                "pp_table2": "PlasterCream"
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterYellow",
                "table_legs": "Metal",
                "pp_table1": "WoodBlue",
                "pp_table2": "WoodRed"
            },
            {
                "floor": "WoodTiles",
                "wall": "PlasterPink",
                "table_legs": "Metal",
                "pp_table1": "PlasterYellow",
                "pp_table2": "Ceramic"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "BricksWhite",
                "table_legs": "SteelBrushed",
                "pp_table1": "Ceramic",
                "pp_table2": "Ceramic"
            },
            {
                "floor": "FeltGray",
                "wall": "PlasterCream",
                "table_legs": "SteelScratched",
                "pp_table1": "Ceramic",
                "pp_table2": "WoodLight"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "PlasterWhite",
                "table_legs": "SteelScratched",
                "pp_table1": "WoodGreen",
                "pp_table2": "PlasterCream"
            },
            {
                "floor": "Dirt",
                "wall": "PlasterWhite",
                "table_legs": "Metal",
                "pp_table1": "Ceramic",
                "pp_table2": "WoodGreen"
            }
        ],
        "eval-easy": [
            {
                "floor": "Custom05",
                "wall": "Custom04",
                "table_legs": "Custom04",
                "pp_table1": "WoodGreen",
                "pp_table2": "Custom02"
            },
            {
                "floor": "Custom04",
                "wall": "WoodBlue",
                "table_legs": "Custom02",
                "pp_table1": "Custom01",
                "pp_table2": "Dirt"
            },
            {
                "floor": "FeltGray",
                "wall": "Custom02",
                "table_legs": "FeltGray",
                "pp_table1": "Dirt",
                "pp_table2": "WoodBlue"
            },
            {
                "floor": "WoodGreen",
                "wall": "WoodgrainGray",
                "table_legs": "WoodGreen",
                "pp_table1": "FeltGray",
                "pp_table2": "Dirt"
            },
            {
                "floor": "WoodGreen",
                "wall": "WoodRed",
                "table_legs": "Custom05",
                "pp_table1": "Custom01",
                "pp_table2": "Custom05"
            },
            {
                "floor": "Custom02",
                "wall": "WoodgrainGray",
                "table_legs": "Custom02",
                "pp_table1": "WoodGreen",
                "pp_table2": "Custom03"
            },
            {
                "floor": "WoodGreen",
                "wall": "Custom04",
                "table_legs": "Custom05",
                "pp_table1": "Custom03",
                "pp_table2": "Custom03"
            },
            {
                "floor": "WoodBlue",
                "wall": "WoodBlue",
                "table_legs": "WoodRed",
                "pp_table1": "Custom01",
                "pp_table2": "Dirt"
            },
            {
                "floor": "FeltGray",
                "wall": "WoodgrainGray",
                "table_legs": "FeltGray",
                "pp_table1": "Custom05",
                "pp_table2": "WoodRed"
            },
            {
                "floor": "Custom02",
                "wall": "FeltGray",
                "table_legs": "Custom02",
                "pp_table1": "Custom03",
                "pp_table2": "Custom03"
            }
        ],
        "eval-hard": [
            {
                "floor": "Custom06",
                "wall": "Custom07",
                "table_legs": "Custom22",
                "pp_table1": "Custom18",
                "pp_table2": "WoodPanels"
            },
            {
                "floor": "Custom11",
                "wall": "Custom23",
                "table_legs": "Custom08",
                "pp_table1": "WoodPanels",
                "pp_table2": "Custom09"
            },
            {
                "floor": "WoodPanels",
                "wall": "Custom21",
                "table_legs": "Custom07",
                "pp_table1": "Custom25",
                "pp_table2": "Custom06"
            },
            {
                "floor": "Custom12",
                "wall": "Custom16",
                "table_legs": "Custom08",
                "pp_table1": "Custom21",
                "pp_table2": "WoodPanels"
            },
            {
                "floor": "Custom11",
                "wall": "Custom06",
                "table_legs": "Custom08",
                "pp_table1": "Custom15",
                "pp_table2": "Custom13"
            },
            {
                "floor": "Custom13",
                "wall": "Custom18",
                "table_legs": "Custom07",
                "pp_table1": "Custom17",
                "pp_table2": "BricksWhite"
            },
            {
                "floor": "Custom16",
                "wall": "Custom13",
                "table_legs": "Custom25",
                "pp_table1": "Custom17",
                "pp_table2": "Custom08"
            },
            {
                "floor": "Custom15",
                "wall": "Custom23",
                "table_legs": "Custom19",
                "pp_table1": "Custom21",
                "pp_table2": "WoodPanels"
            },
            {
                "floor": "BricksWhite",
                "wall": "Custom10",
                "table_legs": "Custom19",
                "pp_table1": "WoodPanels",
                "pp_table2": "Custom09"
            },
            {
                "floor": "Custom21",
                "wall": "Custom24",
                "table_legs": "Custom19",
                "pp_table1": "Custom20",
                "pp_table2": "Custom21"
            }
        ],
        "eval-extreme": [
            {
                "floor": "Custom28",
                "wall": "Custom32",
                "table_legs": "Custom30",
                "pp_table1": "Custom29",
                "pp_table2": "Custom30"
            },
            {
                "floor": "Custom31",
                "wall": "Custom35",
                "table_legs": "Custom30",
                "pp_table1": "Custom31",
                "pp_table2": "Custom40"
            },
            {
                "floor": "Custom27",
                "wall": "Custom35",
                "table_legs": "Custom40",
                "pp_table1": "Custom31",
                "pp_table2": "Custom35"
            },
            {
                "floor": "Custom33",
                "wall": "Custom29",
                "table_legs": "Custom40",
                "pp_table1": "Custom28",
                "pp_table2": "Custom40"
            },
            {
                "floor": "Custom34",
                "wall": "Custom37",
                "table_legs": "Custom37",
                "pp_table1": "Custom35",
                "pp_table2": "Custom26"
            },
            {
                "floor": "Custom38",
                "wall": "Custom27",
                "table_legs": "Custom38",
                "pp_table1": "Custom26",
                "pp_table2": "Custom27"
            },
            {
                "floor": "Custom31",
                "wall": "Custom39",
                "table_legs": "Custom37",
                "pp_table1": "Custom30",
                "pp_table2": "Custom40"
            },
            {
                "floor": "Custom30",
                "wall": "Custom31",
                "table_legs": "Custom31",
                "pp_table1": "Custom30",
                "pp_table2": "Custom37"
            },
            {
                "floor": "Custom27",
                "wall": "Custom35",
                "table_legs": "Custom34",
                "pp_table1": "Custom34",
                "pp_table2": "Custom31"
            },
            {
                "floor": "Custom37",
                "wall": "Custom35",
                "table_legs": "Custom28",
                "pp_table1": "Custom35",
                "pp_table2": "Custom31"
            }
        ]
    },
    "PickPlaceCereal": {
        "train": [
            {
                "floor": "WoodTiles",
                "wall": "PlasterCream",
                "table_legs": "SteelScratched",
                "pp_table1": "WoodLight",
                "pp_table2": "PlasterCream"
            },
            {
                "floor": "WoodTiles",
                "wall": "PlasterWhite",
                "table_legs": "Metal",
                "pp_table1": "PlasterCream",
                "pp_table2": "PlasterGray"
            },
            {
                "floor": "WoodTiles",
                "wall": "PlasterPink",
                "table_legs": "Metal",
                "pp_table1": "WoodGreen",
                "pp_table2": "WoodLight"
            },
            {
                "floor": "Dirt",
                "wall": "BricksWhite",
                "table_legs": "Metal",
                "pp_table1": "WoodBlue",
                "pp_table2": "WoodLight"
            },
            {
                "floor": "WoodLight",
                "wall": "BricksWhite",
                "table_legs": "Metal",
                "pp_table1": "PlasterCream",
                "pp_table2": "WoodBlue"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "PlasterWhite",
                "table_legs": "Metal",
                "pp_table1": "PlasterYellow",
                "pp_table2": "PlasterGray"
            },
            {
                "floor": "FeltGray",
                "wall": "PlasterPink",
                "table_legs": "SteelScratched",
                "pp_table1": "WoodLight",
                "pp_table2": "WoodRed"
            },
            {
                "floor": "WoodTiles",
                "wall": "BricksWhite",
                "table_legs": "SteelScratched",
                "pp_table1": "WoodDark",
                "pp_table2": "WoodRed"
            },
            {
                "floor": "WoodLight",
                "wall": "PlasterYellow",
                "table_legs": "SteelBrushed",
                "pp_table1": "WoodGreen",
                "pp_table2": "WoodDark"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "PlasterWhite",
                "table_legs": "SteelScratched",
                "pp_table1": "WoodLight",
                "pp_table2": "WoodLight"
            }
        ],
        "eval-easy": [
            {
                "floor": "FeltGray",
                "wall": "FeltGray",
                "table_legs": "Custom03",
                "pp_table1": "Custom03",
                "pp_table2": "WoodGreen"
            },
            {
                "floor": "Custom03",
                "wall": "WoodgrainGray",
                "table_legs": "WoodgrainGray",
                "pp_table1": "Custom04",
                "pp_table2": "Custom02"
            },
            {
                "floor": "Dirt",
                "wall": "WoodBlue",
                "table_legs": "Custom02",
                "pp_table1": "Custom03",
                "pp_table2": "Custom02"
            },
            {
                "floor": "Dirt",
                "wall": "Custom01",
                "table_legs": "Dirt",
                "pp_table1": "WoodRed",
                "pp_table2": "FeltGray"
            },
            {
                "floor": "WoodBlue",
                "wall": "WoodgrainGray",
                "table_legs": "Custom03",
                "pp_table1": "FeltGray",
                "pp_table2": "Custom02"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "Custom02",
                "table_legs": "Custom04",
                "pp_table1": "WoodGreen",
                "pp_table2": "Custom05"
            },
            {
                "floor": "Custom05",
                "wall": "Custom04",
                "table_legs": "Custom02",
                "pp_table1": "Custom02",
                "pp_table2": "WoodBlue"
            },
            {
                "floor": "Custom05",
                "wall": "Custom04",
                "table_legs": "FeltGray",
                "pp_table1": "WoodRed",
                "pp_table2": "FeltGray"
            },
            {
                "floor": "Custom02",
                "wall": "Custom02",
                "table_legs": "WoodRed",
                "pp_table1": "Custom02",
                "pp_table2": "Custom02"
            },
            {
                "floor": "WoodBlue",
                "wall": "Custom01",
                "table_legs": "WoodgrainGray",
                "pp_table1": "WoodBlue",
                "pp_table2": "WoodBlue"
            }
        ],
        "eval-hard": [
            {
                "floor": "Custom24",
                "wall": "Custom14",
                "table_legs": "Custom23",
                "pp_table1": "BricksWhite",
                "pp_table2": "Custom07"
            },
            {
                "floor": "Custom09",
                "wall": "Custom22",
                "table_legs": "Custom10",
                "pp_table1": "Custom13",
                "pp_table2": "Custom17"
            },
            {
                "floor": "Custom14",
                "wall": "Custom10",
                "table_legs": "Custom12",
                "pp_table1": "Custom11",
                "pp_table2": "Custom20"
            },
            {
                "floor": "Custom24",
                "wall": "Custom14",
                "table_legs": "Custom10",
                "pp_table1": "Custom23",
                "pp_table2": "Custom07"
            },
            {
                "floor": "WoodPanels",
                "wall": "Custom15",
                "table_legs": "BricksWhite",
                "pp_table1": "Custom11",
                "pp_table2": "Custom21"
            },
            {
                "floor": "Custom08",
                "wall": "Custom20",
                "table_legs": "Custom18",
                "pp_table1": "Custom23",
                "pp_table2": "Custom17"
            },
            {
                "floor": "Custom17",
                "wall": "Custom13",
                "table_legs": "WoodPanels",
                "pp_table1": "Custom06",
                "pp_table2": "Custom21"
            },
            {
                "floor": "Custom11",
                "wall": "Custom24",
                "table_legs": "Custom25",
                "pp_table1": "Custom13",
                "pp_table2": "Custom17"
            },
            {
                "floor": "Custom20",
                "wall": "Custom07",
                "table_legs": "BricksWhite",
                "pp_table1": "Custom15",
                "pp_table2": "Custom10"
            },
            {
                "floor": "Custom14",
                "wall": "Custom20",
                "table_legs": "WoodPanels",
                "pp_table1": "Custom24",
                "pp_table2": "Custom09"
            }
        ],
        "eval-extreme": [
            {
                "floor": "Custom27",
                "wall": "Custom38",
                "table_legs": "Custom34",
                "pp_table1": "Custom28",
                "pp_table2": "Custom34"
            },
            {
                "floor": "Custom30",
                "wall": "Custom37",
                "table_legs": "Custom38",
                "pp_table1": "Custom32",
                "pp_table2": "Custom29"
            },
            {
                "floor": "Custom38",
                "wall": "Custom32",
                "table_legs": "Custom37",
                "pp_table1": "Custom32",
                "pp_table2": "Custom31"
            },
            {
                "floor": "Custom34",
                "wall": "Custom34",
                "table_legs": "Custom33",
                "pp_table1": "Custom40",
                "pp_table2": "Custom28"
            },
            {
                "floor": "Custom32",
                "wall": "Custom27",
                "table_legs": "Custom26",
                "pp_table1": "Custom40",
                "pp_table2": "Custom37"
            },
            {
                "floor": "Custom31",
                "wall": "Custom38",
                "table_legs": "Custom40",
                "pp_table1": "Custom36",
                "pp_table2": "Custom27"
            },
            {
                "floor": "Custom38",
                "wall": "Custom40",
                "table_legs": "Custom38",
                "pp_table1": "Custom30",
                "pp_table2": "Custom35"
            },
            {
                "floor": "Custom37",
                "wall": "Custom33",
                "table_legs": "Custom29",
                "pp_table1": "Custom33",
                "pp_table2": "Custom36"
            },
            {
                "floor": "Custom39",
                "wall": "Custom35",
                "table_legs": "Custom40",
                "pp_table1": "Custom37",
                "pp_table2": "Custom39"
            },
            {
                "floor": "Custom29",
                "wall": "Custom33",
                "table_legs": "Custom33",
                "pp_table1": "Custom40",
                "pp_table2": "Custom28"
            }
        ]
    },
    "PickPlaceMilk": {
        "train": [
            {
                "floor": "WoodTiles",
                "wall": "PlasterCream",
                "table_legs": "SteelScratched",
                "pp_table1": "PlasterYellow",
                "pp_table2": "WoodDark"
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterCream",
                "table_legs": "SteelScratched",
                "pp_table1": "WoodBlue",
                "pp_table2": "PlasterGray"
            },
            {
                "floor": "WoodTiles",
                "wall": "PlasterGray",
                "table_legs": "SteelBrushed",
                "pp_table1": "WoodGreen",
                "pp_table2": "PlasterGray"
            },
            {
                "floor": "WoodPanels",
                "wall": "PlasterGray",
                "table_legs": "Metal",
                "pp_table1": "Ceramic",
                "pp_table2": "Ceramic"
            },
            {
                "floor": "Dirt",
                "wall": "PlasterPink",
                "table_legs": "SteelScratched",
                "pp_table1": "WoodLight",
                "pp_table2": "PlasterCream"
            },
            {
                "floor": "WoodPanels",
                "wall": "PlasterCream",
                "table_legs": "SteelBrushed",
                "pp_table1": "Ceramic",
                "pp_table2": "WoodLight"
            },
            {
                "floor": "Dirt",
                "wall": "PlasterPink",
                "table_legs": "SteelScratched",
                "pp_table1": "WoodLight",
                "pp_table2": "WoodLight"
            },
            {
                "floor": "WoodLight",
                "wall": "PlasterYellow",
                "table_legs": "Metal",
                "pp_table1": "PlasterCream",
                "pp_table2": "PlasterCream"
            },
            {
                "floor": "FeltGray",
                "wall": "PlasterYellow",
                "table_legs": "Metal",
                "pp_table1": "WoodDark",
                "pp_table2": "WoodDark"
            },
            {
                "floor": "WoodTiles",
                "wall": "PlasterCream",
                "table_legs": "SteelBrushed",
                "pp_table1": "WoodRed",
                "pp_table2": "WoodGreen"
            }
        ],
        "eval-easy": [
            {
                "floor": "Custom05",
                "wall": "WoodBlue",
                "table_legs": "Custom03",
                "pp_table1": "Custom05",
                "pp_table2": "Custom02"
            },
            {
                "floor": "WoodGreen",
                "wall": "Custom03",
                "table_legs": "WoodRed",
                "pp_table1": "Custom05",
                "pp_table2": "Custom03"
            },
            {
                "floor": "Custom04",
                "wall": "Dirt",
                "table_legs": "Dirt",
                "pp_table1": "Custom05",
                "pp_table2": "WoodGreen"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "WoodBlue",
                "table_legs": "FeltGray",
                "pp_table1": "Custom02",
                "pp_table2": "WoodgrainGray"
            },
            {
                "floor": "FeltGray",
                "wall": "Custom04",
                "table_legs": "Custom03",
                "pp_table1": "Custom02",
                "pp_table2": "Dirt"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "Custom01",
                "table_legs": "WoodRed",
                "pp_table1": "Custom02",
                "pp_table2": "Custom05"
            },
            {
                "floor": "Dirt",
                "wall": "Custom04",
                "table_legs": "Custom05",
                "pp_table1": "WoodRed",
                "pp_table2": "FeltGray"
            },
            {
                "floor": "Custom02",
                "wall": "WoodRed",
                "table_legs": "Custom05",
                "pp_table1": "Custom03",
                "pp_table2": "Dirt"
            },
            {
                "floor": "Custom03",
                "wall": "Custom04",
                "table_legs": "Dirt",
                "pp_table1": "Custom03",
                "pp_table2": "Custom04"
            },
            {
                "floor": "WoodRed",
                "wall": "FeltGray",
                "table_legs": "WoodGreen",
                "pp_table1": "Dirt",
                "pp_table2": "Custom04"
            }
        ],
        "eval-hard": [
            {
                "floor": "Custom24",
                "wall": "Custom13",
                "table_legs": "Custom07",
                "pp_table1": "Custom24",
                "pp_table2": "Custom07"
            },
            {
                "floor": "Custom07",
                "wall": "Custom25",
                "table_legs": "Custom14",
                "pp_table1": "Custom25",
                "pp_table2": "BricksWhite"
            },
            {
                "floor": "Custom17",
                "wall": "Custom17",
                "table_legs": "Custom23",
                "pp_table1": "Custom11",
                "pp_table2": "Custom13"
            },
            {
                "floor": "Custom15",
                "wall": "Custom13",
                "table_legs": "Custom23",
                "pp_table1": "Custom16",
                "pp_table2": "Custom16"
            },
            {
                "floor": "Custom16",
                "wall": "Custom18",
                "table_legs": "Custom19",
                "pp_table1": "Custom15",
                "pp_table2": "BricksWhite"
            },
            {
                "floor": "Custom21",
                "wall": "Custom09",
                "table_legs": "Custom21",
                "pp_table1": "Custom23",
                "pp_table2": "Custom24"
            },
            {
                "floor": "Custom10",
                "wall": "Custom23",
                "table_legs": "Custom23",
                "pp_table1": "Custom21",
                "pp_table2": "Custom15"
            },
            {
                "floor": "Custom14",
                "wall": "Custom20",
                "table_legs": "Custom22",
                "pp_table1": "Custom09",
                "pp_table2": "Custom09"
            },
            {
                "floor": "Custom12",
                "wall": "Custom20",
                "table_legs": "Custom17",
                "pp_table1": "Custom23",
                "pp_table2": "Custom20"
            },
            {
                "floor": "Custom21",
                "wall": "Custom19",
                "table_legs": "BricksWhite",
                "pp_table1": "Custom10",
                "pp_table2": "Custom21"
            }
        ],
        "eval-extreme": [
            {
                "floor": "Custom35",
                "wall": "Custom36",
                "table_legs": "Custom31",
                "pp_table1": "Custom28",
                "pp_table2": "Custom29"
            },
            {
                "floor": "Custom33",
                "wall": "Custom27",
                "table_legs": "Custom33",
                "pp_table1": "Custom40",
                "pp_table2": "Custom39"
            },
            {
                "floor": "Custom33",
                "wall": "Custom27",
                "table_legs": "Custom30",
                "pp_table1": "Custom27",
                "pp_table2": "Custom35"
            },
            {
                "floor": "Custom35",
                "wall": "Custom27",
                "table_legs": "Custom30",
                "pp_table1": "Custom30",
                "pp_table2": "Custom28"
            },
            {
                "floor": "Custom35",
                "wall": "Custom33",
                "table_legs": "Custom36",
                "pp_table1": "Custom32",
                "pp_table2": "Custom37"
            },
            {
                "floor": "Custom36",
                "wall": "Custom35",
                "table_legs": "Custom32",
                "pp_table1": "Custom36",
                "pp_table2": "Custom40"
            },
            {
                "floor": "Custom36",
                "wall": "Custom37",
                "table_legs": "Custom36",
                "pp_table1": "Custom33",
                "pp_table2": "Custom28"
            },
            {
                "floor": "Custom35",
                "wall": "Custom30",
                "table_legs": "Custom30",
                "pp_table1": "Custom29",
                "pp_table2": "Custom27"
            },
            {
                "floor": "Custom35",
                "wall": "Custom27",
                "table_legs": "Custom30",
                "pp_table1": "Custom27",
                "pp_table2": "Custom33"
            },
            {
                "floor": "Custom29",
                "wall": "Custom34",
                "table_legs": "Custom37",
                "pp_table1": "Custom38",
                "pp_table2": "Custom28"
            }
        ]
    },
    "PickPlaceSingle": {
        "train": [
            {
                "floor": "WoodTiles",
                "wall": "BricksWhite",
                "table_legs": "SteelScratched",
                "pp_table1": "WoodBlue",
                "pp_table2": "WoodGreen"
            },
            {
                "floor": "WoodPanels",
                "wall": "PlasterPink",
                "table_legs": "SteelScratched",
                "pp_table1": "WoodRed",
                "pp_table2": "WoodBlue"
            },
            {
                "floor": "WoodPanels",
                "wall": "Clay",
                "table_legs": "Metal",
                "pp_table1": "WoodGreen",
                "pp_table2": "WoodBlue"
            },
            {
                "floor": "WoodDark",
                "wall": "Clay",
                "table_legs": "SteelBrushed",
                "pp_table1": "Ceramic",
                "pp_table2": "WoodBlue"
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterGray",
                "table_legs": "SteelBrushed",
                "pp_table1": "WoodDark",
                "pp_table2": "WoodDark"
            },
            {
                "floor": "WoodTiles",
                "wall": "BricksWhite",
                "table_legs": "SteelBrushed",
                "pp_table1": "PlasterGray",
                "pp_table2": "WoodLight"
            },
            {
                "floor": "WoodPanels",
                "wall": "Clay",
                "table_legs": "Metal",
                "pp_table1": "WoodBlue",
                "pp_table2": "PlasterGray"
            },
            {
                "floor": "Dirt",
                "wall": "BricksWhite",
                "table_legs": "SteelBrushed",
                "pp_table1": "PlasterGray",
                "pp_table2": "Ceramic"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "BricksWhite",
                "table_legs": "Metal",
                "pp_table1": "PlasterGray",
                "pp_table2": "PlasterCream"
            },
            {
                "floor": "Dirt",
                "wall": "PlasterYellow",
                "table_legs": "Metal",
                "pp_table1": "Ceramic",
                "pp_table2": "PlasterCream"
            }
        ],
        "eval-easy": [
            {
                "floor": "Dirt",
                "wall": "Dirt",
                "table_legs": "FeltGray",
                "pp_table1": "WoodgrainGray",
                "pp_table2": "Custom05"
            },
            {
                "floor": "Custom02",
                "wall": "WoodBlue",
                "table_legs": "WoodGreen",
                "pp_table1": "Dirt",
                "pp_table2": "Custom05"
            },
            {
                "floor": "Custom05",
                "wall": "WoodgrainGray",
                "table_legs": "Custom02",
                "pp_table1": "WoodBlue",
                "pp_table2": "WoodBlue"
            },
            {
                "floor": "Dirt",
                "wall": "Custom05",
                "table_legs": "WoodRed",
                "pp_table1": "Custom04",
                "pp_table2": "WoodgrainGray"
            },
            {
                "floor": "Custom03",
                "wall": "Dirt",
                "table_legs": "Custom05",
                "pp_table1": "Custom03",
                "pp_table2": "FeltGray"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "Custom02",
                "table_legs": "Custom01",
                "pp_table1": "WoodRed",
                "pp_table2": "Custom02"
            },
            {
                "floor": "Custom05",
                "wall": "WoodRed",
                "table_legs": "Custom01",
                "pp_table1": "WoodgrainGray",
                "pp_table2": "WoodGreen"
            },
            {
                "floor": "WoodBlue",
                "wall": "Custom01",
                "table_legs": "Custom05",
                "pp_table1": "Custom04",
                "pp_table2": "WoodGreen"
            },
            {
                "floor": "WoodGreen",
                "wall": "WoodGreen",
                "table_legs": "Custom01",
                "pp_table1": "WoodBlue",
                "pp_table2": "Custom04"
            },
            {
                "floor": "Dirt",
                "wall": "Custom03",
                "table_legs": "Custom04",
                "pp_table1": "Dirt",
                "pp_table2": "WoodGreen"
            }
        ],
        "eval-hard": [
            {
                "floor": "Custom09",
                "wall": "Custom17",
                "table_legs": "Custom07",
                "pp_table1": "Custom16",
                "pp_table2": "Custom16"
            },
            {
                "floor": "Custom22",
                "wall": "Custom16",
                "table_legs": "Custom16",
                "pp_table1": "WoodPanels",
                "pp_table2": "Custom24"
            },
            {
                "floor": "Custom22",
                "wall": "Custom08",
                "table_legs": "Custom12",
                "pp_table1": "Custom25",
                "pp_table2": "Custom14"
            },
            {
                "floor": "Custom07",
                "wall": "Custom25",
                "table_legs": "WoodPanels",
                "pp_table1": "Custom16",
                "pp_table2": "Custom15"
            },
            {
                "floor": "Custom21",
                "wall": "Custom16",
                "table_legs": "Custom20",
                "pp_table1": "Custom12",
                "pp_table2": "Custom07"
            },
            {
                "floor": "Custom08",
                "wall": "Custom07",
                "table_legs": "Custom10",
                "pp_table1": "Custom21",
                "pp_table2": "Custom23"
            },
            {
                "floor": "BricksWhite",
                "wall": "Custom24",
                "table_legs": "Custom21",
                "pp_table1": "WoodPanels",
                "pp_table2": "Custom15"
            },
            {
                "floor": "Custom24",
                "wall": "Custom19",
                "table_legs": "Custom14",
                "pp_table1": "WoodPanels",
                "pp_table2": "WoodPanels"
            },
            {
                "floor": "Custom12",
                "wall": "Custom22",
                "table_legs": "WoodPanels",
                "pp_table1": "Custom14",
                "pp_table2": "Custom23"
            },
            {
                "floor": "Custom17",
                "wall": "Custom12",
                "table_legs": "Custom19",
                "pp_table1": "WoodPanels",
                "pp_table2": "Custom09"
            }
        ],
        "eval-extreme": [
            {
                "floor": "Custom33",
                "wall": "Custom33",
                "table_legs": "Custom39",
                "pp_table1": "Custom28",
                "pp_table2": "Custom30"
            },
            {
                "floor": "Custom35",
                "wall": "Custom36",
                "table_legs": "Custom34",
                "pp_table1": "Custom35",
                "pp_table2": "Custom33"
            },
            {
                "floor": "Custom26",
                "wall": "Custom28",
                "table_legs": "Custom33",
                "pp_table1": "Custom39",
                "pp_table2": "Custom38"
            },
            {
                "floor": "Custom37",
                "wall": "Custom37",
                "table_legs": "Custom34",
                "pp_table1": "Custom37",
                "pp_table2": "Custom38"
            },
            {
                "floor": "Custom33",
                "wall": "Custom39",
                "table_legs": "Custom26",
                "pp_table1": "Custom39",
                "pp_table2": "Custom36"
            },
            {
                "floor": "Custom39",
                "wall": "Custom32",
                "table_legs": "Custom28",
                "pp_table1": "Custom36",
                "pp_table2": "Custom36"
            },
            {
                "floor": "Custom40",
                "wall": "Custom33",
                "table_legs": "Custom35",
                "pp_table1": "Custom33",
                "pp_table2": "Custom35"
            },
            {
                "floor": "Custom33",
                "wall": "Custom35",
                "table_legs": "Custom27",
                "pp_table1": "Custom27",
                "pp_table2": "Custom38"
            },
            {
                "floor": "Custom38",
                "wall": "Custom32",
                "table_legs": "Custom36",
                "pp_table1": "Custom32",
                "pp_table2": "Custom40"
            },
            {
                "floor": "Custom31",
                "wall": "Custom36",
                "table_legs": "Custom29",
                "pp_table1": "Custom31",
                "pp_table2": "Custom29"
            }
        ]
    },
    "Stack": {
        "train": [
            {
                "floor": "WoodDark",
                "wall": "PlasterGray",
                "table_legs": "SteelBrushed",
                "table": "PlasterYellow",
                "stack_object1": "WoodGreen",
                "stack_object2": "WoodBlue"
            },
            {
                "floor": "FeltGray",
                "wall": "PlasterCream",
                "table_legs": "SteelBrushed",
                "table": "WoodDark",
                "stack_object1": "WoodBlue",
                "stack_object2": "WoodGreen"
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterYellow",
                "table_legs": "SteelBrushed",
                "table": "PlasterCream",
                "stack_object1": "WoodRed",
                "stack_object2": "WoodRed"
            },
            {
                "floor": "FeltGray",
                "wall": "Clay",
                "table_legs": "SteelScratched",
                "table": "PlasterGray",
                "stack_object1": "WoodGreen",
                "stack_object2": "WoodBlue"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "PlasterWhite",
                "table_legs": "SteelBrushed",
                "table": "Ceramic",
                "stack_object1": "WoodGreen",
                "stack_object2": "WoodGreen"
            },
            {
                "floor": "WoodTiles",
                "wall": "PlasterGray",
                "table_legs": "SteelBrushed",
                "table": "WoodLight",
                "stack_object1": "WoodRed",
                "stack_object2": "WoodGreen"
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterPink",
                "table_legs": "Metal",
                "table": "Ceramic",
                "stack_object1": "WoodRed",
                "stack_object2": "WoodRed"
            },
            {
                "floor": "WoodPanels",
                "wall": "PlasterGray",
                "table_legs": "Metal",
                "table": "Ceramic",
                "stack_object1": "WoodRed",
                "stack_object2": "WoodRed"
            },
            {
                "floor": "Dirt",
                "wall": "Clay",
                "table_legs": "Metal",
                "table": "WoodLight",
                "stack_object1": "WoodRed",
                "stack_object2": "WoodBlue"
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterGray",
                "table_legs": "SteelScratched",
                "table": "WoodLight",
                "stack_object1": "WoodGreen",
                "stack_object2": "WoodGreen"
            }
        ],
        "eval-easy": [
            {
                "floor": "Custom04",
                "wall": "Custom05",
                "table_legs": "WoodRed",
                "table": "Custom05",
                "stack_object1": "Custom02",
                "stack_object2": "Dirt"
            },
            {
                "floor": "FeltGray",
                "wall": "WoodGreen",
                "table_legs": "Dirt",
                "table": "WoodgrainGray",
                "stack_object1": "Custom04",
                "stack_object2": "Custom02"
            },
            {
                "floor": "Custom05",
                "wall": "FeltGray",
                "table_legs": "WoodRed",
                "table": "Custom03",
                "stack_object1": "Custom01",
                "stack_object2": "Custom05"
            },
            {
                "floor": "WoodBlue",
                "wall": "WoodRed",
                "table_legs": "Custom01",
                "table": "Dirt",
                "stack_object1": "Custom04",
                "stack_object2": "WoodBlue"
            },
            {
                "floor": "WoodBlue",
                "wall": "Custom02",
                "table_legs": "WoodBlue",
                "table": "Custom04",
                "stack_object1": "WoodgrainGray",
                "stack_object2": "Custom01"
            },
            {
                "floor": "Custom02",
                "wall": "WoodBlue",
                "table_legs": "FeltGray",
                "table": "FeltGray",
                "stack_object1": "WoodRed",
                "stack_object2": "WoodRed"
            },
            {
                "floor": "Custom05",
                "wall": "Custom04",
                "table_legs": "Dirt",
                "table": "WoodBlue",
                "stack_object1": "FeltGray",
                "stack_object2": "Custom05"
            },
            {
                "floor": "Custom01",
                "wall": "Custom05",
                "table_legs": "Custom02",
                "table": "Custom02",
                "stack_object1": "Custom05",
                "stack_object2": "WoodBlue"
            },
            {
                "floor": "Custom01",
                "wall": "WoodRed",
                "table_legs": "Dirt",
                "table": "WoodGreen",
                "stack_object1": "FeltGray",
                "stack_object2": "Custom01"
            },
            {
                "floor": "Custom03",
                "wall": "WoodGreen",
                "table_legs": "Custom04",
                "table": "Custom01",
                "stack_object1": "Custom05",
                "stack_object2": "WoodBlue"
            }
        ],
        "eval-hard": [
            {
                "floor": "Custom17",
                "wall": "Custom21",
                "table_legs": "Custom23",
                "table": "Custom20",
                "stack_object1": "Custom18",
                "stack_object2": "Custom18"
            },
            {
                "floor": "Custom07",
                "wall": "Custom17",
                "table_legs": "Custom20",
                "table": "Custom08",
                "stack_object1": "BricksWhite",
                "stack_object2": "Custom11"
            },
            {
                "floor": "Custom15",
                "wall": "Custom18",
                "table_legs": "Custom21",
                "table": "Custom19",
                "stack_object1": "Custom17",
                "stack_object2": "Custom23"
            },
            {
                "floor": "Custom22",
                "wall": "Custom19",
                "table_legs": "Custom06",
                "table": "WoodPanels",
                "stack_object1": "Custom22",
                "stack_object2": "Custom11"
            },
            {
                "floor": "Custom18",
                "wall": "Custom17",
                "table_legs": "Custom06",
                "table": "Custom17",
                "stack_object1": "Custom24",
                "stack_object2": "Custom18"
            },
            {
                "floor": "Custom24",
                "wall": "Custom11",
                "table_legs": "Custom22",
                "table": "Custom25",
                "stack_object1": "Custom19",
                "stack_object2": "Custom12"
            },
            {
                "floor": "Custom24",
                "wall": "Custom08",
                "table_legs": "BricksWhite",
                "table": "Custom08",
                "stack_object1": "Custom20",
                "stack_object2": "Custom11"
            },
            {
                "floor": "Custom15",
                "wall": "Custom20",
                "table_legs": "Custom07",
                "table": "Custom17",
                "stack_object1": "Custom14",
                "stack_object2": "Custom06"
            },
            {
                "floor": "Custom21",
                "wall": "Custom11",
                "table_legs": "Custom24",
                "table": "Custom25",
                "stack_object1": "Custom11",
                "stack_object2": "WoodPanels"
            },
            {
                "floor": "BricksWhite",
                "wall": "Custom07",
                "table_legs": "Custom22",
                "table": "Custom23",
                "stack_object1": "Custom17",
                "stack_object2": "Custom21"
            }
        ],
        "eval-extreme": [
            {
                "floor": "Custom36",
                "wall": "Custom27",
                "table_legs": "Custom27",
                "table": "Custom26",
                "stack_object1": "Custom26",
                "stack_object2": "Custom38"
            },
            {
                "floor": "Custom36",
                "wall": "Custom28",
                "table_legs": "Custom37",
                "table": "Custom28",
                "stack_object1": "Custom30",
                "stack_object2": "Custom26"
            },
            {
                "floor": "Custom39",
                "wall": "Custom34",
                "table_legs": "Custom36",
                "table": "Custom31",
                "stack_object1": "Custom28",
                "stack_object2": "Custom38"
            },
            {
                "floor": "Custom27",
                "wall": "Custom27",
                "table_legs": "Custom33",
                "table": "Custom32",
                "stack_object1": "Custom33",
                "stack_object2": "Custom26"
            },
            {
                "floor": "Custom32",
                "wall": "Custom32",
                "table_legs": "Custom40",
                "table": "Custom31",
                "stack_object1": "Custom30",
                "stack_object2": "Custom30"
            },
            {
                "floor": "Custom30",
                "wall": "Custom38",
                "table_legs": "Custom26",
                "table": "Custom37",
                "stack_object1": "Custom33",
                "stack_object2": "Custom28"
            },
            {
                "floor": "Custom27",
                "wall": "Custom38",
                "table_legs": "Custom32",
                "table": "Custom34",
                "stack_object1": "Custom39",
                "stack_object2": "Custom26"
            },
            {
                "floor": "Custom28",
                "wall": "Custom28",
                "table_legs": "Custom27",
                "table": "Custom36",
                "stack_object1": "Custom33",
                "stack_object2": "Custom26"
            },
            {
                "floor": "Custom29",
                "wall": "Custom29",
                "table_legs": "Custom30",
                "table": "Custom31",
                "stack_object1": "Custom40",
                "stack_object2": "Custom31"
            },
            {
                "floor": "Custom36",
                "wall": "Custom38",
                "table_legs": "Custom36",
                "table": "Custom26",
                "stack_object1": "Custom34",
                "stack_object2": "Custom26"
            }
        ]
    },
    "Wipe": {
        "train": [
            {
                "floor": "WoodDark",
                "wall": "PlasterCream",
                "table_legs": "SteelBrushed",
                "table": "Ceramic"
            },
            {
                "floor": "Dirt",
                "wall": "BricksWhite",
                "table_legs": "SteelBrushed",
                "table": "PlasterGray"
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterCream",
                "table_legs": "Metal",
                "table": "Ceramic"
            },
            {
                "floor": "Dirt",
                "wall": "PlasterCream",
                "table_legs": "Metal",
                "table": "PlasterYellow"
            },
            {
                "floor": "WoodPanels",
                "wall": "PlasterCream",
                "table_legs": "Metal",
                "table": "WoodDark"
            },
            {
                "floor": "FeltGray",
                "wall": "PlasterWhite",
                "table_legs": "SteelScratched",
                "table": "WoodDark"
            },
            {
                "floor": "FeltGray",
                "wall": "PlasterCream",
                "table_legs": "Metal",
                "table": "WoodDark"
            },
            {
                "floor": "WoodDark",
                "wall": "Clay",
                "table_legs": "SteelScratched",
                "table": "WoodLight"
            },
            {
                "floor": "WoodDark",
                "wall": "PlasterGray",
                "table_legs": "Metal",
                "table": "PlasterGray"
            },
            {
                "floor": "Dirt",
                "wall": "Clay",
                "table_legs": "SteelScratched",
                "table": "PlasterYellow"
            }
        ],
        "eval-easy": [
            {
                "floor": "WoodRed",
                "wall": "FeltGray",
                "table_legs": "Custom02",
                "table": "WoodBlue"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "Custom01",
                "table_legs": "WoodGreen",
                "table": "Custom01"
            },
            {
                "floor": "Dirt",
                "wall": "WoodGreen",
                "table_legs": "WoodRed",
                "table": "WoodgrainGray"
            },
            {
                "floor": "FeltGray",
                "wall": "Dirt",
                "table_legs": "Dirt",
                "table": "Custom03"
            },
            {
                "floor": "WoodBlue",
                "wall": "WoodgrainGray",
                "table_legs": "WoodgrainGray",
                "table": "Custom01"
            },
            {
                "floor": "Dirt",
                "wall": "Custom03",
                "table_legs": "WoodRed",
                "table": "FeltGray"
            },
            {
                "floor": "Custom03",
                "wall": "FeltGray",
                "table_legs": "WoodRed",
                "table": "Custom03"
            },
            {
                "floor": "WoodBlue",
                "wall": "Custom03",
                "table_legs": "Dirt",
                "table": "WoodBlue"
            },
            {
                "floor": "WoodRed",
                "wall": "Custom01",
                "table_legs": "WoodBlue",
                "table": "WoodGreen"
            },
            {
                "floor": "FeltGray",
                "wall": "FeltGray",
                "table_legs": "WoodgrainGray",
                "table": "FeltGray"
            }
        ],
        "eval-hard": [
            {
                "floor": "Custom19",
                "wall": "Custom09",
                "table_legs": "Custom08",
                "table": "Custom13"
            },
            {
                "floor": "Custom12",
                "wall": "Custom06",
                "table_legs": "Custom22",
                "table": "Custom09"
            },
            {
                "floor": "Custom06",
                "wall": "Custom22",
                "table_legs": "Custom06",
                "table": "BricksWhite"
            },
            {
                "floor": "Custom24",
                "wall": "Custom24",
                "table_legs": "Custom06",
                "table": "Custom11"
            },
            {
                "floor": "Custom15",
                "wall": "Custom25",
                "table_legs": "Custom11",
                "table": "Custom13"
            },
            {
                "floor": "Custom13",
                "wall": "Custom22",
                "table_legs": "Custom10",
                "table": "Custom17"
            },
            {
                "floor": "Custom12",
                "wall": "Custom16",
                "table_legs": "Custom18",
                "table": "Custom09"
            },
            {
                "floor": "Custom13",
                "wall": "Custom09",
                "table_legs": "Custom16",
                "table": "Custom07"
            },
            {
                "floor": "Custom11",
                "wall": "Custom14",
                "table_legs": "Custom24",
                "table": "Custom23"
            },
            {
                "floor": "Custom19",
                "wall": "Custom06",
                "table_legs": "Custom23",
                "table": "Custom06"
            }
        ],
        "eval-extreme": [
            {
                "floor": "Custom33",
                "wall": "Custom32",
                "table_legs": "Custom38",
                "table": "Custom36"
            },
            {
                "floor": "Custom37",
                "wall": "Custom39",
                "table_legs": "Custom39",
                "table": "Custom28"
            },
            {
                "floor": "Custom34",
                "wall": "Custom37",
                "table_legs": "Custom34",
                "table": "Custom28"
            },
            {
                "floor": "Custom28",
                "wall": "Custom40",
                "table_legs": "Custom27",
                "table": "Custom35"
            },
            {
                "floor": "Custom29",
                "wall": "Custom37",
                "table_legs": "Custom34",
                "table": "Custom27"
            },
            {
                "floor": "Custom31",
                "wall": "Custom29",
                "table_legs": "Custom33",
                "table": "Custom38"
            },
            {
                "floor": "Custom28",
                "wall": "Custom37",
                "table_legs": "Custom28",
                "table": "Custom27"
            },
            {
                "floor": "Custom37",
                "wall": "Custom35",
                "table_legs": "Custom34",
                "table": "Custom29"
            },
            {
                "floor": "Custom39",
                "wall": "Custom38",
                "table_legs": "Custom32",
                "table": "Custom32"
            },
            {
                "floor": "Custom35",
                "wall": "Custom34",
                "table_legs": "Custom26",
                "table": "Custom37"
            }
        ]
    },
    "TwoArmHandover": {
        "train": [
            {
                "floor": "WoodgrainGray",
                "wall": "Clay",
                "table_legs": "SteelScratched",
                "table": "PlasterCream",
                "handoff_hammer_head": "SteelScratched",
                "handoff_hammer_body": "WoodGreen"
            },
            {
                "floor": "WoodLight",
                "wall": "PlasterGray",
                "table_legs": "SteelScratched",
                "table": "WoodDark",
                "handoff_hammer_head": "Metal",
                "handoff_hammer_body": "WoodRed"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "PlasterYellow",
                "table_legs": "SteelScratched",
                "table": "Ceramic",
                "handoff_hammer_head": "SteelScratched",
                "handoff_hammer_body": "WoodRed"
            },
            {
                "floor": "WoodDark",
                "wall": "Clay",
                "table_legs": "SteelScratched",
                "table": "PlasterYellow",
                "handoff_hammer_head": "Metal",
                "handoff_hammer_body": "WoodLight"
            },
            {
                "floor": "WoodPanels",
                "wall": "PlasterCream",
                "table_legs": "SteelScratched",
                "table": "WoodDark",
                "handoff_hammer_head": "SteelScratched",
                "handoff_hammer_body": "WoodRed"
            },
            {
                "floor": "Dirt",
                "wall": "Clay",
                "table_legs": "SteelScratched",
                "table": "Ceramic",
                "handoff_hammer_head": "Metal",
                "handoff_hammer_body": "WoodLight"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "PlasterGray",
                "table_legs": "SteelScratched",
                "table": "PlasterGray",
                "handoff_hammer_head": "SteelScratched",
                "handoff_hammer_body": "WoodRed"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "PlasterYellow",
                "table_legs": "SteelScratched",
                "table": "PlasterGray",
                "handoff_hammer_head": "SteelScratched",
                "handoff_hammer_body": "WoodRed"
            },
            {
                "floor": "FeltGray",
                "wall": "PlasterYellow",
                "table_legs": "Metal",
                "table": "WoodDark",
                "handoff_hammer_head": "SteelScratched",
                "handoff_hammer_body": "WoodLight"
            },
            {
                "floor": "WoodPanels",
                "wall": "PlasterCream",
                "table_legs": "SteelScratched",
                "table": "WoodDark",
                "handoff_hammer_head": "Brass",
                "handoff_hammer_body": "WoodBlue"
            }
        ],
        "eval-easy": [
            {
                "floor": "Custom05",
                "wall": "WoodBlue",
                "table_legs": "WoodGreen",
                "table": "Custom03",
                "handoff_hammer_head": "Custom04",
                "handoff_hammer_body": "WoodBlue"
            },
            {
                "floor": "Custom03",
                "wall": "WoodRed",
                "table_legs": "Custom02",
                "table": "Custom01",
                "handoff_hammer_head": "Custom02",
                "handoff_hammer_body": "WoodBlue"
            },
            {
                "floor": "WoodBlue",
                "wall": "WoodGreen",
                "table_legs": "WoodBlue",
                "table": "WoodBlue",
                "handoff_hammer_head": "Custom02",
                "handoff_hammer_body": "Dirt"
            },
            {
                "floor": "Custom03",
                "wall": "Custom05",
                "table_legs": "WoodGreen",
                "table": "WoodRed",
                "handoff_hammer_head": "Custom01",
                "handoff_hammer_body": "Custom02"
            },
            {
                "floor": "WoodGreen",
                "wall": "Custom01",
                "table_legs": "WoodBlue",
                "table": "Dirt",
                "handoff_hammer_head": "FeltGray",
                "handoff_hammer_body": "Custom02"
            },
            {
                "floor": "Custom05",
                "wall": "Custom03",
                "table_legs": "WoodGreen",
                "table": "Custom03",
                "handoff_hammer_head": "Dirt",
                "handoff_hammer_body": "FeltGray"
            },
            {
                "floor": "Custom02",
                "wall": "WoodBlue",
                "table_legs": "WoodRed",
                "table": "Custom05",
                "handoff_hammer_head": "Dirt",
                "handoff_hammer_body": "WoodBlue"
            },
            {
                "floor": "WoodgrainGray",
                "wall": "WoodGreen",
                "table_legs": "Custom01",
                "table": "Custom03",
                "handoff_hammer_head": "WoodgrainGray",
                "handoff_hammer_body": "Custom05"
            },
            {
                "floor": "WoodRed",
                "wall": "Custom05",
                "table_legs": "WoodRed",
                "table": "Custom01",
                "handoff_hammer_head": "Custom02",
                "handoff_hammer_body": "WoodgrainGray"
            },
            {
                "floor": "WoodRed",
                "wall": "Custom02",
                "table_legs": "WoodgrainGray",
                "table": "WoodBlue",
                "handoff_hammer_head": "Custom02",
                "handoff_hammer_body": "WoodGreen"
            }
        ],
        "eval-hard": [
            {
                "floor": "Custom07",
                "wall": "Custom09",
                "table_legs": "Custom22",
                "table": "Custom15",
                "handoff_hammer_head": "Custom25",
                "handoff_hammer_body": "Custom20"
            },
            {
                "floor": "Custom07",
                "wall": "Custom23",
                "table_legs": "Custom17",
                "table": "Custom17",
                "handoff_hammer_head": "Custom20",
                "handoff_hammer_body": "Custom17"
            },
            {
                "floor": "Custom22",
                "wall": "WoodPanels",
                "table_legs": "Custom20",
                "table": "Custom21",
                "handoff_hammer_head": "BricksWhite",
                "handoff_hammer_body": "Custom22"
            },
            {
                "floor": "Custom16",
                "wall": "Custom14",
                "table_legs": "Custom19",
                "table": "Custom19",
                "handoff_hammer_head": "Custom07",
                "handoff_hammer_body": "Custom17"
            },
            {
                "floor": "BricksWhite",
                "wall": "Custom12",
                "table_legs": "Custom20",
                "table": "Custom18",
                "handoff_hammer_head": "Custom22",
                "handoff_hammer_body": "Custom07"
            },
            {
                "floor": "Custom08",
                "wall": "Custom22",
                "table_legs": "Custom23",
                "table": "Custom25",
                "handoff_hammer_head": "Custom25",
                "handoff_hammer_body": "Custom21"
            },
            {
                "floor": "Custom19",
                "wall": "Custom15",
                "table_legs": "Custom18",
                "table": "Custom24",
                "handoff_hammer_head": "Custom07",
                "handoff_hammer_body": "Custom12"
            },
            {
                "floor": "Custom20",
                "wall": "Custom16",
                "table_legs": "Custom10",
                "table": "Custom20",
                "handoff_hammer_head": "Custom24",
                "handoff_hammer_body": "Custom18"
            },
            {
                "floor": "Custom12",
                "wall": "Custom18",
                "table_legs": "BricksWhite",
                "table": "Custom19",
                "handoff_hammer_head": "Custom12",
                "handoff_hammer_body": "Custom06"
            },
            {
                "floor": "Custom23",
                "wall": "WoodPanels",
                "table_legs": "Custom11",
                "table": "Custom15",
                "handoff_hammer_head": "Custom24",
                "handoff_hammer_body": "Custom09"
            }
        ],
        "eval-extreme": [
            {
                "floor": "Custom34",
                "wall": "Custom30",
                "table_legs": "Custom30",
                "table": "Custom36",
                "handoff_hammer_head": "Custom33",
                "handoff_hammer_body": "Custom32"
            },
            {
                "floor": "Custom40",
                "wall": "Custom32",
                "table_legs": "Custom27",
                "table": "Custom33",
                "handoff_hammer_head": "Custom26",
                "handoff_hammer_body": "Custom40"
            },
            {
                "floor": "Custom33",
                "wall": "Custom37",
                "table_legs": "Custom26",
                "table": "Custom26",
                "handoff_hammer_head": "Custom39",
                "handoff_hammer_body": "Custom27"
            },
            {
                "floor": "Custom32",
                "wall": "Custom32",
                "table_legs": "Custom31",
                "table": "Custom29",
                "handoff_hammer_head": "Custom33",
                "handoff_hammer_body": "Custom37"
            },
            {
                "floor": "Custom34",
                "wall": "Custom27",
                "table_legs": "Custom36",
                "table": "Custom39",
                "handoff_hammer_head": "Custom33",
                "handoff_hammer_body": "Custom38"
            },
            {
                "floor": "Custom37",
                "wall": "Custom38",
                "table_legs": "Custom27",
                "table": "Custom38",
                "handoff_hammer_head": "Custom28",
                "handoff_hammer_body": "Custom39"
            },
            {
                "floor": "Custom36",
                "wall": "Custom40",
                "table_legs": "Custom34",
                "table": "Custom35",
                "handoff_hammer_head": "Custom32",
                "handoff_hammer_body": "Custom35"
            },
            {
                "floor": "Custom36",
                "wall": "Custom36",
                "table_legs": "Custom38",
                "table": "Custom30",
                "handoff_hammer_head": "Custom30",
                "handoff_hammer_body": "Custom32"
            },
            {
                "floor": "Custom37",
                "wall": "Custom38",
                "table_legs": "Custom30",
                "table": "Custom39",
                "handoff_hammer_head": "Custom29",
                "handoff_hammer_body": "Custom29"
            },
            {
                "floor": "Custom27",
                "wall": "Custom27",
                "table_legs": "Custom29",
                "table": "Custom32",
                "handoff_hammer_head": "Custom38",
                "handoff_hammer_body": "Custom30"
            }
        ]
    },
}
